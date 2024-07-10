import cv2
import face_recognition
import os
import numpy as np

class FaceRecognitionSystem:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.load_known_faces()

    def load_known_faces(self):
        # Carregar imagens de uma pasta e codificar os rostos conhecidos
        path = 'known_faces'
        for filename in os.listdir(path):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                img = face_recognition.load_image_file(os.path.join(path, filename))
                encoding = face_recognition.face_encodings(img)[0]
                self.known_face_encodings.append(encoding)
                self.known_face_names.append(os.path.splitext(filename)[0])

    def recognize_faces(self):
        video_capture = cv2.VideoCapture(0)

        while True:
            ret, frame = video_capture.read()

            rgb_frame = frame[:, :, ::-1]

            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                name = "Unknown"

                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.known_face_names[best_match_index]

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    frs = FaceRecognitionSystem()
    frs.recognize_faces()
