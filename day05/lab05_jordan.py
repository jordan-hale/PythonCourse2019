import re

# open text file of 2008 NH primary Obama speech
with open("obama-nh.txt", "r") as f:
	obama = f.readlines()

alltext = ''.join(obama)

## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]

keyword = re.compile(r"the[a-z]*")
for i, line in enumerate(obama):
  if not keyword.search(line):
  	print(i)
    print(line)

# TODO: print lines that contain a word of any length starting with s and ending with e

keyword = re.compile(r'\bs\w+e\s')
for j, line in enumerate(obama):
	if keyword.search(line):
		print(j)
		print(line)

## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = input("Please enter a date in the format MM.DD.YY: ")
finaldate = re.findall(r"\d{2}\.\d{2}\.\d{2}", date)
