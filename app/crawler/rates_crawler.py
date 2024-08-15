import requests
from bs4 import BeautifulSoup
import json

# URL of the page to scrape
url = "https://www.bnr.rw/currency/exchange-rate/"

# Send a request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table with the specified class
table = soup.find('table', class_='table')

# Initialize an empty list to store the data
data = []

# Iterate over each row in the table body
for row in table.find('tbody').find_all('tr'):
    cells = row.find_all('td')
    
    country = cells[0].find('img')['title']
    code = cells[1].get_text().strip()
    date = cells[2].get_text().strip()
    
    # Remove commas and convert to float
    buying_value = float(cells[3].get_text().strip().replace(',', ''))
    average_value = float(cells[4].get_text().strip().replace(',', ''))
    selling_value = float(cells[5].get_text().strip().replace(',', ''))
    
    # Append the data to the list as a dictionary
    data.append({
        'country': country,
        'code': code,
        'date': date,
        'buying_value': buying_value,
        'average_value': average_value,
        'selling_value': selling_value
    })

# Save the data to a JSON file
with open('bnroutput.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Data saved to bnroutput.json")
