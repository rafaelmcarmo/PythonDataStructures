fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    palavra = line.rstrip().split()
    for element in palavra:
        if element in lst:
            continue
        else:
            lst.append(element)
lst.sort()
print(lst)
