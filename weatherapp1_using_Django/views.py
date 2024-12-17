from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url='https://www.timeanddate.com/weather/'
res=requests.get(url).content
soup=BeautifulSoup(res,'html.parser')


def home(request,soup=soup):
    date=datetime.today().date
    data=soup.find('span',class_='my-city__city')
    data1=soup.find('span',class_='my-city__temp')
    data2=soup.find('span',class_='my-city__wtdesc')
   
    return render(request,'index.html',{'city':data.text,'temp':data1.text,'condition':data2.text,'date':date})