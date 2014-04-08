#!/usr/bin/python
import sys
def getFactorial(i) :
    if i < 1 :
        return 1;
    else :
        return (i * getFactorial(i - 1));
if len(sys.argv) == 2 :
    print getFactorial(int(sys.argv[1]));
else :
    print 'Invalid arguments';
