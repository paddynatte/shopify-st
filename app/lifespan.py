from __future__ import annotations

import json
import asyncio
import logging
from contextlib import asynccontextmanager

from google.cloud import pubsub_v1
from litestar import Litestar

from app.config import settings

logger = logging.getLogger(__name__)


@asynccontextmanager
async def pubsub_lifespan(app: Litestar):
    """Pub/Sub subscriber lifecycle."""

    if not settings.project_id or not settings.subscription_id:
        logger.warning("Pub/Sub not configured")
        yield
        return

    subscriber = pubsub_v1.SubscriberClient()
    sub_path = subscriber.subscription_path(settings.project_id, settings.subscription_id)
    loop = asyncio.get_running_loop()

    async def handle_message(msg):
        """Process incoming Shopify webhook."""
        try:
            payload = json.loads(msg.data.decode())
            topic = msg.attributes.get("X-Shopify-Topic")
            shop = msg.attributes.get("X-Shopify-Shop-Domain")

            logger.info(f"Webhook received: {topic} from {shop}")
            msg.ack()

        except Exception as e:
            logger.exception(f"Error processing webhook: {e}")
            msg.nack()

    def on_message(msg):
        asyncio.run_coroutine_threadsafe(handle_message(msg), loop)

    streaming_pull = subscriber.subscribe(sub_path, on_message)
    logger.info(f"Pub/Sub listening: {sub_path}")

    try:
        yield
    finally:
        streaming_pull.cancel()
        subscriber.close()
        logger.info("Pub/Sub shutdown complete")