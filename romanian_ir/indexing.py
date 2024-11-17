from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from pathlib import Path
from romanian_ir.preprocessing import preprocess_text
import os
from docx import Document
import PyPDF2


def define_schema():
    return Schema(
        title=TEXT(stored=True),
        content=TEXT(stored=True),
        path=ID(stored=True, unique=True)
    )


def create_index_dir(index_dir):
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)


def extract_txt_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Failed to read TXT file {file_path}: {e}")
        return ""


def extract_pdf_content(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Failed to extract content from PDF {file_path}: {e}")
        return ""


def extract_docx_content(file_path):
    try:
        doc = Document(file_path)
        return '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    except Exception as e:
        print(f"Failed to extract content from DOCX {file_path}: {e}")
        return ""


def extract_content(file_path):
    if file_path.endswith('.pdf'):
        return extract_pdf_content(file_path)
    elif file_path.endswith('.docx'):
        return extract_docx_content(file_path)
    elif file_path.endswith('.txt'):
        return extract_txt_content(file_path)
    else:
        print(f"Unsupported file type: {file_path}")
        return ""


def index_documents(folder, index_dir):
    schema = define_schema()
    create_index_dir(index_dir)
    ix = index.create_in(index_dir, schema) if not index.exists_in(index_dir) else index.open_dir(index_dir)
    writer = ix.writer()
    folder_path = Path(folder)

    for file_path in folder_path.glob("*.*"):
        if file_path.suffix.lower() in ['.txt', '.pdf', '.docx']:
            try:
                original_content = extract_content(str(file_path))
                if original_content.strip():
                    processed_content = preprocess_text(original_content)
                    writer.add_document(
                        title=file_path.name,
                        content=processed_content,
                        path=str(file_path)
                    )
                    print(f"Indexed: {file_path.name}")
                else:
                    print(f"Skipped empty file: {file_path.name}")
            except Exception as e:
                print(f"Failed to process {file_path}: {e}")

    writer.commit()
    print("Indexing complete.")
