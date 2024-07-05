import FreeSimpleGUI as sg
import zip_creator

label1 = sg.Text("Select files to compress:", background_color="black")
input1 = sg.Input(key="input1")
choose_button1 = sg.FilesBrowse("Choose", key="fileSelection")

label2 = sg.Text("Select destination folder:", background_color="black")
input2 = sg.Input(key="input2")
choose_button2 = sg.FolderBrowse("Choose", key="fileDestination")

compress_button = sg.Button("Compress")
label3 = sg.Text("", key="message", background_color="black")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, label3]],
                   background_color="black")

while True:
    event, values = window.read()
    filepaths = values["fileSelection"].split(";")
    folder = values["fileDestination"]
    zip_creator.make_archive(filepaths, folder)
    window["message"].update("Compression was successful")
    match event:
        case sg.WINDOW_CLOSED:
            break
window.close()