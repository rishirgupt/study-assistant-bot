import json
from datetime import datetime


def validate_deadline(deadline):
    try:
        datetime.strptime(deadline, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def normalize_status(status):
    shortcut_map = {
        "n": "Not started",
        "not started": "Not started",
        "f": "Finished",
        "finished": "Finished",
        "o": "Ongoing",
        "ongoing": "Ongoing"
    }
    return shortcut_map.get(status.strip().lower())


def validate_status(status):
    return normalize_status(status) is not None


def normalize_command(user_input):
    command = user_input.strip().lower()
    shortcut_map = {
        "a": "add task",
        "add": "add task",
        "add task": "add task",
        "c": "create task",
        "create": "create task",
        "create task": "create task",
        "n": "new task",
        "new": "new task",
        "new task": "new task",
        "s": "show tasks",
        "show": "show tasks",
        "show tasks": "show tasks",
        "l": "list tasks",
        "list": "list tasks",
        "list tasks": "list tasks",
        "d": "display tasks",
        "display": "display tasks",
        "display tasks": "display tasks",
        "q": "quit",
        "quit": "quit",
        "e": "exit",
        "exit": "exit",
        "x": "exit",
        "t": "stop",
        "stop": "stop",
        "b": "bye",
        "bye": "bye",
        "h": "help",
        "help": "help",
        "o": "options",
        "options": "options",
        "m": "commands",
        "commands": "commands",
        "hello": "hello",
        "hi": "hi",
        "hey": "hey",
        "thanks": "thanks",
        "thank you": "thank you",
        "edit": "edit task",
        "edit task": "edit task",
        "update": "edit task",
        "update task": "edit task",
        "u": "edit task",
        "ed": "edit task"
    }
    return shortcut_map.get(command, command)


def load_tasks():
    try:
        with open('homework_data.json', 'r') as json_file:
            taskbase = json.load(json_file)
    except FileNotFoundError:
        taskbase = {}
    except json.JSONDecodeError:
        taskbase = {}
    return taskbase


def tasks_creation(user_input, taskbase):

    if user_input in ["add task", "create task", "new task"]:
        task_name = input("Enter the task name: ")
        task_description = input("Enter the task description: ")
        task_status = input("Enter the task status (Not started / Finished / Ongoing; or n/f/o): ")
        task_deadline = input("Enter the task deadline (dd/mm/yyyy): ")

        while True:
            normalized_status = normalize_status(task_status)
            if normalized_status:
                break
            print("Chatbot: Invalid status. Please choose one of: Not started, Finished, Ongoing.")
            task_status = input("Enter the task status (Not started / Finished / Ongoing; or n/f/o): ")

        while not validate_deadline(task_deadline):
            print("Chatbot: Invalid deadline format. Please enter the deadline in dd/mm/yyyy format.")
            task_deadline = input("Enter the task deadline (dd/mm/yyyy): ")
        
        taskbase[task_name] = {
            "task description": task_description,
            "task status": normalized_status,
            "task_deadline": task_deadline
        }

        with open('homework_data.json', 'w') as json_file:
            json.dump(taskbase, json_file, indent=4)

        print(f"Chatbot: Task '{task_name}' added successfully!")


def tasks_edit(user_input, taskbase):

    if user_input in ["edit task", "update task"]:
        if not taskbase:
            print("Chatbot: No tasks available to edit.")
            return

        task_name = input("Enter the name of the task to edit: ")
        if task_name not in taskbase:
            print(f"Chatbot: Task '{task_name}' not found.")
            return

        details = taskbase[task_name]
        print(f"Chatbot: Current details for '{task_name}':")
        print(f" Description: {details['task description']}")
        print(f" Status: {details['task status']}")
        print(f" Deadline: {details['task_deadline']}")
        print("Enter new values or press Enter to keep existing values.")

        new_name = input("New name (leave blank to keep): ").strip()
        new_description = input("New description (leave blank to keep): ").strip()
        new_status = input("New status (Not started / Finished / Ongoing; or n/f/o) (leave blank to keep): ").strip()
        new_deadline = input("New deadline (dd/mm/yyyy) (leave blank to keep): ").strip()

        if new_status:
            while not validate_status(new_status):
                print("Chatbot: Invalid status. Please choose one of: Not started, Finished, Ongoing.")
                new_status = input("New status (Not started / Finished / Ongoing; or n/f/o) (leave blank to keep): ").strip()

        if new_deadline:
            while not validate_deadline(new_deadline):
                print("Chatbot: Invalid deadline format. Please enter dd/mm/yyyy or leave blank to keep existing.")
                new_deadline = input("New deadline (dd/mm/yyyy) (leave blank to keep): ").strip()
                if not new_deadline:
                    break

        final_name = new_name if new_name else task_name
        final_description = new_description if new_description else details['task description']
        final_status = normalize_status(new_status) if new_status else details['task status']
        final_deadline = new_deadline if new_deadline else details['task_deadline']

        # If the name changed, remove the old key
        if final_name != task_name:
            taskbase.pop(task_name)

        taskbase[final_name] = {
            "task description": final_description,
            "task status": final_status,
            "task_deadline": final_deadline
        }

        with open('homework_data.json', 'w') as json_file:
            json.dump(taskbase, json_file, indent=4)

        print(f"Chatbot: Task '{task_name}' updated successfully!")


def Display_tasks(user_input, taskbase):

    if user_input in ["show tasks", "list tasks", "display tasks"]:
        if not taskbase:
            return "Chatbot: No tasks available."
        else:
            display_tasks_response = "Chatbot: Current Tasks:\n"
            for task_name, details in taskbase.items():
                display_tasks_response += f"\n - {task_name}: \n Description: {details['task description']} - \n Status: {details['task status']}\n Deadline: {details['task_deadline']}\n"
            return display_tasks_response
    return "Chatbot: I didn't understand that command."


def chatbot_response(user_input, taskbase):
    return ""


def main():
    taskbase = load_tasks()

    print("\n" + "="*60)
    print(f"Welcome to your study assistant bot!")
    print(f"Version 2.3!")
    print(f"Created by: Rishi Gupta")
    print("="*60 + "\n")
    
    
    while True:
        user_input = input("You: ").strip()
        command = normalize_command(user_input)

        if command in ["quit", "exit", "stop", "bye"]:
            print("Chatbot: Goodbye!")
            break
        
        if command in ["hello", "hi", "hey"]:
            print("Chatbot: Hello! How can I assist you with your tasks today?")
            continue

        if command in ["thanks", "thank you"]:
            print("Chatbot: You're welcome! If you have any more questions or need assistance, feel free to ask.")
            continue

        if command in ["help", "commands", "options"]:
            print("Chatbot: Here are the available commands:\n- 'a'/'add task'/'create task'/'new task': Add a new task.\n- 's'/'show tasks'/'list tasks'/'display tasks': Show all tasks.\n- 'edit'/'update'/'u': Edit an existing task.\n- 'q'/'quit'/'exit'/'stop'/'bye': Exit the chatbot.")
            continue
        
        if command in ["add task", "create task", "new task"]:
            tasks_creation(command, taskbase)
            continue

        if command in ["edit task", "update task"]:
            tasks_edit(command, taskbase)
            continue

        if command in ["show tasks", "list tasks", "display tasks"]:
            print(Display_tasks(command, taskbase))
            continue

        if not command:
            print("Chatbot: Please enter a command or type 'help' to see available options.")
            continue

        print("Chatbot: I didn't understand that command. Try 'a' for add, 's' for show, or 'q' to quit.")


if __name__ == "__main__":
    main()