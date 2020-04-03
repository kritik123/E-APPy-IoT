# Internet-of-Things-based-Temperature-Prediction-Anomaly-Detection

## Why we work on temperature?
- Temperature plays a major role in today's world, even a minute change in temperature at industries may cause explosions which leads to disasters and loss of precious life of humans. 
- To protect people from these disasters we have designed this project which alerts the people by sending emails & messages when temperature crosses threshold value or if any anomaly is detected.
- Through these messages the person can remind the workers about the temperature crossing threshold value, then there is a chance of taking preventive measures to stop disasters at various industries like pharmaceutical companies, etc...
- In pharmaceutical companies certain temperature must be maintained, if temperature exceeds then the medicine created at that time can't beour product used for medication because they may be harmful if used for medication as temperature was not consistent, leading to a great loss for the company. Our product will also be helpful to reduce these type of losses.

## Project Objective
- We want to maintain a temperature threshold between 0.35 and 0.45 degree Celsius in the chamber and hence want to get updated as soon as the temperature values get beyond the threshold so that I can take early actions.
- Another objective is to check whether the temperature for the chamber should never remain between 0.45 and 0.55 degree Celsius range for longer than 20 minutes at a time. It will be checked through the predictor graph made of polynomial regression ML algorithm predicting the next temperature ranges. We will be able to take early action, whenever the graph shows after prediction that the temperature will be maintained within 0.45 and 0.55 degree Celsius range for longer than 20 minutes.
- Our last objective is to keep a log of how many times the chamber was opened. It is found through anomaly detection system which uses Z-score analysis and sends the message that “Someone has opened the chamber” when an anomaly is detected.

## Hardware Requirement
1. Bolt Wifi Module
2. LM35 Sensor

## Software Requirement
1. Bolt Cloud
2. Bolt Android App
3. Twilio SMS API
4. Mailgun API
5. OS (Linux)

## Circuit Diagram
![Screenshot (235)](https://user-images.githubusercontent.com/40329238/78373346-1d244480-75e8-11ea-9438-b84f31c8f8f9.png)


## Conceptual Diagram
![Screenshot (234)](https://user-images.githubusercontent.com/40329238/78373278-067ded80-75e8-11ea-9850-2df016ee1854.png)




