# AutoAprilTools
Crappy script that automates [AprilTools](https://github.com/thegoodhen/AprilTools).

This python script takes a video, splits it into an image sequence using cv2, estimates the focal length and tracks the video using [AprilTools](https://github.com/thegoodhen/AprilTools).

# Usage
1. Import `colorama` and `opencv-python`.

 `python -m pip colorama
 python -m pip opencv-python`
 
 2. Download [AprilTools](https://github.com/thegoodhen/AprilTools) and set the exe's path in the script
 
 Example: `aprilToolsPath = "D:\Blender\AprilTools\AprilTools.exe"`

3. Run it:

'python <script path> <video path>'
Example: `python D:\Blender\AutoAprilTools.py D:\Blender\test\P1030256.MP4`
# Why
I thought it's a good opportunity to learn python. The script is pretty crappy but it works.
