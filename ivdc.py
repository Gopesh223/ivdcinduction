import cv2
import numpy as np

# Function to process a single video frame
def process_frame(frame):
    # Resize the frame to a fixed 800x800 resolution
    frame = cv2.resize(frame, (800, 800))
    
    # Convert the frame to grayscale for easier processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply binary thresholding to isolate the black line (inverted colors for black detection)
    _, binary = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
    
    # Define a 3x3 kernel for morphological operations
    kernel = np.ones((3, 3), np.uint8)
    
    # Use morphological closing to fill small gaps in the detected lines
    binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    
    # Use morphological opening to remove small noise
    binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    
    # Find contours of the detected lines
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Convert the binary image back to BGR for visualization
    result = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
    
    # Draw the detected contours on the result image in green
    cv2.drawContours(result, contours, -1, (0, 255, 0), 2)
    
    return result

# Open the video file
cap = cv2.VideoCapture('line.mp4')  

# Check if the video file was successfully opened
if not cap.isOpened():
    print("Error: Could not open video feed.")
    exit()

# Define output video properties
frame_width = 800
frame_height = 800
out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (frame_width, frame_height))

# Process each frame in the video
while True:
    # Read a frame from the video
    ret, frame = cap.read()
    
    # Exit the loop if no frame is read
    if not ret:
        print("Error: Failed to read frame.")
        break
    
    # Process the frame to detect the black line
    processed_frame = process_frame(frame)
    
    # Write the processed frame to the output video
    out.write(processed_frame)
    
    # Display the processed frame in a window
    cv2.imshow('Black Line Detection', processed_frame)
    
    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video resources
cap.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
