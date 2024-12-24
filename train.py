from ultralytics import YOLO

def main():
    model = YOLO('yolov8n.pt')
    model.train(data='data.yaml', epochs=50, batch=16, imgsz=800, device=0)

if __name__ == '__main__':
    main()