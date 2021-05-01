# string = "This is Mississippi."
# string = "ben read a rad banana bread ad"
string = "she sells seashells by the seashore"

memlist = []

for c in string:
  if ord(c) not in memlist:
    memlist.append(ord(c))

print(len(string))
print(memlist)