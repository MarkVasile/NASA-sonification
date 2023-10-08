#import the libraries
import cv2 as cv
import numpy as np

cap = cv.VideoCapture('nebula.mp4')
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

ret, frame1 = cap.read()

while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    average = frame.mean(axis=0).mean(axis=0)
    increment = lambda x: x+100
    decrement = lambda x: x-100
    lower_green = np.array([decrement(xi) for xi in average])
    upper_green = np.array([increment(xi) for xi in average])

    #create a mask for green colour using inRange function
    mask = cv.inRange(rgb, lower_green, upper_green)
    mask_inv = cv.bitwise_not(mask)
    res = cv.bitwise_and(rgb, rgb, mask=mask_inv)

    binary = cv.threshold(mask_inv, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
    contours, _  = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        (x,y,w,h) = cv.boundingRect(cnt)
        result = {
            'size': 10,
            'movement': False,
            'position': {
                x: x,
                y: y
            },
            'velocity': {
                x: 0,
                y: 0
            }
        }
        cv.rectangle(res,(x,y),(x+w,y+h),(0,255,0),2)

    cv.imshow('frame1', res)
    cv.imshow('frame2', frame)

    diff_frame = cv.absdiff(frame1, frame)
    cv.imshow('diff_frame', diff_frame)

    frame1 = frame
    cv.imshow('frame3', cv.bitwise_or(res, diff_frame))

    # out.write(mask_inv)
    if cv.waitKey(1) == ord('q'):
        break

#read the image
img = cv.imread("Screenshot.png")

def process_image(img):
    #convert the BGR image to HSV colour space
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    # hsv = img

    average = img.mean(axis=0).mean(axis=0)

    #set the lower and upper bounds for the green hue
    # lower_green = np.array(average)
    # lower_green = average
    increment = lambda x: x+100
    decrement = lambda x: x-100
    lower_green = np.array([decrement(xi) for xi in average])
    upper_green = np.array([increment(xi) for xi in average])

    #create a mask for green colour using inRange function
    mask = cv.inRange(rgb, lower_green, upper_green)
    mask_inv = cv.bitwise_not(mask)

    #perform bitwise and on the original image arrays using the mask
    res = cv.bitwise_and(rgb, rgb, mask=mask)
    anti_res = cv.bitwise_not(rgb, rgb, mask=mask)


    binary = cv.threshold(mask_inv, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]

    # getting mask with connectComponents
    # ret, labels = cv.connectedComponents(binary)
    # for label in range(1,ret):
    #     mask = np.array(labels, dtype=np.uint8)
    #     mask[labels == label] = 255
    #     cv.imshow('component',mask)
    #     cv.waitKey(0)

    # getting ROIs with findContours
    contours, _  = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        (x,y,w,h) = cv.boundingRect(cnt)
        cv.rectangle(mask,(x,y),(x+w,y+h),(0,255,0),2)
    # cv.imshow('ROI2', gray)



    cv.namedWindow("res", cv.WINDOW_NORMAL)
    cv.namedWindow("mask", cv.WINDOW_NORMAL)
    cv.namedWindow("markers", cv.WINDOW_NORMAL)
    cv.namedWindow("anti_res", cv.WINDOW_NORMAL)
    cv.namedWindow("mask_inv", cv.WINDOW_NORMAL)


    #display the images
    cv.imshow("mask", mask)
    # cv.imshow("markers", markers)
    cv.imshow("res", res)
    cv.imshow("anti_res", anti_res)
    cv.imshow("mask_inv", mask_inv)

    if cv.waitKey(0):
        cv.destroyAllWindows()

# process_image(img)
