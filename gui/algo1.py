from algo8 import *from parser import *def deploy(stream, awc, filename):  a=0.0  f = open('thresholdP','r')  thresholdP =float(f.read())  f.close()  inputTraffic = parse(filename)  windowCount = inputTraffic.size/stream.windowSize  attackWindowCount =0.0  normalWindowCount= 0.0  for i in range(windowCount):    p = determineProbability(inputTraffic[i*100:(i*100)+100], stream)    if ( p < thresholdP):      a+=1      attackWindowCount +=1      if a > awc:        a=awc      print "Attack Window"    else:      a-=1      normalWindowCount += 1      if a < 0 :        a=0      print "Normal Window"    if a>=awc:      print "System under Attack"    else:      print "System is in Normal State"  stream.attackWindowCount = attackWindowCount  stream.normalWindowCount = normalWindowCount  print attackWindowCount, normalWindowCount  return stream