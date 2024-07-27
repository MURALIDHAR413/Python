class Task:
    def __init__(self, id, duration):
        self.id = id
        self.duration = duration
        self.predecessors = []
        self.successors = []

        self.est = 0  # Earliest Start Time
        self.eft = 0  # Earliest Finish Time
        self.lst = float('inf')  # Latest Start Time
        self.lft = float('inf')  # Latest Finish Time

def add_dependency(from_task, to_task):
    from_task.successors.append(to_task)
    to_task.predecessors.append(from_task)

def calculate_earliest_times(tasks):
    for task in tasks:
        if not task.predecessors:
            task.est = 0
            task.eft = task.duration
        else:
            task.est = max(pred.eft for pred in task.predecessors)
            task.eft = task.est + task.duration

def calculate_latest_times(tasks, project_finish_time):
    for task in reversed(tasks):
        if not task.successors:
            task.lft = project_finish_time
            task.lst = task.lft - task.duration
        else:
            task.lft = min(succ.lst for succ in task.successors)
            task.lst = task.lft - task.duration

def main():
    # Create tasks
    t1 = Task('T1', 4)
    t2 = Task('T2', 3)
    t3 = Task('T3', 2)
    t4 = Task('T4', 5)
    t5 = Task('T5', 1)

    # Add dependencies
    add_dependency(t1, t3)
    add_dependency(t2, t3)
    add_dependency(t3, t4)
    add_dependency(t3, t5)

    # List of tasks
    tasks = [t1, t2, t3, t4, t5]

    # Calculate earliest start and finish times
    calculate_earliest_times(tasks)

    # Determine project completion time (latest finish time among all tasks)
    project_finish_time = max(task.eft for task in tasks)

    # Calculate latest start and finish times
    calculate_latest_times(tasks, project_finish_time)

    # Output results
    print(f"Earliest project completion time: {project_finish_time}")
    latest_start_times = [task.lst for task in tasks]
    latest_project_completion_time = max(l + task.duration for task, l in zip(tasks, latest_start_times))
    print(f"Latest project completion time: {latest_project_completion_time}")

if __name__ == "__main__":
    main()

# Total Time Complexity: O(n + m)
# Total Space Complexity: O(n + m)