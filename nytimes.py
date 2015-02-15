#!/usr/bin/env python

import scraperwiki
import requests
import json
import time

# Initialize ScraperWiki table
def init_table():
    scraperwiki.sqlite.execute("DROP TABLE nytimes")
    scraperwiki.sqlite.execute("CREATE TABLE nytimes (id string, date_time string)")

# Get total pages
def get_pages(key_word):
    payload = {'api-key':'fa45552479ff69987f5809b3f911bc1c:9:71252208', 
               'q':key_word}
    r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json?', params = payload)
    response = json.loads(r.text)['response']['meta']['hits']
    return int(response/10)-1

# Request from New York Times
def api_request(key_word, page=1):
    time.sleep(10)
    payload = {'api-key':'fa45552479ff69987f5809b3f911bc1c:9:71252208', 
               'q':key_word,
               'page':page}
    r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json?', params = payload)
    response = json.loads(r.text)['response']['docs']
    return response

# Append responses to table
def append_table(response):
    for article in response:
        scraperwiki.sqlite.execute("INSERT INTO nytimes (id, date_time) VALUES (?,?)", 
                                   (article['_id'], article['pub_date']))
    scraperwiki.sqlite.commit()

# List of keywords
keywords = ['budget deficit','compensatory spending','debt','government debt',
            'debt explosion','deficit financing','in the red','megadebt',
            'negative cash flow','no assets','overspending','national debt']


# Main function
def main():
    init_table()
    for keyword in keywords:
        try:
            page_count = get_pages(keyword)
            for page_num in range(page_count):
                try:
                    response_info = api_request(keyword, page_num)
                    append_table(response_info)
                except:
                    pass
        except:
            pass


    
if __name__ == '__main__' :
    main()

