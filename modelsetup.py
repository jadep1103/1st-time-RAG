from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import LlamaCpp
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

def setup_model_and_components(model_path, text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(text_chunks, embedding=embeddings)
    llm = LlamaCpp(
        streaming=True,
        model_path=model_path,
        temperature=0.75,
        top_p=1,
        verbose=True,
        n_ctx=4096
    )
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vector_store.as_retriever(search_kwargs={"k": 2}))
    return qa
