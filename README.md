# This repository contains my computer vision projects
# 1. Automatic License Plate Detection with YOLOv8 and EasyOCR

This project is an automatic license plate detection system built using state-of-the-art deep learning models, YOLOv8 and EasyOCR. The system is capable of detecting and reading license plates from a video stream. It leverages YOLOv8 for robust object detection, accurately identifying vehicles and their bounding boxes in real-time. The detected vehicles are then tracked using the SORT (Simple Online and Realtime Tracking) algorithm, ensuring smooth tracking across frames.

Once the vehicles are tracked, the system utilizes EasyOCR to read the license plate numbers with impressive accuracy. The license plate information, along with the corresponding vehicle data, is extracted and saved in a CSV file for further analysis or processing

# 2. Parking Space Counter using Image Processing

This project is a parking space counter that automatically detects and counts free parking spaces in a given parking lot. The system processes video frames using image processing techniques to analyze each parking space's occupancy. Predefined positions representing parking space coordinates are used to crop regions of interest (ROIs) from the frames. The pixel intensity in each ROI is examined, and parking spaces with low pixel counts are considered available (displayed in green), while occupied spaces are shown in red. The system provides real-time feedback on the number of free parking spaces and the total number of spaces available. Additionally, users can interactively define and adjust parking space positions using the mouse. This solution helps efficiently manage parking lots and optimize parking operations.

