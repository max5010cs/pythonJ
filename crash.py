# print("Hello World!")
# message = "wassup in python world"
# print(message)


##########################################################################
# MESSAGE HERE IS A VARIABLE
# VARIABLES CAN BE USED TO STORE INFORMATION
# AND REFERENCE IT LATER IN YOUR CODE
# EVERY VARIABLE IS CONNECTED TO A VALUE
# THE VALUE CAN BE A STRING, A NUMBER, A LIST, ETC.
# IN THIS CASE, THE VALUE IS A STRING
# STRINGS ARE SEQUENCES OF CHARACTERS
# STRINGS ARE WRAPPED IN QUOTATION MARKS
# YOU CAN USE SINGLE OR DOUBLE QUOTES





# message = 'Welcome to hell'
# print(message)

# message = 'Go do your homework'
# print(message)


#########################################
#WHEN I USE VAIRABLES I NEED TO KEEP THESE THINGS IN MIND. SOME OF THEM ARE CURIAL AND BREAKING THEM WILL CAUSE ERRIRS AND SOME OTHERS HELP ME TO WRITE THAT IS EASY TO READ AND DEBUG CODE.
# 1. VARIABLE NAMES CAN ONLY CONTAIN LETTERS,NUMBERS AND UNDERSCORES. THEY CAN BE STARTED WITH A LETTER OR UNDERSCORE BUT NOT A NUMBER.EXAMPLE: message_1 (correct), 1_message(wrong).
# 2. SPACEES ARE NOT ALLOWED IN VARIABLES AND UNDERSCORES CAN BE USED INSTEAD. EXAMPLE: greeting_messag(correct), greeting message(error)
# 3. I SHOULD AVOID USING WORDS RESERVED FOR PROGRAMMATIC PURPOSES.
# 4. I SHOULD MAKE SURE VARIABLE NAMES I USE HAVE MEANING THAT IS DESCRIPTIVE OF WHAT I WANT
# 5. I SHOULD BE CAREFUL WHEN USING LETTERS THAT CAN BE CONFUSED WITH NUMBERS. EXAMPLE: l >> 1, O >> 0



# message = "Hello python crash course reader!"
# # print(mesage)

# print(message)


# name = input('What is your name? ')
# print(name.title())


# nickname = input("How do your friends call you? ")
# print(nickname.title())
# print(nickname.lower())
# print(nickname.upper())

# name = input ("what is your name? ") 
# # print("Hello", name.upper())

# # print("Wassup", name.lower())

# data = input('What did you like about the tour you had? ')
# print(data.lower())



# 


# f_name = input("What's your name? ")
# l_name = input("What is your last name? ")
# full_name = f'{f_name.title()} {l_name.title()}'

# print(f'If his first name is {f_name} and last time is {l_name} and then his full name would be {full_name}!')



# 


# n1 = 4
# n2 = 6
# order = '1, 2, 3, {}, 5, {}'.format(n1,n1)
# print(order)


# p1 = 'apple'
# p2 = 'banana'
# p3 = 'dumbass'
# list = 'smht, also, word, {}, another, {},{}'.fomat(p1,p2,p3)
# print(list)

# n1 =  'car'
# n2 = 'bugatti'

# print('{} is a very nice {}'.format(n2,n1))


# n1 = 'supra'
# n2 = 'loud'
# print('{} is a very {}'.f'Supra,loud')
# THIS IS WRONG

# message = "Python is an automation language!"
# print(f'{message.upper()}. Yes you are absolutely right!')

# print(f'{message.title()}. \t\t\t\t\t Yes you are absolutely rihgt>>')


# print(f'{message.lower()}\n\n\n\n Yes you are absolutly right! ')

# print(f'{message.title()}!! \n Yep you are right!!')
# print(f'\t{message.lower()}\n\tYes you are right bro!')

#STRIPPING WHITE SPACES



# bool_str = "True"
# bool_val = bool(bool_str)
# print(bool_val)

# num_int = 0
# bool_val = bool(num_int)
# print(bool_val)

# Python, bool (short for Boolean) is a fundamental data type that can only have one of two possible values: True or False.
# Think of it as a simple on/off switch, a yes/no answer, or a statement being correct or incorrect.

# Python, bool (short for Boolean) is a fundamental data type that can only have one of two possible values: True or False.
# Think of it as a simple on/off switch, a yes/no answer, or a statement being correct or incorrect.

# num_int = 0
# print(bool(num_int))

# space = (" ")
# print(bool(space))



# num_float = 3.14
# num_int = float(num_float)
# print(num_int)

# n1 = 6.454
# print(bool(n1))



# message = "My name is {} and i am a fucking {}".format("Max", "idiot") 
# print(message)

# name = input("wtf is your name? ")
# print("I dont reall care {}!".format(name.title()

# name = input("Who are yooou?")
# # print("Mr {} can you step outside so we can {}, we got a {}".format(name.swapcase(), reason="talk".upper(), r1="warrant warrant warrant".capitalize()))

# # The main string must use {reason} and {r1} placeholders
# print("Mr {} can you step outside so we can {reason}, we got a {r1}.".format(
#     name.swapcase(),          # 1. Positional argument
#     reason="talk".upper(),    # 2. Keyword argument
#     r1="warrant...".capitalize() # 3. Correct Keyword argument syntax
# ))
# name = input("What is your name? ")
# car = input("What was your first car? ")
# the_date = input(f"When did you buy your fist car, {car}? ")
# data = f"His name is {name} and his first car was {car} which he bought in {the_date}" 

# print(data)



# name = input("What is your name? ")
# the_int = input("Do you like riding a bike? ")
# the_bike = input("What was your first bike {}? ".format(name.upper()))
# date = input("When did you buy your first bike, {}? "
#              .format(the_bike.capitalize()))
# data = 'His name is {}, and he has is interested in riding a bike and he bought his first bike {} in {}.'
# result = data.format(
#     name.swapcase(),
#     the_bike.title(),
#     date
# )
# # init = the_bike.format(
# #     name.uppper()
# # )
# print(result)



# the_college_name = input("What is the name of your college? ")
# date_found = input("When was {} founded? "
# .format(
#     the_college_name.title()
# ))
# first_year_st_number = input("How many student have you had in {}? "
#                              .format(
#                                  date_found
#                              ))
# ceo = input("Who was the CEO of the college {}? "
#             .format(
#                 the_college_name.title()
#             ))
# data = "{} was founded in {} and it had over {} in the first year and CEO was {}.".format(the_college_name.title(), int(date_found), int(first_year_st_number), ceo.title())
# print(data)


# n1 = 1
# n2 = 2
# adding = f"{n1 + n2}"
# print(adding)


# n1 = 23
# n2 = 34
# substraction = f"{n1-n2}"
# print(substraction)



# message = "wassup {0} it is me {1}".format("homie", "Dane")
# print(message)


# message_rev = "wassup {1} it is me {1}"
# res_m = message_rev.format("homie","jane")
# print(res_m)


# message = "Pull up your gun and choot me please."
# lower_c = message.islower()
# print(lower_c) wtf i ddnt know that i thought it is gonna do the same as .lower().

# findings = "I ddnt find nothing from this research and i am still going to look for smht but i know i wont find shit".isupper()
# print(findings)


# summary = "i don't even know what i had yesterday for dinner, so please dont fucking ask".islower()
# print(summary)

# number = bool(90)
# print(number)

# message = input("What is your take from this lesson dumbass -- ")
# ans = message.islower()   # it should return yes or no, not some kind of lowercasing sh*t!
# # print(ans)

# quest = input("What is your birthyear and day? ")
# message = quest.upper().lower()
# print(message)



# message = input("wtf is your name mate? ")
# result = message#.strip()

# print(result)



# message  = "hi mr can i have your phone and i donno why i even need it"
# print(message)

# user_data = "he                    is 29 years old with two kids             ".strip()

# print(user_data)




# mr_tab = "\t\t\thi\tim\ta\tmir\ttab\tand\ti\tdo\tusually\tput\tsome\tbig\tass\tspaces\tbetween\tjust\tlike\tthis "
# print(mr_tab.strip())

# mt_n_line = "hi im mr n line im not \nnigga line \ni am next line"
# print(mt_n_line)

# message = "Python is so boring ass lang".strip("g")
# print(message)

# message = "not gonna do frontend even if u shoot me".strip("n e")
# print(message)


# inn = "\n"
# res = bool(inn)
# print (inn)
# print(res)


# fav_game = "\tmy favourite game is gta V"
# res = fav_game.lstrip()
# print(res)


# my_list = [1,2,3,4,5]
# print(my_list)


# my_list = [1,2,3,"   ",4,5]
# print(my_list)

# my_list = [1,2,3,4,5]
# print(my_list[0])

# my_list = [1,2,3,4,5]
# print(my_list[-1])


# my_list = [1,2,3,4,5]
# index = my_list.index(2)
# print(index)

# my_list = [1,2,3,4,5]
# print(my_list[2])


# my_list = [1,2,3,4,5]
# print(my_list.index(4))

# my_list = [1,2,3,4,5]
# print(my_list[2])

# my_list = [[1,2],[3,4],[5,6]]
# # print(my_list[-1][0])

# my_list = [1,2,3,4,5]
# print(my_list[-3])

# my_list = [1,2,3,4,5]
# index = 2
# print(my_list[index+1])

# my_list = [1,2,3,4,5]
# index_q = input("What index do you want? Please choose 4... ")
# print(my_list[int(index_q)-3])

# my_list = ["hi","hello"]
# print(my_list[0].index("i"))

# my_list = ["Hi","Hello","Wassup"]
# print(my_list[-1][-1][0][0][-1][0][-1])

# # my_list = [1,2,3,4]
# # print(my_list[1][-1])


# my_list = ["mr","donut"]
# index = 2
# print(my_list[1][index+1])

# my_list = ["don't","do"]
# element_at_index_1 = my_list[1]
# print(element_at_index_1)

# my_list = ["wassup","buddy"]
# element = my_list[0][0]
# print(element)

# my_list = ["mr","hello"]
# print(my_list[0].index("r"))


# my_list = [["Herlo","dumbass"]]
# element = my_list[0][0][3]
# print(element)


# my_list = [1,2,3,4]
# print(my_list)
# my_list.append(int("5"))
# print(my_list)


# my_list = ["do your homeword kiddo","go to the gyp fatass"]
# my_list.append("do the laundry")
# print(my_list)
# quest = input("choose 3 please: ")
# if int(quest) == 3:
#     print(my_list[-1])
# else:
#     print("")




# my_list = [1,2]
# my_list.append([])
# # print(my_list)

# my_list = [1,2,3]
# print(my_list)
# another_list = [4,5,6]
# my_list.append(another_list)
# print(my_list)



# list1 = [1,2,3,4]
# list2 = [5,6,7,7]
# res = list1 + list2
# print(res)

# my_list = [1,2,3]
# the_number = "4"
# result = my_list + list(the_number)
# print(result)

# my_list = [1,2,3]
# print(my_list)
# my_list.insert(0,0)


# my_list = [1,2,3]
# my_list.append(my_list)
# print(my_list)


# my_list = [1,2,3]
# print(my_list)
# my_list.insert(1,4)
# print(my_list)

# my_list = [1,2,3,4]
# my_list.append((5,6))
# print(my_list)

# my_list = [1,2,3]
# print(my_list)
# my_list.insert(0,6)
# print(my_list)

# my_list = [1,2,[3,4]]
# my_list.insert(-1,5)
# print(my_list)

# my_list = [1,2,[3,4]]
# my_list.insert(3,5)
# print(my_list)

# my_list = [1,2,[3,4]]
# my_list.insert(2,5)
# print(my_list)

# my_list = [1,2,3]
# my_list.insert(-1,4)
# print(my_list)

# my_list = [1,2,3]
# my_list.insert(len(my_list),4)
# print(my_list)

# my_list = [1,2,3,4]
# index = 3
# element = "wtf"
# my_list.insert(0,element)
# print(my_list)

# my_list = [1,2,3,4]
# my_list.remove(1)
# print(my_list)

# my_list = [1,2,[5,6],3,4,"hello"]
# my_list[2].remove(5)
# print(my_list)

# my_list = [[1,2],[3,4],[5,6]]
# my_list[0].remove(1)
# print(my_list)

# my_list = [1,2,3,4]
# del my_list[1]
# print(my_list)

# my_list = [1,2,4,34]
# del my_list[-1]
# print(my_list)

# my_list = [1,2,3,4,3]
# del my_list
# print(my_list)

# my_list = [1,2,33,4]
# print(my_list)
# pop_element = my_list.pop()
# print(pop_element)

# my_list = [1,2,3,4]
# print(my_list.pop(0))


# my_list = [1,2,3]
# print(my_list) 
# print(my_list.pop(0))
# print(my_list)

# my_list = [[1,2],[3,4],[5,6]]
# print(my_list)
# my_list.pop(0)
# print(my_list.pop(0))
# print(my_list)

# my_list.pop(0)
# print(my_list)

# my_list = [1,3,4,5,]
# my_list.clear()
# print(my_list)

# my_list = [1,2,34,5,5,6,4,"wasup","dummy"]
# my_list.clear()
# print(my_list)

# my_list = ["wassup","mr","donut"]
# my_list.clear()
# print(my_list)
# my_list.clear()
# print(my_list)

# my_list = [1,2,3]
# my_list *=0
# print(my_list)

# # n1 = 2
# n1 = 3
# print(n1)


# list = [1,2,3]
# list *=3
# print(list)

# list = [1,2,3]
# list *=2
# print(list)


# my_tuple = ([1,2],[3,4])
# print(my_tuple)

# my_tuple = ([1,2],[3,4])
# print(my_tuple)
# print(my_tuple[0][0])
# print(my_tuple[0][1])
# print(my_tuple[1][0])
# print(my_tuple[1][1])
# print(my_tuple[0][0], my_tuple[0][1], my_tuple[1][0], my_tuple[1][1])


# my_tuple = ([1,2],[3,4])
# my_tuple[0].append(5)
# print(my_tuple*2)


# my_tuple = ([1,2],[3,4])
# my_tuple[1].insert(len(my_tuple),[5,6])
# print(my_tuple)

# my_tuple[1].pop(-1)
# print(my_tuple)

# print(my_tuple[0].pop(0))

# underscore = 14_000_000_000
# print(underscore)

# x,y,x = 1,2,3
# print(x)

# MAX_CONNECTIONS = 5000
# print(MAX_CONNECTIONS)

# import this

# list_of_b = ['trek','cannondale','redline','specialized']
# print(list_of_b)

# # bicycles = ['trek','cannondale','redline']
# # print(bicycles[1])
# bicycles = ['rek','cannondale','redline']
# print(bicycles[2].upper())



# bicycles = ['trek','cannondale','redline']
# print(bicycles[0][1])

# bicycles = ['redline','trek']
# print(f'my first childhood bike was {bicycles[0].title()} model')

# motor_bikes = ['honda', 'suzuki','kawasaki','yamaha']
# print(motor_bikes)

# motor_bikes[0] = 'yamahaaaaa'
# print(motor_bikes)

# motorbikes = ['yamaha','suzuki','kawasaki']
# print(motorbikes)

# motorbikes[0] = 't'
# print(motorbikes)
 
# motor_bikes = ['ducati','suzuki']
# print(motor_bikes)

# motor_bikes.append("kawasaki")
# print(motor_bikes)

# motorcycles = []
# print(motorcycles)
# motorcycles.append('ducati')
# motorcycles.append('kawasaki')
# motorcycles.append('Honda')
# motorcycles.append('yamaha')
# print(motorcycles)

# motor_bikes = ['ducati','yamaha']
# print(motor_bikes)
# # motor_bikes.insert(-1,'kawasaki')  this doesnt work if i wanna add smht to th end
# print(motor_bikes)
# motor_bikes.insert(len(motor_bikes),'kawasaki')
# print(motor_bikes)

# motorcycles  = ['yamaha','ducati','kawasaki']
# print(motorcycles)
# # del motorcycles[-1]
# # print(motorcycles)
# del motorcycles[1]
# print(motorcycles)

# motorcycles = ['ducati','kawasaski','yamaha']
# print(motorcycles)
# popping = motorcycles.pop()
# print(motorcycles)
# print(popping)

# motors = ['v6','v8','v10']
# print(motors)
# delete = motors.pop(0)
# print(motors)
# print(delete)

# motors = ['v6','v8','v10']
# print(motors)
# fav = motors[0].upper()
# print(motors)
# print(f'My favourite motor engine is {fav.upper()}')

# motorcycles = ['honda','kawasaki s1000rr','yamaha']
# print(motorcycles)
# popping = motorcycles.pop(1)
# print(f'The last motorcycles i owned was {popping.title()}')

# motorcycles = ['ducati','kawasaski','yamaha']
# print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)

# bikes = ['ducati', 'redline', 'kawasaki','redline']
# print(bikes)
# bikes.remove('redline')
# print(bikes)

# bikes = ['redline','ducati','kawasaki']
# print(bikes)
# the_best = 'kawasaki'
# rem = bikes.remove(the_best)
# print(bikes)
# print(f'{the_best.capitalize()} is the best anyway')


# cars = ['bmw','toyota','tuautare','lambo']
# print(cars)
# cars.sort()
# print(cars)

# cars = ['bugatatta','feriririri','bmw']
# print(cars)
# cars.sort(reverse=True)
# # print(cars)
# cars = ['toyota','maxcyy','bugatti']
# print(cars)
# cars.sort()
# print(cars)

# types = ['toyota','ferrari','koenigsegg']
# print(types)
# types.sort(reverse=True)
# # print(types)
# cars = ['bugatti','bmw','toyota']
# print(cars)
# cars.sort(reverse=False)
# print(cars)


# cars = ['a','d','c','b']
# print('Here is the original list: ')
# print(cars)

# print('\nHere is the sorted list: ')
# print(sorted(cars))

# print(f'Here is the original list again: {cars}')


# cars = ['a','e','b','c']
# print(f' Here is the original list: {cars}')
# sorted_cars =sorted(cars)
# print(f'Here is the sorted list: {sorted_cars}')
# print(f'Org list again: {cars}')

# print(f'org list : {cars}')

# cars = ["a",'d','f']
# print(cars)
# sorted_type = sorted(cars,reverse=False)

# cars = ['bugatti','audi','bmw','subaru']
# print(cars)
# cars.reverse()
# print(cars)

# cars = ['a','b','c','d']
# length = len(cars)
# print(f'we got {length} items in the list')

# locations = ['tashkent','bukxara','namangan','andijan']
# print(locations)
# using_sorted = sorted(locations)
# # using_sort = locations.sort()
# print(using_sorted)
# print(locations)
# using_sorted_for_reverse_alphabetic_order = sorted(locations,reverse=True)
# print(using_sorted_for_reverse_alphabetic_order)
# print(locations)

# print(locations)
# locations.reverse()
# print(locations)
# locations.reverse()
# print(locations)

# locations.sort()
# print(locations)

# locations.sort(reverse=True)
# print(locations)

# people_invited = ['max','jacob','elon musk','hanna']
# n = len(people_invited)
# print(f'I have invited {n} people for my birthday party')

# list = [1,2,3,4,5]
# print(list.index(2))

# list = [1,2,45,6,]
# print(list[-1])

# here comes the loops



# magicians = ['alice','alex','jacob','max']
# for magician in magicians:
#     print(magician)

# cars_list = ['bmw','tuatara','tesla','RR']
# cars_sorted = sorted(cars_list)
# print('Fav cars: ')
# for cars in cars_sorted:
#     print(cars)

# list = [1,2,34,'mrbumba']
# print(list[-2])

# list = [1,2,3]
# app = list.append([])
# print(list)


#print(app)

# list1 = [1,23,4]
# print(list1)
# list2 = [5,6,7]
# print(list2)
# app = list1.append(list2)
# print(list1)  # we should get none


# list_1 = [1,2,3]
# list_2 = [4,5,6]
# app = list_1 + list_2
# print(list_1)
# print(list_2)
# print(f'added together: {app}')


# list_ = [1,2,3]
# my_string = 'hello'
# adding = list_ + list(my_string)
# print(adding)



# # my_list = [1, 2, 3]
# # my_string = '456'
# # result = my_list + my_string
# # print(result)



# my_list = [1, 2, 3]
# my_string = '456'
# result = my_list + list(my_string)
# print(result)


# # DEL TAKES AN INDEX
# list = [1,23,444,4,7]
# del list[0]
# print(list)

# list = [1,2,4]
# del list
# print(list)


# my_list = [1, 2, 3]
# del my_list
# print(my_list)

# my_list = [1,2,3]
# popping = my_list.pop(0)
# print(my_list)
# print(popping)
# my_list = [1, 2, 3]
# my_list.clear()
# print(my_list)


# my_list = [1,2,3]
# my_list.clear()
# print(my_list)

# my_list = [1, 2, 3]
# my_list *= 4
# print(my_list)

# my_tuple = ([1,2],[3,4])
# print(my_tuple[0][0])
# my_tuple = [[1, 2], [3, 4]]
# my_tuple[0].append(5)
# print(my_tuple)  

# my_tuple = ([1, 2], [3, 4])
# my_tuple[0].insert(1, [5, 6])
# print(my_tuple) 

# t = (1, 2, 3)
# lst = list(t)
# print(lst)
# lst.append(4)
# t = tuple(lst)
# print(lst)
# my_tuple = ([1, 2], [3, 4])
# my_tuple[0].append([5,6])
# print(my_tuple)  


# number = " "
# print(bool(number))

# empty_list = [ ]
# print(bool(empty_list))

#   IF THE THERE IS SPACE INSTEAD OF A STRING FOR A VARIABLE THEN IT IS TRUE BUT IF IT IS LIST THEN SPACE DOES NOT MATTER, STILL FALSE

# true_as_a_string = "True"
# print(bool(true_as_a_string))

# true_string = True
# # print(true_string)
# b = ""
# a = b

# print(bool(a))

# false_string = "False"
# print(bool(false_string))


# false_as_string = not False
# print(bool(false_as_string))

# result = not (5>3)
# print(bool(result))

# fruits = ["apple","banana","orange"]
# is_there_smht = bool(fruits)
# print(is_there_smht)

# value = None 
# print(bool(value))

# value = "Yes"
# print(bool(value))

# # Equal to: ==
# 5 == 5
# "apple" == "orange"

# # Not equal to : !=
# 3 != 4
# "cat" != "cat"

# Greater than : >
# 10 > 5
# 7 > 9

# Greate than or equal to : >=
# 7>=7 # True
# 12 >= 15 # False

# print(5 == "5")
# print(True!=1)

# print(4>3==3)

# x = 10 
# y = 7
# x > y
# x != 10 

# "apple" == "apple"  # true
# "cat" > "dog" # false


# (1, "apple") == (1, "apple") # true


# greater_than = 5 > 3
# less_than = 2<1
# equal_to = 10==10
# not_equal_to = 1!=1

# and_op = (4 > 2) and (6 < 8)
# print(and_op)
# equal = (3==3) or (2!=2)
# print(equal)
# not_ = not(5>10)
# print(not_)

# n1 = (5 > 3) and (10 < 7)
# print(n1)

# n2  = (3 != 4) or (6 <= 9)
# print(n2)

# x = 5

# if x > 0:
#     print("x is positive".title())
# else:
#     ""

# x = -3 
# if x > 0:
#     print("x is positive".capitalalize())

# else:
#     print("X is not positive")

# x = 0
# if x > 0:
#     print("X is positive")
# elif x < 0:
#     print("x is negative")
# else:
#     print("X is zero".upper())

# x = 10
# if x > 0:
#     if x % 2 == 0:
#         print("x is a positive even number")
#     else:
#         print("x is a positive odd number")

# x = 10
# y = 5

# if x > 0 and y > 0:
#     print("x and y are both positive")

# x = 5
# y = -5

# print(x > 0 or y > 0)
#     # print("At least one of x and y is positive")

# x = 5

# if not x < 0:
#     print("x is not negative")


# x = 6 * 7
# print(x)

# # WORKING WITH LIST

# magicians = ['alice','daivd','carolina']
# for magician in magicians:
#     print(magician)


# magicians = ['alice','brat','david']
# for magician in magicians:
#     print(f'{magician.title()}, that was a very great trick!')

# magicians = [['alice'],'brat','joanathan']
# for magician in magicians[0]:
#     print(f'{magician.title()}, that a very great trick!')
#     print(f'I can not wait for your next performance, {magician.title()}')

# names = ['alice','brat','david']
# for magician in names:
#     print(f'{magician.title()}, that was a great performance')
# print(f"\nI can't wait for your next performance guys")

# print("\nThank you all")

# names = ['dounut','alice','david']
# for magician in names:
# #  print(magician)
# names = ['alice','david','caroline']
# for magician in names :
#     print(f'Hello, {magician.title()}')
# print(f'Thanks,{magician.title()}')


# message = 'Hello David'
#    print(message)    # Error: Unexepected indent

# my_string  = "Hello world"

# for character in my_string:
#     print(character)

# my_list = [1,2,3,4,5]

# max_value = my_list[0]
# for number in my_list:
#     if number > max_value:
#         max_value = number
# print(max_value)  # my guess is 5

# my_list = [5,3,2,1,4]

# max_value = my_list[0]

# for number in my_list:
#     if number > max_value:
#         max_value = number
#         print(max_value)  #my guess is 


# my_list = [5,3,1,4,2]

# sorted_list = []

# for number in sorted(my_list):
#     sorted_list.append(number)
# print(sorted_list)  # my guess is, in this case i just prints the sorted list 1,2,3,4,5 but if use print inside for then it si gonna print every step 

# my_list = [5,2,3,4,1]
# sorted_list = []

# for number in sorted(my_list):
#     sorted_list.append(number)
#     print(sorted_list)


# my_list = [1,2,3,4,1,5,3]
# unique_list  = []

# for number in my_list:
#     if number not in unique_list:
#         unique_list.append(number)
#         print(unique_list)  # my guess is: in this case 1,2,3,4,5, if print is insdie loop then triangle, if print is inside if then still triangle.
# # mistake, if the print is inside the for loop then it will print every step even if smht is not appended it will print the last situation.

# my_list = [1,2,3,4,4,4,4,4,4,5]
# unique_list = []

# for number in my_list:
#     if number not in unique_list:
#         unique_list.append(number)
#     print(unique_list)

# my_list = [1,2,3,4,5]
# filtered_list = []

# for number in my_list:
#     if number > 3:
#         filtered_list.append(number)

# print(filtered_list)  # my guess is: it should print last result of 4,5 but if i use print inside the for loop and then im gonna get triangle but starting with 3 empty lists and then 4 and then 4,5. but if i use the print inside the if then im gonna get triange lvl2

# my_list = [1,2,3,4,5]
# filtered_list= []

# for number in my_list:
#     if number > 3:
#         filtered_list.append(number)
#     print(filtered_list)


# my_list = [1,2,3,4,5]
# filtered_list = []

# for number in my_list:
#     if number > 3:
#         filtered_list.append(number)
#         print(filtered_list)
          

# students = [("John", 90), ("Mike", 80), ("Sarah", 95)]

# print("Names\t\t\tScores\n")
# for name,grade in students:
#     # print(f'Names\t\t\tScores\n\n{name,grade}')
#     print(f'{name}\t\t\t{grade}')
# # this was clean, love it




# for num in range(0,10,2):
#     print(num)

# fruits = ["apple","banana",'cherry']
# for fruit in fruits:
#     # print(fruit) 

#     if fruit == "banana":
#         # print(fruit)
#         break
        
#     print(fruit)
      # my guess is banana



# fruits = ['apple','banana','cherry']
# for i in range(len(fruits)):
#     print(i,fruits[i])  # my guess: it is gonna be 0 - fruit name and 1 - fruit name ...

# fruits = ['apple','banana','cherry']
# for fruit in fruits:
#     if fruit =="banana":
#         break
#     print(fruit)


# matrix = [[1,2],[3,4]]
# for row in matrix:
#     for num in row:
#         print(num)                   # my guess:  we gota have two columns and first one with 1 and 2 and second one is 3 and 4 or rowss like 1,3 and 2,4


# matrix = [[1, 2], [3, 4]]
# for row in matrix:
#     print(row)
# # i was wrong and i understoof that it coz the code is aactually trying to enter isnde the list


# #   for num in row:
# #     print(num)



# numbers = [1,2,3]
# squares = []
# for num in numbers:
#     square = num ** 2
#     squares.append(square)
# print(squares)


# my_list = [1,2,3,4,5]
# total = 0
# for number in my_list:
#     total += number
#     print(total)


# total = 0
# for number in range(1,101):
#     total+= number


# average = 0
# for number in range(1,101):
#     average += number

# average /=100

# print(average)  # my guess is 50.5 and i was right


# my_list = [1,2,3,4,5]

# max_value = my_list[0]   #  1 | 1 | 3 | 4 | %
# for index in range(1, len(my_list)):  # this gives 1,2,3,4
#     if my_list[index] > max_value:     # 1 > 1 |  3 > 1 |  4 > 3 | 5 > 4
#         max_value = my_list[index]    # 3 | 4 | 5
# # so my guess: as print is required to print the last max_value then it must be 5
# print(max_value)


# my_list = [1,2,3,1,4,5,3]

# unique_list = []
# for index in range (len(my_list)):   # 7 >>>>>>>>> 0,1,2,3,4,5,6

#     if my_list[index] not in unique_list:
#         unique_list.append(my_list[index])
# # my guess 1,2,3,4,5
# print(unique_list)



# LEFT AT EX 17


# my_list = [1,2,3,4,5]
# for i in range(len(my_list)-1,-1,-1):
#     print(my_list[i])

# x = 21-1,-1,-1
# print(x)

# my_list2 = [1,2,3,4,5]
# for i in range(len(my_list2)-1,-1,-1):  # 4,-1,-1  >>> 4,3,2,1,0  
#     print(my_list2[i])


# # my guess is 5,4,3,2,1


# nested_list = [[1,2],[3,4],[5,6]]
# for i in range(len(nested_list)):    # 0,1,2
#     for j in range(len(nested_list[i])): # 0,1  | 0,1  | 0,1
#         print(nested_list[i][j])
# my guess:
# 1
# 2
# 3
# 4
# 5
# 6

# my_list = [i**2 for i in range(5)]
# print(my_list)
# # my_guess:
# # 0
# # 2
# # 4
# # 9
# # 16


# my_list = []

# for i in range(5):
#     my_list.append(i**2)
# print(my_list)
# my_list = [1,2,3,4,5]
# for number in my_list:
#     if number > 3:
#         break
# print(number)
# # my guess is 3
# # i was wrong coz the last number entered the function and the broke the fucntion will be considered


# nested_list = [[1,2],[3,4],[5,6]]
# for i in range(len(nested_list)): # 0,1,3
#     for j in range(len(nested_list[i])):
#         print(nested_list[i][j])

# # # my_guess: 
# 1
# 2
# 3
# 4
# 5
# 6



# my_list1 = [1,2,3]
# my_list2 = [4,5,6]

# for number1 in my_list1:
#     for number2 in my_list2:
#         if number1 + number2 > 10:
#             break
# print(number1)
# # my guess: 3


# my_list = ["John","Jane","Peter","Mary"]

# for name in my_list:
#     if name == "Mary":
#         break
    
# print(name)
# # my_guess : Mary


# my_list = [[1,2,3],[4,5,6],[7,8,9]]

# for sublist in my_list:
#     for item in sublist:
#         if item == 5:
#             break
# print(item)
#         # my guess is 4
        

# my_list = [[1,2,3],[4,5,6],[7,8,9]]

# for sublist in my_list:
#     for item in sublist:
#         if item == 5:
#             break
#         print(item)


# my_another_list = [[1,2,3],[4,5,6],[7,8,9]]

# for item in my_another_list:
#     for number in item:
#         if number == 5:
#             break
#         print(number)
# # my guess:
# # 1
# # 2
# # 3
# # 4
# # 7
# # 8
# # 9


# magicians = ['alice','david','caroline']
# for magician in magicians:
#  print(magician)


# magicians = ['alice','david','caroline']
# for magician in magicians:
#     print(f'{magician.title()}, that was a greak trick!\n')
# print(f"I can't wait to see your next trick, {magician.title()}.")

# magicians = ['alice','david','caroline']
# for magician in magicians:
#     print(f'{magician.capitalize()}, that was a great tick!')
#     print(f"I can't wait to see your next trick, {magician.title()}\n")

# message = "Hello world"
# print(message)

# magicians = ['alice','caroline','david']
# for magician in magicians:
#     print(f'{magician.title()}, that was a great trick!')
#     print(f"i can't wait to see your next trick, {magician.capitalize()}")

# print('\nThank you all for your performance!')


# magicians = ['alice','david','caroline']
# for magician in magicians:
# #  print(magician)


# for value in range(1,5):
#     print(value)


# for value in range(1,6):
#     print(value)

# for value in range(6):
#     print(value)

# numbers = list(range(7))
# for values in numbers:
#     print(values)

# print(numbers)

# number_ag = range(0,19,2)
# number_tg = list(number_ag)

# print("\n")

# print(number_ag)
# print(number_tg)

# print('\n')

# for numbers in number_ag:
#     print(numbers)

# print('\n')

# for numbers in number_tg:
#     print(numbers)

# i need to list even numbers up to 10

# even_numbers = list(range(0,11,2))
# print(even_numbers)

# for numbers in even_numbers:
#     print(numbers)

# for numbers in range(1,11,1):
#     print(int(numbers)**2)

# squares = []
# for value in range(1,11,1):
#     square = int(value)**2
#     squares.append(square)
#     print(squares)


# squares = []

# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)

# print(squares)

# left at statistics with lists

# digits = [1,2,3,4,5,6,7,8,9,0]
# print(min(digits))
# # for mins in digits:
# #     print(min(mins))

# digits =[1,2,3,5]
# print(max(digits))

# digits = [1,2,34,45]
# print(max(digits))

# squares = [value**2 for value in range(1,11)]
# print(squares)


# squares = []

# for values in range(1,11):
#     squared = values**2
#     squares.append(squared)

# print(squares)


# squares = [ value**2 for value in range(1,11)]
# print(squares)

# squares = [value for value in range(1,11)]
# print(squares)

# squares  = [numbers/2 for numbers in range(11)]
# print(squares)

# players = ['charles','martina','michael','florence','eli']
# print(players[0:3])

# players = ['charles','michael','martina','bugatii','eli']

# print(players[0:2])


# cars = ['bugatti','mclaren','gm','minus','xiaomi']
# print(cars[1:4])

# players = [1,2,3,4,56,7,8]
# print(players[:4])

# players = ['martin','emi','ronaldo','messi']
# print(players[1:])

# players = ['martin','emi','messi','ronaldo']
# print(players[-2:])

# players = ['messi','ronaldo','mbappe','azizbek']

# print('Here are the first three players in my team: \n')
# for player in players[0:3]:
#     print(player.title())

# list_of_nums = [1,2,3,4,5,6,7,8,9]

# print("Here are my three favourite numbers: ")
# for nums in list_of_nums[0:3]:
#     print(nums)

# my_foods = ['pizza','falafel','carrot cake']
# friend_foods = my_foods[:]

# print(f'Here is the list of my favourite foods:\n{my_foods}\n')
# print(f"Here is the list of my friend's favourite foods:\n{friend_foods}")

# my_food = ['pizza','falafel','chocolate']
# friend_food = my_food[:]

# another = input("What is your favourite food my friend: ")
# friend_food.append(another)

# print(f'\nmy food: {my_food}')
# print(f'friend_food: {friend_food}')

# print('\nYep they are different lists as u can see!')

# list1 = [1,2,34]
# list2 = list1[:]

# list1.append(56)
# list2.append(78)

# print(list1,"\n",list2)

# dimensions = (200,50)
# print(dimensions[0])
# print(dimensions[1])

# dimensions = (200,500)
# dimensions[0] = 300
# print(dimensions)  # error is produced coz i can not alter a tuple

# my_t = (3)
# define = my_t[0]
# print(define)   # this produces error coz 3 by itself cant but a tuple uless we use comma

# my_t = (3,)
# define = my_t[0]
# # print(define)

# dimensions = (500,200)
# for dimension in dimensions:
#     print(dimension)

# a = 'this is first value'
# print(a)
# a = 'this is second'
# print(a)

# dimensions = (500,200)
# print("Original dimensions: \n")
# for dimension in dimensions:
#     print(dimension)

# dimensions = (1,2)
# print("\nNew dimensions: \n")
# for dimension in dimensions:
#     print(dimension)


# dimensions = (1,2)
# print(f'Org dimensions: \n{dimensions}')

# dimensions = (3,4)
# print(f'\nnew dimensions:\n{dimensions} ')

# +++++++++++++ code styling PEP 8

# left at if stats


# cars = ["audi",'toyota','malibu','bmw','bugatti','mercedes']

# for car in cars:
#     if car == 'bugatti':
#         print(car.upper())

#     else:
#         print(car.title())

# car = 'bmw'
# car == 'bmw'
# print(car)

# car == "audi"

# car = "audi"
# # print(car == "audi")

# car = 1
# print(car==2)

# car = "Audi"
# print(car.lower()=='audi')

# requested_topping = "mushrooms" 

# if requested_topping != "anchovies":
#     print("Hold the anchovies")


# age = 18
# if age != 18:
#     print("He is not 18")

# else:
#     print("he is 18")

# answer = 17

# if answer !=22:
#     print("that answer is not the correct one and correct answer is 22")

# answer = 4

# if answer >= 4:
#     print("thats is the correct answer")

# else:
#     print("wrong answer")


# answer = 1

# if answer > 19:
#     print("that is not correct answer")

# else:
#     print("answer should equal to or greater than 19")


# age = input("Please enter your age: ")
# print(age)

# age2 = input("please enter your frined's age: ")
# print(age2)

# if int(age) > 21 and int(age2) > 21:
#     print("You aare good to proceed!")

# else:
#     print("You must be over 21 sir")
# age1 = input("how old are you? ")
#age2 = input("how old are you? ")

#if int(age1) > 21 and int(age2) > 21:
 #   print("You are welcome, you can come in!")

#else:
#          print("You gotta be over 21, sorry!")

#age_0 = 22
#age_1 = 18
#if age_0 > 21 or age_2 > 21:
#    print("True")

#else:
#    print("False")

#banned_users = ['andrew', 'caroline', 'david']
#user = 'marie'

#if user not in banned_users:
#    print(f"{user.capitalize()}, you can post a response if you wish!")

#else:
#    print(f'You are banned')

'''

age = input("how old are you?")
if int(age) >= 18:
    print("You are old enough to vote")

else:
    print("You need to be 18 or over")


age = input("How old are you? :")

if int(age) >= 18:
    print("You are old enough to vote!")
    yn = input("Have you registered yet? y/n :")

    if yn == "y" or yn == "n":
        if yn == "y":
            print("All right then, good luck")
        else:
            print("You would want to register on the next table")

    else:
        print("Only y/n")

else:
    print("You gotta be at least 18")




age = input("How old are you? : ")

if int(age) < 4:
    print("Your admission cost is free")
elif int(age) < 18:
    print("Your admssions cost is 25")
else:
print("Yours is 40")

age = 19

if age < 4:
    price = "free"

elif age < 18:
    price = 25

else:
    price = 40

print(f'Your admissoin fee is {price}')




age = 98
if age < 4:
    price = "free"
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission fee is {price}")

game_active = True
can_edit = False
print(game_active,can_edit)

car = "subaru"
print("is car == 'subaru'? I predict True")
print(car == 'subaru')


car = "bugatti"
print(car == 'bugatti')

model = 'Tuatara'
print(model.lower() == 'Tuatara' )

'''
'''
requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'papperoni' in requested_toppings:
    print('Adding papperoni')
if 'extra cheese' in requested_toppings:
    print('Adding extracheese')
'''

'''

requested = ['mushrooms', 'extra cheese']
for item in requested:
    if item in requested:
        print(f"Adding {item}")
print('Your pizza is ready')   # this seemed lil bit off but still made things easier than it was in previous piece
'''

'''
alien_color = "green"

if alien_color == 'green':
    print('You just earned 5 points')

alien_color = 'red'

if alien_color == 'green':
    print('You just earned 5 points')
else:
    print('You lost the game, gfo.')

   '''
"""

alien1 = 'red'
alien2 = 'green'
alien3 = 'yellow'

if alien1 == 'red':
    print('You just earned 15 points')
elif alien1 == 'green':
    print('You just earned 5 points')
else:
    print('You just earned 10 points')

if alien2 == 'red':
    print('You just earned 15 points')
elif alien2 == 'green':
    print('You just earned 5 points')
else:
    print('You just earned 10 points')

if alien3 == 'red':
    print('You just earned 15 points')
elif alien3 == 'green':
    print('You just earned 5 points')
else:
    print('You just earned 10 points')



age = input("How old are you? ")

if int(age) < 4:
    print("Your admission ticked is free!")
elif int(age) > 4 and int(age) < 18 :
    print("Your admission ticked costs you $25")
else:
    print("Your admissions ticket is $40")

age = input ("What is your age? ")

if int(age) < 4:
    price = "free"
elif  int(age) < 18:
    price = '$25'
else:
    price = '$40'
print(f"Your admission ticket is {price}")
"""
'''
age = input("What is your age? ")

if not age:
    age = input('Age was not defined\n Exiting...')
elif int(age) < 4:
    price = 0
elif int(age) < 18:
    price = 25
elif int(age) > 65:
    price = 20
elif int(age) <= 65:
    price = 40
else:
    price = 0
print(f'Your admission cost is ${price}')

i dont care at least i did what i wanted



req_toppings = ['mushroom', 'apple', 'extra cheese']
for i in req_toppings:
    if i in req_toppings:
        print(f'Adding {i}...')
print("Your pizza is ready")


requested_toppings = ['mushroom', ' green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f'Adding {requested_topping}')
print('\n Your pizza is ready')




requested_toppings= ['mushroom','green peppers', 'extra cheese']
for i in requested_toppings:
    if i == 'mushroom':
        print(f"Sorry, there is no {i} left")
    else:
        print(f'\nAdding {i}...')
print('\n Your pizza is ready')


#1. so firstly i need to ask the client for what they want
#2. then i need to add them to the list
#3. if the reseponse is null
#4. I will finish requesting for items
#5. then i will check the list if it empy i will ask if they want a plain pizza
#6. if not i will add each thing one by one
#7. finish

requested_toppings = []
topping = input('Welcome sir, what do you want in your pizza? ')
if topping:
    requested_toppings.append(topping)
    print(topping)
elif requested_toppings and not topping:
    print('Accepted your requested topping...')
elif not requested_toppings:
    confirm = input('Do u really want a plain pizza? y/n')
    if confirm == 'y':
        print('Got you')
    else:
        print(topping)
# i tried tho

toppings = []
while True:
    topping = input ("What is the frkn topping you want? ")
    if topping:
        toppings.append(topping)
    else:
        break
if toppings:
    print("Got you")
    for i in toppings:
        print(f"Adding {i} to your pizza...")
    print("Here is your pizza with requested toppings!")
else:
    print("Plain it is!")
    print('Here is your requested plain pizzza!')

 # got it , it is working now
 
            
    


requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Addding {requsted_topping} to your pizza')
    print('You pizza is ready')
else:
    plain = input("So plain one then? ")
    if plain:
        print("BRUH")
    else:
        print('alright')

        #  weird but book is always right

available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for topping in requested_toppings:
    if topping in available_toppings:
        print(f'Adding {topping}...')
    else:
        print(f'{topping} is not available currently')
print('\n Your pizza is ready')




# PEP 8 
# spacing in if statements
if age < 4 # Try to use single space
if age<4  # nope


# DICTIONARY    example_dictionary = {'color' : 'Green'}

alien_0 = {'name' : 'max', 'car'  : 'bmw', 'color' : 'black', 'engine' : 'v6'}

print(alien_0['name'])
print(alien_0['car'])
print(alien_0['engine'])
print(alien_0['name'], '\n', alien_0['car'], '\n', alien_0['engine'])


alien_0 = {'alien_color' : 'green', 'points' : 5}
new_points = alien_0 ['points']
print(f'You just earned {new_points} points')



alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)



dict_0 = {'car' : 'bw'}
print(dict_0)

dict_0['engine'] = 'v8'
print(dict_0)




alien_0 = {}
print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'color' : 'green'}
print(f"{alien_0['color'].title()} is the current color of the alien")

alien_0['color'] = 'yellow'
print(f"{alien_0['color'].title()} is the new color")



# lets try to move the alien from its x position
alien_1 = {'x_position' : 25, 'y_position' : 0, 'speed' : 'medium'}
print(f"Current position is {alien_1['x_position']}")

if alien_1['speed'] == 'slow':
    x_move = 1
elif alien_1['speed'] == 'medium':
    x_move = 2
else:
    x_move = 3

# now i need to apply the new position by adding the x_move to old position(x_position)
alien_1['x_position'] = alien_1['x_position'] + x_move
print(f"New position for the alien is {alien_1['x_position']} after change of {x_move} by x vector")



alien_1 = {'color' : 'green', 'points' : 5}
print(alien_1)

del alien_1['points']
print(alien_1)

favourite_lang = {
        'jen' : 'python',
        'sarah' : 'c',
        'max': 'rust',
        'phil' : 'ruby'

        }
print(favourite_lang)


name = input('What is your name? ')
fav_lang = input (f'What is your favourite language {name}? ')

dictionary = {}
dic0tionary[name] = fav_lang
print(f"{name.title()}'s favourite langauge is {dictionary[name].title()}")




alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['color']
print(alien_0)


favourite_languages = {
        'jen':'python',
        'johanna':'ruby',
        'edward':'ruby',
        'phil':'rust'
        }

name = input('Whose fav language do you wanna know? ')

if name in favourite_languages:
    fav_language = favourite_languages[name].title()
    print(f"{name.title()}'s favourite language is {fav_language}")
else:
    print("Name is required")




alien_0 = {
        'color':'green',
        'speed':'slow'
        }
print(alien_0['points'])



alien_0 = {
        'color':'green',
        'speed':'slow'
        }
print_value = alien_0.get('points','wtf this does not exist bro')
print(print_value)






friend_name = {
        'name':'max',
        'age':'19',
        'fav_language':'rust',
        'hobby':'chess',
        }

print(friend_name['name'])
print(friend_name['age'])
print(friend_name['hobby'])
print(friend_name['fav_language'])



#jane = input('What is your favourite language Jane? ')
#jack = input('What is your favourite language Jack? ')
#johanna = input('What is your favoutite language Johanna? ')
#saidakbar = input('What is your favourite language Saidakabar? )


list = ['jane','jack','johanna','saidakbar','johnson','fiona']
dictionary = {
        }
for name in list :
    fav_lang = input(f'What is your favourite language {name.title()} ? ')
    if fav_lang:
        dictionary[name] = fav_lang
    else:
        print('Lang is required.')
quest = input('Now whose favourite language do you wanna know? ')
if quest in dictionary:
    print(f"{quest.title()}'s favourite language is {dictionary[quest]}")
else:
    print("Aight")



dictionary = {
        'get()':'We use get when we are not sure smth is in the dictionary',
        'dictionary[]':' We use this to print the valueof the key we need',
        'dictionary[]=""': ' we use this when we wanna add new value or change value of the key'

        }
for names in dictionary:
    print(names, ' >>> ', dictionary[names])



user_0 = {
        'username' : 'Fiona',
        'first' : 'flowey',
        'last' : 'fermi'
        }
#for a,b in user_0.items():
 #   print(f'\nKey: {a}')
  #  print(f'Value: {b}')
for k,v in user_0.items():
    print(f"{k}  >>  {v}")    


favourite_languages = {
        'said':'python',
        'jacob':'rust',
        'jenny':'ruby'
        }

for name, language in favourite_languages.items():
    print(f"\n{name.title()}'s favourite language is {language.title()}")


fav_languages = {
        'jane':'python',
        'john':'rsut',
        'smith':'ruby',
        'ops':'javascript'
        }

message = ('People who took the poll::')
print(message)
for name in fav_languages.keys():
    print(name.title())



fav_languages = {
        'jane':'python',
        'jack':'rust',
        'smith':'java'
        }
for names in fav_languages.keys():
    name = names
    lang = fav_languages[name]
    print(f"{name.title()}'s favourite language is {lang.title()}")


the_poll = {
        'pal':''
        }
#print(the_poll[pal])

if 'pal' not in the_poll.keys():
    print('Pal, you better take the poll')
if not the_poll['pal']:
    print('Pal, you better take it bruh')



favourite_languages = {
        'jane':'python',
        'jake':'rust',
        'saida':'vue',
        'john':'java'}
for name in sorted(favourite_languages):
    print(f"{name.title()}, Thank you for taking the poll")


favourite_languages = {
        'jane':'rust',
        'johanna':'ruby',
        'oper':'java',
        'rustam':'python'
        }

print('Here are the values:')
for values in favourite_languages.values():
    print(values)



# when trying to print values, there could be some repeated ones, to print only unique ones we can use set()

langs = {
        'jane':'rust',
        'islam':'python',
        'rustam':'python',
        'said':'ruby',
        'akbar':'ruby'
        }
print("let's print unique ones using set()")
for values in set(langs.values()):
    print(values)

alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow','points':3}
alien_2 = {'color':'red', 'points':1}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)



# Make an empty list 
aliens = []

# append multiple aliens using range()
for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)



# print 5 of em
for alien in aliens[:5]:
    print(alien)
print('...')

print(f'Aliens in the list are {len(aliens)} ')



# create an empty list
aliens = []

# use range to create multiple aliens
for aliens_number in range(10):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

# use for loop and if to change the values of first 3 aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    else:
        print('error')

 # print first 5 of the aliens
for alien_ in aliens[:5]:
    print(alien_)


# create an empty list 
aliens = []

# add 10 aliens usinng range and loop
for number in range(10):
    new_alien = {'color':'green', 'speed':'slow', 'points':5}
    aliens.append(new_alien)

    # loop thought each alien upto third one and then change their value using if/elif
for update in aliens[:3]:
    if update['color'] == 'green':
        update['color'] = 'yellow'
        update['speed'] = 'medium'
        update['points'] = 10
    elif update['color'] == 'yellow':
        update['color'] = 'red'
        update['speed'] = 'fast'
        update['points'] = 15
for alien in aliens[:5]:
    print(alien)


# store pizza info here in a dictionary
pizza = {
        'crust':'thick',
        'toppings': ['mushrooms', 'extra-cheese']
        }
# summarize the order
print(f"Did you order a {pizza['crust']} - crust pizza, with toppings:")
for topping in pizza['toppings']:
    print(topping)

# ask for confirmation
conf = input("Confirm!...y/n ")
if conf == 'y':
    print('Alright it is ready you can take it')
else:
    print('error')


fav_languages = {
        'john':['python', 'ruby'],
        'sara':['java'],
        'said':['javscript', 'typescript'],
        'akbar':['C', 'C#', 'C++']
        }
for name, languages in fav_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print("\t" + language)




# DICTIONARY IN A DICTIONARY

users = {
        'aenstein': {
            'first':'alebert',
            'last':'aenstein',
            'location':'princeton'
            },
        'mcurie': {
            'first':'marie',
            'last': 'curie',
            'location':'paris'
            }
        }



for username, user_info in users.items():
    username = username 
    first = user_info['first']
    last = user_info['last']
    location = user_info['location']

    print(f"\nUsername: {username}\n\t Full Name: {first} {last}\n\t Location: {location}")





message = input('What is your name ? ' )
print(f'Welcome, {message.title()}.')



prompt = 'If you tell us who you are, we can personalize the messages for you!'
prompt += '\nWhat is your name? '

name = input(prompt)
print(f'Thanks, {name}')

intro = 'Please enter your name so we can adjust messages for you'
print(intro)
name_asking_prompt = input ('What is your name? ')
print(f'Thanks, {name_asking_prompt}')


age = input('How old are you? ')
print(age)
# when trying print the quotes will NOT be a problem
#but when trying to use it in some other op then quotes can be a problem for example:
#    if age > 18:     # this will return an error coz the number enetered by the user is saved as a string with quotes ''


age = input ('How old are you? ' )
if age > 18 :
    print('You are an adult')   # WRONG

age = int(input ('How old are you? '))
if int(age) > 18 :  # this is second option
    print('You are an adult')   # Correct


name = input('What is your name? ')
height = input ('How tall are you, in inches? ')

if int(height) > 48:
    print(f"You are tall enought to ride, {name.title()} ")
else:
    print('You can ride when you little bit older!')


################# (%) --- Modulo Operator

number = int(input("Enter a number and i will find you if it is ODD or EVEN_  "))
if number % 2:
    print('It is Odd')
else:
    print('It is Even')

conf = input('Am i right?_y/n ')
if conf == 'y':
    print('I knew it')
else:
    print('My bad')


# While loops

current_number = 1
for a in range(100):
    current_number+=1
    print(current_number)


current_number = 1
while current_number < 100:
    current_number+= 1
    print(current_number)




current_number = 1
while current_number <=5:
    print(current_number)
    current_number+= 1
  #  print(current_number)


prompt = 'Enter whatever you want and i will repeat it for you. '
prompt+= "Enter 'q' to stop me "

message = ""
while message != 'q':
    message = input(prompt)
    print(message)

print("Eneter whatever you want and i will repeat it for you\nEnter 'q' to stop me" )
enter = input('$~')

m = ""
while m != 'q':
    m = enter
    print(m)




while True:

    msg = input ("Say whatever or q to quit: ")
    if msg != 'q':
         print(msg)
    else:
        break

    

#  Using a Flag

active = True
while active:

    msg = input("Hey say antyhing i will repeat or say q to quit: ")
    if msg != 'q':
        print(msg)
    else:
        active = 0


sentence = "Hello, how are you"
words = sentence.split()
print(words)



string = "apple,banana,orange"
fruits = string.split(",")
print(fruits)



string = "one,two,three,four,five"
parts = string.split(",", 2)
print(parts)

multiple_string = "Line 1\n Line2\n Line3"
lines = multiple_string.split("\n")
print(lines)



cars = "bugatti, bmw, audi, tesla"
msg = cars.split(",", -2)
print(msg)  # it does not do anything just split(",") happens


string = "Hello"
characters = list(string)
print(characters)  # i need to remember this coz i thought it would put the Hello into list



sentence = "           Hello, How are you                  "
msg = sentence.strip().split()
print(msg)


sentence = "Hello How Are You"
msg = sentence.lower().split()
print(msg)

string = "Hello how are you"
msg = string.split(" ", maxsplit = 0) # maxsplit = 0 == 
print(msg)


words = ["Hello", "World"]
sentence = "".join(words)
print(sentence)

words = ["Hello", "World"]
sentence = " ".join(words)
print(sentence)

numbers = [1,2,4]
string = ", ".join(str(number) for number in numbers)
print(string)


words = ['apple', 'banana', 'orange']
string = ", ".join(words)
print(string)

words2 = words
string2 = "-".join(words2)
print(string2)


words = ['Hello', 'World']
string1 = "".join(words)
string2 = " ".join(words)
string3 = ", ".join(words)
string4 = "\n".join(words)

print(string1)
print(string2)
print(string3)
print(string4)


numbers = [1,2,4,4,5,6]
print(numbers)
sublist = numbers[1:4]
print(sublist)

numbers = [1,2,34,56]
sublist = numbers[:3]
print(sublist)


numbers = [1,2,3,4,5,6,7,8,9]
print(numbers[::3])


string = "Hello, world"
sub = string[7:]
print(sub)

string = "Hello, world"
section = string[4:9]
print(section)


sentence = "Hello World"
section = sentence[::-1]
print(section)


word = "Python"
sub = word[-4:]
print(sub)


numbers = [1,2,3,4,5]
mid = numbers[1:-1]
print(mid)

sentence = "Hello world"
sections = sentence[:2] + sentence[2:5]
print(sections)

numbers = [1,2,3,4,5,6]
sections = numbers[:3] + numbers[-2:]
print(sections)

word = "Python"
s = slice(0,3)
print(word[s])

s2 = slice(-1)
print(word[s2])

word = "Python"
s = slice(-2)
print(s)   # so basically the slie is some variable that can be reused and takes at least 1 value and upto 3 


word = "Python"
s = slice(-3,-6,-1)
print(word[s])

word = "Python"
s = slice(0,None,2)  # start at index 0 and to the end by jumping by 2, so skip one character each time
print(word[s])


word = "Python"
s= slice(None,None, -1)  # reversing 
print(word[s])

# tasks
# 1. Split a sentence into words
sentence = "Wassup how are you doing these days"
splits = sentence.split(" ")
print(splits)

# 2. Split a string line into individual values
string = "apple,banana,orange"
splits = string.split(",")
print(splits)
for fruit in splits:
    print(f"\n{fruit}")



# 3. Join list of words into a sentence
list1 = ['I', 'do', 'not', 'give', 'a', 'f/']
sentence = " ".join(list1)
print(sentence)

# 4. Join a list of numbers as a hypen separated string
numbers = [1,2,3,4,5]
joining = "-".join(str(number) for number in numbers)
print(joining)


# 5. Slice the first 3 characters of a string
string = "Pyton"
s = slice(0,3)
first_three = string[s]
print(first_three)

print(string[slice(0,3)])


# 6. Reverse a string using slicing
string = "Hello world"
reversing = string[slice(-1,None, -1)]
print(reversing)



# 7. Extract every second characrter
string = "acacacacacaca"
print(string[slice(0,None,2)])
print(string[::2])
print(string.split("c"))



# 8. Split a sentence and then reverse each word 
sentence = "Welcome Home Panda"

a = sentence.split(" ") # split each word and put it into a list
b = sentence[slice(None,None, -1)] # take the word and reverse its order in character level
c = b.split(" ")  # take the reversed string and put it into a list by splitting by space
d = " ".join(c) # take the list of reversed characters and put them into one string and use spaces when joining

print(a)
print(b)
print(c)
print(d)



# 9. Check if a string is a palindrome
while True:

    ask = input("Tell me anything and i will tell you if it is a Plaindrome or not: ")

    a = ask
    b = ask[slice(None,None, -1)]
    if a == b:
        print("Palindrome")
    else:
        print("Not a Palindrome")
# b3aut1ful


# 10. Convert a setence into a title case using split and join
sentence = "This is not a playground"
#print(sentence.title())
splitting = sentence.split(" ")
joining = " ".join(word.title() for word in splitting)
print(joining)



print("Tell me smth and i will repeat it for you.\nEnter q to quit")
message = ""
active = 1
while active:
    message = input("Enter here: ")

    if message == 'q':
        active = 0
    else:
        print(message)



print("Enter the city u have visited to.\nEnter q to quit")
message = ""
while True:
    message = input("Enter here: ")
    if message != 'q':
        print(f"I would love to visit {message.title()}")
    else:
        break

current_number = 0

while current_number < 10:
    current_number+=1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)



toppings = []

print("Please enter the topping you want in your pizza.\nEnter q when you are done")
message = ""
while True:
    message = input("Enter here: ")
    if message == 'q':
        break
    else:
        toppings.append(message)
        print(f"{message.title()} will be added")
print("Toppings you have listed: ")
for topping in toppings:
    print(topping.title())



number = 0
while True:
    number+=1
    print(number)





unconfirmed_users = ['alice', 'bob', 'said', 'akbar']
confirmed_users = []

while unconfirmed_users:
   # user = unconfirmed_users[0]
  #  unconfirmed_users.remove(user)

    user = unconfirmed_users.pop()

    confirmed_users.append(user)
    print(f"Verified user: {user}")

print(confirmed_users)


pets = ['tiger', 'horse', 'cat', 'cow', 'dog', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)



# i need to write a program that asks for the name and mountain and then  save them to dcitionary and then print 

# empty dict
responses = {

        }
poll_active = 1

while poll_active:
    name = input("What is your name? ")
    mountain = input("What is the name of mountain you would like to climb? ")
    
    #save results
    responses[name] = mountain

    # lets aks if there is someone else to answer
    ask = input("Is there someone else to answer? y/n ")
    if ask == "y":
        continue
    else:
        poll_active = 0
#print(responses)
print("\n ------------- Poll Results --------------\n")
   
for name, mountain in responses.items():
    print(f"{name.title()} would like to climb {mountain.title()}.")


def greet_user():
    print("Hello")
greet_user()



def greet_user(username):
    print(f"Hello {username.title()}")
name = input('What is your name? ')
greet_user(name)





def message():
    print("Hello, im learning functons today")
message()

def fav_book(name):
    print(f"Your favourite book is saved as {name.title()}")

x = input("What is your favourite book? ")
fav_book(x)


def describe_pet(animal, name):
    # return he result as
    print(f"i have got a {animal}\nMy {animal}'s name is {name.title()}")


describe_pet('dog','max')




def describe_pet(animal, name):
    print(f"I ve got a {animal}, and its name is {name.title()}")

describe_pet('dog','max')
describe_pet('rabbit', 'sezar')

def des_pet(animal, name):
    print(f"I got a\a {animal}. Its name is {name.title()}")

des_pet(animal = 'dog', name = 'max')
des_pet(name = 'max', animal = 'dog')





def des_pet(animal, name):
    print(f"I got a {animal}\nIts name is {name.title()}")

des_pet('dog', 'max')

def des_pet(animal = 'dog', name):
    print(f"i got a {animal}\nIts name is {name}")
des_pet('dog', 'john')   # lesson learnt: Python does not allow putting defaults values first.


def des_pet(animal, name = 'max'):
    print(f"i got a {animal} and its name is {name.title()}")

des_pet('dog',name = 'harry')
des_pet()



def full_name1(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

#first = input("What is your first name: ")
#last = input("What is your last name: ")
full_name1('max', 'collin')


def format_the_name(first, last):
    print(f"{first} {last}")
 #   return(full_name)

#musician = format_the_name('Jimi', 'Handrix')
#print(musician)
format_the_name('JImmy', 'Smith')

# LESSON: WHEN I USED RETURN, I CANT JUST CALL THE FUNCTION USING ITS NAAME AND ARGUMENTS, AND I DONNO WHY


# now i know why, before i used to use print inside the function but this time im calling the function and then it is actually returning the result, and im just not printing it. 

def get_formatted(first, middle, last):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    
    return full_name.title()

first = input("What is your first name: ")
middle = input("What is your middle name, [optional]: ")
last = input("What is your last name: ")

print(get_formatted(first, middle, last))


def full_name(first_name, last_name):
    # now i need to put them into dictionary
    person = {
    'first': first_name,
    'last': last_name
    }
    return person


get_full_name = full_name('Jimmy', 'Hawks')
print(get_full_name)


def full_name(first, last, age='NG'):
    # i want to put them into dictionary
    person = {
    'first name' : first,
    'last name' : last,
    'age' : age
    } 
    return person


# lets call the function
get_full_name = full_name('Jimmy', 'Hawks', '19')
get_full_name1 = full_name('Akbar', 'Holis')

print(get_full_name)
print(get_full_name1)



def get_formatted(first_name, last_name):
    full_name = f"{first_name} {last_name}"

    return full_name.title()


while True:
    print('Please tell me your first and last name!')
    f_name = input('What is your first name? :  ')
    l_name = input('What is your last name? : ')

    get_full_name = get_formatted(f_name, l_name)

    print(f"Hello, {get_full_name}") 



def greet(lists):
    for name in lists:
        greeting = f"Hello, {name.title()}. Welcome to Islands"

        print(greeting)
        #return greeting

names = ['Johanna', 'akbar', 'hussain', 'umar', 'max']


greet_em = greet(names)
#print(greet_em)


# start by defining 2 lists, and we need to move items from one to another

unprinted = ['phone case', 'robot pendant', 'dodecahedron']
printed = []

# lets try to move items from list 1 to 2
while unprinted:
    for items in unprinted:
        item = unprinted.pop()
        
        print(f'Printing {item}...')
        print('Finished')
        printed.append(item)

print(printed)



# firstly define 2 funtions

def printing(list1, list2):
    while list1:
        for items in list1:
            item = list1.pop()
            print(f"Printing {item}...\nFinished.")
            list2.append(item)
        
    print("Printed these items: ")
    for items2 in list2:
     print(items2)

list1 = ['a', 'b', 'c', 'd']
list2 = []

printing(list1, list2)


def make_pizza(*toppings): # this makes a tuple of toppings
    
    print('Making pizza with these toppings:')
    for topping in toppings:
        print(topping)


make_pizza('peperoni')
make_pizza('shaurma', 'hotdog', 'sausage')

def make_pizza(size, toppings):

    print(f'Making pizza with size {size} and toppings:')
    for topping in toppings:
        print(topping)


size = input('What size do u want: ')
toppings = []
topping = 1
while topping:
    topping_asked = input('What topping do u want: ')
    if topping_asked:
        toppings.append(topping_asked)
    else:
        topping = 0


print(size)
print(toppings)


make_pizza(size, toppings)


def build_profile (first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

user_profile = build_profile('albert', 'einstein', location = 'princeton', age = 18)
print(user_profile)


# here i will start to work with modules so i will create files as needed
# first task to create a files named 
#1. pizza.py 
#and make  a funciton there and call it here

import pizza

pizza.make_pizza(14, 'peperoni')
pizza.make_pizza(18, 'meat', 'sausage', 'icecream')




# importing specific fuctions
# i can also import specific functions from a module
# example
# from pizza import function_name or from pizza import function_1, function_2...


from pizza import make_pizza as mp

mp(34, 'nuts')


import pizza as p

p.make_pizza(9, 'peperpni')


class Dog:
    # now i will simply attempt to model a dog

    def __init__(self, name, age):
        #now i need to initislize the name and age attributes
        self.name = name
        self.age = age


    def sit(self):
        print(f"Simulating {self.name}'s sitting")
    def roll_over(self):
        print(f"Simulating the {self.name}'s rolling over")



my_dog = Dog("max", 14)
print(f"My dog's name is {my_dog.name.title()}")
print(f"My dog's age is {my_dog.age}")




class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print("Sitting")
    def roll_over(self):
        print("Rolling over")

my_dog = Dog('max', 9)
print(f"Hello i got a dog named {my_dog.name.title()} and he is {my_dog.age}")

my_dog.sit()


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f'{self.name} is sitting')
    def roll_over(self):
        print(f'{self.name} is not rolling over')


my_dog = Dog('max', 14)
yo_dog = Dog('willie', 13)

print(f"My dog's name is {my_dog.name.title()} and he is {my_dog.age} years old")
print(f"Your dog's name is {yo_dog.name.title()} and he is {yo_dog.age} years old")

my_dog.sit()
yo_dog.roll_over()


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name.title()


my_new_car = Car('byd', 'Zeekir', '2026')
print(my_new_car.get_descriptive_name())

        

class Car :
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        full_name = f"{self.year} {self.manufacturer} {self.model}"
        return full_name
    def read_odometer(self):
        print(f"This {self.model.title()} has {self.odometer_reading} miles on it")


new_car = Car('byd', 'zeekr', '2026')
print(new_car.get_descriptive_name().title())

new_car.read_odometer()


class Car:

    def __init__(self, model):
        self.model = model
        self.odometer = 0

    def get_model(self):
        print(f"model is {self.model}")

    def read_odometer(self):
        print(f'{self.odometer}')


my_car = Car('zeekr')

my_car.get_model()
my_car.read_odometer()

my_car.odometer = 500
my_car.read_odometer()

        
class Car:
    def __init__(self, model):
        self.model = model
        self.odometer = 0

    def get_model(self):
        print(f"Model is {self.model}")

    def get_odometer(self):
        print(f"It is {self.odometer}")

    def update_odometer(self, value):
        self.odometer = value


my_car = Car('audi')
my_car.get_model()
my_car.get_odometer()

my_car.update_odometer(20)
my_car.get_odometer()


class Car:
    def __init__(self, model):
        self.model = model
        self.mileage = 0
    def get_model(self):
        print(f"Model is {self.model} ")
    def update_mileage(self, value):
        if value > self.mileage:
            self.mileage = value
        else:
            print("Hell nah bruh")

my_car = Car('Zeekr')

my_car.get_model()
print(my_car.mileage)

my_car.update_mileage(23)
print(my_car.mileage)

my_car.update_mileage(20)
print(my_car.mileage)

my_car.update_mileage(25)
print(my_car.mileage)


my_car.update_mileage(23)
print(my_car.mileage)
'''
class Car:
    def __init__(self, model):
        self.model = model
        self.petrol = 20
    def get_model(self):
        print(f"Model is {self.model}")
    def get_petrol(self):
        print(f'{self.model.title()} has {self.petrol} left.')
my_car1 = Car('Zeekr')
#my_car.get_model()
my_car1.get_petrol()



class e_car(Car):
    def __init__(self, model):
        super().__init__(model)
        self.battery = 50
    def get_battery(self):
        print(f"Battery is {self.battery}")
    def get_petrol(self):
        print(f'{self.model.title()} does not run on petrol.')
my_car2 = e_car('Tesla')
my_car2.get_petrol()




