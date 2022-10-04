import numpy
import sys

f = open(sys.argv[1])

d = {}

for line in f.readlines():
    if "|" in line:
        line = line.strip().replace(" ", "").replace("30cumlaude", "31")
        if "Matricola" in line:
            continue
        if "MATRICOLA" in line:
            continue
        if "TEORIA" in line:
            continue
        if "-+-" in line:
            continue
        line = line.split("|")
        line = [line[2], line[-2]]
        if line[0] not in d:
            d[line[0]] = []
        d[line[0]] = [line[1]] + d[line[0]]
        #print(line)


passed = {}
scores = []

for k in d:
    #print(k,d[k])
    if "N.D" not in d[k][-1] and "Ins" not in d[k][-1]:
        if len(d[k]) not in passed:
            passed[len(d[k])] = 0
        passed[len(d[k])]+=1
        scores += [int(d[k][-1])]

    if "N.D" in d[k][-1]:
        if "N.D" not in passed:
            passed["N.D"] = 0
        passed["N.D"] +=1
        




#print(len(d))
#print(passed)

tot_passed = 0
for k in range(5)[1:]:
    print(f"""Promossi in {k}:\t{passed[k]}\t{"{:.2f}".format(passed[k]*100/len(d))}%""")
    tot_passed += passed[k]

tot_passed += passed["N.D"]

print(  f"""Bocciati A.A.:\t{len(d)-tot_passed}\t{"{:.2f}".format( (len(d)-tot_passed)*100/len(d))}%""")
print(  f"""N.D.         :\t{passed["N.D"]}\t{"{:.2f}".format(passed["N.D"]*100/len(d))}%""")

histo = {}

for k in range(32)[18:]:
    histo[k] = 0

for k in scores:
    histo[k] += 1

#print(scores)
print("AVG score:  ", numpy.average(scores))
print("AVG median: ",numpy.median(scores))
print(histo)
