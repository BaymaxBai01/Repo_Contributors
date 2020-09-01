import sys
sys.setrecursionlimit(1000000)
from gevent import monkey
monkey.patch_all()
import gevent
from gevent.queue import Queue
import subprocess
import pandas as pd
import time

current_1 = pd.read_csv('repo_list.csv')

urls = []

for i in range(3):
    RepoFullName = current_1.iloc[i][0]
    url = "https://github.com/{}.git".format(RepoFullName)
    urls.append(url)

work = Queue()
for data_url in urls:
    work.put_nowait(data_url)

def clone_repo(data_url):
    RepoFullName = data_url
    RepoFullName_split = RepoFullName.split("/")
    repo_file = RepoFullName_split[-2] + "_" + RepoFullName_split[-1]
    repo_full = RepoFullName_split[-2] + "/" + RepoFullName_split[-1]
    cmd1 = "cd \\"
    cmd2 = "D:"
    cmd3 = "cd test"
    cmd4 = "mkdir {}".format(repo_file)
    cmd5 = "cd {}".format(repo_file)
    cmd6 = "git init"
    cmd7 = "git remote add origin https://github.com/{}".format(repo_full)
    cmd8 = "git config core.sparsecheckout true"
    cmd9 = "echo *.md >> .git/info/sparse-checkout"
    cmd10 = "echo *.yml >> .git/info/sparse-checkout"
    cmd11 = "git pull origin master"
    cmd = cmd1 + " && " + cmd2 + " && " + cmd3 + " && " + cmd4 + " && " + \
          cmd5 + " && " + cmd6 + " && " + cmd7 + " && " + cmd8 + " && " + \
          cmd9 + " && " + cmd10 + " && " + cmd11
    subprocess.Popen(cmd, shell=True)
    print("the repo {} finished".format(RepoFullName))
    time.sleep(600)

def crawler():
    while not work.empty():
        data_url = work.get_nowait()
        clone_repo(data_url)

tasks_list = []
for x in range(3):
    task = gevent.spawn(crawler)
    tasks_list.append(task)
gevent.joinall(tasks_list)