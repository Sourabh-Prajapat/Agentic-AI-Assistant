from google import genai


client = genai.Client()


# -----------------------------
# Student data
# -----------------------------

students = {
    "Sourabh": {
        "branch": "Mechanical Engineering",
        "year": 4,
        "attendance": 87
    },
    "Priya": {
        "branch": "Computer Science",
        "year": 3,
        "attendance": 91
    },
    "Nidhi": {
        "branch": "Electrical Engineering",
        "year": 4,
        "attendance": 84
    }
}


# -----------------------------
# Tool 1: Calculator
# -----------------------------

def calculator(a: float, b: float, operation: str) -> float:
    """Perform a mathematical operation on two numbers."""

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            return 0

        return a / b

    return 0


# -----------------------------
# Tool 2: Student information
# -----------------------------

def get_student_info(name: str):
    """Get basic information about a student."""

    if name in students:
        return students[name]

    return {"error": "Student not found"}


# -----------------------------
# Tool 3: Student attendance
# -----------------------------

def get_student_attendance(name: str):
    """Get the attendance percentage of a student."""

    if name in students:
        return students[name]["attendance"]

    return {"error": "Student not found"}


# -----------------------------
# Tool registry
# -----------------------------

tool_registry = {
    "calculator": calculator,
    "get_student_info": get_student_info,
    "get_student_attendance": get_student_attendance
}


# -----------------------------
# Tools available to Gemini
# -----------------------------

tools = [
    calculator,
    get_student_info,
    get_student_attendance
]


# -----------------------------
# Create chat
# -----------------------------

chat = client.chats.create(
    model="gemini-2.5-flash",
    config={
        "tools": tools
    }
)


# -----------------------------
# User question
# -----------------------------

question = "What is Sourabh's attendance and how much does he need to reach 90%?"


# -----------------------------
# Send question to Gemini
# -----------------------------

response = chat.send_message(question)


# -----------------------------
# Multi-tool execution loop
# -----------------------------

while response.function_calls:

    for function_call in response.function_calls:

        tool_name = function_call.name
        tool_args = function_call.args

        print(f"\nTool called: {tool_name}")
        print(f"Arguments: {tool_args}")

        # Find tool dynamically
        tool = tool_registry.get(tool_name)

        if tool:

            result = tool(**tool_args)

        else:

            result = {
                "error": f"Tool '{tool_name}' not found"
            }

        print(f"Tool result: {result}")

        # Send tool result back to Gemini
        response = chat.send_message(
            {
                "function_response": {
                    "name": tool_name,
                    "response": {
                        "result": result
                    }
                }
            }
        )


# -----------------------------
# Final answer
# -----------------------------

print("\nFinal Answer:")
print(response.text)