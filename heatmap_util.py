import cv2
import os
import numpy as np
from PIL import Image

def save_frames(filename):
    """
    Save individual frames from video.

    Frames are stored under the folder 'frames' and
    named frame{frame number}

    Parameters:
    filename (string): Name of the video file to save frames

    Returns:
    Nothing

    """
    print("Progress: Saving frames")
    # Open video
    cap = cv2.VideoCapture(filename)
    frame_num = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Save frames in chronological order
        cv2.imwrite("./frames/frame" + str(frame_num) + ".jpg", frame)
        frame_num += 1
    cap.release()

def find_background():
    """
    Find the backgrund of a video.

    Attempt to create an image that does not contain moving
    objects. Look at all frames and keep consistent pixels.

    Parameters:
    None

    Returns:
    Nothing

    """
    print("Progress: Determining background")
    # Holder for all the frames
    all_images = []
    # Iterate through saved frames and add them as numpy arrays
    for filename in os.listdir("./frames/"):
        all_images.append(np.array(Image.open("./frames/" + filename)))
    sequence = np.stack(all_images, 3)
    result = np.median(sequence, 3).astype(np.uint8)
    Image.fromarray(result).save("./background.jpg")
