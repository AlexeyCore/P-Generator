from time import sleep


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()

# make a list
items = list(range(0, 60))
i = 0
l = len(items)

# Initial call to print 0% progress
printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 30)
for item in items:
    # Do stuff...
    sleep(0.1)
    # Update Progress Bar
    i += 1
    printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 30)