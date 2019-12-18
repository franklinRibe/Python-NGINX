import subprocess

subprocess.Popen('sudo apt-get -y install nginx', shell=True, stdin=subprocess.PIPE)
