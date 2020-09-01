import subprocess

# microsoftdocs/azure-docs-sdk-python
RepoFullName = input(str("请输入Repo："))
RepoFullName_split = RepoFullName.split("/")
repo_file = RepoFullName_split[0]+"_"+RepoFullName_split[1]
cmd1 = "cd \\"
cmd2 = "D:"
cmd3 = "cd test"
cmd4 = "mkdir {}".format(repo_file)
cmd5 = "cd {}".format(repo_file)
cmd6 = "git init"
cmd7 = "git remote add origin https://github.com/{}.git".format(RepoFullName)
cmd8 = "git checkout -b baymax_branch"
cmd9 = "git config core.sparsecheckout true"
cmd10 = "echo *.md >> .git/info/sparse-checkout"
cmd11 = "echo *.yml >> .git/info/sparse-checkout"
cmd12 = "git pull origin master"
# cmd13 = "git push origin baymax_branch"
cmd = cmd1 + " && " + cmd2 + " && " + cmd3 + " && " + cmd4 + " && " + \
      cmd5 + " && " + cmd6 + " && " + cmd7 + " && " + cmd8 + " && " + \
      cmd9 + " && " + cmd10 + " && " + cmd11 + " && " + cmd12 #+ " && " + cmd13

subprocess.Popen(cmd, shell=True)
