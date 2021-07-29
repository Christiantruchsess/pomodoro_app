# import required packages 
import PySimpleGUI as sg

# User Interface
layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

# Create the window 
window = sg.Window("Demo", layout)

# Create an event loop 
while True:
    event, values = window.read()
    # end program if user closes window
    # or presses the OK button 
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()