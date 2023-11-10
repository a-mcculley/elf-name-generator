f = open("elfnames_full.txt", "r")
g = open("elfnames.txt", "r")
h = open("elfnames_rejectedv1.txt", "r")
i = open("elfnames_rejectedv2.txt", "r")
j = open("elfnames_rejectedv3.txt", "r")
k = open("elfnames_rejectedv4.txt", "r")
l = open("elfnames_rejectedv5.txt", "r")
m = open("elfnames_rejectedv6.txt", "r")
n = open("elfnames_rejectedv7.txt", "r")
o = open("elfnames_rejectedv8.txt", "r")
p = open("elfnames_rejectedv9.txt", "r")

list1 = f.readlines() 
list2 = g.readlines()
list3 = h.readlines()
list4 = i.readlines()
list5 = j.readlines()
list6 = k.readlines()
list7 = l.readlines()
list8 = m.readlines()
list9 = n.readlines()
list10 = o.readlines()
list11 = p.readlines()

outlist = []
for el in list1 :
    if el not in list2 and el not in list3 and el not in list4 and el not in list5 and el not in list6 and el not in list7 and el not in list8 and el not in list9 and el not in list10 and el not in list11:
        outlist.append(el)

z = open("elfnames_rejectedv10.txt", "w")
for el in outlist:
    z.write(el)