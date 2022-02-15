import requests
from bs4 import BeautifulSoup
import os
head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}  #20210607更新，防止HTTP403错误

def download_pdf(doi,title,save_path):
    url = "https://www.sci-hub.ren/" + doi + "#" #20210515更新：现在换成这个sci hub检索地址
    try:
        download_url = ""  
        r = requests.get(url, headers = head)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, "html.parser")
        if soup.iframe == None: 
            download_url = "https:" + soup.embed.attrs["src"] 
        else:
            download_url = soup.iframe.attrs["src"]  
        print(title + " is downloading...\n  --The download url is: " + download_url)
        download_r = requests.get(download_url, headers = head)
        download_r.raise_for_status()
        with open(save_path, "wb+") as temp:
            temp.write(download_r.content)
        state = "success"
    except:
        state = "fail"
    return state

def download_from_df(df,save_dir):
    state_list = []
    save_path_list = []
    for _,row in df.iterrows():
        title = row['title']
        doi = row['doi'].split(",")[0]
        venue_save_dir = os.path.join(save_dir,row['venue'])
        os.makedirs(venue_save_dir,exist_ok=True)
        save_path = os.path.join(venue_save_dir,f"{title}.pdf")
        if not os.path.exists(save_path):
            state = download_pdf(doi,title,save_path)
        else:
            state = "success"
        state_list.append(state)
        if state:
            save_path_list.append(save_path)
        else:
            save_path_list.append("")
    df['state'] = state_list
    df['save_path'] = save_path_list
    return df
