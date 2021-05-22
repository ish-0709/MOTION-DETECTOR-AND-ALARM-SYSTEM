# Detection of an object and human and also dealing with the motion of both of them.
import cv2
import pandas
from datetime import datetime
import pyttsx3
import speech_recognition as sr

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

baseimg = None

# a list for storing any moving object
status_list = [None, None]

# time of movement
times = []

df = pandas.DataFrame(columns=["Start", "End"])

# capture the video which is playing many images at a faster pace
video = cv2.VideoCapture(0)

# setting parameters for voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', 101110)
engine.setProperty('rate', 150)

r = sr.Recognizer()

############################## introduced this new function to take in text (Arg) and speak ###########


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    #############################CHECK IF THE ABOVE LINE IS NEEDED##################
    engine.say(command)
    engine.runAndWait()

############### new function for password verification if the object is  human ################


def isHumanHome():

    SpeakText("HUMAN DETECTED.")
    print("HUMAN DETECTED .")

    # use the microphone as source for input.
    with sr.Microphone() as source2:
        SpeakText("what's the password?")
        # wait for a second to let the recognizer
        # adjust the energy threshold based on
        # the surrounding noise level
        r.adjust_for_ambient_noise(source2, duration=0.2)

        # listens for the user's input
        audio2 = r.listen(source2)

        # Using ggogle to recognize audio
        MyText = r.recognize_google(audio2)
        MyText = MyText.lower()
        # Exception handling to handle
    # exceptions at the runtime
    try:
        print("Did you say "+MyText)
        SpeakText(MyText)
        if(MyText == "star"):
            SpeakText("Welcome home!")
        else:
            SpeakText("Entry denied!")

    except:
        pass


while True:
    isHuman = 0
    check, frame = video.read()
    status = 0
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    faces = face_cascade.detectMultiScale(gray_frame, 1.1, 4)

    # face recognition
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        isHuman = 1

    if baseimg is None:
        baseimg = gray_frame
        continue

    frame_diff = cv2.absdiff(baseimg, gray_frame)
    threshframe = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)[1]
    threshframe = cv2.dilate(threshframe, None, iterations=2)

    (cnts, _) = cv2.findContours(threshframe.copy(),
                                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1

        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        # object=green human =blue

    status_list.append(status)

    status_list = status_list[-2:]

    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())

    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    cv2.imshow("Grey Frame", gray_frame)
    cv2.imshow("Frame Difference", frame_diff)
    cv2.imshow("Threshold Frame", threshframe)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

    if(status == 1 and isHuman == 0):
        engine.say("OBJECT DETECTED.")
        print('OBJECT DETECTED')
        engine.runAndWait()
    if (status == 1 and isHuman == 1):
        # engine.say("HUMAN DETECTED. HELLO BEAUTIFUL.")
        # print("HUMAN DETECTED .")
        # engine.runAndWait()
        isHumanHome()
        isHuman = 0


print(status_list)
print(times)

for i in range(0, len(times), 2):
    df = df.append({"Start": times[i], "End": times[i + 1]}, ignore_index=True)

df.to_csv("Times.csv")
# clear memory
engine.stop()
video.release()
cv2.destroyAllWindows()