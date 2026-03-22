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