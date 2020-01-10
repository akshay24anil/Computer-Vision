# Comuter-Vision
Scripts for image manipulation

## Installation

Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install OpenCV and Pillow.

```bash
pip3 install opencv-python
pip3 install pillow
```

## Usage

```python
import numpy as np
from PIL import Image
from PIL import ImageChops
from heatmap_util import *

# Replace with path of video to analyze
filename = './vtest_Trim.mp4'
# Replace with number of frames to analyze
num_frames = 30
```
Set values for `filename` and `num_frames` as they pertain to your video.

## Demo
Below is the first frame of a sample video.

![First Frame](https://raw.githubusercontent.com/akshay24anil/Image-Tools/master/frame0.jpg)

`heatmap.py` scans through all frames and generates a background image without moving objects:

![Background](https://raw.githubusercontent.com/akshay24anil/Image-Tools/master/background.jpg)

The script then generates a heatmap based on movement across frames:
![Result](https://raw.githubusercontent.com/akshay24anil/Image-Tools/master/result.jpg)
