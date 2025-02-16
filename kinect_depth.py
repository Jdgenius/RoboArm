import cv2
import numpy as np
from  import PyKinectRuntime, PyKinectV2

# Initialize Kinect
kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Depth)

def get_depth_frame():
    """Captures a depth frame from Kinect and converts it to 8-bit grayscale."""
    if kinect.has_new_depth_frame():
        depth_frame = kinect.get_last_depth_frame()
        depth_frame = depth_frame.reshape((424, 512))  # Kinect depth resolution
        depth_frame = np.clip(depth_frame, 500, 4000)  # Limit depth range
        depth_frame = (depth_frame - 500) / (4000 - 500) * 255  # Normalize to 8-bit
        return depth_frame.astype(np.uint8)
    return None

def detect_candy_wrappers(depth_frame):
    """Detects objects in the depth frame using contour detection."""
    blurred = cv2.GaussianBlur(depth_frame, (5, 5), 0)
    _, thresholded = cv2.threshold(blurred, 50, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    detected_objects = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if 300 < area < 5000:  # Filter by size
            x, y, w, h = cv2.boundingRect(contour)
            detected_objects.append((x, y, w, h))

    return detected_objects

def draw_detections(frame, objects):
    """Draw bounding boxes around detected candy wrappers."""
    for (x, y, w, h) in objects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Candy Wrapper", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

while True:
    depth_image = get_depth_frame()
    if depth_image is None:
        continue

    detected_objects = detect_candy_wrappers(depth_image)
    draw_detections(depth_image, detected_objects)

    cv2.imshow("Kinect Depth Stream - Object Detection", depth_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cv2.destroyAllWindows()
