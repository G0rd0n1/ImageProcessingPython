import cv2, time, pandas
from datetime import datetime

first_frame = None
frame_counter = 1
status_list = [None, None]
time_slots = []
df = pandas.DataFrame(columns=["START", "END"])


video = cv2.VideoCapture(0)
# This is where the camera starts and records the information it captures

while True:
    frame_counter += 1
    check, frame = video.read()
    status = 0
    # Frame would be the first element of the video object

    # print(check)
    # print(frame)
    # Here I'm simply checking that the numpy array of the check and frame contain something
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey = cv2.GaussianBlur(grey, (21, 21), 0)

    if first_frame is None:
        first_frame = grey
        continue

    delta_frame = cv2.absdiff(first_frame, grey)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts, _) = cv2.findContours(
        thresh_frame.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    for contours in cnts:
        if cv2.contourArea(contours) < 10000:
            continue
        status = 1
        (x, y, width, height) = cv2.boundingRect(contours)
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 3)
    status_list.append(status)

    status_list = status_list[-2:]

    if status_list[-1] == 1 and status_list[-2] == 0:
        time_slots.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        time_slots.append(datetime.now())

    cv2.imshow("Capturing grey video", grey)
    cv2.imshow("Capturing delta_frame", delta_frame)
    cv2.imshow("Capturing threshold_frame", thresh_frame)
    cv2.imshow("Capturing color_frame", frame)
    # This is where we display the video image captured in the first frame

    key = cv2.waitKey(1)
    print(grey)
    print(delta_frame)
    print(thresh_frame)
    # At this point we are displaying the images caught from the cv2 camera

    if key == ord("q"):
        if status == 1:
            time_slots.append(datetime.now())
        break


print("Below is a list of the cv2 image status': \n", status_list)
print(str(frame_counter) + " frames were captured.")
print("Data was captured at the following timestamps \n", time_slots)

for i in range(0, len(time_slots), 2):
    df = df.append(
        {"START": time_slots[i], "END": time_slots[i + 1]}, ignore_index=True
    )
df.to_csv("Captured_timeSlots.csv")
video.release()
cv2.destroyAllWindows()
# Waits for keyboard entry before closing all the windows
