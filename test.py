

"""my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
my_dic = {}
for i in my_list:

    if i not in my_dic:
        my_dic[i] = 1
    else:
        my_dic[i] += 1


for k, v in my_dic.items():
    print(k, v)


my_tup = 1, 2, 3, 4, 5
z, x, c, v, b = my_tup
my_tup = b, v, c, x, z


print(my_tup)
"""


x = {1, 2, 3, 4, 5}
y = {5, 6, 7, 8, 9}

x.add("banana")
y.add("banana")
print(x & y)
