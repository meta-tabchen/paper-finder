from paper_finder.api import download_from_df
import pandas as pd

csv_path = "result.csv"
df = pd.read_csv(csv_path)
df = download_from_df(df,save_dir='pdfs')
df.to_csv(csv_path.replace('.csv','_download_result.csv'),index=False)