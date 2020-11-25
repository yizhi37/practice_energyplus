# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:29:46 2020

@author: YingliLou
"""

import subprocess
        
eplus_path ='energyplus8'
weather_file ='weather.epw'   
eplus_file = 'SmallOffice.idf'

subprocess.call([eplus_path, '-w', weather_file, eplus_file])