# Feito na Aula de Docker HPD CODEOPS

## Simple Dockerfile

Clone o repositorio; Navegue até a pasta "simple"; Lá contem um simples Dockerfile para criação de imagem DEBIAN com NGINX

### Construindo a imagem

` docker build -t mynginx:v1.0 . `

### Rodando a imagem construida e expondo a porta 

`docker container run -d --name meunginx -p 8080:80 mynginx:v1.0`

#### Para acessar o nginx iphost:8080

## Multistage 

Navegue até a pasta "multistage";  Lá contem um simples Dockerfile HelloWorld criado com multistage gerando uma imagem golang/alpine


### Contruindo a imagem 

`docker build -t mygolang:v1.0 . `

### Rodando a imagem contruida

`docker container run -d --name mygolang mygolang:v1.0`

#### Retornara a mensagem giropops strigus girus
