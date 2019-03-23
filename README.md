# hackBMU2019_Elantris
## Attendance System Using Facial Recognition. 
Facial recognition is a type of biometric technology that uses statistical measurements of people's features to digitally determine identity.
The system is developed for deploying an easy and a secure way of taking down attendance.
<br/>
*Why Facial recognition you may ask?*
1. Face recognition is time efficient.
2. Face recognition can be used in many work environment.
3. Fast and Accurate.
4. Cheap and Easy Installation.
5. Does not store personal data.
>Face recognition devices create a 3D model of your face by mapping out distinct points. The system then stores a numerical code to represent this model. The numerical code cannot be used for anything other to check if it is you in front of the camera.

## How it works?
We use three libraries *face_recognition*,*mtcnn* and *cv2* for Facial Recognition. Teacher can take attendance with just a single click, A closed portal is used for this. The teacher must first login to the online portal before he/she can take attendance. When the button is clicked the camera captures the photo which is then compared to the face encodings already stored in the database.

```
import face_recognition
image = face_recognition.load_image_file("your_file.jpg")
face_locations = face_recognition.face_locations(image)
```
**Get the locations and outlines of each person's eyes, nose, mouth and chin. The face_detection command lets you find the location (pixel coordinatates) of any faces in an image.**

```
from mtcnn.mtcnn import MTCNN
import cv2
img = cv2.imread("ivan.jpg")
detector = MTCNN()
```
**It gives  [x, y, width, height] under the key 'box'** <br/>
face_encoding now contains a universal 'encoding' of the person's facial features that can be compared to any other picture of a face! Then we can compare the two face encodings are of the same person with *compare_faces*!
