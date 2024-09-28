from ultralytics import YOLO
import numpy, pandas

# Load the YOLO model
model = YOLO("yolov8n.pt")

# Perform object detection on an image
detection_output = model.predict(source="/Users/jarvis/pymycod/yolo/inferences/images/1.jpeg", conf=0.25, save=False)

# Print the detection output
print(detection_output)

# Uncomment to print the output as a numpy array
# print(detection_output[0].numpy())
