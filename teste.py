#!/usr/bin/python
# coding: utf-8

import subprocess
import pdb

if __name__ == "__main__":


    ## Atualizando pacotes
    subprocess.Popen('sudo apt-get update', shell=True, stdin=subprocess.PIPE)
    
    
    apt = "sudo apt-get -y install "
    packages = "nginx apt-transport-https ca-certificates curl gnupg2 software-properties-common"

    print("Instalando pacotes necessarios para o NGINX e o Docker")

    for package in packages.split():
        command = apt + package
        p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
        p_status = p.wait()

    
