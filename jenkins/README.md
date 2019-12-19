# Feito na Aula de Jenkins HPD CODEOPS

## 

Clone o repositorio; Navegue até a pasta "Jenkins"; Lá contem um simples Dockerfile para criação de imagem Jenkins/Alpine/Docker

### Construindo a imagem

``` docker build -t myjenkins:v1.0 . ```

### Rodando a imagem construida e expondo a porta 

```docker container run -d --name myjenkins -v /var/run/docker.sock:/var/run/docker.sock -v jenkins-home:/var/jenkins_home -p 8080:8080 -p 50000:50000 myjenkins:v1.0```

### Permissão docker
```docker container exec -it --user root myjenkins chmod 666 /var/run/docker.sock ```

#### Para acessar o jenkins iphost:8080

### Install Blue Ocean Plugin
Manage Jenkins > Jenkins Plugins > available > Blue Ocean



