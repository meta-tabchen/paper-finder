from .utils.download import download_from_df
import pandas as pd

if __name__ =='__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-i','--input_path', type=str)
    parser.add_argument('-o','--output', type=str)
    args = parser.parse_args()
    df = pd.read_csv(args.input_path)
    df = download_from_df(df,save_dir=args.output)
    df.to_csv(args.input_path.replace('.csv','_download_results.csv'),index=False)