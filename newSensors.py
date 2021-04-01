import random
import pytz
import time
import pigpio

class Patient():
  pi1 = pigpio.pi()
  setpointtemp = 32.0
  tempreading = 32.0
  alarmOn = False
  tempSensor   = None

  def __init__(self):
    tempSensor = 0
    # 23 is shutdown
    self.pi1.set_mode(23, pigpio.OUTPUT)
    self.pi1.write(23,False)
    
    # speaker PWM
    self.pi1.set_PWM_dutycycle(24,200)
    self.pi1.set_PWM_frequency(24,5000)
  def setpoint(self):
      return self.setpointtemp
      
  def temperature(self):
      
      val1 = False
      val2 = False
      x = 0
      y = 0
      for i in range(1000000, 1000000, 1000):
          self.pi1.hardware_PWM(18, 1000, 1)
          time.sleep(0.03)
          x = self.pi1.read(6)
          y = self.pi1.read(26)
          if(x == 1):
              self.tempreading = x
              val1 = True
          if(y == 1):
              self.setpointemp = y
              val2 = True
          if(val2 and val1):
              break
        
              
      self.setpointtemp = 35.0
      self.tempreading = 37.0
      

      return self.tempreading

  def temp_warning(self):
    temp = self.tempreading
    
    print(str(temp) + str(self.alarmOn))
        

    if temp > 39 or temp < 20:
        self.alarmOn = True
        self.pi1.set_PWM_frequency(24,5000)
        return True
    else:
    
        self.alarmOn = False
        self.pi1.set_PWM_frequency(24,0000)
        return False
    
class MachineStatus():
  patient = None
  ambient = None
  Apnea   = None
  textToDisplay = ""

  def __init__(self, pSensors, aSensors):
    self.patient = pSensors
    #self.ambient = aSensors
    #self.Apnea   = ApneaPad()

  def AC_power_state(self):
    connected = True
    if connected:
      return ''
    else:
      return ''
    
    

  def alarm_state(self):
    alarms = True # Button to mute alarms
    
    if alarms:
      a = ''
    else:
      a = ''
    return '{}'.format(a)
    
  def check_alarms(self):
      
    temp_warning = self.patient.temp_warning()
                 
    '''
    rh_warning = (self.ambient.rh < 40) | (self.ambient.rh > 77)
    apnea_warning = self.Apnea.check_apnea()
    textToDisplay = "Apnea level warning"
    hr_warning = (self.patient.hr < 120) | (self.patient.hr > 160)
    o2_warning = (self.patient.o2 < 95) | (self.patient.o2 > 100)

    warnings = [
                  temp_warning,   # T
                  rh_warning,     # RH
                  apnea_warning,  # A
                  hr_warning,     # HR
                  o2_warning      # O2
                  
               ]
    if (temp_warning) :
        self.textToDisplay = "Check tempearture"
    elif (hr_warning):
        self.textToDisplay = "Check heart rate"
    elif (o2_warning):
        self.textToDisplay = "Check oxygen saturation"
    elif(apnea_warning):
        self.textToDisplay = "Check apnea levels"
    
        
    
    '''
         
    warnings = [ temp_warning]
    colors = [ self.get_color(w) for w in warnings]
    return colors

  def get_color(self, alarm):
    if alarm:
        
      return 'red'
    else:
      return 'dark slate grey'
