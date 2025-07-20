from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def create_summarization_chain():
    """
    Sets up and returns a LangChain chain for text summarization.
    """
    # --- LLM Setup ---
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct",
        task='text-generation'
    )
    model = ChatHuggingFace(llm=llm)
    parser = StrOutputParser()

    # --- Chain 1: Summarization ---
    template_summarize = PromptTemplate(
        template='Summarize the following text:\n\n{text}',
        input_variables=['text']
    )
    
    # Define and return the chain
    chain_summarize = template_summarize | model | parser
    return chain_summarize

def create_translation_chain():
    """
    Sets up and returns a LangChain chain for translation.
    """
    # --- LLM Setup ---
    # We can reuse the same model for both tasks
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct",
        task='text-generation'
    )
    model = ChatHuggingFace(llm=llm)
    parser = StrOutputParser()

    # --- Chain 2: Translation ---
    template_translate = PromptTemplate(
        template="Translate the following text into {language}:\n\n{text_to_translate}",
        input_variables=['language', 'text_to_translate']
    )
    
    # Define and return the chain
    chain_translate = template_translate | model | parser
    return chain_translate

