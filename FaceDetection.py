# OpenCV program to detect face in real time 
# import libraries of python OpenCV 
# where its functionality resides 
import cv2 
import time

# Grey Scale Cascade Pre-Built Modules
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml') 
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml') 

# Detection of facial features and etc using gray scale cascading wih a ratio of 3:5 or 3:4 (not a nanami reference) by checking the frame in gray scale and implementing on VGR GBR
# This uses ROI calculation of coordinates x,y,width,height
def detect(gray, frame): 
	faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
	for (x, y, w, h) in faces: 
		cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (0, 255, 0), 2) 
		roi_gray = gray[y:y + h, x:x + w] 
		roi_color = frame[y:y + h, x:x + w] 
		smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20) 

		for (sx, sy, sw, sh) in smiles: 
			cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 255, 0), 1)  
	# loop over the detected faces
	for (x,y,w,h) in faces:
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		# detects eyes of within the detected face area (roi)
		eyes = eye_cascade.detectMultiScale(roi_gray)
		
		# draw a rectangle around eyes
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)
	return frame

# Finally reading the video and detection at once taking place by constantly capturing video while video_capture is activated
# Creating gray scale and controlling using q
video_capture = cv2.VideoCapture(0) 
while video_capture.isOpened(): 
# Captures video_capture frame by frame 
	_, frame = video_capture.read() 

	# To capture image in monochrome					 
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
	
	# calls the detect() function	 
	canvas = detect(gray, frame) 

	# Displays the result on camera feed					 
	cv2.imshow('Video', canvas) 

	# Click Photo
	if cv2.waitKey(1) & 0xff == ord('v'):			 
		cv2.imwrite(filename='saved_img.jpg', img=frame)
		video_capture.release()
		img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
		img_new = cv2.imshow("Captured Image", img_new)
		cv2.waitKey(1650)
		cv2.destroyAllWindows()
		print("Processing image...")
		img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
		print("Converting RGB image to grayscale...")
		gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
		print("Converted RGB image to grayscale...")
		print("Resizing image to 28x28 scale...")
		img_ = cv2.resize(gray,(28,28))
		print("Resized...")
		img_resized = cv2.imwrite(filename=f'{time.strftime("%Y-%m-%D")}.jpg', img=img_)
		print("Image saved!")

	# The control breaks once q key is pressed						 
	if cv2.waitKey(1) & 0xff == ord('q'):			 
		break

# Release the capture once all the processing is done. 
video_capture.release()								 
cv2.destroyAllWindows() 
