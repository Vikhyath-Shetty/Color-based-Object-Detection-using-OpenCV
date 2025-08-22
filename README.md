# 🎨 Color-Based Object Detection

This project implements a simple **object detection system using OpenCV**.  
It detects objects in a video stream (camera or file) based on their **color**.  

---

## ✨ Features
- Detects objects of **4 colors**:
  - 🔴 Red
  - 🔵 Blue
  - 🟢 Green
  - 🟡 Yellow
- User specifies **which color** to track.
- User can set the **maximum number of objects** to detect at once.
- Highlights detected objects with bounding boxes.
- Clean modular code for easy extension

---
## 🛠 Requirements
- Python
- OpenCV
- NumPy
- uv

## ▶️ Usage
Install dependencies:
```bash
uv pip install requirements.txt
```

**Run**(flags are optional)
```bash
uv run main.py --camera <value> --color <value> -n <value>
```
```bash
 --camera(optional) : 0(default) | file | http 
```
---
#### FLAGS:

Specifies the camera source **(optional):**
```
--camera : 0(default) | http | file
```
Specifies the object color **(optional):**
```
--color(optional) : red(default) | Any color out of {red, green, blue, yellow} or its combination. 
```

Specifies the maximum number of objects to be detected,  at a time **(optional):**
```
-n(optional) : 1(default) | any number
```






