import  picamera

import  picamera.array

import  time

with picamera.PiCamera() as camera:
    camera.resolution=(640,480)
    camera.framerate=30
    print("start preview direct form GPU")
    camera.start_preview()
    time.sleep(10)
    print("end preview")