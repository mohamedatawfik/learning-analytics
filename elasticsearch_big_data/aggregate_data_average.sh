#!/bin/bash

# Elasticsearch URL and index name
ES_URL="http://localhost:9200"
INDEX_NAME="products"

# Aggregation query
AGGREGATION_QUERY='{
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
}'

# Perform aggregation
curl -X POST "$ES_URL/$INDEX_NAME/_search" -H "Content-Type: application/json" -d "$AGGREGATION_QUERY"
