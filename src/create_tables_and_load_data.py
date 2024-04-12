from db_connecor import DBConnector
import csv
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get database connection information from environment variables
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

# Function to check if tables exist in the database
def tables_exist(cursor):
    cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM   information_schema.tables 
            WHERE  table_schema = 'public'
            AND    table_name = 'articles_table'
        );
    """)
    articles_table_exists = cursor.fetchone()[0]

    cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM   information_schema.tables 
            WHERE  table_schema = 'public'
            AND    table_name = 'domains_location_table'
        );
    """)
    domains_location_table_exists = cursor.fetchone()[0]

    cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM   information_schema.tables 
            WHERE  table_schema = 'public'
            AND    table_name = 'traffic_data_table'
        );
    """)
    traffic_data_table_exists = cursor.fetchone()[0]

    return articles_table_exists and domains_location_table_exists and traffic_data_table_exists

# Function to create articles table
def create_articles_table(cursor):
    cursor.execute("""
        CREATE TABLE articles_table (
            article_id SERIAL PRIMARY KEY,
            source_id TEXT,
            source_name TEXT,
            author TEXT,
            title TEXT,
            description TEXT,
            url TEXT,
            url_to_image TEXT,
            published_at TIMESTAMP,
            content TEXT,
            category TEXT,
            article TEXT,
            title_sentiment FLOAT
        );
    """)

# Function to create domains location table
def create_domains_location_table(cursor):
    cursor.execute("""
        CREATE TABLE domains_location_table (
            source_common_name TEXT PRIMARY KEY,
            location TEXT,
            country TEXT
        );
    """)

# Function to create traffic data table
def create_traffic_data_table(cursor):
    cursor.execute("""
        CREATE TABLE traffic_data_table (
            global_rank INT PRIMARY KEY,
            tld_rank INT,
            domain TEXT,
            tld TEXT,
            ref_subnets INT,
            ref_ips INT,
            idn_domain TEXT,
            idn_tld TEXT,
            prev_global_rank INT,
            prev_tld_rank INT,
            prev_ref_subnets INT,
            prev_ref_ips INT
        );
    """)

# Function to load data from CSV into PostgreSQL table
def load_data_from_csv(cursor, table_name, csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            cursor.execute(f"INSERT INTO {table_name} VALUES (%s);" % ','.join(['%s']*len(row)), row)

def main():
    # Connect to PostgreSQL database
    connector = DBConnector(
        dbname="your_database_name",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cursor = connector.get_cursor()

    # Check if tables exist
    if not tables_exist(cursor):
        # Create tables
        create_articles_table(cursor)
        create_domains_location_table(cursor)
        create_traffic_data_table(cursor)

        # Load data into tables
        load_data_from_csv(cursor, 'articles_table', 'data.csv')
        load_data_from_csv(cursor, 'domains_location_table', 'domains_location.csv')
        load_data_from_csv(cursor, 'traffic_data_table', 'traffic_data.csv')

        # Commit changes
        connector.commit()
        print("Tables created and data loaded successfully.")
    else:
        print("Tables already exist. Skipping creation and data loading.")

    # Close cursor and connection
    connector.close()

if __name__ == "__main__":
    main()
