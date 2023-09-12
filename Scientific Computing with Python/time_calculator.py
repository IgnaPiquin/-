def add_time(start, duration, day=""):
    #dividing the time into the hours and minutes and the time set
    if len(start)==7:
        start_time = start[:4]
        time_set = start[5:7]
    else:
        start_time = start[:5]
        time_set = start[6:8]
    
    # dividing the durations into 2 variables, hours and minutes
    duration_hours, duration_minutes = duration.split(":")
    # dividing the start time into 2 variables, hours and minutes
    start_hours, start_minutes = start_time.split(":")

    # setting th hours depending on if the starting time was AM or PM
    if time_set == "PM":
        start_hours = int(start_hours) + 12
    else:
        start_hours = int(start_hours)

    # Working out the new minutes
    minutes = int(start_minutes) + int(duration_minutes)
    new_minutes = minutes%60
    if new_minutes < 10:
        new_minutes= "0" + str(new_minutes)
    else: 
        new_minutes = str(new_minutes)
    
    # Working out the new hours
    hours = int(minutes/60)

    hours = hours + start_hours + int(duration_hours)

    new_hours = hours%24
    hours = hours - new_hours

    # Working out the new days
    days = int(hours/24)

    # setting if the new time is AM or PM
    if new_hours > 12:
        new_hours = new_hours -12
        new_time_set = "PM"
    elif new_hours == 12:
        new_time_set = "PM"
    elif new_hours == 0:
        new_hours = 12
        new_time_set = "AM"
    else:
        new_time_set = "AM"
    
    
    
    #setting the new time
    new_time = str(new_hours) + ":" + new_minutes + " " + new_time_set
    if day != "":
        day = day.lower()
        day = day.capitalize()
        if days >= 1:
            weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            for i in range(len(weekdays)):
                if day == weekdays[i]:
                    new_day = days + i
                    break
            while new_day > 6:
                new_day= new_day - 7
            new_time = new_time + ", " + weekdays[new_day]
        else:
            new_time = new_time + ", " + day
        
    if days == 1:
        new_time = new_time + " (next day)"
    elif days > 1:
        new_time = new_time + f" ({str(days)} days later)"


    return new_time

print(add_time("11:59 PM", "24:05"))