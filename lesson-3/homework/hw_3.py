#1.Create a list containing five different fruits and print the third fruit.

fruits=['apple','apricot', 'banana','strawberry','pinapple']
fruits[2]

#2.Create two lists of numbers and concatenate them into a single list.

num_1=[1,2,3,4]
num_2=[5,6,7]
single_list=num_1+num_2
single_list

#3.Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

numbers_input=input("Enter numbers:")
numbers_given = [int(x) for x in numbers_input.split(',')]

first_num=numbers_given[0]
middle_num= numbers_given[len(numbers_given)//2]
last_num=numbers_given[-1]

extracted=[first_num,middle_num,last_num]
extracted


#4.Create a list of your five favorite movies and convert it into a tuple.

movies_list=['limitless', 'avengers', 'terminator', 'It','Godfather']
tuple_my_list=tuple(movies_list)

print(tuple_my_list)

#5.Given a list of cities, check if "Paris" is in the list and print the result.

input_cities=input("enter cities:")
cities_list=input_cities.split(',')

if 'Paris' in cities_list:
    print("Paris is in the list")
else:
    print("Paris is NOT in the list")

#6.Create a list of numbers and duplicate it without using loops.

nums=[2,4,5,3,6]
nums_duplic=nums.copy()

splitted=nums+nums_duplic
print(splitted)

#7.Given a list of numbers, swap the first and last elements.

numbers_input=input("Enter numbers:")
numbers_given = [int(x) for x in numbers_input.split(',')]

numbers_given[0], numbers_given[-1] = numbers_given[-1], numbers_given[0]

print("Swapped list:", numbers_given)

#8.Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

numbers_range=tuple(range(1,11))
sliced=numbers_range[3:8]
print(sliced)

#9.Create a list of colors and count how many times "blue" appears in the list.

list_colors=['red','blue','orange','yellow','blue']

blue_times=list_colors.count('blue')
print(blue_times)

#10.Given a tuple of animals, find the index of "lion".
input_animal=input("Enter animal with commas:")
animal_tuple= tuple(animal.strip() for animal in input_animal.split(','))
index_lion=animal_tuple.index('lion')
print("lion's index is:", index_lion


#11.Create two tuples of numbers and merge them into a single tuple.

tuple_1=(1,2,3,4,5,5)
tuple_2=(5,6,7,8,22)
tuple_splitted=tuple_1+tuple_2
tuple_splitted

#12.Given a list and a tuple, find and print their lengths.

input_nums_t=input("enter numbers with commas:")
tuple_num= tuple(num.strip() for num in input_nums_t.split(','))

input_nums_l=input("enter numbers with commas:")
list_num= list(num.strip() for num in input_nums_l.split(','))

length_tuple= len(tuple_num)
lenght_list=len(list_num)

print("Length of tuple:", length_tuple)
print("Length of list:", lenght_list)

#13.Create a tuple of five numbers and convert it into a list.

tuple_list_num=(1,2,3,4,5)
converted=list(tuple_list_num)
print(converted)

#14.Given a tuple of numbers, find and print the maximum and minimum values.
input_nums_t=input("enter numbers with commas:")
tuple_num= tuple(num.strip() for num in input_nums_t.split(','))

max_val=max(tuple_num)
min_val=min(tuple_num)

print("Max value:", max_val)
print("Min value:", min_val)

#15.Create a tuple of words and print it in reverse order.

words_tuple= ('red', 'phone', 'table', 'classwork')
reversed_order_1= tuple(reversed(words_tuple))

reversed_order_1


