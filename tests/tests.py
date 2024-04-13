import unittest
import sys, os
if os.path.abspath("..") not in sys.path:
    sys.path.insert(0, os.path.abspath(".."))

import matplotlib.pyplot as plt

from src import NewsDataLoader
import pandas as pd

class Test(unittest.TestCase):
    
    def setUp(self):
        self.loader = NewsDataLoader()

    def test_get_news(self):
        expected_file_path = '../data/rating.csv'
        self.assertEqual(self.loader.get_news_data_path(), expected_file_path)

    def test_get_traffic(self):
        expected_file_path = '../data/traffic.csv'
        self.assertEqual(self.loader.get_traffic_data_path(), expected_file_path)

    def test_get_domain_location(self):
        expected_file_path = '../data/domains_location.csv'
        self.assertEqual(self.loader.get_domains_location_data_path(), expected_file_path)

if __name__ == '__main__':
    unittest.main()