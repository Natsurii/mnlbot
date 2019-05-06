import tweepy
import random
import os

consumer_key = os.environ['CONKEY']
consumer_secret = os.environ['CONSECRET']
access_token =  os.environ['ACCTOKEN']
acc_secret = os.environ['TOKENSEC']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, acc_secret) 

text_file1 = open("adj.txt", "r")
adj = random.choice(text_file1.readlines()).replace('\n','')
text_file2 = open("mnlmem.txt", "r")
oshi = random.choice(text_file2.readlines())
oshis = oshi.replace('\n','')

api = tweepy.API(auth) 
 # toDo 
image_path = f'images/{oshis}.png'
tweet = f'Our oshi MNL48 {oshis} is{adj}.'  # toDo 


# to attach the media file 
status = api.update_with_media(image_path, tweet)
