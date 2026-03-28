class Task:
    def __init__(self, title, duration, priority, time="09:00", frequency="once"):
        self.title = title
        self.duration = duration
        self.priority = priority
        self.time = time
        self.frequency = frequency

    def __repr__(self):
        return f"{self.title} (Time: {self.time}, Priority: {self.priority}, Duration: {self.duration})"


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
        return sorted(tasks, key=lambda x: (-x.priority, x.time))

    def generate_daily_plan(self, tasks, available_hours):
        sorted_tasks = self.sort_tasks(tasks)   
        plan = []
        time_used = 0

        for task in sorted_tasks:
            if time_used + task.duration <= available_hours:
                plan.append(task)
                time_used += task.duration

        return plan

    def sort_by_time(self, tasks):
        return sorted(tasks, key=lambda task: task.time)

    def detect_conflicts(self, tasks):
        conflicts = []
        seen_times = {}

        for task in tasks:
            if task.time in seen_times:
                conflicts.append((seen_times[task.time], task))
            else:
                seen_times[task.time] = task

        return conflicts

