import argparse

# from datetime import datetime
# from pick import pick
# from time import sleep
import pandas as pd


# Create wrapper classes for using news_sdk in place of newser
class NewsDataLoader:
    '''
    a class that will load news related datasets when provided path
    
    '''
    news_path = '../data/rating.csv'
    traffic_path = '../data/traffic.csv'
    domain_location_path = '../data/domains_location.csv'
    def __init__(self):
        '''
        data: Dictionary to store loaded data
        '''
        self.data = {}
    
    def load_data(self,path):
        if(path not in self.data):
            self.data[path] = pd.read_csv(path)
        return self.data[path]
    

    def get_news_data_path(self):        
        return self.news_path
    
    def get_traffic_data_path(self):        
        return self.traffic_path
    
    def get_domains_location_data_path(self):        
        return self.domain_location_path
    
    def get_news_data(self):        
        return pd.read_csv(self.get_news_data_path())
    
    def get_traffic_data(self):        
        return pd.read_csv(self.get_traffic_data_path())
      
    def get_domain_location_data(self):
        return pd.read_csv(self.get_domains_location_data_path())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Export news history')
    parser.add_argument('--zip', help="Name of a zip file to import")
    args = parser.parse_args()