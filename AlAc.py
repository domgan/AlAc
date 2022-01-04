import time, pyautogui
import PySimpleGUI as sg
import threading


def KeepUI():
    sg.theme('Dark')
    layout = [
        [sg.Text('''AlAc is now running.\n
                    Close it to disable it.''')]
    ]
    window = sg.Window('AlAc', layout)
    
    thr = threading.Thread(target=dontsleep, daemon=True)
    thr.start()
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break


def dontsleep():
    while True:
        pyautogui.press('volumedown')
        time.sleep(1)
        pyautogui.press('volumeup')
        time.sleep(100)


if __name__ == '__main__':
    KeepUI()
