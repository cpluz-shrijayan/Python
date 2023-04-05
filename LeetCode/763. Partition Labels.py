s = "ababcbacadefegdehijhklij"
last_index={}
for i,j in enumerate(s): 
    last_index[j] = i

end, size = 0, 0
return_list = []

for i,j in enumerate(s):  
    size += 1
    end = max(end,last_index[j])
    if i == end:
        return_list.append(size)
        size = 0