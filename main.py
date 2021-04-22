import luigi
from src.load import LuigiLoader 

def main():
    luigi.run(main_task_cls = LuigiLoader, local_scheduler = False)

if __name__ == "__main__":
    main()
