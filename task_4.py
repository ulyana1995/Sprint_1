new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006'] 

#Перенеси task_005 из списка new_tasks в список completed_tasks. Сделай это в одно действие.
completed_tasks.append(new_tasks.pop(new_tasks.index('task_005')))

#Удали task_007 из списка new_tasks.
new_tasks.remove('task_007')

#Выведи на экран последнюю задачу из списка new_tasks.
print(new_tasks[-1])