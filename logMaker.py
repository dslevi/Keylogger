import struct, datetime, os
#built off of Trevino's codebase http://stackoverflow.com/questions/5060710/format-of-dev-input-event

def createLog(port, user, directory):
    infile_path = "/dev/input/event" + str(port)

    #long int, long int, unsigned short, unsigned short, unsigned int
    FORMAT = 'llHHI'
    EVENT_SIZE = struct.calcsize(FORMAT)

    #open file in binary mode
    in_file = open(infile_path, "rb")

    if not os.path.exists(directory):
        os.makedirs(directory)

    keylog_file = open((directory + user + 'log.txt'), 'w')
    keylog_file.write("=====================================================================\nCreated: " + 
                    str(datetime.datetime.now()) +
                    "\n=====================================================================\n\n" + 
                    "CODE | VALUE | TYPE | TIME\n")

    event = in_file.read(EVENT_SIZE)
    count = 0

    while event:
        (tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, event)

        if type != 0 or code != 0 or value != 0:
            keylog_file.write("%u, %u, %u, %d.%d\n" % \
                (code, value, type, tv_sec, tv_usec))
            count += 1

        #replace with limitation needed
        if count == 500:
            event = False
        else:
            event = in_file.read(EVENT_SIZE)

    keylog_file.close()
    in_file.close()

    print "Finished recording"
    return True