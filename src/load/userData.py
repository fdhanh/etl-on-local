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

class userData(luigi.Task):
    task_complete = False
    def complete(self):
        return self.task_complete
    def requires(self):
        return []
    def run(self):
        c = sqlite3.connect("database.db")
        data = extract('file', ['First Name', 'Last Name', 'Gender', 'Country', 'Age', 'Date', 'Id'])
        data['fullName'] = data['First Name'] + ' ' + data['Last Name']
        data['Gender'] = data['Gender'].map({'Female': 0, 'Male': 1})
        data.drop(['First Name', 'Last Name'], axis = 1, inplace = True)
        #data.Date = pd.to_datetime(data.Date)
        data.to_sql("user", c, if_exists = "replace", index = False)
        c.close()
        self.task_complete = True
