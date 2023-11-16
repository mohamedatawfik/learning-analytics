from elasticsearch import Elasticsearch

# Elasticsearch URL and index name
ES_URL = 'http://localhost:9200'
INDEX_NAME = 'products'

# Initialize the Elasticsearch client
client = Elasticsearch([ES_URL])

# GET _cluster/health
cluster_health = client.cluster.health()
print(cluster_health)

# Define the aggregation query
aggregation_query = {
    "size": 0,
    "aggs": {
        "category_agg": {
            "terms": {
                "field": "category.keyword"
            },
            "aggs": {
                "avg_price": {
                    "avg": {
                        "field": "price"
                    }
                }
            }
        }
    }
}

# Perform the aggregation
aggregation_result = client.search(index=INDEX_NAME, body=aggregation_query)

# Display the aggregation result
aggs = aggregation_result['aggregations']['category_agg']['buckets']
for bucket in aggs:
    category = bucket['key']
    avg_price = bucket['avg_price']['value']
    print(f"Category: {category}, Average Price: {avg_price}")

# Close the Elasticsearch client
client.transport.close()
