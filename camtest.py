import cv2 as cv 

def testDevice(source):
   cap = cv.VideoCapture(source) 
   cap.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc('M', 'J', 'P', 'G'))

   if cap is None or not cap.isOpened():
    print('Warning: unable to open video source: ', source)
   
   while(cap.isOpened()): 
      while True: 
          
        ret, img = cap.read() 
        cv.imshow('img', img) 
        if cv.waitKey(30) & 0xff == ord('q'): 
            break
              
        cap.release() 
        cv.destroyAllWindows() 
   else: 
      print("Alert ! Camera disconnected") 
    

# testDevice(0) # no printout
# testDevice(1)
testDevice(2)
# testDevice(3)
