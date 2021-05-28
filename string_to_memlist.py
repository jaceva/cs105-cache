# string = "This is Mississippi."
# string = "ben read a rad banana bread ad"
string = "Mission in Mississippi"

memlist = []
loclist = []

for c in string:
  if c not in memlist:
    memlist.append(c)

  loclist.append(memlist.index(c))
  

print(len(string))
print(len(memlist), memlist)
print(len(loclist), loclist)