from bs4 import BeautifulSoup
import requests
import csv
import os


source = requests.get('https://quotes.toscrape.com').text
soup = BeautifulSoup(source, 'lxml')


quotes = soup.find_all('div', class_='quote')


csv_file_name = 'quotes_data.csv'

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, csv_file_name)


with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(['Author', 'Quote', 'Tags'])
    
    # Loop through every quote found on the page
    for quote in quotes:
        # Extract the data for this specific quote
        author = quote.find('small', class_='author').text
        message = quote.span.text
        
        # Get all tags and join them into a single string separated by commas
        tags_list = [tag.text for tag in quote.find_all('a', class_='tag')]
        tags_string = ", ".join(tags_list)
        
        # Write this quote's data as a new row in the CSV
        writer.writerow([author, message, tags_string])

print(f"Successfully saved data to {file_path}")