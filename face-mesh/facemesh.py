import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

res = cv2.VideoWriter('facemesh.mov', cv2.VideoWriter_fourcc('m','p','4','v'), 15, (1920, 1080), True)

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image)

    # Draw the face mesh annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_face_landmarks:
      for face_landmarks in results.multi_face_landmarks:
        for landmark in face_landmarks.landmark:
          shape = image.shape 
          relative_x = int(landmark.x * shape[1])
          relative_y = int(landmark.y * shape[0])

          cv2.circle(image, (relative_x, relative_y), radius=1, color=(225, 255, 255), thickness=1)

    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Face Mesh', cv2.flip(image, 1))

    image = cv2.resize(image, (1920, 1080))
    res.write(image)


    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
res.release()