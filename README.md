```
# LangChain Conversational Retrieval Chain

This script demonstrates the creation of a conversational retrieval chain using the LangChain framework. It involves setting up a ChatOpenAI instance, OpenAI embeddings, and a Pinecone vector store to create a conversational retrieval chain.

## Components

### ChatOpenAI

The ChatOpenAI instance is initialized with the following parameters:
- `temperature`: Set to 0 for deterministic responses.
- `openai_api_key`: The API key for OpenAI.
- `model`: The model to use, in this case "gpt-3.5-turbo-0125".

### OpenAIEmbeddings

The OpenAIEmbeddings component is initialized with the following parameters:
- `api_key`: The OpenAI API key.
- `model`: The model to use for embeddings, in this case "text-embedding-ada-002".

### PineconeVectorStore

The PineconeVectorStore component is initialized with the following parameters:
- `index_name`: The name of the Pinecone index.
- `embedding`: The OpenAIEmbeddings instance.
- `pinecone_api_key`: The Pinecone API key.
- `text_key`: The key for the text data, in this case "chunk".

## Conversational Chain

A conversational retrieval chain is established using the ChatOpenAI instance as the language model (LLM) and the Pinecone vector store as the retriever with search parameters set to return 3 results.

## User Interaction Loop

The script enters a loop where it prompts the user for input, processes the input through the conversational chain, and displays token details related to the OpenAI callback. It then updates the chat history with the user's question and the model's answer.

## Usage

To use this script, you'll need to set up the necessary environment variables for the OpenAI and Pinecone API keys. Then, simply run the script and interact with the model through the command line.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

