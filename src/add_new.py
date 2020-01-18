from main import time_register as tim_reg

new_task = tim_reg('16/01/2020','AbCdE','Create of new template')

print(new_task.date)
print(new_task.count)


new_task.date = input("Input date in DD/MM/YYYY format: ")
new_task.proj = input("Insert project name: ")
new_task.task = input("Insert task description: ")

print(new_task.date)
print(new_task.count)
