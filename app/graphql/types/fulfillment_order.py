from ariadne_graphql_modules import ObjectType, gql


class FulfillmentOrderAcceptFulfillmentRequestPayload(ObjectType):
    __schema__ = gql("""
        type FulfillmentOrderAcceptFulfillmentRequestPayload {
            success: Boolean!
            error: String
        }
    """)

