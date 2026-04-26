#!/usr/bin/python3
result = ""
for i in range(122, 96, -1):
    if i % 2 == 0:
        result = result + chr(i)
    else:
        result = result + chr(i - 32)
print("{}".format(result), end="")
