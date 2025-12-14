class TaskError(Exception):
    pass

def check_task(task: list[dict]):
    for i in task:
        if 'title' not in i or 'completed' not in i:
            raise TaskError('Задание не корректно, не хватает ключей')
    print('Задание выполнено корректно')

