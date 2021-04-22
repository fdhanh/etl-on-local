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

class reviewsData(luigi.Task):  
    task_complete = False
    def complete(self):
        return self.task_complete
    def requires(self):
        return []
    def run(self):
        c = sqlite3.connect("database.db")
        data = extract('reviews', ['listing_id', 'id', 'date', 'reviewer_id', 'reviewer_name', 'comments'])
        data['date'] = pd.to_datetime(data.date)
        data.to_sql("reviews", c, if_exists = "replace", index = False)
        c.close()
        self.task_complete = True