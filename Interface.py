from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Mensagem'), sg.Input(key='mensagem', size=(50, 10))],
    [sg.Checkbox('Crifrar documento?')],
    [sg.Button('Sim')]
]
#Janela
janela = sg.Window('Criptografia', layout)

#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Sim':
        if valores['mensagem'] == 'Cifrar documentos com textos e decifrar em Python':
            print("Mensagem cifrada com sucesso")

