# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# #Write your 1 line code 👇 below:
#
# squared_numbers=[num*num for num in numbers]
# resualt=[num for num in numbers if num%2==0]
# #Write your code 👆 above:
#
# print(resualt)


# import random
# names=["Alex","Beth","Carolin","Dave","Eleanor","Freddie"]
# students_score={student:random.randint(1,100) for student in names}
# print(students_score)
# passed_student={student:score for (student,score) in students_score.items() if score>60}
# print(passed_student)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
# # Write your code below:
# # text_list=sentence.split()
# resualt={word:len(word) for word in sentence.split()}
#
# print(resualt)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
# Write your code 👇 below:
weather_f={day:(temp*9/5)+32 for (day,temp) in weather_c.items()}

print(weather_f)

