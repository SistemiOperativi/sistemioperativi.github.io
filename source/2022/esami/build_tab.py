f = open("set.txt")

sep="+---+-------------+------+------+------+------------+--------------------+----------+"
h1= "|   |             |  **TEORIA**                     | **PROGRAMMAZIONE** |          |"
h2= "|   +             +------+------+------+------------+--------------------+          +"
h3= "|#  |**MATRICOLA**|**Q1**|**Q2**|**Q3**|**PARZIALE**|**Q4**              |**TOTALE**|"


res=[sep,h1,h2,h3,sep]
for l in res:
    print(l)
lens=[13, 6, 6, 6, 12, 20, 10]
count=1
for line in f.readlines():
    spa = 2
    if count >= 10:
        spa-=1
    if count >= 100:
        spa-=1
    line=line.strip()
    if line == "":
        continue
    if "Assente" in line:
        continue
    line = line.replace("\t", " ")
    while "  " in line:
        line = line.replace("  ", " ")
    line = line.replace("Ritirato", "Insuf.").replace("Insufficiente", "Insuf.")
    line = line.split(" ")

    res = [" "*spa+str(count)]
    i=0
    for l in line:
        if i == 7:
            i+=1
            continue
        res += [" "*(lens[i]-len(l))+l]
        i+=1
    print("|"+"|".join(res)+"|")
    count+=1
    print(sep)

    
