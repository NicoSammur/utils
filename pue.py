#!/usr/bin/env python

'''
PUE  = Total Facility Energy / IT Equipment Energy
DCiE = (Total IT Load / Total Facility Load) * 100%
'''

facilityLoad = float(raw_input("Total Facility Load: "))
itLoad = float(raw_input("Total IT Load: "))


PUE = float(facilityLoad / itLoad)
DCiE = float((itLoad / facilityLoad) * 100.00)

print ("+----------------------------------+")
print ("| PUE | DCiE | Level of Efficiency |")
print ("|-----|------|---------------------|")
print ("| 3.0 | 33%  | Ver Inefficient     |")
print ("| 2.5 | 40%  | Inefficient         |")
print ("| 2.0 | 50%  | Average             |")
print ("| 1.5 | 67%  | Efficient           |")
print ("| 1.2 | 83%  | Very Efficient      |")
print ("+----------------------------------+")

print "[*] PUE : Power Usage Effectiveness: ", round(PUE, 2)
print "[*] DCiE: Data Center Infrastructure Efficiency: ", round(DCiE, 2)
