# 🕹️ Temple Run - Hand Gesture Control

This project allows you to control **Temple Run** using hand gestures, powered by your webcam. It uses **OpenCV** and **MediaPipe** for real-time hand tracking and gesture recognition.

### 🎯 Features

- Control game character with hand gestures (e.g., jump, slide, move left/right)
- Real-time video feed with gesture detection
- Fun and hands-free gameplay experience!

### 🛠️ Tech Stack

- Python
- OpenCV
- MediaPipe
- PyAutoGUI (for simulating keyboard presses)

### 🚀 How It Works

1. Webcam captures your hand in real-time
2. MediaPipe tracks hand landmarks
3. Gestures are mapped to keyboard inputs
4. These inputs control Temple Run on your PC

### 🖥️ Requirements

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI

Install dependencies:
```bash
pip install opencv-python mediapipe pyautogui
