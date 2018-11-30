from sys import argv
import gzip

filename = argv[1]
new_filename = filename + ".xyz"
if filename.endswith(".gz"):
    inputfile = gzip.open(filename, 'rt')
else:
    inputfile = open(filename, 'r')

with open(new_filename, 'w') as outputfile:
    while inputfile.readline() != "":
        line = inputfile.readline()
        line = inputfile.readline()
        num_particles = int(inputfile.readline())
        outputfile.write("{}\ncomment\n".format(num_particles))
        line = inputfile.readline()
        line = inputfile.readline().split()
        x_len = float(line[1])-float(line[0])
        for i in range(3):
            line = inputfile.readline()
        for i in range(num_particles):
            line = inputfile.readline()
            line = line.split()
            x = float(line[2]) * x_len
            y = float(line[3]) * x_len
            z = float(line[4]) * x_len
            outputfile.write("A\t{}\t{}\t{}\n".format(x, y, z))

inputfile.close()
