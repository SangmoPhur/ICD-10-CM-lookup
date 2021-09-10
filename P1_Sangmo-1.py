import re
infile = open("icd10cm.txt", "r")
#lines = infile.readlines()
#infile.close()
code = input("Please enter the ICD-10 code or diagnosis: ")
# print(description)
for line in infile.readlines():
    if re.search(code, line):
        elements = line.strip().split("\t")
        print(elements[0], elements[1])