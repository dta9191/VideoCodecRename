'''
Release Notes: 1.2

- Removed import serial line.
- updated version number
- Replaced <'{}'.format(stream.codec())> with <stream.codec()>
- Replaced " with ' for consistency.
- Updated version number in window
- Replaced <if ex in file.lower()> with <if ex in file.lower().lower()> to ensure that extensions of any case will be read properly.
- Created a dictionary for the video codec counts to clean up the code: VideoCodecCounts[].
- function check_pressed renamed to find_videos_pressed
- Changed how extensions are handled. Can now handle extensions of any length, such as .m2ts.
- Added file counts to all operations
- Standardized all output formatting for all operations.
- Set each operation to reset variable TotalCount after it ran to ensure accurate counts between operations.
- Replaced <path = path_entry.get()> with <path = path_entry.get()>

'''
import tkinter as tk
import os
from ffprobe3 import FFProbe
import datetime
from os import rename
import re

VersionNumber = '1.0.2'

VideoCodecs = ['utvideo', 'dnxhd', 'h265', 'h264', 'xvid', 'mpeg4', 'msmpeg4v3', 'error']
VideoCodecCounts = {'utvideo': 0, 'dnxhd': 0, 'h265': 0, 'h264': 0, 'xvid': 0, 'mpeg4': 0, 'msmpeg4v3': 0, 'error': 0}
#----------------------------------------------------------
window = tk.Tk()
#----------------------------------------------------------
# Greeting

greeting = tk.Label(text='CodecRenameUtility ' + VersionNumber,
    fg='white',
    bg='purple')

greeting.pack()

#----------------------------------------------------------
path_entry = tk.Label(text='Working Directory')
path_entry.pack()
path_entry = tk.Entry(width=100)
path_entry.pack()
path = path_entry.get()
#----------------------------------------------------------
# List Button

button_list_all = tk.Button(
  text='List All Files',
  width=50,
  height=2,
  bg='grey',
  fg='white',
  )

button_list_all.pack()
#----------------------------------------------------------
#----------------------------------------------------------
# Check Button

button_list_videos = tk.Button(
  text='Find Video Files',
  width=50,
  height=2,
  bg='blue',
  fg='white',
  )

button_list_videos.pack()

#----------------------------------------------------------

#----------------------------------------------------------
# Add Button

button_add = tk.Button(
  text='Add Video Codec To File Name',
  width=50,
  height=2,
  bg='green',
  fg='white',
  )
button_add.pack()
#----------------------------------------------------------
# Remove Button

button_remove = tk.Button(
  text='Remove Video Codec From File Name',
  width=50,
  height=2,
  bg='red',
  fg='white',
  )

button_remove.pack()    
#----------------------------------------------------------
#----------------------------------------------------------
# Clear Screen Button

button_clear_screen = tk.Button(
  text='Clear Output Display',
  width=25,
  height=2,
  bg='orange',
  fg='white',
  )

button_clear_screen.pack()    
#----------------------------------------------------------

#----------------------------------------------------------

#----------------------------------------------------------
# Debug Window
##Make text entry box. Retrieve with <.get(1, tk.END). Indexes: first is line, second is character.
output_box = tk.Label(text='Output')
output_box.pack()
output_box = tk.Text(width=100, height=50)
output_box.pack()
#----------------------------------------------------------
def clear_screen_pressed(event):
    output_box.delete(1.0,tk.END)
    
button_clear_screen.bind('<Button-1>', clear_screen_pressed)
#----------------------------------------------------------
def add_pressed(event):
    path = path_entry.get()
    
    TotalCount = 0
    VideoCount = 0

    VideoExtensions = ['.mov', '.mp4', '.mkv', '.avi', '.m4v', '.mpg']
    VideoCodecs = ['utvideo', 'dnxhd', 'h265', 'h264', 'xvid', 'mpeg4', 'msmpeg4v3', 'error']
    VideoCodecCounts = {'utvideo': 0, 'dnxhd': 0, 'h265': 0, 'h264': 0, 'xvid': 0, 'mpeg4': 0, 'msmpeg4v3': 0, 'error': 0}
    files = []
    current = 0
    
    output_box.insert('1.0', 'Add Operation Started: ' + str(datetime.datetime.now()))
    output_box.insert(1.0, '\n')
    output_box.insert('1.0', '-' * 20)
    output_box.insert(1.0, '\n')
    
    while True:
        try:
            for r, d, f in sorted(os.walk(path, topdown=True)):
                for file in f:
                    TotalCount += 1
                    Extension = os.path.splitext(file)[1] # Returns a tuple, with the extension at index 1
                    if '[' not in file:
                        for ex in VideoExtensions:
                            if ex in file.lower():
                                current = os.path.join(r, file)                                
                                metadata = FFProbe(str(current))
                                for stream in metadata.streams:
                                    codec = stream.codec()
                                    if stream.codec() in VideoCodecs:
                                        VideoCount += 1
                                        VideoCodecCounts[codec] += 1
                                        newName = f'{current[0:-len(Extension)]}[{codec}]{Extension}'
                                        rename(current, newName)
                                        output_box.insert('1.0', 'New name: ' + newName)
                                        output_box.insert(1.0, '\n')
        except:
            VideoCodecCounts['error'] += 1
            rename(current, current[0:-4] + '[ERROR]' + current[-4:])
            TotalCount += 1
            output_box.insert('1.0', 'New name: ' + newName)
            output_box.insert(1.0, "\n")

            pass
        else:
            output_box.insert(1.0, '\n')
            output_box.insert('1.0', '-' * 20)
            output_box.insert(1.0, '\n')
            output_box.insert('1.0', 'Files Renamed: ' + str(VideoCount))
            output_box.insert(1.0, '\n')
            output_box.insert('1.0', 'Files Scanned: ' + str(TotalCount))
            output_box.insert(1.0, '\n')
            output_box.insert(1.0, "Errors Ecountered: " + str(VideoCodecCounts['error']))
            output_box.insert(1.0, "\n")
            output_box.insert('1.0', 'Video Rename Operation Completed: ' + str(datetime.datetime.now()))
            output_box.insert(1.0, '\n')
            output_box.insert('1.0', '-' * 20)
            output_box.insert(1.0, '\n')
            break
                                    
                                    
#----------------------------------------------------------
            output_box.insert('1.0', '-' * 20)
            output_box.insert(1.0, '\n')
            output_box.insert(1.0, 'Files Renamed: ' + str(TotalCount))            
            output_box.insert(1.0, '\n')
            output_box.insert(1.0, 'Codec Add Operation Completed: ' + str(datetime.datetime.now()))
            output_box.insert(1.0, '\n')
            output_box.insert('1.0', '-' * 20)
            output_box.insert(1.0, '\n')
            
            output_box.insert(50.0, '\n')
            output_box.insert('50.0', '-' * 20)
            output_box.insert(50.0, '\n')
            TotalCount = 0
            break
button_add.bind('<Button-1>', add_pressed)
#----------------------------------------------------------
def find_videos_pressed(event):
    path = path_entry.get()
    
    TotalCount = 0
    VideoFileCount = 0
    VideoExtensions = ['.mov', '.MOV', '.MP4', '.mp4', '.MKV', '.mkv', '.AVI', '.avi', '.M4V', '.m4v', '.MPG',  '.mpg']
    files = []
    current = 0
    
    output_box.insert('1.0', 'Video Search Operation Started: ' + str(datetime.datetime.now()))
    output_box.insert(1.0, '\n')
    output_box.insert('1.0', '-' * 20)
    output_box.insert(1.0, '\n')
    
    while True:
        try:
            for r, d, f in sorted(os.walk(path, topdown=True)):
                for file in f:
                    Extension = os.path.splitext(file)[1] # Returns a tuple, with the extension at index 1
                    for ex in VideoExtensions:
                        if ex in file.lower():
                            current = os.path.join(r, file)
                            TotalCount += 1
                            output_box.insert(1.0, "\n")
                            output_box.insert(1.0, current)
        except:
            VideoCodecCounts['error'] += 1
            output_box.insert("1.0", "**ERROR: " + str(current))
            output_box.insert(1.0, "\n")
            rename(current, current[0:-4] + '[ERROR]' + current[-4:])
            
            pass
        else:
            output_box.insert(1.0, '\n')
            output_box.insert('1.0', '-' * 20)
            output_box.insert(1.0, '\n')
            output_box.insert('1.0', 'Videos Found: ' + str(TotalCount))
            output_box.insert(1.0, '\n')
            output_box.insert('1.0', 'Video Search Operation Completed: ' + str(datetime.datetime.now()))
            output_box.insert(1.0, '\n')
            output_box.insert('1.0', '-' * 20)
            output_box.insert(1.0, '\n')
            break
button_list_videos.bind('<Button-1>', find_videos_pressed)
#----------------------------------------------------------
#----------------------------------------------------------
def list_all_pressed(event):
    path = path_entry.get()
    TotalCount = 0
    
    while True:
        try:
            for r, d, f in sorted(os.walk(path, topdown=True)):
                for file in f:                       
                    current = os.path.join(r, file)
                    TotalCount += 1
                    output_box.insert(1.0, current + '\n')
                                           
                                   
        except:
            pass
        else:
            output_box.insert(1.0, '\n')
            output_box.insert('1.0', '-' * 20)
            output_box.insert(1.0, '\n')
            output_box.insert('1.0', 'Files Found: ' + str(TotalCount))
            output_box.insert(1.0, '\n')
            output_box.insert('1.0', 'File List Operation Completed: ' + str(datetime.datetime.now()))
            output_box.insert(1.0, '\n')
            output_box.insert('1.0', '-' * 20)
            output_box.insert(1.0, '\n')
            break
    output_box.insert(50.0, '\n')
    output_box.insert('50.0', '-' * 20)
    output_box.insert(50.0, '\n')
button_list_all.bind('<Button-1>', list_all_pressed)
#----------------------------------------------------------
def remove_pressed(event):
    path = path_entry.get()
    output_box.insert('1.0', 'Remove Operation Started: ' + str(datetime.datetime.now()))
    output_box.insert(1.0, '\n')
    output_box.insert('1.0', '-' * 20)
    output_box.insert(1.0, '\n')
    
    TotalCount = 0
    CurrentName = 0

    for r, d, f in sorted(os.walk(path, topdown=True)):
        for file in f:
            CurrentName = os.path.join(r, file)
            BaseName = re.sub('[[@*&?].*[]@*&?]', '', CurrentName)
            if '[' in file:
                rename(CurrentName, BaseName)
                TotalCount += 1
                FinalName = BaseName[:-4] + BaseName[-4:]
                rename(BaseName, FinalName)
                output_box.insert('1.0', 'New Name: ' + str(FinalName))
                output_box.insert(1.0, '\n')

    output_box.insert(1.0, '\n')
    output_box.insert('1.0', '-' * 20)
    output_box.insert(1.0, '\n')
    output_box.insert('1.0', 'Files Renamed: ' + str(TotalCount))
    output_box.insert(1.0, '\n')
    output_box.insert('1.0', 'Codec Remove Operation Completed: ' + str(datetime.datetime.now()))
    output_box.insert(1.0, '\n')
    output_box.insert('1.0', '-' * 20)
    output_box.insert(1.0, '\n')
    
    output_box.insert(50.0, '\n')
    output_box.insert('50.0', '-' * 20)
    output_box.insert(50.0, '\n')
    TotalCount = 0

button_remove.bind('<Button-1>', remove_pressed)
#----------------------------------------------------------

#----------------------------------------------------------

window.mainloop()



