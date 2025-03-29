from ultralytics import YOLO

model = YOLO('yolov8x')
results = model.predict('input_video/08fd33_4.mp4', save=False)
print(results[0])
print('====================')
for box in results[0].boxes:
    print(box)