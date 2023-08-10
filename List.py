import pandas as pd
from bs4 import BeautifulSoup
import requests
url="https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue#"
page= requests.get(url)
soup= BeautifulSoup(page.text, "html")
#print(soup)
a= soup.find("table",class_="wikitable sortable")
#print(a)
b= table= soup.find_all("table")[1]
#print(b)
world_titles=soup.find_all("th")
#print(world_titles)
world_table_titles=[title.text.strip() for title in world_titles]
#print(world_table_titles)
df= pd.DataFrame(columns= world_table_titles)
columns_data=soup.find_all("tr")
for row in columns_data[2:][:102][:100]:
    row_data=row.find_all("td")
    individual_row_data=[data.text.strip() for data in row_data]
    print( individual_row_data)
    length= len(df)
    df.loc[length]=individual_row_data
