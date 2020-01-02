#!/home/sregor/Projects/HPD-CODEOPS/python/aula_python/venv/bin/python
import docker
import argparse
from datetime import datetime


def logando(mensagem, e, logfile='docker-cli.log'):
    data_atual = datetime.now().strftime('%d/%m/%Y %H:%M')
    with open('dokcker-cli.log', 'a') as log:
        texto = "%s \t %s \t %s \n" % (data_atual, mensagem, str(e))
        log.write(texto)


def criarContainers(args):
    try:
        client = docker.from_env()
        executando = client.containers.run(
            args.imagem, args.comando, detach=True)
        print("O container %s foi criado com sucesso" % executando.short_id)
        return(executando)
    except docker.errors.ImageNotFound as e:
        logando('erro: essa imagem não existe', e)
    except docker.errors.NotFound as e:
        logando('erro: essa comando não existe', e)
    except Exception as e:
        logando('erro: favor verificar o comando', e)
    finally:
        print('comando executado')


def listar(args):
    client = docker.from_env()
    get_all = client.containers.list()
    for cada_container in get_all:
        conectando = client.containers.get(cada_container.id)
        print("o container %s uitliza a imagem %s e esta rodando o comando %s" % (
            conectando.short_id, conectando.attrs['Config']['Image'], conectando.attrs['Config']['Cmd']))


def procurar_container(args):
    client = docker.from_env()
    get_all = client.containers.list()
    for cada_container in get_all:
        conectando = client.containers.get(cada_container.id)
        imagem_container = conectando.attrs['Config']['Image']
        if str(args.imagem).lower() in str(imagem_container).lower():
            print("achei o container %s que contem a palavra %s no nome de sua imagem %s" % (
                cada_container.short_id, args.imagem, imagem_container))


parser = argparse.ArgumentParser(description='Meu cli docker fodao')
subparser = parser.add_subparsers()

criar_opt = subparser.add_parser('criar')
criar_opt.add_argument('--imagem', required=True)
criar_opt.add_argument('--comando', required=False)
criar_opt.set_defaults(func=criarContainers)

listar_opt = subparser.add_parser('listar')
listar_opt.set_defaults(func=listar)

procurar_opt = subparser.add_parser('procurar')
procurar_opt.add_argument('--imagem', required=False)
procurar_opt.set_defaults(func=procurar_container)

cmd = parser.parse_args()
cmd.func(cmd)
