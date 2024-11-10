# audioMicroservicePomodoro

## Description: 

<ins>**microservice.py**</ins>

This microservice (microservice.py) accepts requests via a ZeroMQ socket for a selected song, a random song or a random category within a theme from the iLife Sound Effects library. It then converts the respective file from a Core Audio Format (.caf) into a Waveform Audio Format (.wav) compatible with most programatic audio players. The converted file is then saved within your local project directory in a folder called tempaudiofolder where it can be played. 
  
This file contains a predefined dictionary (file_dict) of .caf files selected from the iLife Sound Effects library that are greater than 30 seconds long.

**Functions:**
  Arguments for these selected song and category parameters are included at the bottom of this README as a part of additional information.

    convert_caf_to_wav(category, filename):
       convert caf to wav format and save file to tempaudiofolder (create directory if needed)

    def get_random():
       Returns a random song in a random category.

    def get_random_from_category(category):
       Returns a random song in a specified category.

    def get_file(selected_song):
       Returns a specified song.

    def read_request():
       Waits for the main program to send a request for a song and then processes the request to the appropriate functions listed above.

    def return_status():
       Returns "True" to the main program if the file was converted and saved to the local directory folder (tempaudiofolder) and "False" otherwise.

    
<ins>**testprogram.py**</ins>

Contains three example calls to the microservice, the basic setup for the two sockets needed to send and receive the feedback to and from the microservice respectively. 

<ins>**scandirect.py**</ins>

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

  ### How to request a song

  There are 3 different requests that the microservice is able to handle. The first if a user who is requesting a specific song. In this case the userRequestedSong parameter will need to have a .caf file specified that the user is looking for (see example 1 below). Alternatively, if a user is looking for a random song within a category they will just specify the userRequestedTheme (see example 2 below). Lastly if the user wants a completely random song then none of the parameters need to be assigned a value (see example 3 below). 

  - Example 1: A user wanting a specific song
```
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5556")              # tcp socket 1
userRequestedSong = "Island Long.caf"
userRequestedTheme = None
myMessage = (userRequestedSong or userRequestedTheme) or "random"
socket.send_string(myMessage)
```

* Example 2: A user wanting a random song within a category
```
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5556")              # tcp socket 1
userRequestedSong = None
userRequestedTheme = "Jingles"
myMessage = (userRequestedSong or userRequestedTheme) or "random"
socket.send_string(myMessage)
```

+ Example 3: A user wanting a completely random song
```
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5556")              # tcp socket 1
userRequestedSong = None
userRequestedTheme = None
myMessage = (userRequestedSong or userRequestedTheme) or "random"
socket.send_string(myMessage)
```

### How to receive a song

The song will automatically be saved to a local directory (which will automatically be created for the user) called tempaudiofolder. This is where a file called temp.wav will be stored and overwritten when additional song requests occur. However, if you are looking for confirmation that the file is converted and saved in the location the microservice will return "True" if the transaction occured and "False" otherwise. 

- Example of User receiving confirmation that file has been converted and saved to tempaudiofolder directory
```
received = None

while received== None:
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:5557")             # tcp socket 2
    received = socket.recv().decode('utf-8')
    print("file upload received in tempaudiofolder")
```

## UML Diagram
The UML diagram below shows the basic interactions between the main program and the microservice. 

![image](https://github.com/user-attachments/assets/37159030-0200-4c31-a286-1cba6529a1b4)



## Communication Contract:
Write a mitigation plan by answering these questions:
  1.	For which teammate did you implement “Microservice A”?
        -  Guillermo Morales
  2.	What is the current status of the microservice? Hopefully, it’s done!
        -  The microservice is complete.
  3.	If the microservice isn’t done, which parts aren’t done and when will they be done?
        -  No problems.
  4.	How is your teammate going to access your microservice? Should they get your code from GitHub (if so, provide a link to your public or private repo)? Should they run your code locally? Is your microservice hosted somewhere? Etc.
        -  The microservice is located at the GitHub link below as microservice.py https://github.com/rrowland15/audioMicroservicePomodoro and will need to be run locally.
        -  Additionally, example calls to the microservice are included as testprogram.py and a script to build a dictionary of the .CAF files that are greater than 30 seconds is included as scandirect.py. 
  5.	If your teammate cannot access/call YOUR microservice, what should they do? Can you be available to help them? What’s your availability?
        -  Message over discord and we will set up a time to discuss. My schedule is flexible and we are both on PST so it shouldn’t be a problem to find a time that works for the two of us. Should be able to find a time the day you contact me or the day after. 
  6.	If your teammate cannot access/call your microservice, by when do they need to tell you?
        -  I understand that things come up but please do your best to contact me at least 48 hours before the assignment due date (November 23rd)
  7.	Is there anything else your teammate needs to know? Anything you’re worried about? Any assumptions you’re making? Any other mitigations / backup plans you want to mention or want to discuss with your teammate?
        -  We have already verified your main program is able to play the files converted to the .WAV format so I don’t expect there should be any issues. It appears that the path to the iLife Sound Effects was common on both our machines. If they aren’t in a common location or if there are files missing on your computer that aren’t included in your iLife Effects some calls to the microservice may return “False”. If this is the case, we can run fix the path to the directory or in the case where files are missing we can run the script I used to scan the directory and pull the songs of length greater than 30 seconds to rebuild the dictionary (I have included this file in the repo as scandirect.py)

## Additional Information:
Below I have included information about the song categories/themes that the user will be able to choose among as well as the corresponding song .caf files that a user would be able to choose from in the event that they wanted a specific song. These will have to be preprescibed for the user. *Note that the .caf files shown are those that are greater than 30 seconds in length*

Song Categories/Themes: 
  dict_keys(['Textures', 'Transportation', 'Stingers', 'Jingles', 'People', 'Ambience', 'Booms', 'Foley'])

Song Names:
  dict_values([['Super Stager.caf'], ['Sail Boat.caf', 'Ship in Heavy Sea.caf', 'Airplane Cabin.caf'], ['Synthetic Design 02.caf', 'Space Log .caf'], ['Starlight Lounge.caf', 'Park Bench.caf', 'Offroad Long.caf', 'Half Dome Medium.caf', 'Stepping Out Medium.caf', 'Galleria Long.caf', 'Jaracanda.caf', 'Catwalk Long.caf', 'Collins Avenue Long.caf', 'Headspin Long.caf', 'Half Moon Bay Long.caf', 'Greasy Wheels Long.caf', 'Three Pointer Long.caf', 'Tour Bus Long.caf', 'Dogma.caf', 'Sanskrit.caf', 'Progressive House.caf', 'Spacey Club.caf', 'Vino.caf', 'First Snowfall.caf', 'Daydream.caf', 'Campfire.caf', 'Shetland.caf', 'Peach Cobbler.caf', 'Newborn.caf', 'Chaise Lounge Long.caf', 'Highlight Reel Long.caf', 'Travel.caf', 'Vista.caf', 'Chelsea Loft Long.caf', 'Wild Card Long.caf', 'Torn Jeans Long.caf', 'Tigris.caf', '44th Street Long.caf', 'Island Long.caf', 'Tennessee Twister Long.caf', 'East Ender Long.caf', 'Electric Rodeo Long.caf', 'Pendulum.caf', 'Curtain Call Long.caf', 'Off Broadway.caf', 'Dolce Vita.caf', 'Acoustic Sunrise.caf', 'Gelato.caf', 'Elysium Long.caf', 'Motocross.caf', 'Watercolor Long.caf', 'Yearbook Long.caf', 'Medal Ceremony Long.caf', 'Carousel.caf', 'Havana.caf', 'Undercover.caf', 'Dustbowl.caf', 'Bossa Lounger Long.caf', 'Dewdrops.caf', 'Swing City Long.caf', 'Jazzy Downtempo.caf', 'Lazy Day.caf', 'Celestial Body Long.caf', 'Stepping Out Long.caf', 'Glide Long.caf', 'Kickflip Long.caf', 'Buddy.caf', 'Piano Ballad.caf', 'Broadcast News Long.caf', 'West Precinct Long.caf', 'Indulge.caf', 'Time Lapse.caf', 'Lotus.caf', 'Roller Derby.caf', 'Fireside.caf', 'Gleaming Long.caf', 'Breakbeat Long.caf', 'Pastel Slide Long.caf', 'Shogun.caf', 'Midnite Dialog Long.caf', 'River Walk.caf', 'Barbeque Blues Long.caf', 'Fifth Avenue Stroll.caf', 'Two Seater Long.caf', 'Half Dome Long.caf'], ['Lobby Conversation.caf', 'Stadium Crowd Chant.caf', 'Cheering Crowd Studio.caf', 'Busy Station.caf', 'Swimming.caf'], ['Ocean Surf.caf', 'Rain Heavy Thunder.caf', 'Forest.caf', 'Cave Water Drops.caf', 'Forest Evening.caf', 'Concrete Jungle.caf', 'Traffic.caf', 'Jungle.caf'], ['Volcano Erupting.caf'], ['Scuba Breathing.caf', 'Rescue Helicopter.caf', 'Clock Wind Up.caf', 'Grandfather Clock Strike.caf', 'Antique Clock Strike.caf', 'Traffic Helicopter.caf']])
