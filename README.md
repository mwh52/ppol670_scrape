# PPOL 670 Programming Assignment - Scraping

This analysis use data from the [NY Times API](http://developer.nytimes.com/docs/read/article_search_api_v2) to create a monthly time series of coverage of budget deficits issues.

## Budget Deficit Coverage in NYTimes (all time)
![Budget Deficit Coverage in NYTimes (all time)](figure/all_time_yearly.png)

The coverage of budget deficit start as early as 1850s. The highest ten years in the history are listed as followings:

|Rank|Year|Freq.|
|----|----|---------|
|1   |2014|   530   |
|2   |2011|   524   |
|3   |2015|   413   |
|4   |2010|   251   |
|5   |2013|   226   |
|6   |2012|   202   |
|7   |1990|   191   |
|8   |1980|   183   |
|9   |1986|   176   |
|10  |1985|   173   |

## Budget Deficit Coverage in NYTimes (2000 - current)
![Budget Deficit Coverage in NYTimes (2000-now)](figure/since_2000.png)

More media coverage on budget deficit since 2010. As shown in the table below, among highest ten month in the history, 9 month were in 2010s.

|Rank|Month|Freq.|
|----|----|---------|
|1 |2015-01|238 |
|2 |2015-02|175 |
|3 |2011-07|160 |
|4 |2014-12|129 |
|5 |2011-08| 83 |
|6 |1990-10| 72 |
|7 |2011-11| 58 |
|8 |2010-11| 46 |
|9 |2014-11| 45 |
|10|2014-02| 43 |

## Files in this repo
In this repo:

-  `nytimes.py` is the Python script to retrive information with NY Times Article Search API v2. 12 key words were used in the query (see details later). Scraped data was inserted into ScraperWiki's data table with SQL queries and downloaded from ScraperWiki. The code is scheduled to run hourly on ScraperWiki while keeping the progress (since ScraperWiki automatically terminate task hourly).  This code was deployed on [ScraperWiki](https://scraperwiki.com/).
-  `nytimes.csv` is the collected information from NY Times Article Search API v2.
-  `visualization.R` is the R script to clean the collected information and visualize it. Duplicated articles were removed based on article id. 
-  `figures` folder contains final graph outputs.

## Keywords selection
The keywords used in this analysis include:
    budget deficit, compensatory spending, debt, government debt, debt explosion, deficit financing, in the red, megadebt, negative cash flow, no assets, overspending, national debt
