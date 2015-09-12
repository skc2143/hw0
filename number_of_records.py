# Reads a file and computes the number of records matching a case
# insensitive phrase

def read_file(filename):
    file = open(filename, 'r')
    count = 0
    for line in file:
        if "single malt scotch" in line.lower():
            count += 1
    print "%d records containing \"Single Malt Scotch\" were found." % count

read_file("iowa-liquor-sample.csv")
