#!/usr/bin/env python

import scraperwiki
import requests
import json
import time

# Get total pages
def get_pages(key_word):
    payload = {'api-key':'fa45552479ff69987f5809b3f911bc1c:9:71252208', 
               'q':key_word}
    r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json?', params = payload)
    response = json.loads(r.text)['response']['meta']['hits']
    if int(response/10)-1 < 100:
        return int(response/10)-1
    else:
        return 100

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
def append_table(response, keyword, page):
    for article in response:
        scraperwiki.sqlite.execute("INSERT INTO nytimes (epoch_time, id, date_time, keyword, page) VALUES (?,?,?,?,?)", 
                                   (int(100*time.time()), article['_id'], article['pub_date'], keyword, page))

# List of keywords
keywords = ['budget deficit','compensatory spending','debt','government debt',
            'debt explosion','deficit financing','in the red','megadebt',
            'negative cash flow','no assets','overspending','national debt']

# Continue scrape
def left_over():
    try:
        current = scraperwiki.sqlite.execute("SELECT keyword, page FROM nytimes ORDER BY epoch_time DESC LIMIT 1")
        current_word = current['data'][0][0]
        current_page = current['data'][0][1]
        return [current_word,current_page]
    except:
        scraperwiki.sqlite.execute("CREATE TABLE nytimes (epoch_time int, id string, date_time string, keyword string, page int)")
        return ['budget deficit', 0]

# Main function
def main():
    current_pos = left_over()
    keyword_pos = [i for i,x in enumerate(keywords) if x == current_pos[0]][0]
    for i in range(keyword_pos, len(keywords)):
        try:
            page_count = get_pages(keywords[i])
            
            if i==keyword_pos:
                start_page = int(current_pos[1])
            else:
                start_page = 0
            for page_num in range(start_page,page_count):
                try:
                    response_info = api_request(keywords[i], page_num)
                    append_table(response_info, keywords[i], page_num)
                except:
                    pass
        except:
            pass


if __name__ == '__main__' :
    main()


