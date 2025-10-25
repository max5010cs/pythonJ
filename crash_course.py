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