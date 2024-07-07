import FreeSimpleGUI as sg
import zip_creator

sg.theme("Black")
label1 = sg.Text("Select files to compress:")
input1 = sg.Input(key="input1")
choose_button1 = sg.FilesBrowse("Choose", key="fileSelection")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input(key="input2")
choose_button2 = sg.FolderBrowse("Choose", key="fileDestination")

compress_button = sg.Button("Compress")
label3 = sg.Text("", key="message")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, label3]])

while True:
    event, values = window.read()
    match event:
        case sg.WINDOW_CLOSED:
            break
        case "Compress":
            filepaths = values["fileSelection"].split(";")
            folder = values["fileDestination"]
            if len(filepaths) == 0 or len(folder) == 0:
                zip_creator.make_archive(filepaths, folder)
                window["message"].update("Compression was successful")
            else:
                sg.popup("PLease choose folder and destination")
window.close()