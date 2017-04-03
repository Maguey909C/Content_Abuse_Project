import feedparser
import pandas as pd

python_wiki_rss_url = "http://www.aljazeera.net/sitereadercomment/api/readercomment/getrss?entityId=f6451603-4dff-4ca1-9c10-122741d17432&objectId=eccae0ce-1ff9-4cb2-9a9e-36efd238eca3&pageSize=1000&format=xml"

feed = feedparser.parse(python_wiki_rss_url)
f = feed["items"]
df = pd.DataFrame.from_dict(f)
df.head()

def print_summaries(rssfeed):
    dic_length = len(f)
    for i in range(dic_length):
        print("Comment:", i+1)
        print(rssfeed[i]['summary'])

print_summaries(f)
