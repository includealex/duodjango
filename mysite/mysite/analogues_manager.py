import pandas as pd

from collections import defaultdict
from pathlib import Path

DB_FILE = Path("data/analogues.csv")

def get_current_analogues():
    analogues_df = pd.read_csv(DB_FILE)
    analogues = analogues_df.to_dict(orient='index')

    return analogues

def get_stats():
    df = pd.read_csv(DB_FILE)
    user_word_count = df[df['adder'] != 'base']['adder'].value_counts()
    top_users = user_word_count.nlargest(3).to_dict()

    database_word_count = df[df['adder'] == 'base'].shape[0]
    user_input_words_count = df[df['adder'] != 'base'].shape[0]

    stats = {
        'top_users': top_users,
        'database_word_count': database_word_count,
        'user_input_words_count': user_input_words_count
    }
    return stats

def add_analogue(new_russian_word, new_oldrussian_word, username):
    tmp_str = f"{new_russian_word},{new_oldrussian_word},{username}"
    with open(DB_FILE, 'a') as ifile:
        ifile.write(f"\n{tmp_str}")

def get_stats_by_name(username):
    df = pd.read_csv(DB_FILE)

    df = (df[df["adder"] == username].drop(["adder"], axis=1)).reset_index(drop=True)
    user_analogues = df.to_dict(orient='index')

    return user_analogues
