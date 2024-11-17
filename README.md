# Romanian Information Retrieval System

This project is a Romanian Information Retrieval System designed to index and search documents efficiently, considering the specific linguistic features of the Romanian language.

## **Dependencies**
Install the dependencies using requirements.txt:
```bash
pip install -r requirements.txt
```

## **Usage**
### **1. Indexing Documents**
To index documents located in a folder, use the following command:
```bash
python main.py -index -directory <path_to_documents>
```

### **2. Searching for queries**
To search for one or more queries, use:
```bash
python main.py -search -query <query1> <query2>
```

**Important** You MUST first run the indexing for the searching to work.

## **Features**
- **Document Preprocessing**:
  - Uses Stanza for lemmatization to handle Romanian-specific grammar.
  - Removes diacritics from Romanian text.
  - Tokenizes text into words.
  - Removes stop words.
- **Indexing**:
  - Supports `.txt`, `.pdf`, and `.docx` file formats.
- **Searching**:
  - Allows searching by single or multiple queries.
  - Supports ranking of documents by relevance.
  - Returns an ordered list of the top 5 document names containing the query.
 
## Key Libraries
  - Whoosh: For indexing and searching.
  - Stanza: For Romanian language processing.
  - PyPDF2: For handling PDF files.
  - python-docx: For handling DOCX files.

## **Project Structure**
```bash
project/
├── main.py              # The main script to run indexing and searching
├── romanian_ir/              # Core logic for indexing and searching
│   ├── __init__.py
│   ├── indexing.py      # Functions for indexing documents
│   ├── searching.py     # Functions for searching the index
│   ├── preprocessing.py # Preprocessing logic (diacritics removal, lemmatization, etc.)
├── requirements.txt     # List of dependencies
├── documents/           # Sample documents to be indexed
```

## **Contribution**
This project was developed to demonstrate an effective information retrieval system for the Romanian language. My contributions include:

  - Designing and implementing the preprocessing pipeline tailored to Romanian linguistic features.
  - Developing an efficient indexing and searching mechanism using Python and Whoosh.
  - Providing support for multiple document formats (.txt, .pdf, .docx).
  - Ensuring the system outputs an ordered list of the top 5 relevant documents for any given query.
