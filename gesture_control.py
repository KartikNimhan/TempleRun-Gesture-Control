import cv2
import mediapipe as mp
import numpy as np
from pynput.keyboard import Controller, Key
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,  # Only track one hand
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)
mp_draw = mp.solutions.drawing_utils

# Keyboard Controller
keyboard = Controller()

# Game Controls
JUMP_KEY = Key.up
DUCK_KEY = Key.down
LEFT_KEY = Key.left
RIGHT_KEY = Key.right

# Gesture Thresholds (adjust based on your movement)
SWIPE_THRESHOLD = 80  # Minimum pixels for swipe detection
JUMP_THRESHOLD = 60   # Vertical rise for jump
DUCK_THRESHOLD = 60   # Vertical drop for duck
HOLD_DURATION = 0.3   # Seconds to hold a key press

# Previous hand position (for movement tracking)
prev_hand_x, prev_hand_y = None, None
last_action_time = 0
action_cooldown = 0.2  # Prevent rapid repeated inputs

# Main loop
cap = cv2.VideoCapture(0)
prev_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Mirror the frame
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get frame dimensions
    height, width, _ = frame.shape

    # Draw control zone (helps with hand positioning)
    control_zone = (width//4, height//4, 3*width//4, 3*height//4)
    cv2.rectangle(frame, (control_zone[0], control_zone[1]), 
                 (control_zone[2], control_zone[3]), (0, 255, 0), 2)

    # Hand detection
    results = hands.process(rgb_frame)
    action = None

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get wrist (base of hand) and index fingertip positions
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            wrist_x, wrist_y = int(wrist.x * width), int(wrist.y * height)
            index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

            # Draw movement direction (helps visualize gestures)
            cv2.arrowedLine(frame, (wrist_x, wrist_y), (index_x, index_y), (255, 0, 0), 2)

            # Detect movement if previous position exists
            if prev_hand_x and prev_hand_y:
                dx = wrist_x - prev_hand_x
                dy = wrist_y - prev_hand_y

                # Detect swipe left/right
                if abs(dx) > SWIPE_THRESHOLD:
                    if dx > 0:
                        action = "RIGHT"
                    else:
                        action = "LEFT"

                # Detect jump (hand moves up)
                elif dy < -JUMP_THRESHOLD:
                    action = "JUMP"

                # Detect duck (hand moves down)
                elif dy > DUCK_THRESHOLD:
                    action = "DUCK"

            prev_hand_x, prev_hand_y = wrist_x, wrist_y

    # Execute action (with cooldown)
    current_time = time.time()
    if action and (current_time - last_action_time > action_cooldown):
        print(f"Action: {action}")
        if action == "LEFT":
            keyboard.press(LEFT_KEY)
            time.sleep(HOLD_DURATION)
            keyboard.release(LEFT_KEY)
        elif action == "RIGHT":
            keyboard.press(RIGHT_KEY)
            time.sleep(HOLD_DURATION)
            keyboard.release(RIGHT_KEY)
        elif action == "JUMP":
            keyboard.press(JUMP_KEY)
            time.sleep(0.1)  # Short press for jump
            keyboard.release(JUMP_KEY)
        elif action == "DUCK":
            keyboard.press(DUCK_KEY)
            time.sleep(0.2)  # Slightly longer for duck
            keyboard.release(DUCK_KEY)

        last_action_time = current_time

    # Display FPS and action status
    fps = 1 / (time.time() - prev_time)
    prev_time = time.time()
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
    cv2.putText(frame, f"Last Action: {action if action else 'None'}", (10, 70), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

    cv2.imshow("Temple Run Hand Gesture Control", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


