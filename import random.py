import random
list1=[random.randint(0,50) for i in range(20)]
list2=list1[0:10]
list3=list1[10:20]
list2.sort()
list3.sort(reverse=True)
list1[0:10]=list2
list1[10:20]=list3
print(list1)
