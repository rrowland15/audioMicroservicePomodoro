import os
from pydub import AudioSegment

# Get the list of all files and directories
final_dict = dict()
path_categories = "/Applications/iMovie.app/Contents/Resources/iLife Sound Effects"
dir_list = os.listdir(path_categories)
print(dir_list)

for category in dir_list:
    path_files = "/Applications/iMovie.app/Contents/Resources/iLife Sound Effects/{}".format(category)
    dir_list2 = os.listdir(path_files)
    print(dir_list2)
    final_dict[category]=[]

    for file in dir_list2:
        file_path = "/Applications/iMovie.app/Contents/Resources/iLife Sound Effects/{}/{}".format(category,file)
        audio_length = AudioSegment.from_file(file_path).duration_seconds
        print(audio_length)
        if audio_length > 30:
            final_dict[category].append(file)

print(final_dict)
#
# def get_audio_length(file_path):
#     audio = AudioSegment.from_file(file_path)
#     return audio.duration_seconds
#
# for file in dir_list:
#     length_in_seconds = get_audio_length(path+file)
#     if length_in_seconds>10:
#         final_list.append(file)
#     print("Length of the audio file:", length_in_seconds, "seconds")