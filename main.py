import argparse
from romanian_ir.indexing import index_documents
from romanian_ir.searching import search_index


def main():
    parser = argparse.ArgumentParser(description="Romanian Information Retrieval System")
    parser.add_argument("-index", action="store_true", help="Run the indexing process")
    parser.add_argument("-search", action="store_true", help="Run the search process")
    parser.add_argument("-directory", type=str, help="Path to the folder containing documents to index")
    parser.add_argument("-query", nargs="+", help="Query strings to search the index")
    parser.add_argument("-index_dir", default="indexdir", help="Path to the index directory")

    args = parser.parse_args()

    if args.index:
        if not args.directory:
            print("Error: You must specify a directory containing documents using -directory")
        else:
            index_documents(args.directory, args.index_dir)
    elif args.search:
            if not args.query:
                print("Error: You must specify at least one query using -query")
            else:
                search_index(args.index_dir, args.query)
    else:
        print("Error: You must specify either -index or -search.")


if __name__ == "__main__":
    main()
