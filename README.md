# Black Line Detection in Video

## Overview
This project demonstrates a computer vision pipeline for detecting black lines in video frames. The program processes each frame, highlights the black line by drawing contours around it, and outputs the processed frames to a new video file. 

The initial approach used the GrabCut algorithm for background isolation, but it was replaced with a more efficient thresholding-based method due to performance limitations.

---

## Working of the Code
1. **Video Input and Frame Resizing**  
   The program begins by loading a video file (`line.mp4`). Each frame is resized to 800x800 pixels for consistency and to reduce computational overhead.  

2. **Grayscale Conversion**  
   The frame is converted to a grayscale image to simplify processing since color information is not required for black line detection.  

3. **Thresholding**  
   Binary inverse thresholding is applied to isolate black areas (the lines) in the frame. Pixels with intensity values below the threshold (50) are turned white, while others are turned black.

4. **Morphological Operations**  
   Morphological transformations (closing and opening) are used to:
   - Fill small gaps in the black line (closing).
   - Remove noise from the binary image (opening).

5. **Contour Detection and Drawing**  
   Contours of the detected black line are identified using the `findContours` function. These contours are then drawn on the frame in green to highlight the detected line.

6. **Frame Output**  
   The processed frames are displayed in real-time and written to an output video file (`output.mp4`).

---

## Why GrabCut Was Replaced
Initially, the GrabCut algorithm was implemented to isolate the black line from the background. However:
- GrabCut had high computational overhead, making it unsuitable for real-time video processing.
- Re-initializing the GrabCut mask for every frame caused further delays.

In contrast, the thresholding-based approach is faster, simpler, and more efficient, making it ideal for detecting black lines in video frames.

---

## Limitations and Problems
1. **Noise in Frames**  
   Dark areas such as shadows, barriers, or other objects in the video can sometimes be misidentified as black lines.

2. **Road-like Areas in Videos**  
   If the black line is not sufficiently dark, the thresholding operation may fail to detect it accurately, leaving parts of the line undetected.

---


