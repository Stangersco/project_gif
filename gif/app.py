import os

from PIL import Image

directory = os.path.join(os.getcwd(), 'homer')

directory_files = os.listdir(directory)

directory_files.sort(key=lambda x: int(x.split(".")[0]))

frame_list = []

for frame_number in directory_files:
    frame = Image.open(os.path.join(directory, frame_number))
    frame_list.append(frame)
    print(frame_number)


frame_list[0].save(
    'homer.gif',
    save_all=True,
    append_images=frame_list[1:],
    optimize=True,
    duration=100,
    loop=0
)
