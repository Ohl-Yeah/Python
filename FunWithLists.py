my_list = [1,2,3,4,5] #list values can used and adjust
my_tup = (1,2,3,4,5) #tup values can NOT be adjust 
print(my_list)
print(my_list[0])

my_unordered_list = ['a', 23, 'because','pizza', 500]
print(my_unordered_list)
print(my_unordered_list[3])

# Use [] to acces a specific position or Index in the list
my_list[2] = 4 #changes the value in the specific index 2 (3rd value)
print(my_list)

my_list.append(7) #adds new value to the end of the list
print(my_list)

'''
my_list. #use to see what you can do to the list
'''

#----------
for item in my_list:
    print(item)

for n in range(0, len(my_list)):
    print(my_list[n])