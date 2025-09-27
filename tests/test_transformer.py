import unittest
from etl.transformer import Transformer

class TestTransformer(unittest.TestCase):
    def setUp(self):
        self.mock_data = [
            {"full_name": f"repo{i}", "language": "Python", "stargazers_count": 1500+i, "forks_count": 10+i,
             "created_at": "2023-01-01T00:00:00Z", "updated_at": "2025-09-01T00:00:00Z"}
            for i in range(12)
        ] + [
            {"full_name": "repo_java", "language": "Java", "stargazers_count": 50, "forks_count": 5,
             "created_at": "2022-06-01T00:00:00Z", "updated_at": "2025-01-01T00:00:00Z"},
            {"full_name": "repo_none", "language": None, "stargazers_count": 10, "forks_count": 1,
             "created_at": "2022-01-01T00:00:00Z", "updated_at": "2023-01-01T00:00:00Z"}
        ]
        self.transformer = Transformer()

    def test_transform_filters_null_language(self):
        df = self.transformer.transform(self.mock_data)
        self.assertEqual(df["language"].isnull().sum(), 0)

    def test_transform_filters_languages(self):
        df = self.transformer.transform(self.mock_data)
        self.assertTrue(all(df["language"] == "python"))

if __name__ == "__main__":
    unittest.main()