# with open ('weather_data.csv') as csv_file:
#     contents=csv_file.readlines()
#     for item in contents:
#         item.strip()
#         print([item])
# ---------------------------------------------------
# import csv
# with open('weather_data.csv') as csv_file:
#     data= csv.reader(csv_file)
#     tempretures=[]
#     for row in data:
#         if row[1] !='temp':
#             tempretures.append(int(row[1]))
#     print(tempretures)

 # ---------------------------------------------------------------
# import pandas
# data= pandas.read_csv('weather_data.csv')
# data_dict= data.to_dict()
# print(data_dict)
# temp_list=data['temp'].to_list()
# avg_temp= sum(temp_list)/len(temp_list)
# print(avg_temp)
# print(data['temp'].mean())
# max_temp=data['temp'].max()
# print(data[data.temp == max_temp])
# data_monday=data[data.day=='Monday']
# print(data_monday.temp)
# ------------------squirrel cences------------------------------------

import pandas
data= pandas.read_csv('Squirrel_Census.csv')
gray_squirrel_cnt=len(data[data['Primary Fur Color']=='Gray'])
cinnamon_squirrel_cnt=len(data[data['Primary Fur Color']=='Cinnamon'])
black_squirrel_cnt=len(data[data['Primary Fur Color']=='Black'])
data_dict={
    'FurColor':['Gray','Cinnnamon','Black'],
    'Count':[gray_squirrel_cnt,cinnamon_squirrel_cnt,black_squirrel_cnt]
}
print(data_dict)
df= pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')