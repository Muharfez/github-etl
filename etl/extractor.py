import requests
from urllib.parse import urlencode
from util.logger import Logger

class Extractor:
    def __init__(self, config : dict):
        self.logger = Logger().get_logger()
        self.config = config

    def extract(self):   
        data = []

        url = "https://api.github.com/search/repositories"
        page = 1
        pages_size = self.config["page_size"]

        parameters = {"q" : self.config["query"], "per_page" : pages_size, "page" : page}
        headers = {"Authorization" : f'token {self.config["github_token"]}'} if "github_token" in self.config else  {}

        try:
            while True:
                    parameters["page"] = page
                    nextLink = f"{url}?{urlencode(parameters)}"     
                    self.logger.info(f"Requesting the following url: {nextLink}")
        
                    response = requests.get(url=nextLink, headers=headers, timeout=20)
                    response.raise_for_status()

                    data.extend(response.json().get("items", [])) 
                    link_header = response.headers.get("Link", "")
                    if 'rel="next"' not in link_header:
                        break
                    page += 1

        except Exception as e:
            self.logger.error(f"Extract ran into the following error: {e}")

        self.logger.info(f"{len(data)} repos extracted.")         
        return data