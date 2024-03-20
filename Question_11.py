'''Basic Web Scraper: Write a web scraper that extracts data from a website of interest. 
You can use libraries like BeautifulSoup and requests for this task.'''

import requests
from bs4 import BeautifulSoup

# Defining Function to scrape BBC News headlines
def scrape_bbc_news_headlines():
    # URL of the BBC News website
    url = 'https://www.bbc.com/news'

    # Send a GET request to the URL
    response = requests.get(url)

    # Checking if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all headline elements with the specified class
        headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')

        # Extract and print the text of each headline
        for headline in headlines:
            print(headline.get_text().strip())
    else:
        print("Failed to retrieve BBC News headlines.")

# Defining Main function to run the web scraper
def main():
    print("Scraping BBC News headlines...\n")
    scrape_bbc_news_headlines()

if __name__ == "__main__":
    main()
