# Reads GH1 Sequence, counts how many of each nucleotides there are.
# Calculates the GC content
# Written by: Hoikin Cheng

from optparse import OptionParser
from optparse import OptionGroup

def main():

    parser = OptionParser()

    parser.add_option('-f','--filename', type = "string",
    help = 'The name of the file; must be in same folder.')

    (options, args) = parser.parse_args()
    
    nt_counter = {"A" : 0, "T" : 0, "C" : 0, "G" : 0}
    total_nt = 0

    with open(options.filename, "r") as sequence:
        for line in sequence:
            if line.startswith(">"):
                print("Sequence title:")
                print(line.replace(">", ""))
            else:
                for each_nt in line:
                    if (each_nt == "A"):
                        nt_counter["A"] += 1
                        total_nt += 1
                    elif (each_nt == "T"):
                        nt_counter["T"] += 1
                        total_nt += 1
                    elif (each_nt == "C"):
                        nt_counter["C"] += 1
                        total_nt += 1
                    elif (each_nt == "G"):
                        nt_counter["G"] += 1
                        total_nt += 1
                    else:
                        continue

    print("Total number of A: %i" %nt_counter["A"])
    print("Total number of T: %i" %nt_counter["T"])
    print("Total number of C: %i" %nt_counter["C"])
    print("Total number of G: %i" %nt_counter["G"])

    print("\n")

    print("Total nt: %i" %total_nt)

    print("\n")

    print("CG content (percentage): %f"\
    %( (nt_counter["C"] + nt_counter["G"]) * 100 / float (total_nt) ) )


if __name__ == "__main__":
    main()
