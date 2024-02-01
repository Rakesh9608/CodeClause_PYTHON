import requests
from bs4 import BeautifulSoup

# Specify the URL of the website you want to scrape
url = 'https://codeclause.com'

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract information from the page
    # For example, let's extract all the links on the page
    links = soup.find_all('a')
    
    # Print the extracted links
    for link in links:
        print(link.get('href'))

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
