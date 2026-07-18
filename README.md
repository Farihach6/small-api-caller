# Small API Caller

A beginner-friendly Python project that demonstrates how to call a public REST API using the `requests` library. The application connects to the GitHub Public API, retrieves data in JSON format, and displays selected information in the terminal.

---

## Features

- Connects to the GitHub Public API
- Sends an HTTP GET request
- Parses JSON responses
- Displays useful API information
- Handles connection and request errors
- Beginner-friendly and easy to understand

---

## Technologies Used

- Python 3.13
- Requests Library
- Git & GitHub

---

## Project Structure

```
small-api-caller/
│── main.py
│── requirements.txt
│── README.md
└── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Farihach6/small-api-caller.git
```

### 2. Navigate to the project folder

```bash
cd small-api-caller
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows (PowerShell)**

```powershell
.\venv\Scripts\Activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python main.py
```

---

## Sample Output

```
========================================
      GitHub Public API Caller
========================================

API Connected Successfully!

Current User URL:
https://api.github.com/user

Repository URL:
https://api.github.com/repos/{owner}/{repo}

Rate Limit URL:
https://api.github.com/rate_limit
```

---

## How It Works

1. Imports the `requests` library.
2. Sends a GET request to the GitHub Public API.
3. Receives data in JSON format.
4. Converts the JSON response into a Python dictionary.
5. Displays selected API information.
6. Handles errors if the request fails.

---

## Requirements

```
requests
```

Or install using:

```bash
pip install -r requirements.txt
```

---

## Learning Outcomes

Through this project, I learned how to:

- Work with REST APIs
- Send HTTP GET requests
- Parse JSON data
- Handle API responses
- Use the `requests` library
- Manage Python dependencies
- Use Git and GitHub for version control

---

## Author

**Fariha Ch**

BS Software Engineering Student

University of Sargodha

GitHub: https://github.com/Farihach6
