from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file,to_file)

#How do we turn this into one line?
indata = open(from_file).read()

#This is my guess for the answer to simplyfying it. indata = from_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does this output file exist? %r " % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort"
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "All right, all done."

out_file.close()
