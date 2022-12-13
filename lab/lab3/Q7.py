def bmi_risk(bmi, age):
    if (bmi < 22) and (age < 45):
        return "Low"
    elif (bmi >= 22) and (age >=45):
        return "High"
    else:
        return "Medium"