# Feito na Aula de Docker HPD CODEOPS

## Simple Dockerfile

Pasta "simple" contem um simples Dockerfile para criação de imagem DEBIAN com NGINX

### Construindo a imagem

` docker build -t mynginx:v1.0 . `

### Rodando a imagem construida e expondo a porta 

`docker container run -d --name meunginx -p 8080:80 mynginx:v1.0`


## Multistage 

Pasta "multistage" criação de um simples Dockerfile HelloWorld com multistage gerando uma imagem golang/alpine


### Contruindo a imagem 

`docker build -t mygolang:v1.0 . `

### Rodando a imagem contruida

`docker container run -d --name mygolang mygolang:v1.0`
