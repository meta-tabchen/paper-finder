import requests
from .config import max_try_pwc,wait_time_pwc,debug,logger
import time 
import traceback
from tqdm import tqdm


def search_on_pwc(title):
    """search on paperwithcode"""
    response = requests.get(
        url="https://paperswithcode.com/api/v1/papers/",
        params={
            "q": title
        },
    )
    return response.json()

def get_repositories(paper_id):
    response = requests.get(
        url=f"https://paperswithcode.com/api/v1/papers/{paper_id}/repositories/",
    )
    if "Not Found" in response.text:
        return {}
    else:
        return response.json()
    
def get_repos_info_core(title):
    result = search_on_pwc(title)
    if result['count'] != 0:
        paper_details = result['results'][0]
        paper_id = paper_details['id']
        repositories = get_repositories(paper_id)
        paper_details["repositories"] = repositories
    else:
        paper_details = {}
    result = {"search_raw_result": result,
              "paper_details": paper_details}
    return result



def get_repos_info(title):
    success = False
    for i in range(max_try_pwc):
        try:
            result = get_repos_info_core(title)
            success = True
            break
        except:
            logger.error(traceback.format_exc())
            time.sleep(wait_time_pwc)
    if success:
        return result
    else:
        return {}


def add_opensource_url(df,output):
    result_list = []
    url_list = []
    url_official_list = []
    url_pdf_list = []
    conference_url_pdf_list = []
    for title in tqdm(df['title']):
        logger.info(f"Start process {title}")
        result = get_repos_info(title)
        url = url_official = url_pdf= conference_url_pdf = '-'
        if len(result['paper_details']) != 0:
            paper_details = result['paper_details']
            url_pdf = paper_details['url_pdf']
            conference_url_pdf = paper_details['conference_url_pdf']
            repositories = paper_details['repositories']['results']
            repositories = sorted(repositories, key=lambda x: -x['stars'])
            if len(repositories) != 0:
                top1_repo = repositories[0]
                url = top1_repo['url']
                # 查看有没有官方的
                repo_official_list = [
                    x for x in repositories if x['is_official']]
                if len(repo_official_list) != 0:
                    repo_official = repo_official_list[0]
                    url_official = repo_official['url']
        
        url_pdf_list.append(url_pdf)
        conference_url_pdf_list.append(conference_url_pdf)
        url_list.append(url)
        url_official_list.append(url_official)
        result_list.append(result)
    df['code_url'] = url_list
    df['code_url_official'] = url_official_list
    df['url_pdf'] = url_pdf_list
    df['conference_url_pdf'] = conference_url_pdf_list
    df['repo_results'] = result_list
    df.to_csv(output,index=False)
    return df