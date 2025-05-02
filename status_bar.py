##from __future__ import print_function
##import os
##
import sys
##
##total = 10000000
##point = total / 100
##increment = total / 20
##for i in xrange(total):
##    if(i % (5 * point) == 0):
##        print("[" + "=" * (i / increment) +  " " * ((total - i)/ increment) + "]" +  str(i / point) + "%", end='\r')
####        sys.stdout.write("\r[" + "=" * (i / increment) +  " " * ((total - i)/ increment) + "]" +  str(i / point) + "%")
##        sys.stdout.flush()


##total = 10000000
##point = total / 100
##increment = total / 20
##for i in xrange(total):
##    if(i % (5 * point) == 0):
##        print "[" + "=" * (i / increment) +  " " * ((total - i)/ increment) + "]" +  str(i / point) + "%\r"
##        sys.stdout.flush()

for x in range(10):
    print '{0}\r'.format(x),
print

print 1,
print '\r2'

sys.stdout.write('1')
sys.stdout.write('\r2')

##o = 0
##hpi = 1.0
##i = 1
####print "pi calculator"
####acc= int(raw_input("enter accuracy:"))
##acc=999999
##if(acc>999999):
##        print "WARNING: this might take a VERY long time. to terminate, press CTRL+Z"
####print "precision: " + str(acc)
##while i < acc:
##        if(o==0):
##                hpi *= (1.0+i)/i
##                o = 1
##        elif(o==1):
##                hpi *= i/(1.0+i)
##                o = 0
##        else:
##                print "loop error."
##        i += 1
##        if i % 100000 == 0:
##            sys.stdout.write('\r' + str(hpi) + ' ' * 20)
##            sys.stdout.flush() # important
