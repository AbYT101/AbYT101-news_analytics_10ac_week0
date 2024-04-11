import unittest
from src.loader import NewsDataLoader
import pandas as pd

class Test(unittest.TestCase):
    
    def setUp(self):
        self.loader = NewsDataLoader()

    def test_get_news(self):
        expected_file = pd.read_csv('../data/rating.csv')
        self.assertEqual(self.loader.get_news_data(), expected_file)

    def test_get_traffic(self):
        expected_file = pd.read_csv('../data/traffic.csv')
        self.assertEqual(self.loader.get_traffic_data(), expected_file)

    def test_get_domain_location(self):
        expected_file = pd.read_csv('../data/traffic.csv')
        self.assertEqual(self.loader.get_domain_location_data(), expected_file)

if __name__ == '__main__':
    unittest.main()