import logging
from bokeh.plotting import figure
from bokeh.models import Span
import numpy as np
import math

class BollingerBands:
    
    def __init__(self,moving_average_window):
        logging.debug("Enter __init__")        
        self.moving_average_window = moving_average_window       
        pass
    
    def get_bollinger_bands_data(self,switch_rate):
        logging.info("Enter get_bollinger_bands_data")
        logging.debug("Length of Switch Rate array: ")
        logging.debug(len(switch_rate))
        #Variable Declarations        
        #bands
        time = [] #In seconds
        b_upper_band = []
        b_lower_band = []
        b_moving_average = [] #
        b_current_value = []

        start = 0
        end = 1

        #Calculating the bollinger bands data
        for i in range(len(switch_rate)):

            simple_moving_average = np.mean(np.array(switch_rate[start:end]),axis = 0)
            standard_deviation = np.std(np.array(switch_rate[start:end]),axis = 0)
            time.append(i)
            b_current_value.append(switch_rate[i])

            b_moving_average.append(simple_moving_average)
            b_upper_band.append(simple_moving_average+ (2* standard_deviation))
            b_lower_band.append(simple_moving_average-(2 * standard_deviation))

            if (i>self.moving_average_window):                
                start+=1
            end+=1
        
        return time,b_upper_band,b_lower_band,b_moving_average,b_current_value

    def get_bollinger_bands_indicator_data(self,time,b_upper_band,b_lower_band,b_moving_average,b_current_value):
        logging.info("Enter get_bollinger_bands_indicator_data")        
        percentage_b = []
        bandwidth = []

        for i in range(len(time)):                
            percentage_b_value = (b_current_value[i] - b_lower_band[i]) / (b_upper_band[i] - b_lower_band[i]) 
            # If percantage B is NaN appending 0
            percentage_b.append(0 if math.isnan(percentage_b_value) else percentage_b_value)

            bandwidth_value = (b_upper_band[i] - b_lower_band[i]) / b_moving_average[i]
            bandwidth.append(0 if math.isnan(bandwidth_value) else bandwidth_value)

        return percentage_b,bandwidth

    def generate_bollinger_bands_with_bokeh(self,time,b_upper_band,b_lower_band,b_moving_average,b_current_value):    
        logging.info("Enter generate_bollinger_bands_with_bokeh")
        p = figure(title="Bollinger Bands",plot_width=800, plot_height=500)
        p.xaxis.axis_label = "Time (In Seconds)"
        p.yaxis.axis_label = "Switch Rate"
        p.line(time, b_upper_band, line_width=2, color='#A6CEE3')
        p.line(time, b_lower_band, line_width=2, color='#B2DF8A')
        p.line(time, b_moving_average, line_width=0.5, color='grey')
        p.line(time, b_current_value, line_width=2, color='black')
        return p
    
    def generate_bollinger_bands_indicator_graph_with_bokeh(self,time,percentage_b,bandwidth):
        logging.info("Enter generate_bollinger_bands_indicator_graph_with_bokeh")
        p = figure(title="Bollinger Bands Indicators - %B and Bandwidth",plot_width=800, plot_height=500)
        p.xaxis.axis_label = "Time (In Seconds)"
        p.yaxis.axis_label = "Switch Rate"
        p.line(time, percentage_b, line_width=2, color='black')
        p.line(time, bandwidth, line_width=2, color='#B2DF8A')       
        hline = Span(location=1, line_color='red', line_width=1) 
        p.renderers.extend([hline])
        return p

        