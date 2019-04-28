#!/usr/bin/python
import random
import facebook
import os

#login
access_token = os.environ['TOKEN'] #
graph = facebook.GraphAPI(access_token=access_token, version="3.1")

# Init
page = graph.get_object(id='860133054332205', fields='name')
print('Page target on ' + page['name'] +' with id ' + page['id'])

#upload post
text_file1 = open("adj.txt", "r")
adj = random.choice(text_file1.readlines())
text_file2 = open("mnlmem.txt", "r")
oshis = random.choice(text_file2.readlines())

post = graph.put_photo(image=open(f'images/{oshis}.png', 'rb'),
                message=f'Our oshi MNL48 {oshis} is {adj}')

graph.put_object(parent_object=post['post_id'], connection_name='comments',
                  message='Is this true?')
