from initialize import initialize_qa_system

def get_answer(question, context=None):
    """
    Get answer for a legal query
    
    Args:
        question (str): The question to ask
        context (str, optional): Additional context. Defaults to None.
    
    Returns:
        str: The answer to the question
    """
    qa_chain = initialize_qa_system()
    
    if context:
        result = qa_chain({"query": question, "context": context})
    else:
        result = qa_chain({"query": question})
    
    return result["result"]

# Example usage
if __name__ == "__main__":
    question = "If a owner does unauthorized structural changes to the property, what legal actions can the society take"
    answer = get_answer(question)
    print(answer)