#🧮 Python CLI Calculator

A command-line calculator built in Python, developed in two versions to show how a simple program can grow from a basic script into a more robust, user-friendly tool.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Type](https://img.shields.io/badge/Type-CLI%20App-lightgrey)
![Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen)

---

## 📌 Overview

This project contains two implementations of a terminal-based calculator that performs addition, subtraction, multiplication, and division.

| | `Calculator1.py` | `Calculator2.py` |
|---|---|---|
| **Purpose** | Basic, single-run calculator | Enhanced, interactive calculator |
| **Runs** | Once, then exits | In a loop until the user chooses Exit |
| **Input validation** | None (crashes on non-numeric input) | Re-prompts until a valid number is entered |
| **Division by zero** | Handled | Handled |
| **Interface** | Plain text menu | Colored boxed menu using ANSI codes |
| **Exit option** | No | Yes (option 5) |

---

## ✨ Features

### Calculator1 (Basic)
- Menu-driven selection of four arithmetic operations
- Accepts floating-point numbers
- Division-by-zero check
- Invalid menu choice handling

### Calculator2 (Enhanced)
- Continuous loop, so you can run multiple calculations without restarting
- Dedicated `get_number()` helper with `try/except` that keeps asking until the input is valid
- Colored terminal UI (cyan menu, yellow prompts, green results, red errors)
- Clean boxed menu with an Exit option
- Modular structure: `show_menu()`, `get_number()`, `calculator()`

---

## 🛠️ Tech & Concepts Used

- **Language:** Python 3
- **Concepts:** functions, loops, conditionals, exception handling (`try/except`), input validation, f-strings, ANSI escape codes
- **Dependencies:** none (standard library only)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed ([download](https://www.python.org/downloads/))

### Run

```bash
# Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# Run the basic version
python Calculator1.py

# Run the enhanced version
python Calculator2.py
```

---

## 💻 Sample Output

**Calculator1**
```
simple calculator
1. addition
2. subtraction
3. multiplication
4. division
enter your choice (1-4): 4
enter first number: 20
enter second number: 4
result: 5.0
```

**Calculator2**
```
╔══════════════════════════════╗
║      SIMPLE CALCULATOR       ║
╠══════════════════════════════╣
║  1. Addition        (+)      ║
║  2. Subtraction     (-)      ║
║  3. Multiplication  (×)      ║
║  4. Division        (÷)      ║
║  5. Exit                     ║
╚══════════════════════════════╝
Enter your choice (1-5): 3
Enter first number: 6
Enter second number: 7

Result: 42.0
```

> Colors render in most modern terminals. On older Windows terminals, use Windows Terminal or enable ANSI support.

---

## 📂 Project Structure

```
├── Calculator1.py   # Basic version
├── Calculator2.py   # Enhanced version with validation, loop and colored UI
└── README.md
```

---

## 🔮 Future Improvements

- Add more operations (modulus, exponent, square root)
- Keep a calculation history
- Support expression parsing (e.g., `2 + 3 * 4`)
- Build a GUI version with Tkinter

---

## 🎯 What I Learned

- Structuring a program into reusable functions
- Handling bad user input gracefully with exception handling
- Improving user experience in a CLI through loops, validation, and formatting
- Iterating on a project: moving from a working prototype to a more polished version

---

## 👤 Author

**Ganesh Chandra Patnaik**
B.Tech in Computer Science and Engineering

- GitHub: @GaneshPatnaik.cs
- LinkedIn: www.linkedin.com/in/ganesh-chandra-patnaik-cs

---

⭐ If you found this useful, consider starring the repo!
