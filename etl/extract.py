import requests
from urllib.parse import urlencode
from util.logger import Logger

class Extractor:
    def __init__(self, logger):
        self.logger = Logger.get_logger()

    def extract(self, config : dict):   
        data = []

        url = "https://api.github.com/search/repositories"
        pageSize = 100
        headers = {"Authorization" : f'token {config["github_token"]}'} if "github_token" in config else  {}
        paramters = {"q" : config["query"], "per_page" : pageSize}
        nextLink = f"{url}?{urlencode(paramters)}"
        lastLink = ""
        
        try:
            self.logger.info(f"Requesting the following url {nextLink}")
            
            lastIteration = False  
            while not lastIteration:     
                    if (nextLink == lastLink):
                        lastIteration = True

                    response = requests.get(url=nextLink, headers=headers, timeout=20)
                    response.raise_for_status()

                    # Get next and last links
                    if "Link" in response.headers:
                        link_dict = {part.split('rel="')[1].strip('"'): part.split(';')[0].strip('<> ') for part in response.headers["Link"].split(',')}
                        nextLink = link_dict.get("next", "")
                        lastLink = link_dict.get("last", "")
                    else:
                        lastIteration == True

                    data.extend(response.json().get("items", [])) 

            self.logger.info(f"{len(data)} data rows extracted.")

        except Exception as e:
            self.logger.error(f"Extract ran into the following error: {e}")
                 
        return data