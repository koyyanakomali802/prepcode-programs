departments = {"CSE", "CSM", "ECE", "EEE", "MECH" }
department = input("enter the department name:")
if department in departments:
    print("allowed")
else:
    print("not allowed")