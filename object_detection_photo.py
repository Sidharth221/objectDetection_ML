from ultralytics import YOLO
import cv2

model = YOLO('../Yolo-Weights/yolov8n.pt')
results = model("images/sampl.jpg", show=True)
# results = model("../videos/bikes.mp4", show=True)   #FOR VIDEOS
cv2.waitKey(0)