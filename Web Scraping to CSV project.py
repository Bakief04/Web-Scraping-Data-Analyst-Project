#!/usr/bin/env python
# coding: utf-8

# In[5]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

table = soup.find_all('table')[1]
world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]

df = pd.DataFrame(columns = world_table_titles)
df

column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all("td")
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)
    
    length = len(df)
    df.loc[length] = individual_row_data

# Saves out to csv file. If file is needed, Paste in file path with a file name (Example: File.csv)
df.to_csv(r'', index = False)


# In[ ]:




