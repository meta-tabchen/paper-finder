# paper finder
Find papers by keywords and venues. Then download it automatically.

## How to use this?
### CLI

```shell
python search.py -k "knowledge tracing,knowledge trace" -v "KDD,IJCAI" -o result.csv
```
- `min_year` : paper >= min_year
- `max_year` : paper<=max_year
- `-k` : keywords, different keywords split use `,`
- `-v` : venue, split using `,`. If `default`, will use the default venues.
- `o` : output file path



### Python api
see the `demo.py`

```python
from search import search
keyword_list=['knowledge tracing','knowledge trace']
venue_list=['KDD','IJCAI']
search(keyword_list=keyword_list,venue_list=venue_list,min_year=2016,max_year=2021,output='result.csv')
```


## Todo
- [x] Search papers.
- [ ] Download papers