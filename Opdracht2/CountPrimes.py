import sys
import math

fh = open(sys.argv[1], 'r')
i = 0

filelist = list(fh)
k = len(filelist)
grootste = filelist[k-1]

print( 'Largest Prime = ' + str(grootste)+'\n', 'pi(N) = '+ str(k) + '\n', )
