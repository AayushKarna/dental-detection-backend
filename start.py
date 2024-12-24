import cv2
from ultralytics import YOLO

# Load the YOLOv8 model (pre-trained on COCO dataset)
model1 = YOLO('yolov8n.pt')

# Perform prediction on an image
results = model1('person.jpg', show=True)

# To get more details on the results, you can print the results
# print(results)

for result in results:
    img = result.plot()
    cv2.imshow('YOLO prediction', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()