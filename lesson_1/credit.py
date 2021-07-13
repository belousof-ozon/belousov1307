# Считаем кредит
name1=input("Введите имя первого человека: ")
name2=input("Введите имя вторгого человека: ")


salary1=input("ЗП первого человека: ")
salary2=input("ЗП второго человека: ")


credit1=input("Введите сумму кредита: ")
period=input("Введите срок кредита в месяцах: ")
procent=input("Введите процент кредита: ")

pay_per_month = (int(credit1) /int(period))+(int(credit1)/ 100 * int(procent)) / 12
print("Ежемесячный платеж составит -" , pay_per_month, "рублей" )

print(name1, "сможет потратить", int(salary1) - pay_per_month)
print(name2, "сможет потратить", int(salary2) - pay_per_month)
