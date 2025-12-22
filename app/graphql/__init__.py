from ariadne_graphql_modules import make_executable_schema

from .mutations.fulfillment_order import FulfillmentOrderAcceptFulfillmentRequestMutation

schema = make_executable_schema(FulfillmentOrderAcceptFulfillmentRequestMutation)

__all__ = ["schema"]
