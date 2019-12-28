# Feito na Aula de GITLAB HPD CODEOPS

## 

Clone o repositorio; Navegue até a pasta "gitlab"; 

## 

``` docker-compose up -d ```

#### Para acessar o jenkins iphost:

### Configure o GITLAB RUNNER 
```docker container exec -ti 64f gitlab-runner register```
INFOS 
admin Settings > CI/CD > RUNNERS

## Push to repository

### O arquivo de configuração do pipeline

gitlabexample/.gitlab-ci.yml
```
stages:
  - build
  - test
  - release
  - clean
  - deploy

job1:
  stage: build
  script:
    - mvn install
  allow_failure: true

job2:
  stage: test
  script:
    - ls -l
    - hostname

job3:
  stage: release
  script:
    - scp target/meuwebapp.war usuario@host:/var/minha_firma/webapps/
  allow_failure: true

aprovacao:
  stage: deploy
  script:
    - mkdir -r /tmp/deployteste
  when: manual

job_clean:
  stage: clean
  script:
    - rm /tmp/network
  when: on_failure

```
