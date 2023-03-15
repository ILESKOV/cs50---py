import face_recognition
import numpy as np
from PIL import Image, ImageDraw

known_image = face_recognition.load_image_file("Bob.jpg")
encoding = face_recognition.face_encodings(known_image)[0]

unknown_image = face_recognition.load_image_file("group-of-people-18.jpeg")

face_locations = face_recognition.face_locations(unknown)
face_encodings = face_recognition.face_encodings(unknown, face_locations)

pil_image = Image.fromarray(unknown_image)

draw = ImageDraw.Draw(pil_image)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces([encoding], face_encoding)