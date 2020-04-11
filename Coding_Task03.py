f1 = open("/Users/keweichen/Desktop/DNSC_4211/hw/hw4/script01.txt","r")
f2 = open("/Users/keweichen/Desktop/DNSC_4211/hw/hw4/script02.txt","r")
s1 = None
s2 =None
s1 = f1.read()
s2 = f2.read()
s = s1+s2
s




import string
outcome1 = ''
for word in s:
        wd = word.lower()
        if wd in string.ascii_lowercase or wd == " " or wd == "\'":
            outcome1 = outcome1 + wd
        else:
            outcome1 = outcome1 + ''
outcome1 = outcome1.split()
outcome1





outcome = {}
for word in outcome1:
        if word not in outcome:
            outcome[word] = 1
        else:
            outcome[word] += 1
outcome





with open ("partc.txt", 'a') as f:
        for k,v in outcome.items():
            f.write(str(k) + "  " +str(v) +'\n\n')




import operator
f1 = open("script01.txt","r")
f2 = open("script02.txt","r")
s1 = None
s2 =None
s1 = f1.read()
s2 = f2.read()
s = s1+s2
s





import string
outcome1 = ''
for word in s:
        wd = word.lower()
        if wd in string.ascii_lowercase or wd == " " or wd == "\'":
            outcome1 = outcome1 + wd
        else:
            outcome1 = outcome1 + ''
outcome1 = outcome1.split()
outcome1





outcome = {}
for word in outcome1:
        if word not in outcome:
            outcome[word] = 1
        else:
            outcome[word] += 1
outcome





with open ("shradha.txt", 'a') as f:
        for k,v in sorted(outcome.items(),
                          key = operator.itemgetter(1),
                          reverse = True)[:10]:
            f.write(str(k) + "\t" +str(v) +'\n\n')





import operator
f1 = open("/Users/keweichen/Desktop/DNSC_4211/hw/hw4/script01.txt","r")
f2 = open("/Users/keweichen/Desktop/DNSC_4211/hw/hw4/script02.txt","r")
s1 = None
s2 =None
s1 = f1.read()
s2 = f2.read()





import csv
with open("/Users/keweichen/Desktop/DNSC_4211/hw/hw4/stopwords.csv","r") as f:
    stop = csv.reader(f)
    stopword = list(stop)
stopword = [x[0] for x in stopword]




import string
outcome1 = ''
for word in s1:
        wd = word.lower()
        if wd in string.ascii_lowercase or wd == " " or wd == "\'":
            outcome1 = outcome1 + wd
        else:
            outcome1 = outcome1 + ''
outcome1 = outcome1.split()
outcome1





newout1 = {}
for word in outcome1:
    if len(word) >1:
        if word not in stopword:
            if word not in newout1:
                newout1[word] = 1
            else:
                newout1[word] += 1
newout1





outcome2 = ''
for word in s2:
        wd = word.lower()
        if wd in string.ascii_lowercase or wd == " " or wd == "\'":
            outcome2 = outcome2 + wd
        else:
            outcome2 = outcome2 + ''
outcome2 = outcome2.split()
outcome2





newout2 = {}
for word in outcome2:
    if word not in stopword:
        if word not in newout2:
            newout2[word] = 1
        else:
            newout2[word] += 1
newout2





top10 = {}
for k,v in sorted(newout1.items(),
                  key = operator.itemgetter(1),
                  reverse = True)[:10]:
    top10[k] = v

mydic = {}
for k in top10:
    if k in newout2:
        mydic[k] = [top10[k],newout2[k]]
    else:
        mydic[k] = [top10[k],0]
mydic





with open ("parte.txt", 'a') as f:
    f.write("word"+"\t"+"count 1"+"\t"+"count 2"+"\n\n"+"--------------------------------"+"\n\n")
    for k,v in sorted(mydic.items(),
                          key = operator.itemgetter(1),
                          reverse = True):
            f.write(str(k) + "\t" +str(v[0])+"\t"+str(v[1]) +'\n\n')
