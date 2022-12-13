def should_shutdown(battery_level, time_on):
    if time_on < 60 and battery_level < 4.7:
        return True
    elif time_on >=60 and battery_level < 4.8:
        return True
    else:
        return False