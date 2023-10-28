#!/bin/bash

# Elasticsearch URL and index name
ES_URL="http://localhost:9200"
INDEX_NAME="products"

# Search query
SEARCH_QUERY='{
    "query": {
        "bool": {
            "must": [
                { "match": { "product_name": "Laptop" } },
                { "term": { "in_stock": true } }
            ]
        }
    }
}'

# Search for products
curl -X POST "$ES_URL/$INDEX_NAME/_search" -H "Content-Type: application/json" -d "$SEARCH_QUERY"
