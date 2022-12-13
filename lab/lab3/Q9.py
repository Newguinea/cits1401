def record_check(age, gender, location):
    if age > 18 and gender == "M" and location in ["Perth", "Sydney"]:
        print("Found him!")
    else:
        print("Did not find him.")