import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

URL = "http://books.toscrape.com/catalogue/page-{}.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def get_product_data():
    all_products = []
    for page in range(1, 3):  # First 2 pages for demo
        response = requests.get(URL.format(page), headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('article', class_='product_pod')

        for product in products:
            title = product.h3.a['title']
            price = product.find('p', class_='price_color').text.strip()
            availability = product.find('p', class_='instock availability').text.strip()
            rating = product.p['class'][1]

            all_products.append({
                'Title': title,
                'Price': price,
                'Availability': availability,
                'Rating': rating
            })

    df = pd.DataFrame(all_products)
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/latest_prices.csv', index=False)
    return df

if __name__ == '__main__':
    get_product_data()
