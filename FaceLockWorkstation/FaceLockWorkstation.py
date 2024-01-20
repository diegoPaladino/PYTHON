import cv2
import pyautogui
import time
from threading import Thread

class FaceLockWorkstation:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.cap = cv2.VideoCapture(0)
        self.last_time_face_seen = time.time()

    def detect_faces(self, gray):
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        return len(faces) > 0

    def check_for_faces(self):
        while True:
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if self.detect_faces(gray):
                self.last_time_face_seen = time.time()
            else:
                if time.time() - self.last_time_face_seen > 5:
                    pyautogui.hotkey('win', 'ctrl', 'd')
                    break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    face_lock = FaceLockWorkstation()
    face_lock_thread = Thread(target=face_lock.check_for_faces)
    face_lock_thread.start()
