import PySimpleGUI as sg

#layout creation
layout=[[sg.Text("This is a GUI Test")], [sg.Button("Button Test")]]

#window creation
window=sg.Window("GUI Demo", layout)

#Event loop creation
while True:
    event, values = window.read()
    #End program if user closes or button is pressed
    if event == "Button Test" or event == sg.WIN_CLOSED:
        break