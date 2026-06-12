import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titles = []
companies = []
locations = []
dates = []

jobs = soup.find_all("div", class_="card-content")

for job in jobs:
    # Job Title
    title = job.find("h2", class_="title").text.strip()

    # Company Name
    company = job.find("h3", class_="company").text.strip()

    # Location
    location = job.find("p", class_="location").text.strip()

    # Date
    date = job.find("time")["datetime"].strip()

    titles.append(title)
    companies.append(company)
    locations.append(location)
    dates.append(date)

df = pd.DataFrame({
    "Title": titles,
    "Company": companies,
    "Location": locations,
    "Date": dates
})

print(df.head())
