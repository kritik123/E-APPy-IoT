#Set the chart library used to visualize the data 
setChartLibrary('google-chart'); 

#Set the title of the graph according to your choice 
setChartTitle('Polynomial Regression'); 

#Set the type of chart to be plotted 
setChartType('predictionGraph'); 

#Set the display name for each of the graph axis setAxisName('time_stamp','temp'); 

#The mul function is present to multiply a every value retrieved from the Bolt WiFi module 
mul(0.0977); 

#Display the graph on the screen for the given variables plotChart('time_stamp','temp');
