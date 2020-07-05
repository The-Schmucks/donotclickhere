import json
infile = open("example.json", 'r')
content = json.loads(infile.read())
print(content)