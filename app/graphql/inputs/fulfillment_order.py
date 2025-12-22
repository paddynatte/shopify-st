from ariadne_graphql_modules import InputType, gql, convert_case


class FulfillmentOrderAcceptFulfillmentRequestInput(InputType):
    __schema__ = gql("""
        input FulfillmentOrderAcceptFulfillmentRequestInput {
            shopDomain: String!
            id: ID!
            message: String
        }
    """)
    __args__ = convert_case

