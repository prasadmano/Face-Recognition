# Kivy is a graphical user interface library
import kivy.core.text
from kivy.app import App
from kivy.base import EventLoop
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition,SlideTransition
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
# OpenCV is an open source computer vision and machine learning software library.
import cv2,csv
# pickle is an byte converter
import time, os, pickle
# PIL is the Python Imaging Library
import PIL.Image
#  Numerical computing tools
import numpy as np
# The collection Module in Python provides different types of containers.
from collections import OrderedDict
from datetime import date
import pandas as pd




# prediction page function for kivy camera
class KivyCamera_student(Image):
    # Initialization of funtion without any operation
    def __init__(self, **kwargs):
        super(KivyCamera_student, self).__init__(**kwargs)
        self.capture = None
    # Switching on the camera
    def start(self, capture, fps=30):
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)
    # Switching off the camera
    def stop(self):
        Clock.unschedule_interval(self.update)
        self.capture = None
    # camera operation
    def update(self, dt):
        return_value, frame = self.capture.read()
        if return_value:
            texture = self.texture
            w, h = frame.shape[1], frame.shape[0]
            fname = "trainer.yml"
            global face_cascade, recognizer, data
            with open('data.pkl', 'rb') as fp:
                 data = pickle.load(fp)
            if not texture or texture.width != w or texture.height != h:
                global onframe1,photo_count1,num1, final_name, count
                #Initializating all variables
                onframe1 = 0
                photo_count1 = 0
                num1 = 3
                count = {}
                final_name = ['Train again']
                #print('inside first loop')
                face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                recognizer.read(fname)
                self.texture = texture = Texture.create(size=(w, h))
                texture.flip_vertical()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            # FOR COUNTDOWN
            if onframe1 <= 60:
                cv2.putText(frame,  str(num1),  (250, 250), cv2.FONT_HERSHEY_SIMPLEX , 3,  (0, 255, 255),  20,  cv2.LINE_4)
                if onframe1 <= 30 and onframe1 % 20 == 0:
                    num1 -= 1

            elif onframe1 >= 60 and onframe1 <= 100:
                for (x,y,w,h) in faces:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
                    ids,conf = recognizer.predict(gray[y:y+h,x:x+w])
                    print(data)
                    # getting name from directory
                    name = data.get(ids)
                    print(name)
                    if conf < 50:
                        cv2.putText(frame, str(name), (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (150,255,0),2)
                        final_name.append(name)
                    else:
                        cv2.putText(frame, 'No Match', (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
                    #print(onframe1)
            else:
                test = most_frequent(final_name)
                if test == 'Train again':
                    text_output = 'Not Registered'
                else:
                    text_output = 'Thank You ' + test
                    csv_registering(test)
                cv2.rectangle(frame, (0, 0), (800, 700), (0, 0, 0), -1)
                cv2.putText(frame,  str(text_output),  (10, 60), cv2.FONT_HERSHEY_SIMPLEX , 2,  (0, 255, 255),  2,  cv2.LINE_4)
            onframe1 += 1
            cv2.rectangle(frame, (150, 100), (420, 420), (0, 20, 200), 10)
            texture.blit_buffer(frame.tobytes(), colorfmt='bgr')
            self.canvas.ask_update()
        else:
            onframe1 = 0
            num1 = 3
            final_name = ['Train again']
            count = {}

class KivyCamera_admin(Image):

    def __init__(self, **kwargs):
        super(KivyCamera_admin, self).__init__(**kwargs)
        self.capture = None

    def start(self, capture, fps=30):
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)

    def stop(self):
        Clock.unschedule_interval(self.update)
        self.capture = None

    def update(self, dt):
        return_value, frame = self.capture.read()
        image = frame
        if return_value:
            texture = self.texture
            w, h = frame.shape[1], frame.shape[0]
            if not texture or texture.width != w or texture.height != h:
                global onframe,photo_count,num
                onframe = 0
                photo_count = 0
                num = 3
                self.texture = texture = Texture.create(size=(w, h))
                texture.flip_vertical()
            if onframe <= 60:
                cv2.putText(frame,  str(num),  (250, 250), cv2.FONT_HERSHEY_SIMPLEX , 3,  (0, 255, 255),  20,  cv2.LINE_4)
                if onframe <= 30 and onframe % 20 == 0:
                    num -= 1
            elif onframe >= 60 and onframe % 2 == 0:
                 #print(onframe)
                 if photo_count <= 30:
                     print(path)
                     filepath = path +'\\'+ str(photo_count)+'.png'
                     #print(filepath)

                     cv2.imwrite(filepath, image)
                     photo_count += 1
                 else:
                     pass
            if photo_count >= 30:# and photo_count <= 60:
                cv2.rectangle(frame, (0, 0), (800, 700), (0, 0, 0), -1)
                photo_count += 1
            else:
                cv2.putText(frame,  '.',  (50, 50),  cv2.FONT_HERSHEY_SIMPLEX , 1,  (0, 255, 255),  2,  cv2.LINE_4)
            cv2.rectangle(frame, (150, 100), (420, 420), (0, 20, 200), 10)
            texture.blit_buffer(frame.tobytes(), colorfmt='bgr')
            self.canvas.ask_update()
            onframe += 1
        else:
            if onframe>1:
                onframe = 0
                photo_count = 0
                num = 3


def for_col(self):
    today = str(date.today())
    #print(today)
    df = pd.read_csv('test.csv',index_col=False)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    print(df)
    dates = list(df)
    #print(dates[-1])
    if dates[-1] == today:
        #print('in if')
        pass
    else:
        #print('in else')
        df[today] = np.nan
        #print(df)
        df.to_csv('test.csv', index=False)


for_col('test')

# dataframe names ask_update

def for_names(name_update):
    df = pd.read_csv('test.csv', index_col=False)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    #print(df)
    name_list = df['name'].tolist()
    print(name_list)
    name_list_dup = name_list
    for name in name_list:
        print(name)
        if name == name_update:
            n = 1
            #print('in if')
        else:
            n = 0
    if n == 0:
        #name_list_dup.append(name_update)
        print(name_list_dup)
        with open('test.csv','a+', newline='') as f:
            wr = csv.writer(f, dialect='excel')
            a = [name_update]
            wr.writerow(a)

        #print(df)


def csv_registering(present_name):
    today = str(date.today())
    df = pd.read_csv('test.csv', index_col=False)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df.at[(df['name'] == present_name), today] = 1
    df.to_csv('test.csv', index=False)


def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i

    return num

# for training dataSet
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector= cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml");
id_num = 0

def getImagesAndLabels(path):
    folder = os.listdir(path)
    id_num = 0
    faceid_dict = {}

    #create empth face list
    faceSamples=[]
    #create empty ID list
    Ids=[]
    for i in folder:
        # taking folder inside directory
        folder_path = str(path) +'/'+ str(i)
        files = os.listdir(folder_path)
        faceid_dict[id_num] = i

        print(i)
        for j in files:
            print(j)
            # taking files inside the folder
            imagepath = str(folder_path) +'/'+ str(j)
            id = id_num
            #loading the image and converting it to gray scale
            pilImage= PIL.Image.open(imagepath).convert('L')
            #Now we are converting the PIL image into numpy array
            imageNp=np.array(pilImage,'uint8')
            # extract the face from the training image sample
            faces=detector.detectMultiScale(imageNp)
            #If a face is there then append that in the list as well as Id of it
            for (x,y,w,h) in faces:
                faceSamples.append(imageNp[y:y+h,x:x+w])
                #to see the image which is being trained
                img = cv2.rectangle(imageNp,(x,y),(x+w,y+h),(255,0,0),2)
                Ids.append(id)

                #print(Ids)
        id_num += 1
        #print(faceid_dict)
    a_file = open("data.pkl", "wb")
    pickle.dump(faceid_dict, a_file)
    a_file.close()
    return faceSamples,Ids

capture = None

class HomeScreen(Screen):
    pass

class RightSide(Screen):

    def dostart(self, *largs):
        global capture
        capture = cv2.VideoCapture(0)
        self.ids.qrcam.start(capture)

class LeftSide(Screen):

    def dostart(self, *largs):
        global capture
        capture = cv2.VideoCapture(0)
        self.ids.qrcam.start(capture)

    def textinputandcreatefolder(self):

       text = self.ids.textinput.text
       #print(text)
       for_names(str(text))
       databasefolder = '\\testdatabase'
       directory = text
       parent_dir = os.getcwd()
       parent_dir = parent_dir + databasefolder
       global path
       path = os.path.join(parent_dir, directory)
       try:
           os.mkdir(path)
       except:
           print('change path name')
       print(text)

kv = Builder.load_file("qrtest.kv")

class qrtestApp(App):

    def build(self):
        Window.bind(on_request_close=self.on_request_close)
        Window.size = (1020, 700)
        return kv

    def on_request_close(self, *args):
        
        print('going to exit')

    def on_stopapp(self):
        global capture
        if capture:
            capture.release()
            capture = None

    def dostart(self, *largs):
        global capture
        capture = cv2.VideoCapture(0)
        self.ids.qrcam.start(capture)

    def doexit(self, *largs):
        global capture

        if capture != None:
            capture.release()
            capture = None

    def traindata(self):
        global capture
        if capture:
            capture.release()
            capture = None
        faces,Ids = getImagesAndLabels('testdatabase')
        #print(Ids)
        #print(len(faces))
        labels=[0]*len(faces)
        #print(labels)
        #print(np.array(labels))
        recognizer.train(faces, np.array(Ids))
        #labels = np.random.randint(0, size=len(faces))
        #recognizer.train(faces, np.array(Ids))
        os.remove("trainer.yml")
        recognizer.write('trainer.yml')
        print('training completed')



qrtestApp().run()
