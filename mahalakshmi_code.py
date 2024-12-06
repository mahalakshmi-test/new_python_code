import requests
import pandas as pd
from bs4 import BeautifulSoup

def fetch_wikipedia_table(url, table_index=0):

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the page: {url}")
        return None

    soup = BeautifulSoup(response.content, "html.parser")

    tables = pd.read_html(str(soup))

    if table_index >= len(tables):
        print(f"Table index {table_index} is out of range. This page has {len(tables)} tables.")
        return None

    return tables[table_index]


url = "https://meta.wikimedia.org/wiki/List_of_Wikipedias/Table"
table_index = 0
table = fetch_wikipedia_table(url, table_index)

if table is not None:
    table.head()
    table.to_csv("output.csv", index=False)

df = pd.read_csv("output.csv")


def findTotalArticlesByLanguages(languages):
  x = [i for i in df["Articles"]]
  y = [j for j in df["Language"]]

  print("Sum of articles as per Languages : ",sum(x))
  print("Languages list : ",y)
findTotalArticlesByLanguages(df["Language"])
