import requests
from bs4 import BeautifulSoup

def find_csv_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Look for anchor tags containing download links
        links_found = False
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and 'csv' in href:
                print("Found CSV link:", href)
                links_found = True
        
        if not links_found:
            print("No CSV links found.")
    else:
        print(f"Failed to retrieve page, status code: {response.status_code}")

# Example call to the function
find_csv_links('https://platform.who.int/mortality/themes/theme-details/mdb/noncommunicable-diseases')
