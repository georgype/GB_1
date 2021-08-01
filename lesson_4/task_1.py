from sys import argv
script_name, work_time, work_cost, bonus = argv
print("Зарплата сотрудника ", int(work_time)*int(work_cost) + int(bonus))