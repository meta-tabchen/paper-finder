from paper_finder.api import download_pdf
import pandas as pd

title = "Attention is not Explanation"
save_path = "Attention is not Explanation.pdf"
print(download_pdf(title,title,save_path))

# csv_path = "kt_result.csv"
# df = pd.read_csv(csv_path)
# df = download_pdf(df,save_dir='pdfs')
# df.to_csv(csv_path.replace('.csv','_download_result.csv'),index=False)