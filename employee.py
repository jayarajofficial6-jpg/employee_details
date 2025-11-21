# employee.py

def get_employee_info(name, emp_id, department, salary):
    """
    Returns a formatted string containing employee details.
    """
    return (
        f"Employee Name: {name},"
        f"Employee ID: {emp_id},"
        f"Department: {department},"
        f"Salary: {salary:.2f}"
    )

# Example usage (optional)
if __name__== "_main_":
    print(get_employee_info("John Doe", "E101", "IT", 55000))
