import requests
from bs4 import BeautifulSoup
import pandas
import sqlalchemy
"""
Key Features:
1. Which color of shirt is the mean color?
2. Which color is mostly worn throughout the week?
3. Which color is the median?
4. BONUS Get the variance of the colors
5. BONUS if a colour is chosen at random, what is the probability that the color is red?
6. Save the colours and their frequencies in postgresql database
"""

# Replace url with appropriate url
url = "http://127.0.0.1:3000/interview.html"

def main():
    df = get_table(url)

    # Feature 1, 3 and 4 cannot be implemented as such calculations can only
    # be done on continuous variables. Table presented contains categorical
    # variables.

    # Feature 2: Which color is mostly worn throughout the week?
    most_worn_colour = df.stack().mode().iloc[0]
    print(f"The most worn colour throughout the week was: {most_worn_colour}")

    # Feature 5: if a colour is chosen at random, what is the probability that
    # the color is red?
    frequency = df.stack().value_counts()
    red_freq = frequency['RED']
    total = frequency.sum()
    probability = red_freq / total
    print(
        "The probability that a colour chosen at random is red is:",
        f"{probability} or {probability:.2%}"
        )
    
    # Feature 6: Save the colours and their frequencies in postgresql database
    save_to_db(frequency)


def save_to_db(df):
    # Replace these with your PostgreSQL details
    username = 'charis'
    password = 'ayanfeoluwa'
    host = 'localhost'  # or your database host
    port = '5432'       # default PostgreSQL port
    database = 'bincom'

    # Create the connection string
    connection_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'

    # Create the SQLAlchemy engine
    engine = sqlalchemy.create_engine(connection_string)

    df = df.to_frame(name='frequency')
    df.to_sql('colour_frequency', engine, if_exists='replace', index=True)

    df_from_db = pandas.read_sql('SELECT * FROM colour_frequency', engine)
    print(df_from_db)


def get_table(url):
    """
    A function that scrapes a webpage, gets the first table on the page and
    loads the content of the table unto a pandas data frame
    """
    # Fetch content from url
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    # Extract table from content
    table = soup.find('table')

    # Create Dict to store table
    colours_dict = {}

    # Extract rows from table and store in dict
    for tr in table.find_all('tr'):
        row = tr.find_all('td')
        colours_dict[row[0].get_text()] = row[1].get_text(strip=True).replace(',', '').split()

    # Load dict unto data frame for easy manipulation and return df
    return pandas.DataFrame(colours_dict)


if __name__ == '__main__':
    main()
