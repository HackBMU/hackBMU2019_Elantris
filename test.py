import face_recognition
import cv2

cap = cv2.VideoCapture(0)
image = face_recognition.load_image_file("deeshant.jpg")
known_encodings = face_recognition.face_encodings(image)[0]

print('Press s to dectect face')
print('Press x to exit')
while True:
    try:
        n = input()
        if n == 's':
            while True:
                ret, frame = cap.read()
                if ret:
                    image = frame[..., [2, 1, 0]]
                    try:
                        unknown_encoding = face_recognition.face_encodings(image)[0]
                    except:
                        pass
                    results = face_recognition.compare_faces([known_encodings],unknown_encoding)
                else:
                    break

                if results[0]:
                    print("face detected")

                cv2.imshow("window", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        elif n == 'x':
            exit(0)

        else:
            3/0
    except ZeroDivisionError:
        print("Please press from the choice")

    except:
        break

cap.release()
cv2.destroyAllWindows()
# known_image = face_recognition.load_image_file("Documents/known_people/deeshant.jpg")
# unknown_image = face_recognition.load_image_file("unknown.jpg")

# biden_encoding = face_recognition.face_encodings(known_image)[0]
# unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
