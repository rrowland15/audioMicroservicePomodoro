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

