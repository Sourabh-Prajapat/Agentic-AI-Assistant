# 🤖 Agentic AI Assistant

A beginner-friendly **Agentic AI project** built with Python and the **Google Gemini API**, demonstrating how an LLM can understand user requests, select appropriate tools, and use their results to generate responses.

The project currently focuses on **LLM Tool Calling**, **multiple tool selection**, and **automatic function calling** using the Google GenAI SDK.

---

## ✨ Features

* 🤖 Gemini-powered AI assistant
* 🛠️ LLM tool calling
* 🔀 Multiple tool selection
* 🔄 Automatic function calling
* 🧮 Mathematical calculations
* 🎓 Student information retrieval
* 📊 Student attendance retrieval
* 🐍 Built with Python
* 🔑 Gemini API integration

---

## 🧠 How It Works

The assistant sends the user's question to Gemini along with a set of available Python tools.

Gemini understands the request and determines whether a tool is required. If a tool is needed, the Google GenAI SDK handles the function-calling process, executes the appropriate Python function, and provides the result back to Gemini.

```text
                         User
                           │
                           ▼
                     Gemini LLM
                           │
                    Understands Request
                           │
                           ▼
                   Selects Appropriate Tool
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
        Calculator    Student Info    Attendance
             │             │             │
             └─────────────┼─────────────┘
                           │
                           ▼
                      Tool Result
                           │
                           ▼
                     Gemini LLM
                           │
                           ▼
                     Final Answer
```

The tool-calling process is handled automatically by the **Google GenAI SDK** in the current implementation.

---

## 🛠️ Available Tools

### 🧮 Calculator

Performs basic mathematical operations:

* Addition
* Subtraction
* Multiplication
* Division

Example:

```text
User: What is 125 multiplied by 8?

Gemini → calculator()
Calculator → 1000
Gemini → Final response
```

---

### 🎓 Student Information

Retrieves basic information about a student, including:

* Branch
* Year
* Attendance

Example:

```text
User: What branch is Sourabh studying in?

Gemini → get_student_info("Sourabh")
Tool → Mechanical Engineering
Gemini → Final response
```

---

### 📊 Student Attendance

Retrieves the attendance percentage of a student.

Example:

```text
User: What is Sourabh's attendance?

Gemini → get_student_attendance("Sourabh")
Tool → 87%
Gemini → Final response
```

---

## 🔄 Multi-Tool Workflow

The assistant can handle queries that require information from a tool and further processing.

For example:

```text
User:
How many percentage points does Sourabh need to reach 95%?
```

Conceptually, the workflow is:

```text
User Query
     │
     ▼
Gemini
     │
     ▼
get_student_attendance("Sourabh")
     │
     ▼
87%
     │
     ▼
Gemini
     │
     ▼
calculator(95, 87, "subtract")
     │
     ▼
8
     │
     ▼
Gemini
     │
     ▼
Final Answer
```

The LLM determines which tools are required based on the user's request, while the Google GenAI SDK manages the function-calling interaction.

---

## 📁 Project Structure

```text
Agentic AI Assistant/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

> `.venv/` and API keys should not be uploaded to GitHub.

---

## ⚙️ Technologies Used

* **Python**
* **Google Gemini API**
* **Google GenAI SDK**
* **LLM Tool Calling**
* **Automatic Function Calling**
* **Python Functions**

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Sourabh-Prajapat/Agentic-AI-Assistant.git
```

```bash
cd Agentic-AI-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Set your Gemini API key

In PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

Replace `YOUR_API_KEY` with your Gemini API key.

**Never hard-code your API key in `main.py` or upload it to GitHub.**

### 6. Run the project

```bash
python main.py
```

---

## 💡 Example Queries

Try questions such as:

```text
What is 25 multiplied by 8?
```

```text
What is Sourabh's attendance?
```

```text
What branch is Sourabh studying in?
```

```text
Tell me about Sourabh.
```

```text
How many percentage points does Sourabh need to reach 95%?
```

```text
What is Nidhi's attendance?
```

The assistant determines which available tool is appropriate for the request.

---

## 🎯 Learning Objectives

This project was built to understand the fundamentals of **Agentic AI and LLM Tool Calling**, including:

* How LLMs interact with external tools
* How tools are defined using Python functions
* How function parameters are exposed to an LLM
* How an LLM selects an appropriate tool
* How the Google GenAI SDK handles automatic function calling
* How tool results are returned to the LLM
* How multiple tools can be used for a single task
* The foundation of tool-using AI agents

---

## 🔄 Current Architecture

```text
                    User Query
                        │
                        ▼
                   Gemini LLM
                        │
                        ▼
                Tool Selection
                        │
             ┌──────────┼──────────┐
             ▼          ▼          ▼
        Calculator  Student Info  Attendance
             │          │          │
             └──────────┼──────────┘
                        │
                        ▼
                   Tool Result
                        │
                        ▼
                   Gemini LLM
                        │
                        ▼
                  Final Response
```

The current implementation uses the **Google GenAI SDK's automatic function-calling capability**, rather than manually implementing the complete tool-calling loop.

---

## 👨‍💻 Author

**Sourabh Prajapat**

B.Tech Graduate, IIT Jammu

## [GitHub](https://github.com/Sourabh-Prajapat)
