#Computer usage monitor

import PySimpleGUI as sg
#import psutil
import platform
from datetime import datetime

# Create some Elements
cpu_btn = sg.Button('View CPU Statistics')
mem_btn = sg.Button('View Memory Statistics')
dsk_btn = sg.Button('View Disk Statistics')
net_btn = sg.Button('View Network Statistics')
gpu_btn = sg.Button('View GPU Statistics')
cancel_btn = sg.Button('Cancel')
layout = [[cpu_btn, mem_btn, dsk_btn, net_btn, gpu_btn, cancel_btn]]

# Create the first Window
window = sg.Window('Menu', layout)
win2_active = False

#Create the event loop
while True:
    event1, values1 = window.read(timeout=100)
    if event1 in (None, 'Cancel'):
        # User closed the Window or hit the Cancel button
        break
    if not win2_active and event1 == 'View CPU Statistics':
        win2_active = True
        layout2 = [[sg.Text('Window 2')],
                   [sg.Button('Exit')]]
        window2 = sg.Window('Window 2', layout2)
    if win2_active:
        events2, values2 = window2.Read(timeout=100)
        if events2 is None or events2 == 'Exit':
            win2_active  = False
            window2.close()
window.close()