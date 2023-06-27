#privateGPT (Color Theory GPT)

Ask questions about color theory and receive answers using the power of the privateGPT model. This AI-powered language model is designed to provide accurate responses based on the extensive knowledge it has acquired from a range of color theory source materials. Color Theory GPT ensures complete privacy, as no data leaves your execution environment during the question-answering process.

## Features

- **Private Question Answering:** Color Theory GPT allows you to ask questions and obtain answers without the need for an internet connection. All processing occurs locally within your execution environment.
- **Comprehensive Color Theory Knowledge:** The model has been trained on a diverse set of color theory source materials, enabling it to provide insightful and informed answers to questions on various color theory topics.
- **Wide Range of Supported Documents:** Color Theory GPT supports a variety of document types, including CSV, Word documents (DOCX and DOC), EverNote, email files (EML), EPub, HTML, Markdown, Outlook Message (MSG), Open Document Text (ODT), PDF, and PowerPoint documents (PPTX and PPT).
- **Flexible Model Selection:** You can choose between the LlamaCpp or GPT4All models as the underlying language model for color theory question answering.
- **Efficient Context Retrieval:** The model retrieves relevant context from the ingested documents stored in a local vector store, allowing it to generate answers based on the most appropriate information.
- **Easy Environment Setup:** Color Theory GPT provides clear instructions for environment setup, including installing requirements and downloading the necessary language models.

## Usage

To use Color Theory GPT, follow these steps:

1. **Environment Setup:** Set up your environment by installing the required dependencies listed in the README file. Download the LLM model of your choice and place it in a directory. Configure the `.env` file with the appropriate variables.
2. **Ingest Your Documents:** Prepare your color theory source materials by placing them in the `source_documents` directory. Ensure your documents are in one of the supported formats listed in the README.
3. **Run Ingestion Script:** Execute the `ingest.py` script to ingest your documents and create embeddings. This process will create a local vector store with the accumulated information from your source materials.
4. **Ask Questions:** Run the `privateGPT.py` script and enter your color theory-related questions when prompted. Color Theory GPT will utilize the local LLM model to process your question and provide answers based on the context retrieved from the local vector store.
5. **Review and Repeat:** Read the generated answer along with the sources used for context. You can continue asking questions without rerunning the script; simply wait for the prompt and enter your next query.

Please note that the initial download of the embeddings model might require an internet connection, but the subsequent usage of the model does not rely on an internet connection.

## Limitations

While Color Theory GPT aims to provide accurate and private question answering, it has some limitations:

- **Test Project Disclaimer:** Color Theory GPT is a test project and not intended for production use. Its model selection prioritizes privacy over performance, and optimizations for specific use cases may be required.
- **Limited to Document Context:** The model relies on the context provided by the ingested color theory documents to generate answers. It may not have access to real-time information or internet sources.
- **Visual Analysis Limitations:** Color Theory GPT primarily processes textual information and may have limitations in analyzing visual elements or color-related images.
- **Model Performance:** The performance of the model may vary based on your machine specifications and the size of the documents being processed.

## System Requirements

Ensure that your system meets the following requirements:

- **Python Version:** Color Theory GPT requires

 Python 3.10 or later to function correctly. Earlier versions of Python may not be compatible.
- **C++ Compiler:** If you encounter any errors during the installation process, such as while building a wheel, you may need to install a C++ compiler. Refer to the README file for specific instructions based on your operating system.

## Disclaimer

Color Theory GPT is an experimental project aimed at exploring the feasibility of a privacy-focused question answering solution using language models and vector embeddings. It is not intended for production use and may not meet performance optimization requirements. Exercise caution and use your discretion when relying on the information provided by Color Theory GPT.
