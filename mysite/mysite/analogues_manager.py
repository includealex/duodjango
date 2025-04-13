import pandas as pd

from pathlib import Path

DB_FILE = Path("data/analogues.csv")

def get_current_analogues():
    analogues_df = pd.read_csv(DB_FILE)
    analogues = analogues_df.to_dict(orient='index')

    return analogues

def add_analogue(new_russian_word, new_oldrussian_word, username):
    tmp_str = f"{new_russian_word},{new_oldrussian_word},{username}"
    with open(DB_FILE, 'a') as ifile:
        ifile.write(f"\n{tmp_str}")
