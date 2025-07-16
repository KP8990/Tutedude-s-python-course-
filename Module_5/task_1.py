try:
    a={
    "Alice":85,
    "Maan":96,
    "Utsav":86,
    "Dev":40,
    }
    p=str(input("Enter Student's Name: "))
    print(f"{p}'s marks:{a[p]}")

except KeyError:
    print("Student not found")