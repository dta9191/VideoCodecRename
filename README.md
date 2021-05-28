# VideoCodecRename
Python program using ffprobe3 to recursively search all files in a directory, identify video files, and add their codec to the file name for easy filtering in any system. Easily modified to find, rename, move, and sort all kinds of files using ffmpeg. This is just the video specific program.

![VideoCodecRename_codec_added](https://user-images.githubusercontent.com/57654891/119913564-3561cc00-bf2c-11eb-8a25-ce453b790543.png)


Combined with HBBatchBeast for bulk video conversion, standardizing video collections from multiple sources is far easier and faster.
This project actually inspired me to get into programming, so many, many thanks for all the work that went into it.
HBBatchBeast can be found Here: https://github.com/HaveAGitGat/HBBatchBeast

It requires ffprobe3, which can be found at: https://github.com/DheerendraRathor/ffprobe3. 
Much thanks to DheerendraRathor for making ffprobe3. I might be able to work with ffmpeg directly these days, but there was no chance when I first started on this project. This is also my first GitHub project, so bear with me as I try to learn it all. This project is one giant learning experience for me.
I've only ever tested it on Linux systems, so I have no idea how it will do on other systems. This is the first program I ever made, so it's rough, but functional. I hope it might help someone someday.

I made this program when I was working on organizing a large media collection, consisting mostly of videos. Old DVD backups mostly. Some of the files used modern codecs, like h264, but many used outdated codecs, like mpeg. These older codecs weren't ideal for streaming over my local network, and I decided it was time to convert them and get everything as modern as possible. The problem I ran into was that I had no idea what codecs the files were using, or how to find them in bulk. Linux doesn't have any kind of built in filter for video codec that I could find, and I couldn't find a single useable solution for months. I remember seeing something in Sonaar or something where it could filter by codec, but I couldn't even find documentation on that. I ended up asking a friend to teach me to program in Python so I could solve the problem myself. Luckily he was a software engineer at the time and got me off to a great start. I set programming aside for about a year to rebuild my life after the pandemic hit in 2020, and this project sat dormant for the longest time. Today I overhauled the entire thing, added a few nice features, and built a simple GUI using tkinter. I tried to keep everything as simple and standard as possible so it could run on most systems. The only special code is the ffprobe3 code, as far as I know, but that's easy enough to install.

Warnings:
This program works, but not well. There is no progress indicator as of the first release, so it looks like the program is frozen as it runs. If the button you clicked stays gray, it's most likely running. You can open the working directory to see the files being renamed. I have no idea of the likelihood of corrupting files with this program, so use at your own risk, though, I hven't had a single problem over many thousands of files. Not all codecs are supported, as I haven't gotten to that point. The program writes "[ERROR]" to the file name for any file that throws any kind of exception. It's a quick and dirty way to just chug through the files and get it done. This will be fixed when I dive into error handling. These problems will be far easier to work around as I add features. 

Some instructions:

Start the program, and paste or type in the directory you'd like to work with in the "Working Directory" field at the top. Press the "List All Files" button to see all files in the directory and all the directories it contains(recursive lookup). I always list them all first to make sure I have a valid, and the proper directory. Use the "Clear Output Display" button to clear the screen, if needed. Please note that the tidy file stats will eventually be implemented in all operations, so that you can see exactly what has been done after every operation. 

Descriptions of buttons and features:

"List All Files":

Show all files of all types found in the directory(recursive lookup).
  ![VideoCodecRename_Listed_files](https://user-images.githubusercontent.com/57654891/119913606-588c7b80-bf2c-11eb-9fa2-0fd3ffb73665.png)

"Find Video Files": 

Attempts to open every file with ffmpeg and read its stream data and determine the codec used for stream 0(usually the main video stream for video files). It compares the codec found to the <VideoCodecs> list, and if a match is found, prints the file directory and name, as well as the video codec to the output box in the main window.I have the option to ignore all files that don't match a known video file extension type(such as .mp4), but I exclude it in order to find video files that may be hiding under different extensions. The ffporbe3 module should be able to open the video regardless of extension. No changes are made to files using this option.
  ![VideoCodecRename_filtered_videos](https://user-images.githubusercontent.com/57654891/119913621-604c2000-bf2c-11eb-81e2-0be7db10af29.png)

"Add Video Codec To File Name":
  
This is the main feature of the program, which renames the file by adding [<codec>] before the file extension. Example: farts.mp4, encoded with h265 becomes farts[h265].mp4. The square brackets([]) were chosen as media software such as Plex, EMby, and Jellyfin will ignore anything in brackets in the file name. I started with Plex, which is why this was important to me. I didn't want the codec name to appear anywhere users could see it. It worked just fine last I checked. Please verify that this will not be a problem.
  ![VideoCodecRename_codec_added](https://user-images.githubusercontent.com/57654891/119913764-b8832200-bf2c-11eb-8ff6-38b0ab32ac2c.png)

"Remove Video Codec From File Name":
  
This button undoes the "Add Video Codec To File Name" actions. It doesn't simply reverse the changes like "undo", it checks the files names for "[" and removes anything between square brackets. Be careful with this one as it will remove anything in brackets, not just the video codec. I plan to have it check the list of known codecs before renaming the file, but that will have to wait. This feature is useful for when you need to update the codec type, as the "ADD" program skips any files that have codec information in the name already. That skipping speeds things up considerably when files don't change and only new ones are being added. It can cause problems though, as things get converted and the file name information becomes outdated. It is recommended to run the "Remove" operation, followed by the "Add" operation before trying to do any batch work with video files. I will likely combine the "Remove" and "Add" functions in the near future to make updating files easier. The program would "Remove" any codec information from the file names, then "Add" it back to get things up to date.  
  ![VideoCodecRename_codec_removed](https://user-images.githubusercontent.com/57654891/119914837-29c3d480-bf2f-11eb-9bcf-55de89eb2163.png)


"Clear Output Display":
  
This button just wipes the screen, so you can start fresh. I find it helpful as the output is a bit messy during the early stages. 

That's all for now. I hope you find this as useful as I have. 
