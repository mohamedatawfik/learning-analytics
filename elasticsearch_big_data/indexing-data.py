from elasticsearch import Elasticsearch

# Elasticsearch URL and index name
ES_URL = 'http://localhost:9200'
INDEX_NAME = 'products'

# Data to be indexed
data = {
    'product_id': 1,
    'product_name': 'Laptop',
    'description': 'High-performance laptop with the latest Intel processor.',
    'category': 'Electronics',
    'price': 999.99,
    'brand': 'ExampleTech',
    'in_stock': True,
    'tags': ['laptop', 'electronics', 'tech'],
    'timestamp': '2023-10-20T10:30:00'
}

# Initialize the Elasticsearch client
client = Elasticsearch([ES_URL])

# GET _cluster/health
cluster_health = client.cluster.health()
print(cluster_health)

# Index the data
response = client.index(index=INDEX_NAME, doc_type='_doc', body=data)

# Check the response
if response['result'] == 'created':
    print("Document indexed successfully.")

# Close the Elasticsearch client
client.transport.close()
