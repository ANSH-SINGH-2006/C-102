import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(1,100)
    #Initialising the camera
    videocaptureobject=cv2.VideoCapture(0)
    result=True
    while (result):
        #read the frames while cam is on
        ret,frame=videocaptureobject.read()
        #cv.imwrite() used to save image to any storage device.
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time=time.time()
        result=False
    return img_name
    print("Snapshot taken")
    #release the cam
    videocaptureobject.release()
    #destroy all the windows that might be involved in the process.
    cv2.destroyAllWindows()

def upload_files(img_name):
    access_token="igGWm8_WrTUAAAAAAAAAAWiWV4biEzUwUktMeH6EJ5iiUPAA_qsQDafvYg3CxIyx"
    file=img_name
    file_from=file
    file_to="/testfolder/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File Successfully Uploaded!")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_files(name)

main()