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
    def __init__(self):
        '''
        data: Dictionary to store loaded data
        '''
        self.data = {}
    
    def load_data(self,path):
        if(path not in self.data):
            self.data[path] = pd.read_csv(path)
        return self.data[path]

   



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Export news history')
    parser.add_argument('--zip', help="Name of a zip file to import")
    args = parser.parse_args()
