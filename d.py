
import requests
import numpy as np
import pandas as pd
import json

r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
# print(len(r.json()['data']))



data= r.json()['data']

# print(data2)
list_data = data.split(',')

# print(list_data[0])



def convert_dict(a):
  init=iter(list_data)
  res_dict=dict(zip(init,init))
  return res_dict

# print(convert_dict(list_data))

dict_data = convert_dict(list_data)


# print('************* line 30')
# print(dict_data)
list_age =[]
for x in dict_data:
  list_age.append(dict_data[x])

# print(list_age)
list_2=[]
for i in list_age:
  list_2.append(i.split('='))

# print(len(list_2))

list_3 =[]
for i in list_2:
  # print(i[1])
  if int(i[1])>50:
    list_3.append(i[1])

# print(list_3)
# print('the result is ********* ')
print(len(list_3))
  