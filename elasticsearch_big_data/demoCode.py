from elasticsearch import Elasticsearch

# Initialize the Elasticsearch client
client = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# GET _cluster/health
cluster_health = client.cluster.health()
print(cluster_health)

# DELETE favorite_candy
client.indices.delete(index='favorite_candy', ignore=[400, 404])

# PUT favorite_candy
client.indices.create(index='favorite_candy')

# POST favorite_candy/_doc
data = {
    "first_name": "Lisa",
    "candy": "Sour Skittles"
}
client.index(index='favorite_candy', doc_type='_doc', body=data)

# PUT favorite_candy/_doc/1
data = {
    "first_name": "John",
    "candy": "Starburst"
}
client.index(index='favorite_candy', doc_type='_doc', id=1, body=data)

# PUT favorite_candy/_create/1
data = {
    "first_name": "Finn",
    "candy": "Jolly Ranchers"
}
client.create(index='favorite_candy', doc_type='_doc', id=1, body=data)

# GET favorite_candy/_doc/1
doc_1 = client.get(index='favorite_candy', doc_type='_doc', id=1)
print(doc_1)

# POST favorite_candy/_update/1
data = {
    "doc": {
        "candy": "M&M's"
    }
}
client.update(index='favorite_candy', doc_type='_doc', id=1, body=data)

# DELETE favorite_candy/_doc/1
client.delete(index='favorite_candy', doc_type='_doc', id=1)

# GET news_headlines/_search
news_headlines_search = client.search(index='news_headlines')

# GET news_headlines/_search with track_total_hits
news_headlines_search_with_hits = client.search(index='news_headlines', track_total_hits=True)

# GET news_headlines/_search with date range query
date_range_query = {
    "query": {
        "range": {
            "date": {
                "gte": "2015-06-20",
                "lte": "2015-09-22"
            }
        }
    }
}
news_headlines_date_range = client.search(index='news_headlines', body=date_range_query)

# GET news_headlines/_search with aggregation by category
aggregation_query = {
    "aggs": {
        "by_category": {
            "terms": {
                "field": "category",
                "size": 100
            }
        }
    }
}
news_headlines_aggregation = client.search(index='news_headlines', body=aggregation_query)

# GET news_headlines/_search with query and aggregation
query_and_aggregation = {
    "query": {
        "match": {
            "category": "ENTERTAINMENT"
        }
    },
    "aggregations": {
        "popular_in_entertainment": {
            "significant_text": {
                "field": "headline"
            }
        }
    }
}
news_headlines_query_and_aggregation = client.search(index='news_headlines', body=query_and_aggregation)
