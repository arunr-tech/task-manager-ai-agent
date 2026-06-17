agent = {
    "name": "Arun",
    "tasks": [
        "Study Python",
        "Build AI Agent",
        "Upload to GitHub"
    ],
    "completed_tasks": []
}


def show_tasks():
    print("\n📋 Pending Tasks:")
    if len(agent["tasks"]) == 0:
        print("No pending tasks.")
    else:
        for task in agent["tasks"]:
            print("-", task)

    print("\n✅ Completed Tasks:")
    if len(agent["completed_tasks"]) == 0:
        print("No completed tasks.")
    else:
        for task in agent["completed_tasks"]:
            print("-", task)


def add_task():
    task = input("Enter new task: ").strip()

    if task == "":
        print("❌ Task cannot be empty.")
    else:
        agent["tasks"].append(task)
        print("✅ Task added!")


def complete_task():
    task = input("Enter task to complete: ").strip()

    if task in agent["tasks"]:
        agent["tasks"].remove(task)
        agent["completed_tasks"].append(task)
        print("🎉 Task completed!")
    else:
        print("❌ Task not found.")


def remove_task():
    task = input("Enter task to remove: ").strip()

    if task in agent["tasks"]:
        agent["tasks"].remove(task)
        print("🗑️ Task removed!")
    else:
        print("❌ Task not found.")


def show_progress():
    total = len(agent["tasks"]) + len(agent["completed_tasks"])
    done = len(agent["completed_tasks"])

    print("\n📊 Progress Report")

    if total == 0:
        print("No tasks available.")
    else:
        percentage = (done / total) * 100
        print("Completed:", done, "/", total)
        print("Progress: {:.1f}%".format(percentage))


def recommend_task():
    print("\n🤖 Recommended Task:")

    if len(agent["tasks"]) > 0:
        print(agent["tasks"][0])
    else:
        print("🎉 All tasks completed!")


while True:
    print("\n🤖 AI Task Manager")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Remove Task")
    print("5. Show Progress")
    print("6. Recommend Task")
    print("7. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        show_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        remove_task()

    elif choice == "5":
        show_progress()

    elif choice == "6":
        recommend_task()

    elif choice == "7":
        print("👋 Exiting agent...")
        break

    else:
        print("❌ Invalid choice. Please enter 1-7.")