from datetime import datetime
import getpass
import os
from PySimpleGUI import PySimpleGUI as Sg

#layout
Sg.theme('Reddit')


layouts = [
    [Sg.Text("Usuario: "),Sg.Input(key='usuario',size=(20,1))],
    [Sg.Text("Senha: "),Sg.Input(key='senha',password_char='*',size=(20,1))],
    [Sg.Text("Caminho: "),Sg.Input(key='cam',size=(20,1))],
    [Sg.Text("Ocult(O)/Visible(V): "),Sg.Input(key='opc',size=(20,1))],
    [Sg.Button('Acessar')]
]
#janela
janela = Sg.Window('Login', layouts)
#ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == Sg.WINDOW_CLOSED:
        break
    if eventos == 'Acessar':
        if valores['usuario'] == 'ITARU' and valores['senha'] == 'teste1':
            print("Usuário logado")
        else:
            print("Usuario ou senha incorreto!")
            with open("LOG.txt","w") as Log:
                Log.write(getpass.getuser() + ' as ' + str(datetime.now()))
                Sg.popup_error('Usuario ou senha incorreto!')
                break
        if valores['opc'] == "O":
            with open("CAMINHOS.TXT","a") as caminho:
                caminho.write(str(valores['cam']))
            os.system('attrib +h ' + str(valores['cam']))
            Sg.popup("Pasta ocultada com sucesso!")
            break
        if valores['opc'] == "V":
            os.system('attrib -h ' + str(valores['cam']))
            Sg.popup_ok('Pasta visivel')
            break
        else:
            print("Ok!")
            break


 