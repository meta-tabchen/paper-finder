from loguru import logger
api_url = 'https://dblp.org/search/publ/api?q={}:venue:{}:&h=1000&format=json'
default_venue_list = ['AAAI', 'IJCAI', 'UAI', 'ICML', 'NIPS', 'AISTATS', 'KDD', 'ICDM', 'WWW', 'SIGIR', 'CIKM','L@S']
max_try = 100
wait_time = 60
wait_time_pwc = 5
max_try_pwc = 5
debug = True

