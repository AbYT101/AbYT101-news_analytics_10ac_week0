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
    # Calculate traffic counts for each website
    website_traffic_counts = data.groupby('Domain')['GlobalRank'].min()

    # Get the top and bottom ten websites
    top_ten_websites_traffic = website_traffic_counts.nlargest(10)

    top_domains = top_ten_websites_traffic.head(top)
    return top_domains

def find_top_country_domain_counts(data):

    # Calculate the count of domains for each country
    country_domain_counts = data['Country'].value_counts()

    # Get the top and bottom ten countries
    top_ten_countries = country_domain_counts.head(10)
    return top_ten_countries

def find_countries_with_many_articles(data):
    # Extract mentions of countries from the article content
    countries = ["Africa", "US", "China", "EU", "Russia", "Ukraine", "Middle East"]  # List of countries to search for

    # Initialize counts for each country
    country_counts = {country: 0 for country in countries}

    # Iterate over each article and count mentions of countries
    for content in data['content']:
        for country in countries:
            # Count occurrences of the country in the content
            country_counts[country] += len(re.findall(r'\b{}\b'.format(country), str(content), re.IGNORECASE))

    # Convert counts to DataFrame for easier manipulation
    country_counts_df = pd.DataFrame.from_dict(country_counts, orient='index', columns=['Count'])

    # Calculate the count of domains for each country
    country_domain_counts = data['Country'].value_counts()

    # Get the top and bottom ten countries
    top_ten_countries = country_domain_counts.head(10)
    return top_ten_countries

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