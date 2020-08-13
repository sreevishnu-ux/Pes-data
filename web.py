from bs4 import BeautifulSoup
import pandas as pd
import requests as rq

url="https://www.pesmaster.com/pes-2020/"
get_url=rq.get(url)
soup=BeautifulSoup(get_url.text,"html.parser")
Name= [i.text for i in soup.findAll('div',{'class':'player-card-name'})]
Role= [i.text for i in soup.findAll('div',{'class':'player-card-position'})]


Table=pd.DataFrame({
    "Name":Name,
    "Role": Role})
Table.to_csv("pes.csv")