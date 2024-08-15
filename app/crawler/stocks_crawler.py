import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# URL of the page to scrape
url = "https://www.rse.rw/"

# Send a GET request to the URL
response = requests.get(url, verify=False)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table with the class 'main__table'
table = soup.find('table', class_='main__table')

# Initialize a list to hold the extracted data
data = []

# Get today's date
today_date = datetime.now().strftime('%Y-%m-%d')

# Iterate through each row in the table body
for row in table.find('tbody').find_all('tr'):
    cells = row.find_all('td')
    
    # Extract data from each cell
    company_name = cells[0].get_text(strip=True)
    closing_price = cells[1].get_text(strip=True).replace(',', '')
    
    # Add the data to the list in the specified format
    data.append({
        'company': company_name,
        'date': today_date,
        'price': float(closing_price)
    })

# Save the data to a JSON file
with open('stocks_output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Data saved to stocks_output.json")
