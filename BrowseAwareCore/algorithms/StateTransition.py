import logging
from bokeh.plotting import figure
from bokeh.models import Span

class StateTransition:
    
    def __init__(self):
        logging.info("Enter __init__")       
        pass

    def get_simple_state_transitions(self,bandwidth,percentage_b):
        state_transitions = []
        state_transitions_ids = []
        current_state = "Start"
        current_state_id = 0
        temp_bandwidth = bandwidth[0]
        # 0 - Start State  1 - Volatile  2 - Not Diverted  3 - Diverted
        # What needs to be done if the bandwidth is not changing?
        for i in range(len(bandwidth)):            
            
            if (bandwidth[i]>temp_bandwidth):                
                if (percentage_b[i]>percentage_b[i-1]):
                    current_state = "Diverted"
                    current_state_id = 3
                else:
                    current_state = "Volatile"
                    current_state_id = 1

            if (bandwidth[i]<temp_bandwidth):
                if (percentage_b[i]<percentage_b[i-1]):
                    current_state = "Not Diverted"
                    current_state_id = 2
                else:
                    current_state = "Volatile"
                    current_state_id = 1
            
            temp_bandwidth = bandwidth[i]
            state_transitions.append(current_state)
            state_transitions_ids.append(current_state_id)

        return state_transitions,state_transitions_ids
    
    def generate_simple_transition_diagram_with_bokeh(self,time,state_transitions_ids,minimumTimeToNudgeInMinutes):        
        colormap = {3: 'red', 2: 'green', 1: 'blue', 0: 'black'}
        colors = [colormap[x] for x in state_transitions_ids]
        p = figure(title = "State Transitions")
        p.xaxis.axis_label = 'Time (In Seconds)'
        p.yaxis.axis_label = 'State'
        p.circle(time,state_transitions_ids,
        color=colors, fill_alpha=0.2, size=10)
        vline = Span(location=minimumTimeToNudgeInMinutes*60, dimension='height',line_dash='dashed',line_color='grey', line_width=2) 
        p.renderers.extend([vline])
        return p
    