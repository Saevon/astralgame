#file opening
file_name = raw_input("File name:\n:")
if "." not in file_name:
    file_name += ".py"
text_file = open(file_name, "r")\

text = text_file.read().split("\n")
text_file.close()

counter = 0
define = {}
while counter < len(text):
    item = text[counter]
    if item.strip()[:3] == "def":
        name = item.strip()[3:].strip()
        name = name[:name.index("(")]
        counter += 1
        code = item + "\n"
        while counter < len(text) and text[counter].strip()[:3] != "def":
            code += text[counter]
            code += "\n"
            counter += 1
        define[name] = code
    counter += 1
  
keys = []
for key in define:
    keys.append(ey)
keys.sort()
for key in keys:
    print define[key]