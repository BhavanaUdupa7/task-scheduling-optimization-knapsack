#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

def knapsack_dp(durations, priorities, available_time):
    n = len(durations)
    dp = [[0 for _ in range(available_time + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for t in range(available_time + 1):
            if durations[i - 1] <= t:
                dp[i][t] = max(priorities[i - 1] + dp[i - 1][t - durations[i - 1]], dp[i - 1][t])
            else:
                dp[i][t] = dp[i - 1][t]
    
    # Backtrack to find selected tasks
    selected_tasks = []
    t = available_time
    for i in range(n, 0, -1):
        if dp[i][t] != dp[i - 1][t]:
            selected_tasks.append(i - 1)
            t -= durations[i - 1]
    
    return dp[n][available_time], selected_tasks

# User Input for Tasks
tasks = []
durations = []
priorities = []
n = int(input("Enter number of tasks: "))
for i in range(n):
    task_name = input(f"Enter name of task {i+1}: ")
    duration = int(input(f"Enter duration (hours) for '{task_name}': "))
    priority = int(input(f"Enter priority value for '{task_name}': "))
    tasks.append(task_name)
    durations.append(duration)
    priorities.append(priority)

available_time = int(input("Enter available working hours: "))

# Solve Task Scheduling Problem
max_priority, selected_indices = knapsack_dp(durations, priorities, available_time)

# Display Results
print(f"\nMaximum Priority (Total Productivity): {max_priority}")
print("Selected Tasks:")
selected_task_names = []
selected_task_durations = []
for i in selected_indices:
    print(f"- {tasks[i]} (Duration: {durations[i]} hours, Priority: {priorities[i]})")
    selected_task_names.append(tasks[i])
    selected_task_durations.append(durations[i])

# Visualization
plt.figure(figsize=(6, 3))
plt.barh(selected_task_names, selected_task_durations, color='skyblue')
plt.xlabel("Duration (hours)")
plt.ylabel("Tasks")
plt.title("Selected Tasks for Maximum Productivity")
plt.gca().invert_yaxis()
plt.show()


# In[ ]:




