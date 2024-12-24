import cv2
from ultralytics import YOLO

def predict(image):
    model = YOLO('runs/detect/train8/weights/best.pt')

    results = model(f"./{image}")

    for result in results:
        img = result.plot()
        cv2.imshow('YOLO prediction', img)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    output = []
    for result in results:
        result_dict = {
            "path": result.path,
            "orig_shape": result.orig_shape,
            "boxes": [],
            "names": result.names,
            "speed": result.speed
        }

        if result.boxes:
            for box in result.boxes:
                xywh_list = box.xywh.tolist()
                print(box.xywh.tolist())
                box_data = {
                    "x": xywh_list[0][0],
                    "y": xywh_list[0][1],
                    "w": xywh_list[0][2],
                    "h": xywh_list[0][3],
                    "confidence": float(box.conf[0]),
                    "class": int(box.cls[0])
                }

                result_dict["boxes"].append(box_data)

        output.append(result_dict)

    return output
    # print(results.plot())

    # for result in results:
    #     img = result.plot()
    #     cv2.imshow('YOLO prediction', img)

    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()

    # print(results)