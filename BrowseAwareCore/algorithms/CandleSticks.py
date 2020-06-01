import logging
from bokeh.plotting import figure

class CandleSticks:
    
    def __init__(self,candle_width):
        logging.debug("Enter __init__")
        self.candle_width = candle_width               
        pass

    def get_candle_sticks(self,switch_rate):        
        logging.info("Enter get_candle_sticks")        
        #Variable Declarations
        #Candle
        b_open = []
        b_close = []
        b_high = []
        b_low = []
        b_candle_time=[] #Contains the time intervals at which the candle values are calculated 
        
        #Calculating the candle sticks data
        a = 0
        b = a + self.candle_width        
        while (b <= len(switch_rate)):
            temp_min = switch_rate[a]
            temp_max = switch_rate[a]            
            for i in range(a,b):
                if (i == a):
                    b_open.append(switch_rate[i])
                if (i == (b-1)):
                    b_close.append(switch_rate[i])
                if (switch_rate[i] < temp_min ):
                    temp_min = switch_rate[i]
                if (switch_rate[i] > temp_max ):
                    temp_max = switch_rate[i]
            
            b_low.append (temp_min)
            b_high.append (temp_max)
            b_candle_time.append(b)
            a = b
            b = b + self.candle_width
        
        return b_candle_time,b_open,b_close,b_high,b_low
    
    def generate_candle_sticks_diagram_with_bokeh(self,time,b_open,b_close,b_high,b_low):
        logging.info("Enter generate_candle_sticks_diagram_with_bokeh")
        p = figure(title="CANDLE STICKS",plot_width=800, plot_height=500)        
        p.xaxis.axis_label = "Time (In Seconds)"
        p.yaxis.axis_label = "Switch Rate"
        logging.debug("time")
        logging.debug(time)        
        # time is a list that contains the time at which the candle ends
        # midpoint of the time is calculated for visualization purpose
        # in case of time = [30,60,90,120] the 
        # mid_point_of_time will be [15,45,75,105]
        # this mid_point_of_time array is just for visualization purpose
        mid_point_of_time = []        
        for i in range(len(time)):
            if (i==0):
                mid_point_of_time.append(int(time[i]/2))
            else:
                mid_point_of_time.append(int((time[i-1]+time[i])/2))                
        logging.debug("mid_point_of_time")
        logging.debug(mid_point_of_time)

        p.segment(mid_point_of_time,b_high,mid_point_of_time,b_low, color="black")
        p.vbar(mid_point_of_time,self.candle_width,b_open,b_close, fill_color="#D5E1DD", line_color="black")        
        return p