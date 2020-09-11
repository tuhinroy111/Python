import sys

sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')
print(sys.argv)# prints the arguments in command line
#taking input from command line and operating
if len(sys.argv) > 1:
    print(float(sys.argv[1])+5)
