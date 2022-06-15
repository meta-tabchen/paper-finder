import requests
import pandas as pd
from tqdm import tqdm
from .config import api_url
from .config import default_venue_list
from urllib.parse import quote

def search_one(keyword, venue, min_year,max_year):
    url = api_url.format(quote(keyword), quote(venue))
    print(url)
    data = requests.get(url).json()
    if 'hit' not in data['result']['hits']:
        return pd.DataFrame()
    else:
        results = data['result']['hits']['hit']
        df = pd.DataFrame([x['info'] for x in results])
        df = df[(df['year'].apply(int) >= min_year)&(df['year'].apply(int) <= max_year)]
        return df

def search(keyword_list,venue_list,min_year,max_year,output):
    df_list = []
    for keyword in tqdm(keyword_list):
        for venue in venue_list:
            print(f"    Start search keyword:{keyword} in {venue}")
            df = search_one(keyword=keyword,venue=venue,min_year=min_year,max_year=max_year)
            df['keyword'] = keyword
            df_list.append(df)
    df = pd.concat(df_list)
    df['title'] = df['title'].apply(lambda x:x.strip("."))
    df.to_csv(output,index=False)