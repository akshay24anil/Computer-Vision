import sys
from PIL import Image
from PIL import ImageColor
import cv2
import numpy
import sys

def main():
    # Get inputs from command line
    source_name = sys.argv[1]
    output_name = sys.argv[2]
    palette = [sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]]
    pixel_factor = int(sys.argv[7])

    # Deal with images
    if ".mp4" not in source_name:
        im = Image.open(source_name)
        # Get dimensions
        size = (im.size[0], im.size[1])
        im = palettize(size, im, palette, pixel_factor).resize(size=size)
        im.save(output_name)
    # Frames from videos must be extracted
    else:
        extract_frames(source_name, output_name, palette, pixel_factor)

def extract_frames(source_name, output_name, palette, pixel_factor):
    cap = cv2.VideoCapture(source_name)
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    frame_number = 1
    # Output file
    out = cv2.VideoWriter(output_name,cv2.VideoWriter_fourcc(*'DIVX'), cap.get(cv2.CAP_PROP_FPS), size)
    while(1):
        ret, frame = cap.read()
        if ret == True:
            im = Image.fromarray(frame)
            im = palettize(size, im, palette, pixel_factor).resize(size=size)
            # Color correction
            out.write(cv2.cvtColor(numpy.array(im), cv2.COLOR_RGB2BGR))
        else:
            break
        show_progress(frame_number,total_frames)
        frame_number += 1

def palettize(size, im, palette, pixel_factor):
    # Shrink to pixelate
    im = im.resize(size=(int(size[0]/pixel_factor), int(size[1]/pixel_factor)))
    gray_im = im.copy().convert('L').load()
    og_im = im.load()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            val = gray_im[i,j]
            if val > 192:
                og_im[i,j] = ImageColor.getrgb("#" + palette[0])
            elif val > 128:
                og_im[i,j] = ImageColor.getrgb("#" + palette[1])
            elif val > 64:
                og_im[i,j] = ImageColor.getrgb("#" + palette[2])
            else:
                og_im[i,j] = ImageColor.getrgb("#" + palette[3])
    return im

def show_progress(frame_number, total_frames):
    val = frame_number/total_frames
    # Limit prints by only updating when an increment is made
    if int((frame_number/total_frames * 10) % 10) - int(((frame_number - 1)/total_frames * 10) % 10) != 0:
        if val < 0.1:
            sys.stdout.write("\r░░░░░░░░░░")
        elif val < 0.2:
            sys.stdout.write("\r▓░░░░░░░░░")
        elif val < 0.3:
            sys.stdout.write("\r▓▓░░░░░░░░")
        elif val < 0.4:
            sys.stdout.write("\r▓▓▓░░░░░░░")
        elif val < 0.5:
            sys.stdout.write("\r▓▓▓▓░░░░░░")
        elif val < 0.6:
            sys.stdout.write("\r▓▓▓▓▓░░░░░")
        elif val < 0.7:
            sys.stdout.write("\r▓▓▓▓▓▓░░░░")
        elif val < 0.8:
            sys.stdout.write("\r▓▓▓▓▓▓▓░░░")
        elif val < 0.9:
            sys.stdout.write("\r▓▓▓▓▓▓▓▓░░")
        elif val < 1:
            sys.stdout.write("\r▓▓▓▓▓▓▓▓▓░")
        elif val == 1:
            sys.stdout.write("\r▓▓▓▓▓▓▓▓▓▓")
        sys.stdout.flush()

main()
