def job_scheduling(tasks, n):
    """
    :param tasks: List of tuples (task_id, profit, deadline)
    :param n: Number of tasks
    :return: Maximum profit and sequence of scheduled tasks
    """
    # Sort tasks by profit in descending order
    tasks.sort(key=lambda x: x[1],reverse=True)
    print(tasks[1])
    # Find the maximum deadline
    max_deadline = max(task[2] for task in tasks)

    # Create a result array to track task scheduling
    result = [-1] * (max_deadline + 1)

    # Track total profit
    total_profit = 0

    # Track scheduled tasks
    scheduled_tasks = []

    # Iterate through the tasks
    for task in tasks:
        task_id, profit, deadline = task

        # Find a free slot for this task (from the latest possible slot)
        for slot in range(min(deadline, max_deadline), 0, -1):
            if result[slot] == -1:  # Slot is empty
                result[slot] = task_id
                total_profit += profit
                scheduled_tasks.append(task_id)
                break

    return total_profit, scheduled_tasks


# Example usage
tasks=[['T1',100,2],
 ['T2',19 ,1],
 ['T3', 27, 3],
 ['T4', 105, 2],
 ['T5', 15, 3]]

n = len(tasks)
max_profit, schedule = job_scheduling(tasks, n)
print("Maximum Profit:", max_profit)
print("Scheduled Tasks:", schedule)
