#import sys
#print('Python version')
#print(sys.version)
#print(sys.version_info)
'''
from datetime import datetime
now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))'''

from math import pi

r = float(input('Input the radius of the circle: '))

area = pi * r**2
print('The area of the circle with radius ' + str(r) + ' is: ' + str(area))