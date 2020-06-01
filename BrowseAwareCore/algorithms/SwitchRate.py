from datetime import datetime
import logging
from bokeh.plotting import figure

class SwitchRate:
    
    def __init__(self):
        logging.info("Enter __init__")       
        pass

    def get_date_time_object(self,year, month, day, hour, minute, second):        
        logging.info("Enter get_date_time")
        return datetime(year, month, day, hour, minute, second) 
    
    def time_difference_in_seconds(self,to_time,from_time):
        logging.info("Enter time_difference_in_seconds")
        return (to_time - from_time).total_seconds()

    def calculate_switch_rate(self,history_list,categories_to_omit):
        logging.info("Enter calculate_switch_rate")

        temp_category = ''
        temp_time = 1
        number_of_switches = 0
        initial_switch = True
        switch_rate = []
        time = [] #In Seconds
        # enumerate the list of history with the index starting from 0                
        for i in range(len(history_list)):
            #Iterating through every URL                        
            if (i > 0):
                current_url = history_list[i]
                previous_url = history_list[i-1]                

                #1. finding the amount of time spent in a URL
                try:
                    time_spent = self.time_difference_in_seconds(current_url['datetime'],previous_url['datetime'])
                except KeyError:
                    #this is to accomodate the older way to storing date and time as seperate columns
                    #In the re-writtern logic datetime will contain both date and time, rather than seperate entries                                    
                    previous_url_datetime = self.get_date_time_object(*map(int,(previous_url['date'].split('-') + previous_url['time'].split('-'))))
                    current_url_datetime = self.get_date_time_object(*map(int,(current_url['date'].split('-') + current_url['time'].split('-'))))
                    time_spent = self.time_difference_in_seconds(current_url_datetime,previous_url_datetime)

                #2. finding the number of switches b/w different URL categories
                logging.debug("current_url['category']")
                logging.debug(current_url['category'])

                if (current_url['category'] not in categories_to_omit and current_url['category'] != temp_category):
                    temp_category = current_url['category'] 
                    if (not initial_switch):                        
                        number_of_switches += 1                             
                    else:
                        # If the user if going to the first category of website then we don't increase number of switches
                        initial_switch = False                    
                
                #3. Find switch rate array of a URL
                switch_rate_array_of_URL = []                
                for i in range(temp_time, temp_time+int(time_spent)):
                    time.append(str(i))                    
                    switch_rate_array_of_URL.append(number_of_switches/i)   
                temp_time += int(time_spent)

                #4. Appending the switch rate of the URL with the session switch rate
                switch_rate += switch_rate_array_of_URL

        return time,switch_rate

    def generate_switch_rate_graph_with_bokeh(self,time,switchrate,line_color):
        logging.info("Enter generate_switch_rate_graph_with_bokeh")
        p = figure(title="SWITCH RATE OVER TIME",plot_width=800, plot_height=500)
        p.line(x= time , y= switchrate, color=line_color, line_width=2,)                
        p.xaxis.axis_label = "Time (In Seconds)"
        p.yaxis.axis_label = "Switch Rate"
        p.legend.location = "top_right"
        p.legend.click_policy="hide"        
        return p
        
        