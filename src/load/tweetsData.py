import luigi
import numpy as np
import pandas as pd
import sqlite3
import sys
from pathlib import Path
file = Path(__file__). resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))
from extract_file import extract

class tweetsData(luigi.Task):
    task_complete = False
    def complete(self):
        return self.task_complete
    def requires(self):
        return []
    def run(self):
        c = sqlite3.connect("database.db")
        columns = ['truncated', 'text', 'is_quote_status', 'in_reply_to_status_id',
        'in_reply_to_user_id', 'id', 'favorite_count', 'entities', 'retweeted',
        'coordinates', 'source', 'in_reply_to_screen_name', 'id_str',
        'retweet_count', 'metadata', 'favorited', 'retweeted_status', 'user',
        'geo', 'in_reply_to_user_id_str', 'lang', 'created_at',
        'in_reply_to_status_id_str', 'place', 'quoted_status_id',
        'quoted_status', 'possibly_sensitive', 'quoted_status_id_str',
        'extended_entities']
        data = extract('tweet', columns)

        to_int = ['truncated', 'is_quote_status', 'retweeted', 'favorited']
        to_str = ['entities', 'metadata', 'retweeted_status', 'user', 'quoted_status', 'created_at', 'extended_entities', 'place', 'coordinates', 'geo']

        for col in columns:
            if col in to_int:
                data[col] = data[col].astype(int)
                data[col].replace('nan', np.nan, inplace = True)
                data[col].replace('None', np.nan, inplace = True)
            elif col in to_str:
                data[col] = data[col].astype(str)
                data[col].replace('nan', np.nan, inplace = True)
                data[col].replace('None', np.nan, inplace = True)

        data.to_sql("tweets", c, if_exists = "replace", index = False)
        c.close()
        self.task_complete = True
