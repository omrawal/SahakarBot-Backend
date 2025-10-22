from initialize import initialize_qa_system
from typing import List, Dict, Optional

def get_answer(question: str, chat_history: Optional[List[Dict[str, str]]] = None):
    """
    Get answer for a legal query with chat history context
    
    Args:
        question (str): The question to ask
        chat_history (List[Dict[str, str]], optional): List of previous QA pairs
            Each dict should have 'question' and 'answer' keys
    
    Returns:
        str: The answer to the question
    """
    qa_chain = initialize_qa_system()
    
    # Format chat history as context if provided
    context = ""
    if chat_history:
        context = "\n".join([
            f"Previous Q: {qa['question']}\nPrevious A: {qa['answer']}"
            for qa in chat_history[-3:]  # Only use last 3 conversations for context
        ])
    
    # Include chat history in the query
    if context:
        result = qa_chain({
            "query": question,
            "context": f"{context}\n\nCurrent question: {question}"
        })
    else:
        result = qa_chain({"query": question})
    
    return result["result"]