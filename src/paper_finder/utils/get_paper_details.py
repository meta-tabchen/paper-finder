
import requests
import pandas as pd
import traceback
from tqdm import tqdm_notebook
import time
from multiprocessing.pool import ThreadPool

from .config import max_try,wait_time,debug,logger

api_paper_detail = "https://api.semanticscholar.org/graph/v1/paper/{}?fields=title,citations,references,year,abstract,venue,authors,referenceCount,citationCount"
api_search_by_words = "https://api.semanticscholar.org/graph/v1/paper/search?query={}&limit=1"




def get_request_core(api):
    try:
        result = requests.get(api).json()
    except:
        logger.debug(traceback.format_exc())
        result = {}
    return result

def get_request(api):
    success = False
    for i in range(max_try):
        result = get_request_core(api)
        if debug:
            msg = f"api={api},num={i}"
            logger.debug(msg)
        if "message" in result and result['message'] == "Too Many Requests":
            logger.info("start wait")
            time.sleep(wait_time)
        else:
            success = True
            break
    if success:
        return result
    else:
        return {}


def titlt2id(title):
    """获取论文对应在semanticscholar的ID"""
    data = get_request(api_search_by_words.format(title))
    if len(data) == 0 or 'data' not in data:
        return ""
    elif len(data['data']) == 0:
        return ""
    else:
        paper_id = data['data'][0]['paperId']
        return paper_id


def get_paper_detail(paper_id):
    """获取论文细节"""
    data = get_request(api_paper_detail.format(paper_id))
    if len(data) == 0:
        return {"raw_data": data, "state": False}
    elif "citations" not in data or "references" not in data:
        return {"raw_data": data, "state": False}
    else:
        citations = data['citations']
        references = [x for x in data['references']
                      if not x['paperId'] is None]
        return {"raw_data": data, "citations": citations, "references": references, "state": True}


def get_paper_detail_by_title_core(title):
    """获取ID+用ID查询信息"""
    paper_id = titlt2id(title)
    if len(paper_id) != 0:
        data = get_paper_detail(paper_id)
    else:
        data = {"state": False}
    return data


def get_paper_details(titles, n_jobs=5):
    """并行获取"""
    p = ThreadPool(n_jobs)
    paper_detail_list = p.map(get_paper_detail_by_title_core, titles)
    p.close()
    # 获取引用信息
    paper_refs_list = []
    for title, paper_detail in zip(titles, paper_detail_list):
        if paper_detail['state']:
            _ = [x.update({"cited_by_title": title})
                 for x in paper_detail['references']]
            paper_refs_list.extend(paper_detail['references'])
    return paper_refs_list, paper_detail_list


def add_details(df,output,n_jobs=5,add_cols = ['abstract', 'referenceCount', 'citationCount']):
    paper_refs_list, paper_detail_list = get_paper_details(
        df['title'], n_jobs=n_jobs)
    for col in add_cols:
        col_results = []
        for paper_info in paper_detail_list:
            if not paper_info['state']:
                col_results.append("-")
            else:
                col_results.append(paper_info['raw_data'][col])
        df[col] = col_results
    df.to_csv(output,index=False)
    return df

if __name__ == "__main__":
    search_result_path = "kt_result.csv"
    df_result = pd.read_csv(search_result_path).drop_duplicates("title")
    df_result = add_details(df_result)
    df_result.to_csv(search_result_path.replace(
        '.csv', '_add_details.csv'), index=False)
