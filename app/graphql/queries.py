"""External GraphQL queries for Shopify and Router."""

# === SHOPIFY ===

GET_FULFILLMENT_ORDER = """
query($id: ID!) {
  fulfillmentOrder(id: $id) {
    id
    status
    requestStatus
    destination { address1 city countryCode zip firstName lastName }
    order { id name customer { displayName email phone } }
    assignedLocation { location { id name } }
    lineItems(first: 50) {
      edges { node { id remainingQuantity totalQuantity lineItem { id name sku } } }
    }
  }
}
"""

ACCEPT_FULFILLMENT_REQUEST = """
mutation($id: ID!) {
  fulfillmentOrderAcceptFulfillmentRequest(id: $id) {
    fulfillmentOrder { id status requestStatus }
    userErrors { field message }
  }
}
"""

# === ROUTER ===

GET_SHOP_TOKEN = """
query($domain: String!) {
  shopByDomain(domain: $domain) { accessToken }
}
"""

PROCESS_WEBHOOK = """
mutation($shopDomain: String!, $topic: String!, $payload: JSON!) {
  processShopifyWebhook(shopDomain: $shopDomain, topic: $topic, payload: $payload) {
    success
    error
  }
}
"""
