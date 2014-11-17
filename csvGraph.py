#!/usr/bin/python
# -*- coding: latin-1 -*-
#
# CSVGraph
#
# Written by Angel Suarez-B (n0w) & Juan L. Perez
#
import numpy as np
import matplotlib
# matplotlib.use('Agg')   <- Uncomment when running without XWindow
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sys

def banner():
  print "csvGraph - v0.2"
  print "Written by Angel Suarez-B (n0w) & Juan L. Perez\n"

def graph(inputFile, mode, outputFile):
  date, time, watts = np.loadtxt(inputFile, delimiter=',', unpack=True, 
				 converters= 
				 {
				   0: mdates.strpdate2num('%m/%d/%y'),
				   1: mdates.strpdate2num('%H:%M:%S'),
				 })
  			 

  fig = plt.figure()
  ax1 = fig.add_subplot(1,1,1, axisbg='pink')
  plt.plot_date(x=date+time, y=watts, fmt='-')
  
  plt.title('Energy consumption')
  plt.ylabel('Watts')
  plt.xlabel('Time')
  
  if mode == 1:
    print "[>] Writing output graph to %s" % outputFile
    plt.savefig(outputFile)
    print "[>] Done!"
  else:
      plt.show()

if __name__ == "__main__":
  
  banner()

  if (len(sys.argv) == 1 or len(sys.argv) > 4):
    print "\n[+] Usage: %s <CSVfile> [-p outfile.png (Export to png)]" % sys.argv[0]
    print "    Example: %s test_r.csv -p out.png\n" % sys.argv[0]
    exit(0)
  
  CSVFILE = sys.argv[1]
  OUTFILE = ''
  MODE = 0
  # Mode = 0 -> window
  # Mode = 1 -> png

  if len(sys.argv) == 4 and sys.argv[2] == '-p':
    MODE = 1 
    OUTFILE = sys.argv[3]
  
  graph(CSVFILE,MODE,OUTFILE)

  
  
				 
