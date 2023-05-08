import PySimpleGUI as sg 

layout = [
    (sg.Text("Hows it going?"), ),
    (sg.Input(key="-INPUT-"), ),
    (sg.Text(size=(40, 1), key="-OUTPUT-"), ),
    (sg.Button("Answer"), ),
]

window = sg.Window("Mood check", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    window["-OUTPUT-"].update(
        f'We understand that its going {values["-INPUT-"]}',
        background_color="black",
        text_color = "green",
        )

# print(f"We understand that its going {values[0]}")

window.close()



