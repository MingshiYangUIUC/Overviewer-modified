import os 
import random
import sys

'''to be run with server.properties in the same CWD'''

# check if level-seed exists in server.properties, e >= 0 if exists.
e = -1
f = open(os.path.join(os.getcwd(),'server.properties'),'r').readlines()
for i in range(len(f)):
    if 'level-seed=' in f[i]:
        e = i

# generate a new seed based on system time.
random.seed(int(sys.argv[1]))
seed = str(random.randint(-9223372036854775808,9223372036854775807))

# modify or write a new line to server.properties depending on existence.
ff = open(os.path.join(os.getcwd(),'server.properties'),'w')
if e == -1:
    ff.writelines(f)
    ff.write('\nlevel-seed=' + seed)
else:
    ff.writelines(f[:e])
    ff.write('level-seed=' + seed + '\n')
    ff.writelines(f[e+1:])
ff.close()

# save a txt of the seed as temporary file.
ff = open(os.path.join(os.getcwd(),'seed.txt'),'w')
ff.write(seed)
ff.close()