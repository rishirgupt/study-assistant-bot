# 📚 Study Assistant Bot

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


An educational task management chatbot designed to help students create, edit, update, and track their homework assignments and study tasks easily via a Command Line Interface (CLI) or through an interactive Web UI built using Lovable.ai.

---

## 🚀 Live Demo

Check out the interactive web application UI:
👉 **[Study Assistant Bot Web App](https://study-assistant-bot.lovable.app/)**
    
---

## ✨ Features

* ➕ **Task Creation:** Quickly add tasks with descriptions, current status (`Not started`, `Ongoing`, `Finished`), and deadlines.
* 📝 **Task Management & Editing:** Update existing task details, statuses, or deadlines seamlessly.
* 📋 **Display Tasks:** View all active study assignments at a glance.
* 💾 **JSON Data Persistence:** Tasks are saved locally to `homework_data.json` to persist across sessions.
* ⌨️ **Command Shortcuts:** Supports short aliases for commands (`a` for add, `s` for show, `edit`/`u` for update, `q` for quit, etc.).

---

## 🛠️ Requirements

* **Python 3.x** (Uses built-in standard modules `json` and `datetime`; no third-party library installation needed).

---

## Available CLI Commands:

1. Add Task: a, add, add task, create, new
2. Show Tasks: s, show, show tasks, list, display
3. Edit Task: edit, update, u
4. Help: h, help, options, commands
5. Exit: q, quit, exit, stop, bye

---

⚙️ Data Format Example (homework_data.json)
```bash
{
    "english": {
        "task description": "read and analyze chapter 4 of To Kill a Mockingbird",
        "task status": "Not started",
        "task_deadline": "05/12/2026"
    },
    "math": {
        "task description": "solve calculus problem set on derivatives",
        "task status": "Not started",
        "task_deadline": "05/15/2026"
    }
}
```
---

## 👨‍💻 Author
**Rishi Gupta**  
*Grade 12 Student | Aspiring AI Developer*


