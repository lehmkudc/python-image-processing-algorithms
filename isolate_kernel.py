# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 15:28:27 2018

@author: Dustin
"""
import cv2
import sfr_detection_functions as sfr
import sys


sfr_reference = cv2.imread('SFRreg_pillared_tilted_trans.png',0)
sfr.SFR_routine(sfr_reference)

sys.exit(0)

