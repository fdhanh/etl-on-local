import luigi
from .disasterData import disasterData
from .reviewsData import reviewsData
from .tweetsData import tweetsData
from .userData import userData

class LuigiLoader(luigi.Task):
    task_complete = False
    def requires(self):
        return [disasterData(), userData(), reviewsData(), tweetsData()]
    def complete(self):
        return self.task_complete
    def run(self):
        self.task_complete = True

