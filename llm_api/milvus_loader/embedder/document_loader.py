import langchain.document_loaders as loaders
import langchain.text_splitter as splitters
import config


def load_file(path, extension):

    # match extension to loader
    match extension:
        case "pdf":
            doc = loaders.PyPDFLoader(path).load()
        case "docx":
            doc = loaders.Docx2txtLoader(path).load()
        case 'txt':
            doc = loaders.TextLoader(path).load()
        case 'html':
            doc = loaders.BSHTMLLoader(path).load()
        case 'md':
            doc = loaders.UnstructuredMarkdownLoader(path).load()
        case 'pptx':
            doc = loaders.UnstructuredPowerPointLoader(path).load()
        case _:
            raise ValueError(f"Unsupported file extension: {extension}")

    return doc

def split_document(doc, extension):
    chunk_size = int(config.get_config("EMB_CHUNK_TOKENS"))

    match extension:
        case "md":
            splitter = splitters.MarkdownTextSplitter
        case _:
            splitter = splitters.RecursiveCharacterTextSplitter

    split_doc = splitter.from_tiktoken_encoder(
        chunk_size=chunk_size, 
        chunk_overlap=10, 
        separators=[" ", ",", "\n"]
    )

    return split_doc.split_documents(doc)


def load_and_split_file(path):
    # get extension
    extension = path.split(".")[-1]

    # load file
    doc = load_file(path, extension)
    print(len(doc))

    # split file
    split_doc = split_document(doc, extension)

    print(len(split_doc))

    return split_doc


    
        


        

        
