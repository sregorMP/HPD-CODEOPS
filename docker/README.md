# Feito na Aula de Docker HPD CODEOPS

## Simple Dockerfile

Clone o repositorio; Navegue até a pasta "simple"; Lá contem um simples Dockerfile para criação de imagem DEBIAN com NGINX

### Construindo a imagem

` docker build -t mynginx:v1.0 . `

### Rodando a imagem construida e expondo a porta 

`docker container run -d --name meunginx -p 8080:80 mynginx:v1.0`

#### Para acessar o nginx iphost:8080

## Multistage Dockerfile 

### Contruindo uma imagem sem multistage para posterior comparação

Navegue até a pasta "multistage";  Lá contem um simples Dockerfile HelloWorld gerando uma image Golang

`docker build -t mygolang:v1.0 . `

### Rodando a imagem contruida

`docker container run -d --name mygolang mygolang:v1.0`

### Construindo uma imagem com multistage 

Navegue até a pasta "multistage/fodao";  Lá contem um simples Dockerfile HelloWorld gerando uma image Golang/alpine

`docker build -t mygolangfodao:v1.0 . `

### Rodando a imagem contruida

`docker container run -d --name mygolangfodao mygolangfodao:v1.0`

#### Retornara a mensagem giropops strigus girus

#### Comparação Imagens

`docker image ls`

mygolangfodao       v1.0                acb387aa7738        39 seconds ago       7.06MB
mygolang            v1.0                7ee5e1bbd50b        About a minute ago   805MB



