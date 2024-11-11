# This code will take an start tiem during the day, a duration you want to add and an optional starting day of the week and tell you the resulting day and time after adding that time specified in the duration

def add_time(start, duration, initial_day=0):

    week=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    final_day_string='' #this won't appear unless we specified the day of the week we're starting in

    # in the first time of the code we transform the time to a 24 hour format

    count=0

    for _ in start:
        if _==':':
            separator_index=count
        elif _==' ':
            space_index=count
        
        count+=1

    hours=int(start[0:separator_index])
    minutes=int(start[separator_index+1:space_index])
    AMorPM=start[space_index+1:]


    if AMorPM=='PM':
        hours=hours+12 # turning time into 24 hour format

    # now we find how many hours we are adding using the same method

    count=0

    for _ in duration:
        if _==':':
            separator_index=count
        elif _==' ':
            space_index=count
        
        count+=1

    hours_added=int(duration[0:separator_index])
    minutes_added=int(duration[separator_index+1:])

    new_hour=hours+hours_added
    new_minutes=minutes+minutes_added

    if int(new_minutes)>=60:
        new_hour=new_hour+new_minutes//60
        new_minutes=new_minutes%60
    
    

    # we'll check if a day has passed

    day=new_hour//24
    new_hour=new_hour%24

    # we prepare the string depending on the days that have passed
    if day==0:
        day_string=''
    elif day==1:
        day_string=' (next day)'
    else:
        day_string=' ('+str(day)+' days later)'

    if initial_day!=0:
        count=0
        for days in week:
            if days==initial_day.lower():
                result_weekday=week[((count+day)%7)].capitalize()
            count+=1
        final_day_string=', '+result_weekday
        


    # now that we have everything we need let's transform to the desired format

    if new_hour<12:
        if new_hour==0:
            new_hour=12
        AMorPM=' AM'
    elif new_hour==12:
        AMorPM=' PM'
    else: 
        new_hour=new_hour-12
        AMorPM=' PM'


    if new_minutes<10: #a final check to make sure it's in the correct format
        new_minutes='0'+str(new_minutes)

    

    new_time=str(new_hour) + ':' + str(new_minutes) + AMorPM + final_day_string + day_string

    return new_time

add_time('3:00 PM', '12:00', 'tuesday')
