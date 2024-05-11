import requests
from bs4 import BeautifulSoup

def find_csv_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Look for anchor tags containing download links
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href and 'csv' in href:
            print("Found CSV link:", href)

# Call the function with the URL you are interested in
find_csv_links('https://platform.who.int/mortality/themes/theme-details/mdb/noncommunicable-diseases')
