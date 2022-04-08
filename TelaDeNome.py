# construa uma tela que peça um nome, e depois de recebe-lo imprima na tela...

import PySimpleGUI as sg
from time import sleep

# primeiramente vamos criar um bom layout...
layout = [[sg.Text("Digite aqui seu nome, chefia:")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(45,2), key='-OUTPUT-')],
          [sg.Button('CONFIRMAR'), sg.Button('VAZAR')]
]

# depois a função de criar a janela...
window = sg.Window('Nome da página...', layout)

# usando um 'Loop de Event', vamos fazer a função da parada
while True:
    event, values = window.read()
    # verifica se o usuário quer VAZAR da pag. ou se ele fechou usando 'x'
    if event == sg.WINDOW_CLOSED or event == 'VAZAR':
        break
    # mostra uma mensagem dentro da janela
    sleep(1)
    window['-OUTPUT-'].update('Olha, ' +values['-INPUT-'] + ', eu se fosse você, contrataria esse cara. Ele é bom ou não é?')

# agora feche a janela

window.close()
