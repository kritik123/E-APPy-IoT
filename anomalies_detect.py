"""Code for Capstone project""" 

import email_conf, sms_conf, json, time, math, statistics 
from boltiot import Email, Bolt, Sms 

#Function to set upper and lower bound by Z-score analysis 
def compute_bounds(history_data,frame_size,factor): 
        if len(history_data)<frame_size : 
             return None 
        if len(history_data)>frame_size : 
            del history_data[0:len(history_data)-frame_size] 
        Mn=statistics.mean(history_data) 
        Variance=0 
        for data in history_data : 
              Variance += math.pow((data-Mn),2) 
        Zn = factor * math.sqrt(Variance / frame_size) 
        High_bound = history_data[frame_size-1]+Zn 
        Low_Bound = history_data[frame_size-1]-Zn 
        return [High_bound,Low_Bound]

critical_limit = 8 #the critical_value of temperature 
maximum_limit = 10 #the maximum_value of temperature 

# Configuring bolt device 
mybolt = Bolt(email_conf.API_KEY, email_conf.DEVICE_ID) 

# Configuring email alert requirement 
mailer = Email(email_conf.MAILGUN_API_KEY, email_conf.SANDBOXURL, email_conf.SENDER_EMAIL, email_conf.RECIPIENT_EMAIL) 

# Configuring sms alert requirement sms = Sms(sms_conf.SSID, sms_conf.AUTH_TOKEN, sms_conf.TO_NUMBER, sms_conf.FROM_NUMBER) 

# setting up empty list to save the temperature sensor readings 
history_data=[] 

while True: 
       
       # saves bolt module response in a variable 
        response = mybolt.analogRead('A0') 

       # saves the response data in a variable 
       data = json.loads(response) 

       if data['success'] != '1': 

               # display an error when the response in data equals to '0' 
               print("There was an error while retrieving the data.") 
               print("This is the error:"+data['value']) 
               time.sleep(10) 
               continue 

         #display the value of data while the error occurred 
         print ("The is the value"+data['value']) 

         # initialization of sensor_value to 0 
         sensor_value=0 
         try: 
            # saves current senvalue in variable 
            sensor_value = int(data['value']) 
sor except e: 
            print("There was an error while parsing the response: ",e) 
            continue  

# saving the upper and lower bounds by Z-score analysis in a variable named bound
bound = compute_bounds(history_data,email_conf.FRAME_SIZE,email_conf.MUL_FACTOR) 

# checks if bound is empty or not 
# if it is empty, then it will save the current sensor value in the history_data list otherwise, will directly go to try. 

if not bound: 
      required_data_count=email_conf.FRAME_SIZE-len(history_data) 
      print("Not enough data to compute Z-score. Need ",required_data_count," more   data points") 
      history_data.append(int(data['value'])) 
      time.sleep(10) 
     try: 

#convert the temperature to display in degree census 
     temp = sensor_value/10.24 

    # condition for when the temperature crosses the maximum_limit 
     if temp > maximum_limit: 

           print ("The Temperature value increased suddenly. Sending an sms.") 
           # display the temeprature value in degree celsus 
           print ("The Current temperature is: "+str(temp)+" °C") 
           response = sms.send_sms("Alert ! Someone has opened the fridge door") 
           print("This is the response ",response) 

   # condition for the temperature value is between the critical_limit and the maximum_limit 
   elif temp > critical_limit or temp < maximum_limit: 
         print("Urgent! Temperature condition can destroy the tablets. Sending an email.")     
         #display the temperature value in degree Celsius 
         print (" The Current temperature is:" +str(temp)+ "°C") 
         response = mailer.send_email("Alert !","The level temperature can destroy the tablets.") 
        print("This is the response",response) 
    history_data.append(sensor_value) 

# in case of any error 
except Exception as e: 
              print ("Error",e) 
time.sleep(10)
