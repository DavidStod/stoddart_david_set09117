list = ['larry', 'curly', 'moe']
print list
list.append('shemp')  ##append elem at end
list.insert(0, 'xxx')  ##insert elem at index 0
list.extend(['yyy', 'xxx'])  ## all list of elems at end
print list
print list.index('curly')

list.remove('curly') ##search and remove that element
list.pop(1)  ##removes and returns 'larry'
print list
