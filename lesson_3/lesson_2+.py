import random

# print(int(random.random()*100))
# print(random.randint(10, 35))

n = int(input("Введите кол-во участников: "))
win_num = int(input("Введите кол-во победителей: "))
already_win = []
for i in range(1, win_num+1):
    temp = random.randint(1, n)
    while temp in already_win:
        temp = random.randint(1, n)
    already_win.append(temp)
    print("Победител номер", i, "-", temp)




