import subprocess 

def cria_dir():
    global opa
    opa = input('digite o nome do dir desejado: ')
    subprocess.call(['mkdir', opa])
    for i in range(1,40):
        subprocess.call(['touch', str(i)], cwd=opa)

def list_dir():
    subprocess.call(['ls', opa])

cria_dir()
list_dir()