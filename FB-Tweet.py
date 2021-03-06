import threading
import tweepy
import facebook
import random
import logging
import schedule
import time
from PIL import Image, ImageFont, ImageDraw, ImageOps
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import requests
from io import BytesIO

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )
#Variable

import os
consumer_key = os.environ['CONKEY']
consumer_secret = os.environ['CONSECRET']
twitter_token =  os.environ['ACCTOKEN']
acc_secret = os.environ['TOKENSEC']
fb_token = os.environ['TOKEN_PAINTMIN'] 
'''
#for local use or DEBUG
from keys import keys
consumer_key = keys['CONKEY']
consumer_secret = keys['CONSECRET']
twitter_token =  keys['ACCTOKEN']
acc_secret = keys['TOKENSEC']
fb_token = keys['TOKEN_DEBUG'] 

'''
#scrapers
def profilescrape(oshi:str):
	html = urlopen(f'https://mnl48.hallohallo.com/profile/{oshi}')
	soup = BeautifulSoup(html, 'html.parser')
	imgs = soup.find_all('img', attrs={'height':'360'})
	urls =[]
	for i in imgs:
		f= i['src']
		urls.append(f)
	urls
	imgurls = random.choice(urls)
	urllib.request.urlretrieve(imgurls, "oshi.png")

def image(oshi, adjs):

	html = urlopen(f'https://mnl48.hallohallo.com/profile/{oshi}')
	soup = BeautifulSoup(html, 'html.parser')
	imgs = soup.find_all('img', attrs={'height':'360'})
	urls =[]
	for i in imgs:
		f= i['src']
		urls.append(f)
	urls
	imgurls = random.choice(urls)
	urllib.request.urlretrieve(imgurls, "oshi.png")

	size = width, height = 600, 338;

	image = Image.new('RGB', size, 'white') ; profile = Image.open('oshi.png') ; bg = Image.open('bg.png')
	image.paste(bg,(0,0)) ;
	w, h = profile.size
	cropped = profile.crop((54, 0, w-54, 360))

	out = cropped.resize((193,275), Image.LANCZOS)

	image.paste(out,(45,32))
	draw = ImageDraw.Draw(image)
	GothamBold20 = ImageFont.truetype('GothamBold.ttf', 20) ;GothamBold50 = ImageFont.truetype('GothamBold.ttf', 30)
	draw.text((310, 230),f'Our MNL48 {oshi} is', font=GothamBold20, fill='#000000')
	draw.text((305, 250),f'{adjs}.', font=GothamBold50, fill='#000000')	
	image.save('outfile.png','PNG')
	del image
	del draw

#Posters
def facebookpost(oshi:str, adjective:str):
	'''Posting the object to Facebook via GRAPH APi.'''
	graph = facebook.GraphAPI(access_token=fb_token, version="3.1")
	post = graph.put_photo(image=open('outfile.png',"rb"),
                message=f'Our oshi MNL48 {oshi} is {adjective}.')

	graph.put_object(parent_object=post['post_id'], connection_name='comments',
                  message='Is this true?')

def twitterpost(oshi:str, adjective:str):
	'''Posting the object to Twitter via TWITTER APi.'''
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
	auth.set_access_token(twitter_token, acc_secret) 
	api = tweepy.API(auth) 

	image_path = 'outfile.png'
	tweet = f'Our oshi MNL48 {oshi} is {adjective}. #MNL48 #MNL48{oshi}'
	status = api.update_with_media(image_path, tweet)

	return
#Main Threader
def revthread():
	'''Randomized the data and start the thread.'''
	#Randomizer
	text_file1 = open("adj.txt", "r")
	adjran = random.choice(text_file1.readlines())
	adj = adjran.replace('\n','')

	text_file2 = open("mnlmem.txt", "r")
	oshiran = random.choice(text_file2.readlines())
	oshis = oshiran.replace('\n','')

	image(oshi=oshis, adjs=adj)

	def fbthread():
		'''Running for fb thread.'''
		logging.debug('Starting Facebook Thread')
		facebookpost(oshi=oshis, adjective=adj)
		logging.debug('=====================SUCCESS POSTING FB, Exiting....=====================')


	def twitterthread():
		'''Running for twitter thread.'''
		logging.debug('Starting Twitter Thread')
		twitterpost(oshi=oshis, adjective=adj)
		logging.debug('=====================SUCCESS POSTING TW,Exiting....=====================')
	
	fb = threading.Thread(name='Facebook API', target=fbthread)	
	tw = threading.Thread(name='Twitter API', target=twitterthread)

	fb.start()
	tw.start()
	
schedule.every().hour.at(':35').do(revthread) # run every xx:35:xx / 35 * * * * on cron 
schedule.every().hour.at(':05').do(revthread) # run every xx:05:xx / 5 * * * * on cron 
    
while 1:
    schedule.run_pending()
    time.sleep(1)
