#!/bin/bash

# Elasticsearch URL and index name
ES_URL="http://localhost:9200"
INDEX_NAME="products"

# Data to be indexed
DATA='{
    "product_id": 1,
    "product_name": "Laptop",
    "description": "High-performance laptop with the latest Intel processor.",
    "category": "Electronics",
    "price": 999.99,
    "brand": "ExampleTech",
    "in_stock": true,
    "tags": ["laptop", "electronics", "tech"],
    "timestamp": "2023-10-20T10:30:00"
}'

# Index the data
curl -X POST "$ES_URL/$INDEX_NAME/_doc/1" -H "Content-Type: application/json" -d "$DATA"
