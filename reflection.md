# PawPal+ Project Reflection

## 1. System Design

### a. Initial design
My initial UML design included four main classes: Owner, Pet, Task, and Scheduler. The Owner class is responsible for managing pets. Each Pet stores its own tasks. The Task class represents individual pet care activities such as feeding and walking. The Scheduler class is responsible for sorting tasks and generating a daily care plan.

### b. Design changes
During implementation, I kept the overall class structure the same, but I simplified the design to focus on the core scheduling logic. Instead of adding too many attributes at the beginning, I used only the fields needed for task scheduling, such as title, duration, and priority.

## 2. Scheduling Logic and Tradeoffs

### a. Constraints and priorities
My scheduler considers two main constraints: task priority and available time. Higher-priority tasks are scheduled first. A task is only added to the daily plan if it fits within the owner's available hours.

### b. Tradeoffs
One tradeoff in my scheduler is that it uses a simple priority-based strategy instead of a more advanced optimization algorithm. This means the solution is easy to understand and implement, but it may not always produce the absolute best schedule in more complex scenarios. For this project, I think that tradeoff is reasonable because the goal is to demonstrate clear object-oriented design and core scheduling logic.

## 3. AI Collaboration

### a. How you used AI
I used AI to help brainstorm the system design, identify the main classes, and draft the initial scheduling logic. AI was also helpful for generating example UML structure and clarifying how the classes should relate to one another.

### b. Judgment and verification
I reviewed the AI-generated suggestions and simplified them to match the project requirements. I verified the result by running the demo script and checking that tasks were sorted correctly and that the daily plan respected the available time constraint.

## 4. Testing and Verification

### a. What you tested
I tested the creation of tasks, the ability to add tasks to pets, and the scheduler’s ability to sort tasks by priority and generate a daily plan.

### b. Confidence
I am confident that the current version works correctly for the core use case. There is still room to improve the scheduler with more advanced logic in the future.

## 5. Reflection

### a. What went well
The object-oriented structure worked well and made the system easy to organize. The class relationships were simple and matched the real-world problem clearly.

### b. What you would improve
If I continued this project, I would add more detailed time handling, conflict detection, recurring task support, and a stronger user interface.

### c. Key takeaway
This project helped me practice turning a real-world scenario into classes, methods, and scheduling logic. I also learned how AI can help with brainstorming and implementation while still requiring human review and refinement.
## UML Diagram

```mermaid
classDiagram
    class Owner {
        +name
        +available_hours
        +pets
        +add_pet()
        +get_all_tasks()
    }

    class Pet {
        +name
        +species
        +tasks
        +add_task()
    }

    class Task {
        +title
        +duration
        +priority
    }

    class Scheduler {
        +sort_tasks()
        +generate_daily_plan()
    }

    Owner --> Pet
    Pet --> Task
    Scheduler --> Task