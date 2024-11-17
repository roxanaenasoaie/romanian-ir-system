from whoosh import index
from whoosh.qparser import QueryParser
from romanian_ir.preprocessing import preprocess_text


def search_index(index_dir, queries):
    ix = index.open_dir(index_dir)

    with ix.searcher() as searcher:
        for query_str in queries:
            preprocessed_query = preprocess_text(query_str)

            query = QueryParser("content", ix.schema).parse(preprocessed_query)
            results = searcher.search(query, limit=5)

            if results:
                print(f"Top 5 results for '{query_str}':")
                for result in results:
                    print(f"- Title: {result['title']}")
            else:
                print(f"No results found for '{query_str}'")
            print("-" * 50)


