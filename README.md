# paper finder
Find papers by keywords and venues. Then download it automatically.

## Installing
Install and update using `pip`:

```shell
pip install -U paper-finder
```

## Examples
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
- [x] Download papers

## Author Warning
This code is only used for academic communication. 
The author has no liability for copyright. 
DO NOT ENGAGE IN ANY ILLEGAL ACTIVITIES.
**Please download and read the genuine articles from the publisher.**