Employees=[
    ("Josef","Present"),
    ("Gauri","Absent"),
    ("Sagar","On Leave"),
    ("Janhavi","Present"),
    ("Madhura","Resigned"),
    ("Ravi","Absent")
]

for name, status in Employees:
    if status=="Absent":
        continue

    elif status=="On Leave":
        pass
        print(name, "is on Leave")

    elif status=="Resigned":
        print("Processing stopped because of ", name, "Has Resigned")
        break

    else:
        print(name, "is present")