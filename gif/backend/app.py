import os
from PIL import Image
from datetime import datetime


def gif_creat(directory_files):
    
    directory_files.sort(key=lambda x: int(x.split(".")[0]))
    frame_list = []

    for frame_number in directory_files:
        frame = Image.open(os.path.join('homer', frame_number))
        frame_list.append(frame)

    gif_name = F'gif_{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.gif'

    frame_list[0].save(
        f'gif_save/{gif_name}',
        save_all=True,
        append_images=frame_list[1:],
        optimize=True,
        duration=100,
        loop=0
    )

    return gif_name