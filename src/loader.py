import csv
import argparse
import os
import io
import shutil
import copy
from datetime import datetime
from pick import pick
from time import sleep



# Create wrapper classes for using news dataset in place of news
class NewsDataLoader:
    '''
     
    '''
    def __init__(self, path):
        '''
        path: path to the news exported data folder
        '''
        self.path = path
        self.data = self.get_data()
        self.traffic = self.get_traffic()
        self.rating = self.get_rating()
    

    def get_data(self):
        '''
        write a function to get all the data from the csv file
        '''
        with open(os.path.join(self.path, 'data.csv'), 'r') as f:
            data = csv.reader(f)

        return data
    
    def get_traffic(self):
        '''
        write a function to get all the traffic from the csv file
        '''
        with open(os.path.join(self.path, 'traffic.csv'), 'r') as f:
            traffic = csv.reader(f)

        return traffic

    def get_rating(self):
        '''
        write a function to get all the rating from the csv file
        '''
        with open(os.path.join(self.path, 'rating.csv'), 'r') as f:
            rating = csv.reader(f)

        return rating
