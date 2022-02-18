from .utils.config import default_venue_list
from .utils.search import search

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

