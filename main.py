from pawpal_system import Task, Pet, Owner, Scheduler


# 创建 owner
owner = Owner("Alice", available_hours=4)

# 创建 pets
dog = Pet("Buddy", "Dog")
cat = Pet("Kitty", "Cat")

# 添加任务
dog.add_task(Task("Walk", 2, 5))
dog.add_task(Task("Feed", 1, 4))
cat.add_task(Task("Feed Cat", 1, 3))

# 加入 owner
owner.add_pet(dog)
owner.add_pet(cat)

# 收集所有任务
tasks = owner.get_all_tasks()

print("All Tasks:")
for t in tasks:
    print(t)

# 调度
scheduler = Scheduler()
plan = scheduler.generate_daily_plan(tasks, owner.available_hours)

print("\nToday's Schedule:")
for t in plan:
    print(t)