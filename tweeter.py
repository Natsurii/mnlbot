import tweepy
import random

consumer_key = 'FhLPQx359JdCVQAMtJrXBNwbY'#os.environ['CONKEY']
consumer_secret = '27B4WFjCq761Dsf9fx9xIywI9203kPcgqeiQUFHVxi3Dhsl8ce' #os.environ['CONSECRET']
access_token = '1124296742902554624-nWC7mKGPhpec5CYMgYkgIsLiA7oAnk'#os.environ['TOKEN']
acc_secret = 'zMvHpAa0GiXuhXv5Uq0KG7SxSBwcAKoQVzSEZwIy72BZC'#os.environ['TOKENSEC']


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