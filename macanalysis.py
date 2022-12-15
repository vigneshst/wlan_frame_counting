import os
import pandas as pd

def macAnalysis(filename):
    try:
    # Extracting required data using tshark
        os.system(f'tshark -r {os.getcwd()}/{filename} -T fields -e wlan.fc.type -E header=y -E separator=, -E quote=d -E occurrence=f > {os.getcwd()}/mac.csv')
    
    # initial variables
        mgt =  "Total Managment Frames : "
        ctrl = "Total Control Frames   : "
        data = "Total Data Frames      : "
        
    # Reading csv using pandas and grouping frames
        mac = (pd.read_csv('mac.csv').groupby(['wlan.fc.type']))
        
    # extracting number of management frame using pandas groups size
        try:mgt += str(mac.groups[0].size)
        except:mgt += str(0)
        try:ctrl += str(mac.groups[1].size)
        except:ctrl += str(0)
        try:data += str(mac.groups[2].size)
        except:data += str(0)
    except:
        return ['Install tshark then try again.']
    
    # Checking uploaded file has any wlan frames or not 
    if int(mgt.split(':')[1]) > 0 or int(ctrl.split(':')[1]) > 0 or int(data.split(':')[1]) > 0:
        return [mgt,ctrl,data]
    else:
        return ['Uploaded file contains no 802.11 frames']