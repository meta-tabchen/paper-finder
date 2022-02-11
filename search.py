import requests
import pandas as pd
from tqdm import tqdm
from config import api_url
from config import default_venue_list

def search_one(keyword, venue, min_year,max_year):
    url = api_url.format(keyword, venue)
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
    df.to_csv(output,index=False)

if __name__ =='__main__':

    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--min_year', type=int, default=2016)
    parser.add_argument('--max_year', type=int, default=2021)
    parser.add_argument('-k','--keywords', type=str, default="knowledge tracing,knowledge trace")
    parser.add_argument('-v','--venues', type=str,default="AAAI,IJCAI")
    parser.add_argument('-o','--output', type=str,default="result.csv",help="outpu filepath")
    args = parser.parse_args()
    if args.venues=='default':
        venue_list = default_venue_list
    else:
        venue_list = args.venues.split(",")
    keyword_list = args.keywords.split(",")
    print(args)
    print(f"Start to find papers between {args.min_year} to {args.max_year}")
    print(f"The input venues are {venue_list}")
    print(f"The input keywords are {keyword_list}")
    search(keyword_list,venue_list,args.min_year,args.max_year,args.output)

