# this test file 

# مسألة برمجية بسيطة
# " A  قم بترتيب الأسماء من الأصغر للأكبر من ناحية عدد الحروف, والأسماء بالحروف الصغيرة أولا ونحتاج فقط الأسماء التي تبدأ بحرف "

# ["Ameer","alsayed","Mahmoud","Ahmed","ayman","Israa","Anas","amal","amr","aml"]

# #OutPut
# ["aml","amr","amal","ayman","alsayed","Anas","Ahmed","Ameer"]


list_original = ["Ameer","alsayed","Mahmoud","Ahmed","ayman","Israa","Anas","amal","amr","aml"]
print(f'\nlist_original =  {list_original} \n ')


sort_list =[]

for i in list_original:
    if i.startswith(('a','A')):
        sort_list.append(i)


def lenght_item(l):
    return len(l)

sort_list.sort(key=lenght_item)

print(f'list_2 = {sort_list} \n')



