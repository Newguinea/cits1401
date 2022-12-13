def locate_person(age_list, name_list, age, name):
    for i in range(len(age_list)):
        if age_list[i] == age and name_list[i] == name:
            break
    return i