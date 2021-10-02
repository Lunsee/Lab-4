priziv1 = {}

#list1 = []
num = int (input("Сколько призывников хотите записать и вывести?: "))
for i in range (num ):
    surname = input("Введите фамилию призывника: ")
    name = input("Введите имя призывника: ")
    otch = input("Введите отчество призывника: ")
    god = input("Введите год рождения призывника: ")
    ill = input("Введите заболевание призывника: ")
    #priziv1 [surname + " " + name + " " + otch] =  god + " " + ill
    priziv1[i] = surname , name , otch , god , ill

    #list1.append(surname + " " + name + " " + otch)





#item1 = list(priziv1.items())


for k in range (num ):
   #print (list1[k] + " " + priziv1[list1[k]],"\n")
    print(priziv1[k])  #Не смог придумать как вывести идеальной таблицей чтоб каждый элемент был под другим соответсвующим стобцом