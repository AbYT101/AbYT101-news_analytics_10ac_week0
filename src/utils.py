import os
import sys
import glob
import json
import datetime
from collections import Counter
from collections import Counter

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords


# from loader import NewsDataLoader
# loader = NewsDataLoader()

# _news_data = loader.load_data('../data/rating.csv')

def find_top_websites(data,url_column='url',top=10):
    data['domain'] = data[url_column].apply(lambda x: x.split('/')[2])

    #count occurences of each domain
    domain_counts = data['domain'].value_counts()

    top_domains = domain_counts.head(top)
    return top_domains
