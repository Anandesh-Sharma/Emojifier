import cv2

face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')


def detect_faces(photo):
    '''
    :param photo: The real image
    :return: mapped values of normalizing_face and face_coords
    '''
    # face_coords is array of [x,y,w,h]
    face_coords = where_is_face(photo)

    # cropped_face is the cropped ndarray of picture with colour intensity RGB
    cropped_face = [photo[y:y + h, x:x + w] for (x, y, w, h) in face_coords]

    # normalizing_face is the cropped ndarray of picture with colour intensity gray
    normalizing_face = [normalized_face(face) for face in cropped_face]

    # returns the final ndarray of image
    return zip(normalizing_face, face_coords)


def normalized_face(face):
    # convert the image to gray color
    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

    # resize the image
    face = cv2.resize(face, (350, 350))

    # return the ndarray of image
    return face


def where_is_face(img):
    # detect the image and returns the co-ordinates of the face
    faces = face_cascade.detectMultiScale(img, 1.1, 15)
    return faces
    # faces will return (x,y,w,h) of the  face
