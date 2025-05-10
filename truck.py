import cv2
import serial
import time
from ultralytics import YOLO

# Initialize Serial Communication
ser = serial.Serial('COM6', 9600, timeout=1)

# Load YOLO Model
model = YOLO("yolov8l.pt")  
TRUCK_CLASS_ID = 7  

# Open Cameras
cap_uphill = cv2.VideoCapture(0)
cap_downhill = cv2.VideoCapture(1)

# Time tracking variables
last_detected_uphill = 0
last_detected_downhill = 0
DETECTION_TIMEOUT = 3  # seconds

while cap_uphill.isOpened() and cap_downhill.isOpened():
    ret_up, frame_up = cap_uphill.read()
    ret_down, frame_down = cap_downhill.read()

    if not ret_up or not ret_down:
        print("Error: Could not read from one or both cameras")
        break

    results_up = model(frame_up)
    results_down = model(frame_down)

    current_time = time.time()

    def detect_truck(results, frame):
        for result in results:
            for box in result.boxes:
                cls = int(box.cls[0])  
                conf = float(box.conf[0])  
                if cls == TRUCK_CLASS_ID and conf > 0.3:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.putText(frame, "Truck", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                    return True
        return False

    # Detection
    if detect_truck(results_up, frame_up):
        last_detected_uphill = current_time

    if detect_truck(results_down, frame_down):
        last_detected_downhill = current_time

    # Check if trucks are still considered detected
    truck_uphill = (current_time - last_detected_uphill) < DETECTION_TIMEOUT
    truck_downhill = (current_time - last_detected_downhill) < DETECTION_TIMEOUT

    # Serial communication logic
    if truck_uphill and truck_downhill:
        ser.write(b'B')
        print("Truck detected on both sides: Sent 'B' to esp")
    elif truck_uphill:
        ser.write(b'U')
        print("Truck detected on uphill: Sent 'U' to esp")
    elif truck_downhill:
        ser.write(b'D')
        print("Truck detected on downhill: Sent 'D' to esp")
    else:
        ser.write(b'0')
        print("No truck detected: Sent '0' to esp")

    # Camera labels
    cv2.putText(frame_up, "UPHILL", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(frame_down, "DOWNHILL", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    combined_frame = cv2.hconcat([frame_up, frame_down])
    cv2.imshow("Uphill | Downhill Truck Detection", combined_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
ser.close()
cap_uphill.release()
cap_downhill.release()
cv2.destroyAllWindows()
