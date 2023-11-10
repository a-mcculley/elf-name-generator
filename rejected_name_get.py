f = open("elfnames_full.txt", "r")
g = open("elfnames.txt", "r")
#also open any previous rejected lists

list1 = f.readlines() 
list2 = g.readlines()
#also call readlines to create a list3 (or higher) based on previous rejected lists

outlist = []
for el in list1 :
    #add "and el not in list3" for the previous rejected iterations (and increment beyond 3 as needed)
    if el not in list2:
        outlist.append(el)

#update the rejected version number
z = open("elfnames_rejectedv1.txt", "w")
for el in outlist:
    z.write(el)
