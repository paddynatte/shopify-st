from __future__ import annotations

from typing import Any

from ariadne_graphql_modules import MutationType, gql, convert_case

from app.graphql.inputs.fulfillment_order import FulfillmentOrderAcceptFulfillmentRequestInput
from app.graphql.types.fulfillment_order import FulfillmentOrderAcceptFulfillmentRequestPayload


class FulfillmentOrderAcceptFulfillmentRequestMutation(MutationType):
    __schema__ = gql("""
        type Mutation {
            fulfillmentOrderAcceptFulfillmentRequest(input: FulfillmentOrderAcceptFulfillmentRequestInput!): FulfillmentOrderAcceptFulfillmentRequestPayload!
        }
    """)
    __requires__ = [FulfillmentOrderAcceptFulfillmentRequestInput, FulfillmentOrderAcceptFulfillmentRequestPayload]
    __aliases__ = convert_case

    @staticmethod
    async def resolve_mutation(_, info: Any, input: dict):
        """
        Accept a fulfillment request on Shopify.
        
        Mirrors Shopify's fulfillmentOrderAcceptFulfillmentRequest mutation.
        See: https://shopify.dev/docs/api/admin-graphql/latest/mutations/fulfillmentOrderAcceptFulfillmentRequest
        
        Flow:
        1. Get shop access token (from core backend via Router)
        2. Call Shopify Admin API to accept fulfillment request
        3. Optionally sync result back to core backend
        
        TODO: Need to determine best pattern for external API clients
              (via info.context, DI, or module imports)
        """
        shop_domain = input["shop_domain"]
        fulfillment_order_id = input["id"]
        message = input.get("message")

        # TODO: Implement once client pattern is decided
        return {"success": False, "error": "Not implemented"}