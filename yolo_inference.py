from ultralytics import YOLO 

path_model = r''
path_video = r''

model = YOLO(path_model)

results = model.predict(path_video,save=True)
for box in results[0].boxes:
    print(box)