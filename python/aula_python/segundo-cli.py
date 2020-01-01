import argparse, subprocess

def criar(args):
    diretorio = args.nome
    print(diretorio)
    subprocess.call(['mkdir', args.nome])
    for i in range(1,40):
        subprocess.call(['touch', str(i)], cwd=args.nome)

def listar(args):
    subprocess.call(['ls', args.nome])

def listint(args):
    subprocess.call(['ip', args.interface])
        
parser = argparse.ArgumentParser(description="Comando para criar/listar diretorios | listar interfaces")
subparser = parser.add_subparsers()

listar_int = subparser.add_parser('network')
listar_int.add_argument('--interface', required=True)
listar_int.set_defaults(func=listint)

criar_dir = subparser.add_parser('criar')
criar_dir.add_argument('--nome', required=True)
criar_dir.set_defaults(func=criar)

listar_dir = subparser.add_parser('listar')
listar_dir.add_argument('--nome', required=True)
listar_dir.set_defaults(func=listar)

cmd = parser.parse_args() 
cmd.func(cmd)