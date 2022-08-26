import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# Using the haarcascade_frontalface_default built in class in order to render the cv2 face detection algorithm
# Libray can be found in the documentation or downloaded from the cv2 library


img = cv2.imread("GordonDindi.jpg")
# Image being processed. Will later on use mutliple images
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# At this point I'm making the images black and white

faces = face_cascade.detectMultiScale(
    grey_img,
    scaleFactor=1.1,
    # Image will scale down by 10% until it finds each face in the image
    # Looks for features such as eyes, chin and also smile/mouth in
    # order to determine whether a faces is detected
    minNeighbors=5,
)

for x, y, width, height in faces:
    """
    iterating through each face
        We want to use the numpy.array generated from the image
            we will look at the x, y value in order to find the starting point of our detection rectangle
            the actual size of the block will be determined by the x, y values added to the height and width
                I set the color of the block as green(using b,g,r method) with a border thickness of 3
    """
    img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 3)

print(type(faces))
print(faces)

resized = cv2.resize(img, (int(img.shape[1] / 3), int(img.shape[0] / 3)))

cv2.imshow("FaceDetected", resized)
# Name of the new cv2 image
cv2.waitKey(0)
cv2.destroyAllWindows()
