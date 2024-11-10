import zmq
import pygame

# Example of User wanting a specific song
# context = zmq.Context()
# socket = context.socket(zmq.REQ)
# socket.connect("tcp://127.0.0.1:5556")
# userRequestedSong = "Island Long.caf"
# userRequestedTheme = None
# myMessage = (userRequestedSong or userRequestedTheme) or "random"
# socket.send_string(myMessage)


# Example of User wanting a random song within a category
# context = zmq.Context()
# socket = context.socket(zmq.REQ)
# socket.connect("tcp://127.0.0.1:5556")
# userRequestedSong = None
# userRequestedTheme = "Jingles"
# myMessage = (userRequestedSong or userRequestedTheme) or "random"
# socket.send_string(myMessage)



# Example of User wanting a completely random song
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5556")
userRequestedSong = None
userRequestedTheme = None
myMessage = (userRequestedSong or userRequestedTheme) or "random"
socket.send_string(myMessage)
print("request sent from testprogram")



# Now we wait for the microservice to return that the file was converted and uploaded succesfully
received = None

while received== None:
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:5557")             # tcp socket 2
    received = socket.recv().decode('utf-8')
    print("file upload received in tempaudiofolder")




def play_audio(file_path):
    """Plays the selected audio file using pygame."""
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if received == "True":
    print("time to listen!")
    play_audio("tempaudiofolder/temp.wav")

elif received == "False":
    print("song or category does not exist")