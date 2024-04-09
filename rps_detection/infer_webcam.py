import cv2
from ultralytics import YOLO
import argparse

def load_and_infer_video(video_path, model_path):
    # Load the YOLO model
    model = YOLO(model_path)

    # Load the video
    cap = cv2.VideoCapture(video_path)  # Load webcam

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break
        # Perform inference on the frame

        results = model.predict(frame, imgsz=640, conf=0.5)
        # Process the results
        annotated_frame = results[0].plot()
        # ...
        # Display the frame with bounding boxes
        cv2.imshow('Inference' + str(video_path), annotated_frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


# Create an argument parser
parser = argparse.ArgumentParser(description='Video path for load_and_infer_video')

# Add an argument for video path
parser.add_argument('--video_path', default="1", type=int, help='Path to the video file')
parser.add_argument('--model_path', default="rps_detection/pretrained/yolov8n-best.pt", type=str, help='Path to the video file')

# Parse the arguments
args = parser.parse_args()

# Example usage
video_path = args.video_path
model_path = args.model_path
load_and_infer_video(video_path, model_path)

