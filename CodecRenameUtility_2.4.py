import tkinter as tk
import serial
import os
from ffprobe3 import FFProbe
import datetime
from os import rename
import re

VersionNumber = "1.0"

TotalCount = 0

VideoExtensions = [".mov", ".MOV", ".MP4", ".mp4", ".MKV", ".mkv", ".AVI", ".avi", ".M4V", ".m4v", ".MPG",  ".mpg"]

VideoCodecs = ["utvideo", "dnxhd", "h265", "h264", "xvid", "mpeg4", "msmpeg4v3"]

utvideoCount = 0

dnxhdCount = 0

h265Count = 0

h264Count = 0

xvidCount = 0

mpeg4Count = 0

msmpeg4v3Count = 0

errorcount = 0

files = []
current = 0

#----------------------------------------------------------
window = tk.Tk()
#----------------------------------------------------------
# Greeting

greeting = tk.Label(text="CodecRenameUtility " + VersionNumber,
    fg="white",
    bg="purple")

greeting.pack()

#----------------------------------------------------------
path_entry = tk.Label(text="Working Directory")
path_entry.pack()
path_entry = tk.Entry(width=100)
path_entry.pack()
path_entry.insert("0", "/home/dustin/Videos/mr_fish_day")
path = path_entry.get()
#----------------------------------------------------------
# List Button

button_list_all = tk.Button(
  text="List All Files",
  width=50,
  height=2,
  bg="grey",
  fg="white",
  )

button_list_all.pack()
#----------------------------------------------------------
#----------------------------------------------------------
# Check Button

button_list_videos = tk.Button(
  text="Find Video Files",
  width=50,
  height=2,
  bg="blue",
  fg="white",
  )

button_list_videos.pack()

#----------------------------------------------------------

#----------------------------------------------------------
# Add Button

button_add = tk.Button(
  text="Add Video Codec To File Name",
  width=50,
  height=2,
  bg="green",
  fg="white",
  )
button_add.pack()
#----------------------------------------------------------
# Remove Button

button_remove = tk.Button(
  text="Remove Video Codec From File Name",
  width=50,
  height=2,
  bg="red",
  fg="white",
  )

button_remove.pack()    
#----------------------------------------------------------
#----------------------------------------------------------
# Clear Screen Button

button_clear_screen = tk.Button(
  text="Clear Output Display",
  width=25,
  height=2,
  bg="orange",
  fg="white",
  )

button_clear_screen.pack()    
#----------------------------------------------------------

#----------------------------------------------------------

#----------------------------------------------------------
# Debug Window
##Make text entry box. Retrieve with <.get(1, tk.END). Indexes: first is line, second is character.
output_box = tk.Label(text="Output")
output_box.pack()
output_box = tk.Text(width=100, height=50)
output_box.pack()
#----------------------------------------------------------
def clear_screen_pressed(event):
    output_box.delete(1.0,tk.END)
    
button_clear_screen.bind("<Button-1>", clear_screen_pressed)
#----------------------------------------------------------
def add_pressed(event):
    path = path_entry.get()
    
    TotalCount = 0

    VideoExtensions = [".mov", ".MOV", ".MP4", ".mp4", ".MKV", ".mkv", ".AVI", ".avi", ".M4V", ".m4v", ".MPG",  ".mpg"]

    utvideoCount = 0

    dnxhdCount = 0

    h265Count = 0

    h264Count = 0

    xvidCount = 0

    mpeg4Count = 0

    msmpeg4v3Count = 0

    errorcount = 0

    files = []
    current = 0
    while True:
        try:
            for r, d, f in sorted(os.walk(path, topdown=True)):
                for file in f:
                    if '[' not in file:
                        for ex in VideoExtensions:
                            if ex in file:
                                current = os.path.join(r, file)
                                TotalCount += 1
                                metadata = FFProbe(str(current))
                                for stream in metadata.streams:
                                    if '{}'.format(stream.codec()) == 'utvideo':
                                        utvideoCount += 1
                                        rename(current, current[0:-4] + ' [utvideo]' + current[-4:])
                                        output_box.insert("1.0", 'New Name: ' + current[0:-4] + ' [utvideo]' + current[-4:])
                                        output_box.insert(1.0, "\n")
                                    
                                    if '{}'.format(stream.codec()) == 'dnxhd':
                                        dnxhdCount += 1
                                        rename(current, current[0:-4] + ' [dnxhd]' + current[-4:])
                                        output_box.insert("1.0", 'New Name: ' + current[0:-4] + ' [dnxhd]' + current[-4:])
                                        output_box.insert(1.0, "\n")
                                    if '{}'.format(stream.codec()) == 'hevc':
                                        h265Count += 1
                                        rename(current, current[0:-4] + ' [h265]' + current[-4:])
                                        output_box.insert("1.0", 'New Name: ' + current[0:-4] + ' [h265]' + current[-4:])
                                        output_box.insert(1.0, "\n")

                                    if '{}'.format(stream.codec()) == 'h264':
                                        h264Count += 1
                                        rename(current, current[0:-4] + ' [h264]' + current[-4:])
                                        output_box.insert("1.0", 'New Name: ' + current[0:-4] + ' [h264]' + current[-4:])
                                        output_box.insert(1.0, "\n")

                                    if '{}'.format(stream.codec()) == 'xvid':
                                        xvidCount += 1
                                        rename(current, current[0:-4] + ' [xvid]' + current[-4:])
                                        output_box.insert("1.0", 'New Name: ' + current[0:-4] + ' [xvid]' + current[-4:])
                                        output_box.insert(1.0, "\n")

                                    if '{}'.format(stream.codec()) == 'mpeg4':
                                        mpeg4Count += 1
                                        rename(current, current[0:-4] + ' [mpeg4]' + current[-4:])
                                        output_box.insert("1.0", 'New Name: ' + current[0:-4] + ' [mpeg4]' + current[-4:])
                                        output_box.insert(1.0, "\n")

                                    if '{}'.format(stream.codec()) == ' msmpeg4v3':
                                        msmpeg4v3Count += 1
                                        rename(current, current[0:-4] + ' [msmpeg4v3]' + current[-4:])
                                        output_box.insert("1.0", 'New Name: ' + current[0:-4] + ' [msmpeg4v3]' + current[-4:])
                                        output_box.insert(1.0, "\n")
        except:
            errorcount += 1
            output_box.insert("1.0", "**ERROR: " + str(current))
            output_box.insert(1.0, "\n")
            rename(current, current[0:-4] + ' [ERROR]' + current[-4:])
            output_box.insert("1.0", '**Offending File Marked')
            output_box.insert(1.0, "\n")
            
            #e = sys.exc_info()[0]
            #output_box.insert(1.0, "<p>Error: %s</p>" % e )
            
            pass
        else:
            output_box.insert("1.0", "-" * 20)
            output_box.insert(1.0, "\n")
            if utvideoCount != 0:
                output_box.insert("1.0", "utvideo: " + str(utvideoCount))
                output_box.insert(1.0, "\n")
            if dnxhdCount != 0:
                output_box.insert("1.0", 'dnxhd: ' + str(dnxhdCount))
                output_box.insert(1.0, "\n")
            if h265Count != 0:
                output_box.insert("1.0", 'h265: ' + str(h265Count))
                output_box.insert(1.0, "\n")
            if h264Count != 0:
                output_box.insert("1.0", 'h264: ' + str(h264Count))
                output_box.insert(1.0, "\n")
            if xvidCount != 0:
                output_box.insert("1.0", 'XVID: ' + str(xvidCount))
                output_box.insert(1.0, "\n")
            if mpeg4Count != 0:
                output_box.insert("1.0", 'mpeg4: ' + str(mpeg4Count))
                output_box.insert(1.0, "\n")
            if msmpeg4v3Count != 0:
                output_box.insert("1.0", 'msmpeg4v3: ' + str(msmpeg4v3Count))
                output_box.insert(1.0, "\n")
                output_box.insert("1.0", '-' * 20)
                output_box.insert(1.0, "\n")
            if errorcount != 0:
                output_box.insert("1.0", 'Errors: ' + str(errorcount))
                output_box.insert(1.0, "\n")
                output_box.insert("1.0", '-' * 20)
                output_box.insert(1.0, "\n")
            if TotalCount == 0:
                output_box.insert(1.0, "\n")
                output_box.insert("1.0", '-' * 20)
                output_box.insert(1.0, "\n")
                output_box.insert("1.0", '*****No Changes Made*****')
                output_box.insert(1.0, "\n")
                output_box.insert("1.0", '-' * 20)
                output_box.insert(1.0, "\n")
            output_box.insert(1.0, "\n")
            output_box.insert("1.0", '-' * 20)
            output_box.insert(1.0, "\n")
            if TotalCount != 0:
                output_box.insert("1.0", '-' * 20)
                output_box.insert(1.0, "\n")
                output_box.insert("1.0", 'Total Renamed: ' + str(TotalCount))
                output_box.insert(1.0, "\n")
                output_box.insert("1.0", '-' * 20)
                output_box.insert(1.0, "\n")
#----------------------------------------------------------
            output_box.insert("1.0", '-' * 20)
            output_box.insert(1.0, "\n")
            output_box.insert("1.0", 'Codec Check Operation Completed: ' + str(datetime.datetime.now()))
            output_box.insert(1.0, "\n")
            output_box.insert("1.0", '-' * 20)
            output_box.insert(1.0, "\n")
            break
button_add.bind("<Button-1>", add_pressed)
#----------------------------------------------------------
def check_pressed(event):
    path = path_entry.get()
    while True:
        try:
            for r, d, f in sorted(os.walk(path, topdown=True)):
                for file in f:
                    #for codec in VideoCodecs:
                        #if codec in file:                        
                                current = os.path.join(r, file)
                                metadata = FFProbe(str(current))
                                for stream in metadata.streams:
                                    for codec in VideoCodecs:
                                        if codec in '{}'.format(stream.codec()):
                                            output_box.insert(50.0, "\n")
                                            output_box.insert(50.0, current + ": " + "\n" + '{}'.format(stream.codec()))
                                            output_box.insert(50.0, "\n")
                                        
                                        """
                                            output_box.insert(50.0, "\n")
                                            output_box.insert(50.0,'{}'.format(stream.codec()))                                        
                                            output_box.insert(50.0, "\n")
                                            output_box.insert("50.0", current)
                                            output_box.insert(50.0, "\n")
                                            """
                                        
                                           
                                   
        except:
            pass
        else:
            output_box.insert(1.0, "\n")
            output_box.insert("1.0", '-' * 20)
            output_box.insert(1.0, "\n")
            output_box.insert("1.0", 'Codec Check Operation Completed: ' + str(datetime.datetime.now()))
            output_box.insert(1.0, "\n")
            output_box.insert("1.0", '-' * 20)
            output_box.insert(1.0, "\n")

            break
button_list_videos.bind("<Button-1>", check_pressed)
#----------------------------------------------------------
#----------------------------------------------------------
def list_all_pressed(event):
    path = path_entry.get()
    while True:
        try:
            for r, d, f in sorted(os.walk(path, topdown=True)):
                for file in f:                       
                    current = os.path.join(r, file)                            
                    output_box.insert(50.0, current + "\n")
                                           
                                   
        except:
            pass
        else:
            output_box.insert(1.0, "\n")
            output_box.insert("1.0", '-' * 20)
            output_box.insert(1.0, "\n")
            output_box.insert("1.0", 'List Operation Completed: ' + str(datetime.datetime.now()))
            output_box.insert(1.0, "\n")
            output_box.insert("1.0", '-' * 20)
            output_box.insert(1.0, "\n")
            break
button_list_all.bind("<Button-1>", list_all_pressed)
#----------------------------------------------------------
def remove_pressed(event):
    path = path_entry.get()
    output_box.insert("1.0", "Remove Operation Started: " + str(datetime.datetime.now()))
    output_box.insert(1.0, "\n")
    
    TotalCount = 0
    CurrentName = 0

    for r, d, f in sorted(os.walk(path, topdown=True)):
        for file in f:
            CurrentName = os.path.join(r, file)
            BaseName = re.sub("[[@*&?].*[]@*&?]", "", CurrentName)
            if '[' in file:
                rename(CurrentName, BaseName)
                TotalCount += 1
                FinalName = BaseName[:-5] + BaseName[-4:]
                rename(BaseName, FinalName)
                output_box.insert("1.0", "New Name: " + str(FinalName))
                output_box.insert(1.0, "\n")

    output_box.insert("1.0", "Files Renamed: " + str(TotalCount))
    output_box.insert(1.0, "\n")
    if TotalCount == 0:
        output_box.insert(1.0, "\n")
        output_box.insert("1.0", '-' * 20)
        output_box.insert(1.0, "\n")
        output_box.insert("1.0", '*****No Changes Made*****')
        output_box.insert(1.0, "\n")
        output_box.insert("1.0", '-' * 20)

    else:
        output_box.insert(1.0, "\n")
        output_box.insert("1.0", '-' * 20)
        output_box.insert(1.0, "\n")
        output_box.insert("1.0", 'Codec Remove Operation Completed: ' + str(datetime.datetime.now()))
        output_box.insert(1.0, "\n")
        output_box.insert("1.0", '-' * 20)
        output_box.insert(1.0, "\n")

button_remove.bind("<Button-1>", remove_pressed)
#----------------------------------------------------------

#----------------------------------------------------------

window.mainloop()


