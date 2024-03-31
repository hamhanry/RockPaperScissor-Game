# RockPaperScissor-Game

![RockPaperScissor-Game](contents/rps-youtube.png)

## Introduction
It is a model that used to predict rock, paper, scissor game using hand sign. The model is trained using a single GPU with around 6,000 images. 

## Results
The methods used are YOLOV8 with the following results:

| model | size (pixels) | mAP50 val | mAP50-95 val | FLOPs (B) | Link |
| ----- | ------------- | --------- | ------------ | --------- | ---- |
|YOLOv8n| 640| 0.956 | 0.78 | 8.7 | [download](https://huggingface.co/hamhanry/RockPaperScissor-Game/blob/main/yolov8n-best.pt)
|YOLOv8x| 640| 0.962 | 0.792 | 257.8 | [download](https://huggingface.co/hamhanry/RockPaperScissor-Game/blob/main/yolo8x-best.pt)

Download the pretrained model and put those under `pretrained` folder

*Note : I trained with 2 backbone options that you could choose, the smallest one (YOLOv8n) or the biggest one (YOLOv8X).*

## Contact
If any feature requests please write on this [github issues](https://github.com/hamhanry/RockPaperScissor-Game/issues)

## More
Hopefully this pretrained model benefits for those who need it. If you are one that benefits this project, please give me a high five by assigning a *STAR*.