from paper_finder.api import search
keyword_list=['knowledge tracing','knowledge trace']
venue_list=['KDD','IJCAI','L@S']
search(keyword_list=keyword_list,venue_list=venue_list,min_year=2016,max_year=2021,output='kt_result.csv')