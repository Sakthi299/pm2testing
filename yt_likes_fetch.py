#To run as pm2 Script
#pm2 start yt_likes_fetch.py --name likes15min --cron '*/15 * * * *' --no-autorestart

import json
import influxdb
from influxdb import InfluxDBClient
import itertools
import pafy
from datetime import datetime

def get_ytlikes(urls):
	
    title = []
    likes = []
    
    for url in urls:
        video = pafy.new(url)
        title.append(video.title)
        likes.append( video.likes)
	
    add_row(urls, title, likes)

def get_client():

    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'yt_data')
    return client

def show_yt_views():

    client = get_client()
   
    yt_records = client.query('select * from ytviews;')

    print(yt_records)

def add_row(url_list, title_list, likes_list):

    client = get_client()
    
    my_date = datetime.now()
    timestamp = my_date.isoformat()
    
    for (url, title, likes) in zip(url_list, title_list, likes_list):
        yt_entry = [
        {
            "measurement":"ytviews",
            "tags": {
				"youtube_title"  : title,
                "youtube_url"    : url
            },
            "time" : timestamp,
            "fields": {
                "Likes": likes
            }
        }
        ]
        client.write_points(yt_entry)
    
    print('Youtube Likes Entries Added at '+str(my_date))

def startpy():
    
	youtube_urls = [
		"https://www.youtube.com/watch?v=gjnrtCKZqYg",
		"https://youtu.be/x6Q7c9RyMzk",
		"https://www.youtube.com/watch?v=FyF9CRGb2VU",
		"https://www.youtube.com/watch?v=0f_ho4Wem0w",
		"https://youtu.be/PiL5UTTTrxk"
	]

	get_ytlikes(youtube_urls)

if __name__ == '__main__':
    startpy()



