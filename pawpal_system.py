class Task:
    def __init__(self, title, duration, priority):
        self.title = title
        self.duration = duration
        self.priority = priority

    def __repr__(self):
        return f"{self.title} (Priority: {self.priority}, Duration: {self.duration})"


class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)


class Owner:
    def __init__(self, name, available_hours):
        self.name = name
        self.available_hours = available_hours
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def get_all_tasks(self):
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.tasks)
        return tasks


class Scheduler:
    def sort_tasks(self, tasks):
        return sorted(tasks, key=lambda x: x.priority, reverse=True)

    def generate_daily_plan(self, tasks, available_hours):
        sorted_tasks = self.sort_tasks(tasks)
        plan = []
        time_used = 0

        for task in sorted_tasks:
            if time_used + task.duration <= available_hours:
                plan.append(task)
                time_used += task.duration

        return plan


def demo():
    owner = Owner("Alice", 5)

    dog = Pet("Buddy", "Dog")
    cat = Pet("Milo", "Cat")

    dog.add_task(Task("Walk", 2, 5))
    dog.add_task(Task("Feed", 1, 4))
    cat.add_task(Task("Feed Cat", 1, 3))

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler()

    tasks = owner.get_all_tasks()

    print("All Tasks:")
    print(tasks)

    print("\nDaily Plan:")
    plan = scheduler.generate_daily_plan(tasks, owner.available_hours)
    for task in plan:
        print(task)


if __name__ == "__main__":
    demo()