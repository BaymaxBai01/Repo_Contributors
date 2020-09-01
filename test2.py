import subprocess
import pandas as pd
import os
import csv

def GetDesktopPath():
    """获取本地电脑名称路径"""
    return os.path.join(os.path.expanduser("~"))

Total_path = GetDesktopPath().split('\\')[-1] # 获取电脑名称


current_1 = pd.read_csv(r'C:\Users\{}\OneDrive - Microsoft\ContributorCommits\Program\repo_list.csv'.format(Total_path))

# create log
File = open(r'D:\ContributorCommits\Results\log_data_merge\merge.txt', "w+", newline='', encoding='utf-8')
output_url = csv.writer(File)
output_url.writerow(['Article', 'contributors', 'data'])

for i in range(1):
    RepoFullName = current_1.iloc[i][0]
    RepoFullName_split = RepoFullName.split("/")
    repo_file = RepoFullName_split[0] + "_" + RepoFullName_split[1]
    cmd1 = "cd \\"
    cmd2 = "cd D:\\ContributorCommits\\Results".format(Total_path)
    cmd3 = "cd repo_list"
    cmd5 = "cd {}".format(repo_file)

    # print(RepoFullName,repo_file)


    md_path = []
    md_file = []
    for root, dirs, files in os.walk(r"D:\ContributorCommits\Results\repo_list\{}".format(repo_file)):
        for file in files:
            if file.endswith('.md'):
                path = root + "\\" + file
                md_path.append(path)
                md_file.append(file)

    print('-' * 100)
    print('The {} repo {} has {} articles'.format(i, RepoFullName, len(md_path)))
    print('---loading---')
    # print(len(md_path))
    # print(len(md_file))
    try:
        os.mkdir(r'D:\ContributorCommits\Results\log_data\{}'.format(repo_file))
    except:
        print('Cannot create a file when that file already exists')
    for j in range(1):
        print(md_path[j])
        print(md_file[j])
        cmd12 = """git log --pretty=format:"%an" "{}" | sort > D:/ContributorCommits/Results/log_data/{}/{}.csv""".format(md_path[j], Total_path, repo_file, md_file[j])
        cmd = cmd1 + " && " + cmd2 + " && " + cmd3 + " && " + cmd5 + " && " + cmd12
        subprocess.Popen(cmd, shell=True)
        print("The {} repo {} article {} finished".format(i, j, md_file[j]))
        #         try:
        # f1 = open(r'C:\Users\{}\OneDrive - Microsoft\ContributorCommits\Results\log_data\{}\{}.csv'.format(Total_path,repo_file,md_file[j]),'r',encoding='utf-8')
        # reader = csv.reader(f1)
        # tweets_id = [row[0] for row in reader]
        # f1.close()
        # dic = set(tweets_id)
        # path_url_list = md_path[j].split('\\')[5:]
        # path_url = '/'.join(path_url_list)
        # output_url.writerow(["https://github.com/{}/blob/master/{}".format(RepoFullName, path_url), len(dic), dic])
        # print("The {} repo {} article {} author distinct".format(i, j, md_file[j]))
#         except:
#             print("No such file or directory {} repo {} article {} author distinct".format(i,j,md_file[j]))

File.close()