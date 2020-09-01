import subprocess

# microsoftdocs/azure-docs-sdk-python
RepoFullName = input(str("请输入Repo："))
RepoFullName_split = RepoFullName.split("/")
repo_file = RepoFullName_split[0]+"_"+RepoFullName_split[1]
cmd1 = "cd \\"
cmd2 = "D:"
cmd3 = "cd test"
cmd5 = "cd {}".format(repo_file)
cmd6 = "git init"
cmd8 = "git checkout -b baymax_branch"
cmd14 = """git log --pretty=format:"%H,%an,%cd" > D:/test/log_data/log_{}.csv""".format(repo_file)
cmd = cmd1 + " && " + cmd2 + " && " + cmd3 + " && " + \
      cmd5 + " && " + cmd6 + " && " + cmd8 + " && " + cmd14

subprocess.Popen(cmd, shell=True)