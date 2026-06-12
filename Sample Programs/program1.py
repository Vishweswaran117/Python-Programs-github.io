# import requests
# url = "https://jsonplaceholder.typicode.com/posts"
# response = requests.get(url)


# import pandas as pd

# df = pd.DataFrame(response.json())
# print(df)

# https://books.toscrape.com/


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send HTTP request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all h2 headings
headings = soup.find_all("h3")

book_titles = []

for i in headings:
    book_titles.append(i.a.text)


book_details = {
    'title': book_titles
}

df = pd.DataFrame(book_details)





