from pawpal_system import Task, Pet, Owner, Scheduler

owner = Owner("Alice", available_hours=5)

dog = Pet("Buddy", "Dog")
cat = Pet("Kitty", "Cat")

dog.add_task(Task("Walk", 2, 5, "09:00"))
dog.add_task(Task("Feed", 1, 4, "08:00"))
cat.add_task(Task("Feed Cat", 1, 3, "09:00"))

owner.add_pet(dog)
owner.add_pet(cat)

scheduler = Scheduler()
tasks = owner.get_all_tasks()

print("All Tasks:")
for t in tasks:
    print(t)

print("\nTasks Sorted by Time:")
for t in scheduler.sort_by_time(tasks):
    print(t)

print("\nToday's Schedule:")
plan = scheduler.generate_daily_plan(tasks, owner.available_hours)
for t in plan:
    print(t)

print("\nConflicts:")
conflicts = scheduler.detect_conflicts(tasks)
for task1, task2 in conflicts:
    print(f"Conflict: {task1.title} and {task2.title} are both scheduled at {task1.time}")