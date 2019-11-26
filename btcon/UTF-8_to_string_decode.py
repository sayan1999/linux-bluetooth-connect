import sys
with open(sys.argv[1], 'r') as content_file:
    content = content_file.read()
print(content.encode("UTF-8").decode("ascii","ignore"))
