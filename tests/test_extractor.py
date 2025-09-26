import unittest
from unittest.mock import patch, MagicMock
from etl.extractor import Extractor

class TestExtractor(unittest.TestCase):
    def setUp(self):
        config = {
            "query": "Data Engineering",
            "github_token": "fake_token"
        }
        self.extractor = Extractor(config=config)

    @patch("etl.extractor.requests.get")
    def test_pagination(self, mock_get):
        # Mock responses for page 1 and 2
        mock_response_page1 = MagicMock()
        mock_response_page1.status_code = 200
        mock_response_page1.json.return_value = {"items": [{"id": 1}, {"id": 2}]}
        mock_response_page1.headers = {
            "Link": '<https://api.github.com/search/repositories>; rel="next", <https://api.github.com/search/repositories>; rel="last"'
        }

        mock_response_page2 = MagicMock()
        mock_response_page2.status_code = 200
        mock_response_page2.json.return_value = {"items": [{"id": 3}]}
        mock_response_page2.headers = {"Link": ""}  # no next page

        # Configure mock_get to return page1 then page2
        mock_get.side_effect = [mock_response_page1, mock_response_page2]
        all_items = self.extractor.extract()

        # Assert all items from both pages were collected
        self.assertEqual(len(all_items), 3)

        # Assert requests.get was called twice (for two pages)
        self.assertEqual(mock_get.call_count, 2)    

if __name__ == "__main__":
    unittest.main()