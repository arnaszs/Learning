import PySimpleGUI as sg

layout = [
    [sg.Text("Name", size=15), sg.Input(key="Name", size=15)],
    [sg.Text("Last name", size=15), sg.Input(key="Last name", size=15)],
    [
        
        sg.Text("Birth date", size=15),
        sg.Input(key="Year", size=4),
        sg.Input(key="Month", size=3),
        sg.Input(key="Day", size=3),    
    ],
    [sg.Button("Confirm")],
    [sg.Text(key="confirmation")]
]

window = sg.Window("Example", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    window['confirmation'].update(f"{values['Name']} {values['Last name']} \
    born {values['Year']} - {values['Month']} - {values['Day']}")

window.close()
