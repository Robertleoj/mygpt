from embedder import embed_folder
from milvus_utils import get_vectorstore
from sys import argv
import nltk


def main():

    nltk.download('punkt')

    if len(argv) > 1:
        replace = argv[1] == "replace"
    else:
        replace = False

    milvus = get_vectorstore()
    embed_folder("data", milvus, replace=replace)

if __name__ == "__main__":
    main()
