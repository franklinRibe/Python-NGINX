#!/usr/bin/python
# coding: utf-8

import subprocess
import pdb

if __name__ == "__main__":



    
    
    apt = "sudo apt-get -y install "
    packages = "nginx apt-transport-https ca-certificates curl gnupg2 software-properties-common"

    print("Instalando pacotes necessarios para o NGINX e o Docker")

    for package in packages.split():
        command = apt + package
        p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
        p_status = p.wait()

    ## baixando chave GPG do Docker
    subprocess.Popen('curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -', shell=True, stdin=subprocess.PIPE)

    subprocess.Popen('sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"', shell=True, stdin=subprocess.PIPE)
    
    ## Atualizando pacotes
    subprocess.Popen('sudo apt-get update', shell=True, stdin=subprocess.PIPE)

    pcks_dock = "sudo apt-get install docker-ce docker-ce-cli containerd.io"

    for pck_dock in pcks_dock.split():
        cmd = apt + pck_dock
        pop = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE)
        pop_status = pop.wait()


        