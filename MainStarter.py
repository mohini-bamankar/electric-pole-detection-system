from threading import Thread
#import Electric_Pole_status
import DetectionEngine


# polethread = Thread(target = Electric_Pole_status.startElectricPoleMonitoring, args = ("start pole",))
# polethread.start()    
#19.684003496087, 74.45971623714802

latitude = "19.684003496087"
longitude = "74.45971623714802"
mobile = "8999761588"
email = "anuradhadhanwate995@gmail.com"

camerathread = Thread(target = DetectionEngine.startEngine, args = (latitude,longitude,mobile,email))
camerathread.start()    
  

