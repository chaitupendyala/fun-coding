import sys
file = open("keylogger.txt","w")
file.write(sys.stdin)
file.close()
