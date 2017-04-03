import os
import yaml
import twitter
import boto3
import json

def connect_twitter(config_filepath='~/.script/script.yml'):
    """Connect to twitter, return twitter connection."""

    credentials = yaml.load(open(os.path.expanduser(config_filepath)))
    twitter_stream = twitter.TwitterStream(auth=twitter.OAuth(**credentials['twitter']))
    iterator = twitter_stream.statuses.filter(track="Trump")

    f_hose = boto3.client('firehose')
    for tweet in iterator:
        print (tweet)
        break

connect_twitter()
