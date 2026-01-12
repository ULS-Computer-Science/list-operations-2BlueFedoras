import random

#The append() Method (feat. len())
append_list = [1, 2, 3]
append_list.append(input('\nWhat would you like to add to the list?\n'))
print(len(append_list))

#The insert() Method
insert_list = [1, 2, 3, 4]
insert_list.insert(1, 'replacement')
print()
print(insert_list)

#Concatenation (+) & Replication (*)
row = ['_']*3
add_on = ['X', 'O']
final_row = row + add_on
print(final_row)

#The extend() Method
backpack = ['book', 'pen']
found_items = ['apple', 'map']
print(backpack, found_items)
backpack.extend(found_items)
print(backpack)

#The remove() Method (feat. count())
count_list = [1, 2, 2, 2, 3]
print(count_list.count(2))
count_list.remove(2)
print(count_list)

#The pop() Method
VIP_guests = ['Liam', 'Harvey', 'Zlata', 'Angel', 'John Python', 'Cast-iron Pan']
kicked_out = VIP_guests.pop(0)
print(f'We removed {kicked_out} from the party, loser!')
print(VIP_guests)

#The del Statement (Slicing)
del_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del del_list[3:6]
print(del_list)

#The index() Method (feat. in)
index_list = [1, 2, 3, 4, 5]
user_search = int(input('Choose a number to search for:\n').strip().lower())
if user_search in index_list:
    print('The index is: ' + str(index_list.index(user_search)))
else:
    print('Sorry! The number is not in the list!')

#Ordering (sort and reverse)
ordering_list = []
for i in range(5):
    ordering_list.append(random.randint(0, 100))
ordering_list.sort()
print(ordering_list)
ordering_list.reverse()
print(ordering_list)

#The copy() Method
copy_list = [1, 2, 3]
backup_list = copy_list.copy()
copy_list.clear()
print(copy_list, backup_list)

#Random Selection (random.choice)
magic_8_ball = ['Yes', 'No', 'Maybe', 'Definentially not', 'It is decidedly so', 'Ask again later']
for i in range(3):
    input('Please ask the \"Magic 8\" a question.\n')
    print(random.choice(magic_8_ball))

#Nested Lists (Acesssing 2D Data)
matrix = [[1,2], [3,4]]
print(matrix[1][0])