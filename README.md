# 🕹️ Temple Run - Hand Gesture Control

Control **Temple Run** using just your hand gestures! This project uses your webcam and applies real-time hand tracking to simulate key presses like jump, duck, and move left/right — all without touching the keyboard.

## 🎯 Features

- 🖐️ Real-time hand detection using **MediaPipe**
- 🎮 Simulated keyboard control via **pynput**
- 🔄 Swipe detection for left/right
- ⬆️ Raise hand to jump
- ⬇️ Lower hand to duck
- 🧠 Smooth gesture recognition with direction and cooldown logic
- 🟩 Visual guide zones and gesture arrows to help with control

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- pynput (keyboard simulation)
- NumPy

## 🚀 How It Works

1. Webcam captures your hand in real-time.
2. MediaPipe tracks the landmarks of your hand (wrist & fingertip).
3. Code calculates movement directions:
   - Horizontal swipes → left/right
   - Vertical movement → jump/duck
4. Pynput simulates actual keyboard key presses based on gestures.
5. You play Temple Run... hands-only!

## 🔧 Controls

| Gesture           | Action         |
|------------------|----------------|
| Swipe Left        | Move Left      |
| Swipe Right       | Move Right     |
| Raise Hand Up     | Jump           |
| Move Hand Down    | Duck           |

> Tip: Keep your hand within the green control box shown on the screen for better detection.

## 🎥 Visual Demo (Optional)
Add a short GIF or video clip here showing the game being controlled via gestures.

## 📦 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/KartikNimhan/TempleRun-Gesture-Control.git
   ```

2. **Install dependencies**
   ```bash
   pip install opencv-python mediapipe pynput numpy
   ```

3. **Run the app**
   ```bash
   python main.py
   ```

4. Make sure Temple Run (or any game that uses arrow keys) is in focus while the script is running.

## 📁 File Overview

```
temple_run_handgesture/
├── main.py                # Main application logic
├── README.md              # Project description
```

## 🙌 Notes

- Make sure your webcam is enabled.
- Lighting and hand distance can affect tracking accuracy.
- This project is great for exploring computer vision + gesture control for real-world applications!

---

Enjoy hands-free gaming! 😎
```

