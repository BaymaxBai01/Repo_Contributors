import subprocess
import sys

def RunShellWithReturnCode(command,print_output=True,universal_newlines=True):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=universal_newlines)
    if print_output:
        output_array = []
        while True:
            line = p.stdout.readline()
            if not line:
                break
            print(line.strip("/n"))
            output_array.append(line)
        output ="".join(output_array)
    else:
        output = p.stdout.read()
    p.wait()
    errout = p.stderr.read()
    if print_output and errout:
        print(sys.stderr, errout)
    p.stdout.close()
    p.stderr.close()
    return output, p.returncode

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
# cmd8 = "git checkout -b baymax_branch"
cmd9 = "git config core.sparsecheckout true"
cmd10 = "echo *.md >> .git/info/sparse-checkout"
cmd11 = "echo *.yml >> .git/info/sparse-checkout"
cmd12 = "git pull origin master"
cmd13 = "git push origin baymax_branch"
cmd = cmd1 + " && " + cmd2 + " && " + cmd3 + " && " + cmd4 + " && " + \
      cmd5 + " && " + cmd6 + " && " + cmd7 + " && " +  \
      cmd9 + " && " + cmd10 + " && " + cmd11 + " && " + cmd12 + " && " + cmd13

RunShellWithReturnCode(cmd)