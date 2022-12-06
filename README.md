# paper finder
Find papers by keywords and venues. Then download it automatically.

## Installing
Install and update using `pip`:

```shell
pip install -U paper-finder
```
## 功能
### 论文检索
利用 [dblp](https://dblp.org/faq/How+to+use+the+dblp+search+API.html) 提供的API。

### 论文引用
利用 [semanticscholar](https://www.semanticscholar.org/product/api), **5分钟内只能请求100次**，文献多的话可能会比较慢。

### 论文代码获取

利用 [paperswithcode](https://paperswithcode.com/api/v1/docs/) 提供的代码进行代码检查。


## 常用的期刊列表
```python
CV_A = ["CVPR", "ICCV", "TIP", "TPAMI", "TVCG", "TOG", "SIGGRAPH", "IJCV"]
DM_A = ["KDD", "WWW", "ICDE", "TKDE"]
ML_A = ["ICML", "NIPS", "NeurIPS"]
NLP_A = ["ACL", "SIGIR"]
overall_A = ["AAAI", "IJCAI", "CSCW", "CHI", "Ubicomp", "MM"]
ref_ccf_a = ['AAAI', 'NIPS','ACL','CVPR','ICCV','ICML','IJCAI','WWW','KDD','SIGIR']
ref_ccf_b = ['EMNLP','ECCV','COLING','CIKM','WSDM','NAACL']
ref_other = ['ICLR']
refs = ref_ccf_a + ref_ccf_b + ref_other
```
## Examples
点击这里 [查看](examples/quick_start.ipynb)

### Quick Start

### Search

```python
from paper_finder.api import search
keyword_list=['knowledge tracing','knowledge trace']
venue_list=['KDD','IJCAI']
output = 'kt_result.csv'
search(keyword_list=keyword_list,venue_list=venue_list,min_year=2016,max_year=2021,output=output)
```

Your can find venues' name in [there](https://dblp.org/db/journals/index.html).

### Download

```python
import pandas as pd
from paper_finder.api import download_from_df

csv_path = "kt_result.csv"
df = pd.read_csv(csv_path)
df = download_from_df(df,save_dir='pdfs')
df.to_csv(csv_path.replace('.csv','_download_result.csv'),index=False)
```


<!-- #### CLI -->
<!-- 
```shell
python search.py -k "knowledge tracing,knowledge trace" -v "KDD,IJCAI" -o data/kt_result.csv
```
- `min_year` : paper >= min_year
- `max_year` : paper<=max_year
- `k` : keywords, different keywords split use `,`
- `v` : venue, split using `,`. If `default`, will use the default venues.
- `o` : output file path -->



<!-- ### Download -->
<!-- #### CLI

```shell
python download.py -i data/kt_result.csv  -o pdfs
```
- `i` : the csv path from `search`
- `o` : the dir to save pdfs, we will create sub folder for each venue. Such as `pdfs/AIED` -->


## Todo
- [x] Search papers.
- [ ] Download papers

## Author Warning
This code is only used for academic communication. 
The author has no liability for copyright. 
DO NOT ENGAGE IN ANY ILLEGAL ACTIVITIES.
**Please download and read the genuine articles from the publisher.**