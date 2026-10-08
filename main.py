from google import genai

client = genai.Client()


# Student data
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


# Tool 1: Calculator
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

    else:
        return 0


# Tool 2: Student information
def get_student_info(name: str):
    """Get basic information about a student."""

    if name in students:
        return students[name]

    return {"error": "Student not found"}


# Tool 3: Student attendance
def get_student_attendance(name: str):
    """Get the attendance percentage of a student."""

    if name in students:
        return students[name]["attendance"]

    return {"error": "Student not found"}


# User question
question = "Tell me about Sourabh?"


# Send request to Gemini
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=question,
    config={
        "tools": [
            calculator,
            get_student_info,
            get_student_attendance
        ]
    }
)


# Final response
print(response.text)