from embedder.document_loader import load_and_split_file
from langchain.vectorstores import Milvus
from pathlib import Path
from milvus_utils import get_collection
import os

def get_file_timestamp(path: str):
    return int(max(
        os.path.getmtime(path),
        os.path.getctime(path)
    ))

def delete_unexisting(all_combs):

    print("Deleting unexisting documents")
    collection = get_collection()


    db_entries = collection.query(
        expr="category != ''", 
        output_fields=["category", "file", "pk"]
    )


    for entry in db_entries:
        if (entry['category'], entry['file']) not in all_combs:
            print(f"Deleting {entry['category']}/{entry['file']}")
            collection.delete("pk in {}".format([entry['pk']]))




def embed_folder(folder_path: str, milvus: Milvus, replace: bool = False):
    # make map of categories to file paths
    category_map = {}
    for file_path in Path(folder_path).glob("**/*"):
        if file_path.is_file():
            category = file_path.parent.name
            if category not in category_map:
                category_map[category] = []
            category_map[category].append(file_path)

    # embed each file
    collection = get_collection()

    all_combs = set()

    for category, file_paths in category_map.items():


        for file_path in file_paths:

            file_name = file_path.name

            all_combs.add((category, file_name))

            print(f"Embedding {file_path.name} in category {category}")

            # check if documents with same filename and category already exists
            q_res = collection.query(
                expr=f'file in ["{file_path.name}"] and category in ["{category}"]',
                output_fields=["pk", "last_modified"]
            )



            if len(q_res) > 0:
                print("Found existing document")

                file_timestamp = get_file_timestamp(file_path)
                db_timestamp = q_res[0]['last_modified'] if len(q_res) > 0 else 0
                print(file_timestamp, db_timestamp)

                if (
                    replace 
                    or 
                    get_file_timestamp(file_path) > q_res[0]['last_modified']
                ):
                    print("Replacing document")
                    # delete existing document
                    collection.delete("pk in {}".format([doc['pk'] for doc in q_res]))
                else:
                    # skip this document
                    print("Skipping document")
                    continue

            embed_file(str(file_path), category, milvus)

    # delete all documents that are not in the folder
    delete_unexisting(all_combs)


def embed_file(file_path: str, category, milvus: Milvus):

    # load and split file
    split_doc = load_and_split_file(file_path)

    # get filename
    filename = file_path.split("/")[-1]

    # get last modified
    last_modified = get_file_timestamp(file_path) 

    # get text from each page
    texts = [doc.page_content for doc in split_doc]

    metadata = [{"category": category, "file": filename, 'last_modified': last_modified} for _ in texts]


    # embed text
    ids = milvus.add_texts(texts, metadatas=metadata)

    return ids






