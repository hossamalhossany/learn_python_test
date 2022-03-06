

# مسألة برمجية بسيطة
# " A  قم بترتيب الأسماء من الأصغر للأكبر من ناحية عدد الحروف, والأسماء بالحروف الصغيرة أولا ونحتاج فقط الأسماء التي تبدأ بحرف "

# ["Ameer","alsayed","Mahmoud","Ahmed","ayman","Israa","Anas","amal","amr","aml"]

# #OutPut
# ["aml","amr","amal","ayman","alsayed","Anas","Ahmed","Ameer"]

list_original = ["Ameer","alsayed","Mahmoud","Ahmed","ayman","Israa","Anas","amal","amr","aml"]
print(f'\nlist_original =  {list_original} \n ')


list_2 =[]

for i in list_original:
    if i.startswith('a') or i.startswith('A'):
        list_2.append(i)

print(f'list_2 = {list_2} \n')

