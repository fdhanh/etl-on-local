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

class disasterData(luigi.Task):
    task_complete = False
    def requires(self):
        return []
    def complete(self):
        return self.task_complete
    def run(self):
        c = sqlite3.connect("database.db")
        data = extract('disaster', ['id', 'keyword', 'location', 'text', 'target'])
        data.to_sql("disaster", c, if_exists = "replace", index = False)
        c.close() 
        self.task_complete = True