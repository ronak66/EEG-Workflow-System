# EEG-Worflow-System

## Run Locally
1. Install and Create a Virtual Enviroment (If already installed, skip 1st command)  
```
$ python3 -m pip install --user virtualenv
$ python3 -m venv env
$ source env/bin/activate
```
2. Install Reddis server to run the workflow in the background  
```
$ pip3 install redis
$ sudo apt-get install redis-server
```
3. Install all the required dependencies  
```
$ pip3 install requirements.txt
```
4. Run the system  
```
$ python3 server.py
```
