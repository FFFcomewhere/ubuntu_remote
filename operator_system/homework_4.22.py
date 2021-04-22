
file = open('hightemp.txt',mode= 'r',encoding='utf-8')
lines = file.readlines()
List_1 = []
List_2 = []

for i in lines:
    List_1.append(i.split('\t')[0])

for i in List_1:
    if i not in List_2:
        List_2.append(i)
List_2.sort()
for i in List_2:
    print(i)



