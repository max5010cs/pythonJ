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

user_data = "he                    is 29 years old with two kids             ".strip()

print(user_data)