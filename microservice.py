from pydub import AudioSegment
import random
import os
import zmq


file_dict={'Textures': ['Super Stager.caf'],
     'Transportation': ['Sail Boat.caf', 'Ship in Heavy Sea.caf', 'Airplane Cabin.caf'],
     'Stingers': ['Synthetic Design 02.caf', 'Space Log .caf'],
     'Jingles': ['Starlight Lounge.caf', 'Park Bench.caf', 'Offroad Long.caf', 'Half Dome Medium.caf',
                 'Stepping Out Medium.caf', 'Galleria Long.caf', 'Jaracanda.caf', 'Catwalk Long.caf',
                 'Collins Avenue Long.caf', 'Headspin Long.caf', 'Half Moon Bay Long.caf', 'Greasy Wheels Long.caf',
                 'Three Pointer Long.caf', 'Tour Bus Long.caf', 'Dogma.caf', 'Sanskrit.caf', 'Progressive House.caf',
                 'Spacey Club.caf', 'Vino.caf', 'First Snowfall.caf', 'Daydream.caf', 'Campfire.caf', 'Shetland.caf',
                 'Peach Cobbler.caf', 'Newborn.caf', 'Chaise Lounge Long.caf', 'Highlight Reel Long.caf', 'Travel.caf',
                 'Vista.caf', 'Chelsea Loft Long.caf', 'Wild Card Long.caf', 'Torn Jeans Long.caf', 'Tigris.caf',
                 '44th Street Long.caf', 'Island Long.caf', 'Tennessee Twister Long.caf', 'East Ender Long.caf',
                 'Electric Rodeo Long.caf', 'Pendulum.caf', 'Curtain Call Long.caf', 'Off Broadway.caf',
                 'Dolce Vita.caf', 'Acoustic Sunrise.caf', 'Gelato.caf', 'Elysium Long.caf', 'Motocross.caf',
                 'Watercolor Long.caf', 'Yearbook Long.caf', 'Medal Ceremony Long.caf', 'Carousel.caf', 'Havana.caf',
                 'Undercover.caf', 'Dustbowl.caf', 'Bossa Lounger Long.caf', 'Dewdrops.caf', 'Swing City Long.caf',
                 'Jazzy Downtempo.caf', 'Lazy Day.caf', 'Celestial Body Long.caf', 'Stepping Out Long.caf',
                 'Glide Long.caf', 'Kickflip Long.caf', 'Buddy.caf', 'Piano Ballad.caf', 'Broadcast News Long.caf',
                 'West Precinct Long.caf', 'Indulge.caf', 'Time Lapse.caf', 'Lotus.caf', 'Roller Derby.caf',
                 'Fireside.caf', 'Gleaming Long.caf', 'Breakbeat Long.caf', 'Pastel Slide Long.caf', 'Shogun.caf',
                 'Midnite Dialog Long.caf', 'River Walk.caf', 'Barbeque Blues Long.caf', 'Fifth Avenue Stroll.caf',
                 'Two Seater Long.caf', 'Half Dome Long.caf'],
     'People': ['Lobby Conversation.caf', 'Stadium Crowd Chant.caf', 'Cheering Crowd Studio.caf', 'Busy Station.caf',
                'Swimming.caf'],
     'Ambience': ['Ocean Surf.caf', 'Rain Heavy Thunder.caf', 'Forest.caf', 'Cave Water Drops.caf',
                  'Forest Evening.caf', 'Concrete Jungle.caf', 'Traffic.caf', 'Jungle.caf'],
     'Booms': ['Volcano Erupting.caf'],
     'Foley': ['Scuba Breathing.caf', 'Rescue Helicopter.caf', 'Clock Wind Up.caf', 'Grandfather Clock Strike.caf',
               'Antique Clock Strike.caf', 'Traffic Helicopter.caf']}

def convert_caf_to_wav(category, filename):
    """convert caf to wav format and save file to tempaudiofolder (create directory if needed)"""
    if not os.path.isdir("tempaudiofolder"):
        os.mkdir("tempaudiofolder")

    newfilename = "temp.wav"
    audio = AudioSegment.from_file("/Applications/iMovie.app/Contents/Resources/iLife Sound Effects/{}/{}".format(category,filename), format="caf")
    audio.export("tempaudiofolder/{}".format(newfilename), format="wav")

def get_random():
    ''' Returns a random song in a random category'''
    category, songs = random.choice(list(file_dict.items()))
    song = random.choice(list(songs))
    print("category:", category, "song:", song)
    filename = song
    convert_caf_to_wav(category,filename)
    return True

def get_random_from_category(category):
    ''' Returns a random song in a specified category'''
    try:
        song = random.choice(file_dict[category])
        print("song:", song)
        filename = song
        convert_caf_to_wav(category, filename)
        return True
    except:
        return False

def get_file(selected_song):
    ''' Returns a specified song'''
    for category, songs in file_dict.items():
        for song in songs:
            if song == selected_song:
                convert_caf_to_wav(category, song)
                return True
    print("song doesn't exist in list")
    return False


print("waiting for user to make audio selection")
message_rcvd = False
while not message_rcvd:
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:5556") # tcp socket 2
    method = socket.recv().decode('utf-8')
    if method == "random":
        completed = get_random()
    elif method in file_dict.keys():
        completed = get_random_from_category(method)
    else:
        completed = get_file(method)

    # Send message back to user saying everything was completed and the song can be played
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:5557")

    if completed:
        print("Message sent back to main program that file pushed to testaudiofolder")
        socket.send_string("True")

    else:
        print("something went wrong, check your category and song name")
        socket.send_string("False")



