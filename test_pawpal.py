from pawpal_system import Task, Scheduler


def test_sort_tasks():
    scheduler = Scheduler()
    tasks = [Task("A", 1, 1), Task("B", 1, 5)]
    sorted_tasks = scheduler.sort_tasks(tasks)

    assert sorted_tasks[0].title == "B"


def test_generate_daily_plan():
    scheduler = Scheduler()
    tasks = [Task("A", 3, 5), Task("B", 3, 4)]

    plan = scheduler.generate_daily_plan(tasks, 5)

    assert len(plan) == 1
    assert plan[0].title == "A"


def test_sort_by_time():
    scheduler = Scheduler()
    tasks = [
        Task("A", 1, 1, "09:00"),
        Task("B", 1, 1, "08:00"),
    ]

    sorted_tasks = scheduler.sort_by_time(tasks)

    assert sorted_tasks[0].title == "B"
    assert sorted_tasks[1].title == "A"


def test_conflict_detection():
    scheduler = Scheduler()
    tasks = [
        Task("Walk", 1, 5, "09:00"),
        Task("Feed", 1, 3, "09:00"),
    ]

    conflicts = scheduler.detect_conflicts(tasks)

    assert len(conflicts) == 1