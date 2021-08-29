# Use words.txt as the file name
fname = input("Enter file name: ")
print(open(fname,"r").read().upper().rstrip())
