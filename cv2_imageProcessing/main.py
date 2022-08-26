import cv2
import glob

"""     Cv2 representation
    glob will find class names with a certain pattern, in this case we want all the jpg images
    Here we're reading information from the image iterating through each image found with glob
    image is then resized to its preferred size(100 x 100 as instructed in the exercise)
        The resized image will then be saved and saved as a jpg image under the resized_images
            Each image will contain text "resized_" plus the actual name of the image
"""

images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image, 0)
    re = cv2.resize(img, (100, 100))
    cv2.imshow("Processing image", re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_images/resized_" + image, re)
