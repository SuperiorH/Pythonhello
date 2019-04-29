str = 'h a d o o p'
print(str)
map = {}
list = str.split(" ")
print(list)
for i in list:
    if i in map.keys():
        map[i] = map[i]+1
    else:
        map[i] = 1
print(map['o'])