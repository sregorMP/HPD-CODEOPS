#!/home/sregor/Projects/HPD-CODEOPS/python/aula_python/venv/bin/python
import docker
import argparse


def listar(args):
    client = docker.from_env()
    get_all = client.containers.list()
    for cada_container in get_all:
        conectando = client.containers.get(cada_container.id)
        print("o container %s uitliza a imagem %s e esta rodando o comando %s" % (
            conectando.short_id, conectando.attrs['Config']['Image'], conectando.attrs['Config']['Cmd']))


parser = argparse.ArgumentParser(description='Meu cli docker fodao')
subparser = parser.add_subparsers()

listar_opt = subparser.add_parser('listar')
listar_opt.set_defaults(func=listar)

cmd = parser.parse_args()
cmd.func(cmd)
