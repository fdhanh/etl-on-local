# ETL with luigi
Luigi is a Python (2.7, 3.6, 3.7 tested) package that helps you build complex pipelines of batch jobs. It handles dependency resolution, workflow management, visualization, handling failures, command line integration, and much more. (luigi docs)

In this project, I use Python 3.6.8

## Installation
Use git to clone this repository
```
git clone https://github.com/fdhanh/etl-on-local.git
```

## Pipeline graph

## Data
### Input
Download example data <a href = "https://drive.google.com/file/d/1YgqmdI-8oXwPs8AEf3CzOCq3EpvjwRdA/view?usp=sharing"> here </a>

### Output
Check example output file <a href="https://drive.google.com/file/d/1E0vRDAvyTsSCUx2rpnrzw4YhXlu3ceSk/view?usp=sharing"> here </a>

## Usage
### 1. Run luigi on cmd to connect a localhost:8082

```luigid```

open web browser and go to localhost:8082
![alt text](https://github.com/fdhanh/etl-on-local/blob/master/add_files/luigi%20UI.JPG?raw=true)

### 2. Open new cmd and run main.py
Since I can't running with my base environment for python before you run the main file, I recommend to use virtual environment.
Shortly you just need to run this on cmd:
```
mkdir python-virtual-environments && cd python-virtual-environments
python3 -m venv env
env/Scripts/activate
```
source: https://realpython.com/python-virtual-environments-a-primer/

After that, you just need to run ``` python main.py ```

If processes was success, go to luigi UI and depedency graph will look like this
![alt_text](https://github.com/fdhanh/etl-on-local/blob/master/add_files/Job%20tree.JPG?raw=true)
