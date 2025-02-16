import cv2
from ultralytics import YOLO

def main():
    cap = cv2.VideoCapture(0)  # Open default camera
    model = YOLO("runs/detect/train/yolov8s_100epochs/weights/best.pt")  # Load trained YOLO model

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    while True:
        ret, frame = cap.read()  # Capture frame-by-frame
        if not ret:
            print("Failed to grab frame")
            break

        results = model.predict(frame)  # Perform object detection
        annotated_frame = results[0].plot()  # Get the annotated frame with bounding boxes
        
        cv2.imshow("Webcam Feed", annotated_frame)  # Display the frame
        
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
