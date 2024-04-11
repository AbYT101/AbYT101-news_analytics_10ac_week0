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
import re


# from loader import NewsDataLoader
# loader = NewsDataLoader()

# _news_data = loader.load_data('../data/rating.csv')

def find_top_websites(data,url_column='url',top=10):
    data['domain'] = data[url_column].apply(lambda x: x.split('/')[2])

    #count occurences of each domain
    domain_counts = data['domain'].value_counts()

    top_domains = domain_counts.head(top)
    return top_domains

def find_top_ten_websites_traffic(data, top = 10):
    sorted = data.sort_values('GlobalRank')

    # Filter the top 10 websites
    top_ten_websites_traffic = sorted['Domain'].head(10)

    return top_ten_websites_traffic

def find_top_country_with_domain_counts(data, domain):

    merged_data = data.merge(domain[['SourceCommonName', 'Country']], left_on='domain', right_on='SourceCommonName', how='left')
    merged_data = merged_data.drop(columns='SourceCommonName')
    top_ten_countries = merged_data['Country'].value_counts().head(10)

    return top_ten_countries

def find_countries_with_many_articles(data, domain):
    # Countries that have many articles written about them
    countries = domain['Country'].unique()
    category = data['category'].value_counts()
    country_categories = category[category.index.isin(countries)]
    
    return country_categories.head(10)


def find_african_countries_with_website_reporting_content(data):
    # Define the African countries
    african_countries = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Congo (Brazzaville)', 'Congo (Kinshasa)', "Cote d'Ivoire", 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']

    # Initialize counts for each African country
    african_country_counts = {country: 0 for country in african_countries}

    # Iterate over each article and count websites reporting news content for each African country
    for index, row in data.iterrows():
        for country in african_countries:
            # Check if the country is mentioned in the article content
            if country.lower() in row['content'].lower():
                african_country_counts[country] += 1

    # Convert counts to DataFrame for easier manipulation
    african_country_counts_df = pd.DataFrame.from_dict(african_country_counts, orient='index', columns=['Count'])

    # Get the top and bottom ten African countries with websites reporting news content
    top_ten_african_countries = african_country_counts_df.nlargest(10, 'Count')

    return top_ten_african_countries


def find_highest_count_of_positive_sentiment(data):
    # Websites with the highest count of positive sentiment news articles
    positive = data[data['title_sentiment'] == 'Positive']['source_name'].value_counts().head(10)

    return positive

def find_highest_count_of_neutral_sentiment(data):
    # Websites with the highest count of neutral sentiment news articles
    neutral = data[data['title_sentiment'] == 'Neutral']['source_name'].value_counts().head(10)

    return neutral

def find_highest_count_of_negative_sentiment(data):
    # Websites with the highest count of Negative sentiment news articles
    negative = data[data['title_sentiment'] == 'Negative']['source_name'].value_counts().head(10)

    return negative