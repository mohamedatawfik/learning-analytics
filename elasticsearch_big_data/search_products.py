from elasticsearch import Elasticsearch

# Elasticsearch URL and index name
ES_URL = 'http://localhost:9200'
INDEX_NAME = 'products'

# Initialize the Elasticsearch client
client = Elasticsearch([ES_URL])

# GET _cluster/health
cluster_health = client.cluster.health()
print(cluster_health)

# Define the search query
search_query = {
    "query": {
        "bool": {
            "must": [
                {"match": {"product_name": "Laptop"}},
                {"term": {"in_stock": True}}
            ]
        }
    }
}

# Perform the search
search_results = client.search(index=INDEX_NAME, body=search_query)

# Display the search results
print("Search Results:")
for hit in search_results['hits']['hits']:
    print(f"Product Name: {hit['_source']['product_name']}, Description: {hit['_source']['description']}")

# Close the Elasticsearch client
client.transport.close()
