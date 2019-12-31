# Feito na Aula de Elk HPD CODEOPS

### Clone o repositorio; Navegue até a pasta "elk/beats"; 

Usando Centos

Download beats em elastic.co

``` yum install wget java-openjdk ```

```wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.5.1-x86_64.rpm ```

Além do Kibana e Elastic utilizamos esses beats abaixo: 

- filebeat
- metricbeat 
- packetbeat 
- heartbeat

### Para instalação 

``` rpm -ivh nome_do_beat.rpm ```

Efetuar a configuração do beat correspondente no /etc/nome_do_beat/nome_do_beat.yml

### Start serviço
``` systemctl start nome_do_beat``` 

### Acesso Kibana 

iphost:5601
