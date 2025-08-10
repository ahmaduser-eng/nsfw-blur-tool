import cv2
import sys
import os
from nudenet import NudeDetector

detector = NudeDetector()

def blur_nsfw(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video")
        return
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out_path = "blurred_" + os.path.basename(video_path)
    out = cv2.VideoWriter(out_path, fourcc, cap.get(cv2.CAP_PROP_FPS), 
                          (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        detections = detector.detect(frame)
        for det in detections:
            if det['label'] not in ['EXPOSED_ANUS', 'EXPOSED_BREAST_F', 'EXPOSED_GENITALIA_F', 'EXPOSED_GENITALIA_M']:
                continue
            
            x1, y1, x2, y2 = det['box']
            roi = frame[y1:y2, x1:x2]
            if roi.size != 0:
                roi = cv2.GaussianBlur(roi, (99, 99), 30)
                frame[y1:y2, x1:x2] = roi
        
        out.write(frame)
    
    cap.release()
    out.release()
    print(f"Blurred video saved as {out_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nsfw_video_blur.py <video_path>")
    else:
        blur_nsfw(sys.argv[1])