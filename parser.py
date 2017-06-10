import os
import os
import sys
import json
from toolz.dicttoolz import get_in
from functools import partial
import queue
from boto.s3.key import Key
from boto.s3.connection import S3Connection
import ssl
import requests
import feedparser
import datetime

conn = S3Connection()

def create_bucket():

    """Programatically creates a bucket in S3 called scrape.web and set the policy"""

    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    website_bucket = conn.create_bucket('fixed_al_jaz.web')

    website_bucket.set_policy('''{
      "Version":"2012-10-17",
      "Statement": [{
        "Sid": "Allow Public Access to All Objects",
        "Effect": "Allow",
        "Principal": "*",
        "Action": "s3:GetObject",
        "Resource": "arn:aws:s3:::%s/*"
      }
     ]
    }''' % website_bucket.name)

create_bucket()

al_jazerra = "http://www.aljazeera.com/xml/rss/all.xml"

feed = feedparser.parse(al_jazerra)
rss_al_jazerra = feed["items"]


def home_page_links(rss_feed):

    """INPUT: RSS FROM AL-JAZEERA
    OUTPUT: A NUMBER ASSOCIATED W/ EACH LINK TO A LINK OF AL-JAZEERA"""

    href_num_list = []
    for i in range(len(rss_feed)):
        hrefs = (rss_feed[i]['links'][0]['href'])
        things = hrefs.rsplit("-",1)
        things = things[-1]
        href_num_list.append(things.strip(".html"))
    return href_num_list

s = home_page_links(rss_al_jazerra)

def insert_num(href_list):

    """INPUT: H_REF LIST OF NUMBERS
    OUTPUT: A LIST OF FULL WEB ADDRESSES TO POOL RSS FEEDS FOR FRONT PAGE ARTICLES"""

    a = []
    for i in range(len(href_list)):
        a.append(str("http://comments.us1.gigya.com/comments/rss/6269361/aje/"+(href_list[i])))

    return a

rss_links = insert_num(s)

def get_comments(rss_links):

    """INPUT: LIST OF RSS LINKS
    OUPUT: COMMENTS ASSOCIATED W/ EACH ARTICLE

    Function parses through all rss feed to locate only the comments posted by users and stores it in a dic"""

    dics ={}
    for i in range(len(rss_links)):
        rss = feedparser.parse(rss_links[i])
        dics[rss['feed']['title']]={}
        for j in range(len(rss['items'])):
#             print("Comment:", j+1)
            dics[rss['feed']['title']][(rss['items'][j]['author'])]=[(rss['items'][j]['summary'])]
    return dics

comments = get_comments(rss_links)

def dump_news(text):

    """INPUT: a list of urls you want on S3.
    OUTPUT: Puts all the urls on S3 bucket scrape.web
    """

    dates = str(datetime.datetime.now())
    dates = dates[:19]
    # article_text = str(text)
    article_text = json.dumps(text)
    bucket = conn.get_bucket('fixed_al_jaz.web')
    chase = bucket.new_key(dates)
    chase.set_contents_from_string(article_text, policy='public-read')

dump_news(comments) = bucket.new_key(dates)
    chase.set_contents_from_string(article_text, policy='public-read')

dump_news(comments)
