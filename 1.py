import random


with open("is29.list", encoding="utf-8") as f:
    names = f.read().strip().split("\n")

with open("z4") as f:
    tasks = f.read().strip().split("\n")

for name in names:

    print(name)
    for task in tasks:
        old_tasks = []  # чтобы не было одинаковых заданий

        task_name, max_task_value, tasks_count = task.split()

        for _ in range(int(tasks_count)):
            random_task = random.randint(1, int(max_task_value))

            while random_task in old_tasks:
                random_task = random.randint(1, int(max_task_value))
            old_tasks.append(random_task)

            print(task_name, random_task)
    print()
