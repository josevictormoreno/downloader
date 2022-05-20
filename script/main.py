from pytube import YouTube
import PySimpleGUI as sg
import os

#########################################
#      github: https://github.com/josevictormoreno      #
#########################################

sg.theme('Material1') 
layout = [[sg.Text('Paste video link here...')],
          [sg.Text('URL: '), sg.InputText()],
          [sg.Checkbox('MP3', default=False, key='mp3')],
          [sg.Button('Download', key='download'), sg.Button('Cancel')],
          [sg.Output(size=(40,2))]]

window = sg.Window('Youtube Video Downloader', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    video_link = values[0]
    video = YouTube(video_link)
    mp3 = values['mp3']
    if mp3 == True:
        stream = video.streams.filter(only_audio=True).first()
        out_file = stream.download(output_path='./downloaded')
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    else:
        stream = video.streams.get_highest_resolution()
        stream.download(output_path='./downloaded')
    print('Download Complete!')

window.close()
