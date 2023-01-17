import masscan

import logging
import os

mas = masscan.PortScanner()

class scanOptions():
    def mcscan():
        mas.scan('0.0.0.0/8', ports='25565', arguments='--max-rate 100000 -oX tempoutput.txt')
        #using default ports, change if u want

scanOptions.mcscan()