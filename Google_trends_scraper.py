#------------------------
#
# NAME:		Google_trends_scraper.py
#
# CREATED: 	01.09.2022 - dserke
#
# EDITS:	
#
# SOURCE:	https://github.com/GeneralMills/pytrends#historical-hourly-interest
#		https://lazarinastoy.com/the-ultimate-guide-to-pytrends-google-trends-api-with-python/
#
# NOTES:	1. Search term and topics are two different things
# 		2. keyword length limited to 100 characters
#               3. max number of kw values at one time is 5
#------------------------

#------------------------
# import libraries
#------------------------
from   pytrends.request     import TrendReq

import matplotlib           as     mpl
from   matplotlib           import pyplot as plt

import pandas               as pd

#------------------------
# define constants
#------------------------
tz_offset       = 360
kw_list         = ['bitcoin', 'ethereum']
home_lang       = 'en-US'

#------------------------
# data
#------------------------
# connect to Google, create model
pytrends        = TrendReq(hl=home_lang, tz=tz_offset)

# query the keyword term to search for
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

test_df         = pytrends.interest_over_time()
kw_btc_df       = pytrends.get_historical_interest(kw_list, year_start=2020, month_start=1, day_start=1, hour_start=0, year_end=2021, month_end=12, day_end=30, hour_end=0, cat=0, geo='', gprop='', sleep=0)

# Interest by Region
region_df       = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False)
# ... looking at rows where all values are not equal to 0
region_df       = region_df[(region_df != 0).all(1)]
# ... drop all rows that have null values in all columns
region_df.dropna(how='all',axis=0, inplace=True)

# trending searches in real time for United States
pytrends.trending_searches(pn='united_states') 
# trending searches in real time for Japan
pytrends.trending_searches(pn='japan') 

# get today's trending topics
trendingtoday   = pytrends.today_searches(pn='US')
trendingtoday.head(20)

# Get Google Top Charts for YYYY
top_df          = pytrends.top_charts(2021, hl=home_lang, tz=tz_offset, geo='GLOBAL')
top_df

kw_sugg_df      = pytrends.suggestions(keyword='bitcoin')

pytrends.categories()

pytrends.related_topics()

# get related queries
related_queries = pytrends.related_queries()
related_queries.values()
# ...build lists dataframes
top             = list(related_queries.values())[0]['top']
rising          = list(related_queries.values())[0]['rising']
# ... convert lists to dataframes
dftop           = pd.DataFrame(top)
dfrising        = pd.DataFrame(rising)
# ... join two data frames
joindfs         = [dftop, dfrising]
allqueries      = pd.concat(joindfs, axis=1)
# ... function to change duplicates
cols            = pd.Series(allqueries.columns)
for dup in allqueries.columns[allqueries.columns.duplicated(keep=False)]: 
    cols[allqueries.columns.get_loc(dup)] = ([dup + '.' + str(d_idx) 
                                     if d_idx != 0 
                                     else dup 
                                     for d_idx in range(allqueries.columns.get_loc(dup).sum())]
                                    )
allqueries.columns = cols
# ... rename to proper names
allqueries.rename({'query': 'top query', 'value': 'top query value', 'query.1': 'related query', 'value.1': 'related query value'}, axis=1, inplace=True)
allqueries.head(50)
# ... save to csv
allqueries.to_csv('allqueries.csv')
# ... download from collab
files.download("allqueries.csv")

#------------------------
# plotting
#------------------------
fig, ax         = plt.subplots(figsize=(20, 6))
kw_btc_df['bitcoin'].plot(color='purple')
# adding title and labels
plt.title('Total Google Searches for "bitcoin"', fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')

region_df.plot(figsize=(20, 12), y=kw_list, kind ='bar')