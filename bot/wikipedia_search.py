import wikipedia

def wikipedia_search(query):
    """
    Searches for a summary of the query on Wikipedia.

    Parameters:
    query (str): The search term.

    Returns:
    str: A summary of the search result or an error message.
    """
    try:
        if not query or query.strip() == "":
            raise ValueError("The search query cannot be empty.")
        
        # Fetch a summary of the topic
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query led to multiple results. Please be more specific. Suggestions: {', '.join(e.options[:5])}"
    except wikipedia.exceptions.PageError:
        return "No page found for the query. Please try a different search term."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
