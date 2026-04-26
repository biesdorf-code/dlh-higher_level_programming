#!/usr/bin/python3
result = ""
for i in range(97, 123):
    if chr(i) != 'q' and chr(i) != 'e':
        result = result + chr(i)
print("{}".format(result), end="")
