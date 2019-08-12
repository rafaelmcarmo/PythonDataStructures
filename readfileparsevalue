# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
x = 0
y = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    y = y + float(line.strip("X-DSPAM-Confidence: ").rstrip())
    x = x + 1
print("Average spam confidence:",y/x)
