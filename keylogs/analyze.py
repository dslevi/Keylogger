def findDuration():
    pass

def findLatency():
    pass

def convertLog(log):
    for event in log:
        if event[3] == 1:
            event[3] == "P"
        elif event[3] == 0:
            event[3] == "R"

def analyzeLog(path):
    log = []
    f = open(path, "r")
    for line in f:
        tokens = line.strip().split()
        log.append([tokens[0], tokens[1], tokens[2], tokens[3]])
    f.close()

    for x in log:
        print x[3]
