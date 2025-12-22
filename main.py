from __future__ import annotations

from typing import Any, Callable

from litestar import Litestar, asgi
from ariadne.asgi import GraphQL

from app.graphql import schema
from app.lifespan import pubsub_lifespan


graphql_app = GraphQL(schema, debug=True)


@asgi(path="/graphql", is_mount=True)
async def graphql_handler(
    scope: dict[str, Any],
    receive: Callable[[], Any],
    send: Callable[[dict[str, Any]], Any],
) -> None:
    """Mount Ariadne GraphQL as ASGI handler."""
    await graphql_app(scope, receive, send)


app = Litestar(
    route_handlers=[graphql_handler],
    lifespan=[pubsub_lifespan],
)
