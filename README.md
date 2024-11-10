# audioMicroservicePomodoro

## Description: 

**microservice.py**

This microservice (microservice.py) accepts requests via a ZeroMQ socket for a selected song, a random song or a random category within a theme from the iLife Sound Effects    library. It then converts the respective file from a Core Audio Format (.caf) into a Waveform Audio Format (.wav) compatible with most programatic audio players. The converted file is then saved within your local project directory in a folder called tempaudiofolder where it can be played. 
  
This file contains a predefined dictionary (file_dict) of .caf files selected from the iLife Sound Effects library that are greater than 30 seconds long.

Functions:

    convert_caf_to_wav(category, filename):
       convert caf to wav format and save file to tempaudiofolder (create directory if needed)

    def get_random():
       Returns a random song in a random category

    def get_random_from_category(category):
       Returns a random song in a specified category

    def get_file(selected_song):
       Returns a specified song

    
**testprogram.py**

Contains three example calls to the microservice, the basic setup for the two sockets needed to send and receive the feedback to and from the microservice respectively. 

**scandirect.py**

Used to regenerate a dictionary of songs from the iLife Sound Effects library of the desired length. An existing dictionary of songs >30 seconds exists in the microservice.py file. This file is only needed if it is desired to change the songs that are available. 

## Technologies:
Python
- ZeroMQ (microservice)
- pydub (fileconversion)
- random (random file selection)

## Requirements:
cffi==1.17.1
ffmpeg==1.4 
ffprobe==0.5
pycparser==2.22
pydub==0.25.1
pygame==2.6.1
pyzmq==26.2.0
sounddevice==0.5.1
soundfile==0.12.1
zmq==0.0.0

## Usage Instructions:
  Example Calls:
    Example of User wanting a random song within a category
```
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5556")
userRequestedSong = None
userRequestedTheme = "Jingles"
myMessage = (userRequestedSong or userRequestedTheme) or "random"
socket.send_string(myMessage)
```

## Communication Contract:
Write a mitigation plan by answering these questions:
  1.	For which teammate did you implement “Microservice A”?
      - Guillermo Morales
  2.	What is the current status of the microservice? Hopefully, it’s done!
      - The microservice is complete.
  3.	If the microservice isn’t done, which parts aren’t done and when will they be done?
      - Not applicable, microservice is complete.
  4.	How is your teammate going to access your microservice? Should they get your code from GitHub (if so, provide a link to your public or private repo)? Should they run your code locally? Is your microservice hosted somewhere? Etc.
      - The microservice is located at the GitHub link below as microservice.py https://github.com/rrowland15/audioMicroservicePomodoro 
      - Additionally, example calls to the microservice are included as testprogram.py and a script to build a dictionary of the .CAF files that are greater than 30 seconds is included as scandirect.py. 
  5.	If your teammate cannot access/call YOUR microservice, what should they do? Can you be available to help them? What’s your availability?
      - Message over discord and we will set up a time to discuss. My schedule is flexible and we are both on PST so it shouldn’t be a problem to find a time that works for the two of us. Should be able to find a time the day you contact me or the day after. 
  6.	If your teammate cannot access/call your microservice, by when do they need to tell you?
      - I understand that things come up but please do your best to contact me at least 48 hours before the assignment due date. 
  7.	Is there anything else your teammate needs to know? Anything you’re worried about? Any assumptions you’re making? Any other mitigations / backup plans you want to mention or want to discuss with your teammate?
      - We have already verified your main program is able to play the files converted to the .WAV format so I don’t expect there should be any issues. It appears that the path to the iLife Sound Effects was common on both our machines. If they aren’t in a common location or if there are files missing on your computer that aren’t included in your iLife Effects some calls to the microservice may return “False”. If this is the case, we can run fix the path to the directory or in the case where files are missing we can run the script I used to scan the directory and pull the songs of length greater than 30 seconds to rebuild the dictionary (I have included this file in the repo as scandirect.py)

  100. First list item
  - First nested list item
    - Second nested list item



