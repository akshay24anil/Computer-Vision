import numpy as np
from PIL import Image
from PIL import ImageChops
from heatmap_util import *

# Replace with path of video to analyze
filename = './vtest_Trim.mp4'
# Replace with number of frames to analyze
num_frames = 30

save_frames(filename)
find_background()
# Open background in grayscale for easier processing
background = Image.open("./background.jpg").convert("L")
result = np.array(Image.open("./background.jpg"))
changes = np.zeros(shape=np.array(background).shape)

print("Progress: Analyzing frames")
for frame_num in range(num_frames):
    frame = Image.open("./frames/frame" + str(frame_num) + ".jpg").convert("L")
    diff = np.array(ImageChops.difference(background, frame))
    for index, pixel in np.ndenumerate(diff):
        # Threshold for relavant pixels
        if pixel > 50:
            changes[index] += 1
# 1020 from 255s for rgb
multiplier = 1020 / np.max(changes)
for index, pixel in np.ndenumerate(changes):
    if pixel > 0:
        red = 0
        blue = 0
        green = 0
        val = pixel * multiplier
        if val <= 255:
            blue = 255
            green = val
        elif val <= 510:
            blue = 510 - val
            green = 255
        elif val <= 765:
            red = val - 510
            green = 255
        else:
            red = 255
            green = 765 - val
        result[index] = (red, green, blue)

Image.fromarray(result).save("result.jpg")
print("Progress: Finished")
