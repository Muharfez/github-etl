import requests
from urllib.parse import urlencode
from util.logger import AppLogger

def extract(query : str, token : str):   
    data = []
    logger = AppLogger().get_logger() 

    url = "https://api.github.com/search/repositories"
    pageSize = 100
    headers = {"Authorization" : f"token {token}"} if token else  {}
    paramters = {"q" : query, "per_page" : pageSize}
    nextLink = f"{url}?{urlencode(paramters)}"
    lastLink = ""
    
    lastIteration = False 
    while not lastIteration:
        try:
            if (nextLink == lastLink):
                lastIteration = True

            logger.info(f"Requesting the following url {nextLink}")

            response = requests.get(url=nextLink, headers=headers, timeout=20)
            response.raise_for_status()

            ## Get next and last links
            if "Link" in response.headers:
                link_dict = {part.split('rel="')[1].strip('"'): part.split(';')[0].strip('<> ') for part in response.headers["Link"].split(',')}
                nextLink = link_dict.get("next", "")
                lastLink = link_dict.get("last", "")
            else:
                lastIteration == True

            data.extend(response.json().get("items", [])) 
        
        except Exception as e:
            logger.error(f"Extract ran into the following error: {e}")
            break      
    
    return data