# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render , HttpResponse
from django.views.generic import TemplateView
# Create your views here.
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
import time

def scraper():
	url="http://gadgets.ndtv.com/?pfrom=home-header-globalnav"
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

	uClient=requests.get(url,headers=headers)
	time.sleep(3)
	page_html=uClient.text
	page_soup=soup(page_html,"html.parser")

	containers1=page_soup.find_all('div',class_="thumb")
	containers2=page_soup.find_all('div',class_="caption")

	item1 =[]
	item2=[]
	item3=[]

	for container in containers1:
		img=container.img["src"]
		item1.append(img)

	for container in containers2:
		text=container.text
		item2.append(text)

	for i in range(0,len(item1)):
	        item3.append(item1[i]+" : " + item2[i])

	return item1,item2


class HomeView(TemplateView):
	template_name="home/home.html"
	
	def get(self,request):
		file1,file2=scraper()
		length=len(file1)
		args={'file1':file1, 'file2':file2, 'n': range(length)}
		return render(request,self.template_name, args)