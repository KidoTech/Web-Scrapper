import pandas as pd
import asyncio
import requests
from bs4 import BeautifulSoup as soup
from requests_html import AsyncHTMLSession
import pyppdf.patch_pyppeteer

filename = 'price.csv'
label-Title = 'h1'
label-Ship = ''
label-Rate = '.overview-rating-average'
label-Price = '.product-price-value'

async def getURL(URL, label-Title, label-Price, label-Rate):
	header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
	asession = AsyncHTMLSession()
	r = await asession.get(URL)
	await r.html.arender()
	Title = r.html.find(label-Title)
	print(Title[0].text)


print('Start scrapping');
df = pd.read_csv(filename)
asyncio.get_event_loop().run_until_complete(getURL(URL))
print('Scrapping completed');