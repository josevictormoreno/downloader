from pytube import YouTube
import globais as g
import PySimpleGUI as sg

sg.theme('Material1')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Paste video link here...')],
            [sg.Text('URL: '), sg.InputText()],
            [sg.Button('Download'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Youtube Video Downloader', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    video_link =  values[0]

    video = YouTube(video_link)
    video.streams.filter(res='1080').first().download('/home/nriskdev2/Downloads')

window.close()
