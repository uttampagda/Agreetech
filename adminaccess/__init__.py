dict_1 = [{'id':1, 'area':2}, {'id':3, 'area':4}, {'id':1, 'area':6}]

dict_2 = []
for i in dict_1:
    if dict_2:
        for j in dict_2:
            if j['id'] == i['id']:
                j['area'] += i['area']
                # print(dict_2)
                break
            else:
                dict_2.append(i)
                break
    else:
        dict_2.append(i)

print(dict_2)