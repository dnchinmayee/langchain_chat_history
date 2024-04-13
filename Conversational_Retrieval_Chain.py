from langchain_community.callbacks import get_openai_callback
from langchain.chains import ConversationalRetrievalChain
# from creds import openai_key, PINECONE_API_KEY, index_name
from langchain_openai import ChatOpenAI
import os
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv,find_dotenv


load_dotenv(find_dotenv(),override=True)
openai_key=os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
index_name = "pneindex"
# Initialize components
chat = ChatOpenAI(temperature=0, openai_api_key=openai_key, model="gpt-3.5-turbo-0125")
embeddings = OpenAIEmbeddings(api_key=openai_key, model="text-embedding-ada-002")
vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings, pinecone_api_key=PINECONE_API_KEY, text_key="chunk")

# Create conversational chain
chain = ConversationalRetrievalChain.from_llm(llm=chat, retriever=vectorstore.as_retriever(search_kwargs={'k': 3}))

chat_history = []
result = {}
while True:
    question = input("user: ")
    if question.lower() == "exit" or question.lower() == "quit":
        break
    else:
        with get_openai_callback() as cb:
            result = chain.invoke({"question": question, "chat_history": chat_history})
            print("------------------- TOEKN DETAILS ---------------------------")
            print("PROMPT TOEKNS --- ", cb.prompt_tokens)
            print("COMPLETION TOEKNS --- ", cb.completion_tokens)
            print("TOTAL TOEKNS --- ", cb.total_tokens)
        chat_history.append((question, result["answer"]))
        print("-------------ANSWER------------")
        print(result['answer'])
        print("-------------CHAT HISTORY------------")
        print(chat_history)

