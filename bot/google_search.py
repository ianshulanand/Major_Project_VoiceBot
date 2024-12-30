import requests

# Replace 'your_api_key' and 'your_cse_id' with your actual Google API key and Custom Search Engine ID.
API_KEY = "AIzaSyDe-Sj-u_cJpPm_7iMu50PaDjtpexV5A3I"
CSE_ID = "e1f8ab58089374ed1" #Search Engine ID

def google_search(query):
    """
    Performs a Google search using the Custom Search JSON API.

    Parameters:
    query (str): The search query.

    Returns:
    str: Top search results with titles and links.
    """
    if not query.strip():
        return "Search query cannot be empty."

    try:
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CSE_ID}&q={query}"
        #url = f"https://www.google.com/search?q={query}&sca_esv=8324505d2d7d6421&source=hp&ei=7UJxZ82yNObs1e8P4LTT0Qw&iflsig=AL9hbdgAAAAAZ3FQ_Yf5btzx5XomUjbdOGuEpmRTpT3b&ved=0ahUKEwiN3Yfc_8yKAxVmdvUHHWDaNMoQ4dUDCBA&uact=5&oq=hi&gs_lp=Egdnd3Mtd2l6IgJoaTINEAAYgAQYsQMYQxiKBTINEAAYgAQYsQMYQxiKBTINEAAYgAQYsQMYQxiKBTINEAAYgAQYsQMYQxiKBTIQEAAYgAQYsQMYQxiDARiKBTIQEAAYgAQYsQMYQxiDARiKBTIIEAAYgAQYsQMyDRAAGIAEGLEDGEMYigUyEBAAGIAEGLEDGEMYgwEYigUyDRAuGIAEGEMY1AIYigVI-wFQAFgLcAB4AJABAZgB3AGgAfYCqgEFMC4xLjG4AQPIAQD4AQGYAgGgArMBmAMAkgcDMC4xoAfnDQ&sclient=gws-wiz"
        
        response = requests.get(url)
        
        if response.status_code != 200:
            return f"Failed to fetch results. HTTP Status Code: {response.status_code}"
        else:
            data = response.json()
            

        if "items" not in data:
            return "No results found."
        else:
            results = data["items"]
        
            output = ""
            for item in results[:5]:  # Fetch top 5 results
                title = item.get("title", "No Title")
                link = item.get("link", "No Link")
                output += f"{title}\n{link}\n\n"

            return output.strip()
    
    except Exception as e:
        return f"An error occurred: {str(e)}"
