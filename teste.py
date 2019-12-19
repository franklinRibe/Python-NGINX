#!/usr/bin/python
# coding: utf-8

import subprocess
import pdb
import os

if __name__ == "__main__":
    
    #Classe criada para criar objetos que vão ser usados para executar comandos no Shell
    class commands:
        def __init__(self, commands, packages):
            self.commands = commands
            self.packages = packages
        
        def execute_apt(self):
            
            ## Laço que vai separar os pacotes linha a linha e executar o apt-install
            for package in self.packages.split():
            
                cmd = self.commands + self.packages
                p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE)
                p.wait()
        
        def execute_command(self):
            p = subprocess.Popen(self.commands, shell=True, stdin=subprocess.PIPE)
            p.wait()
    
    
    ## função para criar o container
    def create_container(ospath, fpaths, nconfs, fdestines, name_apps):
        i = 0
        for fpath in fpaths:
            filesource = ospath+fpath
            fdestine = fdestines[i]
            confsource = ospath+nconfs[i]
            app = url_apps[i].split(".")

            copy = "sudo cp "+filesource+fdestine 
            conf = "sudo cp "+confsource+"/etc/nginx/sites-available"
            mkdir = "sudo mkdir /var/log/nginx/app"+str(i)
            ln = "sudo ln /etc/nginx/sites-available/"+name_apps[i]+".conf /etc/nginx/sites-enabled/"+name_apps[i]+".conf"            
            upcontainer = "sudo docker run -dit --name "+name_apps[i]+" -p 808"+str(i)+":80 -v "+fdestine+":/usr/local/apache2/htdocs/ httpd:latest"
            rstart = "sudo systemctl restart nginx"

            command_cp = commands(copy, '')
            command_cp.execute_command()

            command_conf = commands(conf, '')
            command_conf.execute_command()

            command_mkdir = commands(mkdir, '')
            command_mkdir.execute_command()

            command_ln = commands(ln, '')
            command_ln.execute_command()

            container = commands(upcontainer, '')
            container.execute_command()

            rs = commands(rstart, '')
            rs.execute_command()

            i += 1

    ## Instalando NGINX e pacotes usados  no Docker-ce

    apt = "sudo apt-get -y install "
    pcks = "nginx apt-transport-https ca-certificates curl gnupg2 software-properties-common"
    
    ## Objeto que vai executar a instalação dos pacotes
    command1 = commands(apt, pcks)
    command1.execute_apt()
  
    ## baixando chave GPG do Docker
    dock_cmd = 'curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -'
    
    ## Objeto usado para executar o Curl do Docker
    command2 = commands(dock_cmd, '')
    command2.execute_command()

    ## adicionando o repositorio do Docker
    repo_cmd = 'sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/debian \
    $(lsb_release -cs) \
    stable"'

    ## Objeto usado para o instalar o repo do docker
    command3 = commands(repo_cmd, '')
    command3.execute_command()
    
    ## Atualizando pacotes
    update_cmd = 'sudo apt-get update'
    command4 = commands(update_cmd, '')
    command4.execute_command()

    ## Executando a instalação do Docker
    apt_dock = "sudo apt-get -y install" 
    pcks_dock = "docker-ce docker-ce-cli containerd.io"
    command5 = commands(apt, pcks_dock)
    command5.execute_command()

    ## Retirando o Default do NGINX
    ulink = "sudo unlink /etc/nginx/sites-enabled/default"
    command6 = commands(ulink, '')
    command6.execute_command()

    ## Criando as pastas do APP no host
    touch = "sudo mkdir /var/www/app1 && sudo mkdir /var/www/app2 && sudo mkdir /var/www/app3"
    command7 = commands(touch, '')
    command7.execute_command()

    ## configurando o caminho do SO
     
    os_path = os.path.dirname(os.path.abspath(__file__))
    file_paths = ["/app1/index.html ", "/app2/index.html ", "/app3/index.html "]
    nginx_confs = ["/nginx/app1.conf ", "/nginx/app2.conf ", "/nginx/app3.conf "]
    filedestines = ["/var/www/app1", "/var/www/app2", "/var/www/app3"]
    apps = ["app1", "app2", "app3"]
    create_container(os_path, file_paths, nginx_confs, filedestines, apps)

    ## copiando os arquivos de conf do nginx



    