import pandas as pd

from pathlib import Path

def get_current_analogues():
    start_ifile = Path("data/analogues.csv")
    analogues_df = pd.read_csv(start_ifile)
    analogues = analogues_df.to_dict(orient='index')

    return analogues
