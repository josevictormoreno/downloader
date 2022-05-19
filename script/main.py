from pytube import YouTube
import PySimpleGUI as sg

#########################################
#      github: https://github.com/josevictormoreno      #
#########################################

sg.theme('Material1') 
layout = [[sg.Text('Paste video link here...')],
          [sg.Text('URL: '), sg.InputText()],
          [sg.Button('Download', key='download'), sg.Button('Cancel')],
          [sg.Output(size=(40,2))]]

window = sg.Window('Youtube Video Downloader', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    video_link = values[0]
    video = YouTube(video_link)

    stream = video.streams.get_highest_resolution()
    stream.download(output_path='./downloads')
    print('Download Complete!')

window.close()
