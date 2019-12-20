# Provisionamento de máquina com Apache e NGINX como proxy reverso

Script criado para instalar de maneira automatizada o NGINX para fazer proxy reverso de 3 apps que rodam em containeres
com apache.

Primeiro o Script instala o NGINX
Segundo o Script instala o Docker
Terceiro o Script move os arquivos de conf para as pastas correspondentes
Quarto o Script ativa os containeres
Quinto configura o SO para responder um DNS local para cada uma das aplicações
