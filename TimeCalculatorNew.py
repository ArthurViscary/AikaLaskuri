
def add_time(start, duration, startDay:str = False):

    startAmPm = str(start.split(" ")[1])
    startHours = int(start.split(":")[0])
    startMinutes = int(start.split(":")[1][0:2])

    durationHours = int(duration.split(":")[0])
    durationMinutes = int(duration.split(":")[1][0:2])

    #loppuminuuttien laskenta
    endMinutes = 0
    if startMinutes + durationMinutes < 60:
        endMinutes = startMinutes + durationMinutes
    else:
        endMinutes = (startMinutes + durationMinutes) % 60
        durationHours += 1
    if endMinutes < 10:
        endMinutes = str("0") + str(endMinutes)

    #lopputuntien laskenta
    endHours = 0
    if startHours + durationHours <= 12:
        endHours = startHours + durationHours
    else:
        endHours = (startHours + durationHours) % 12
        if endHours == 0:
            endHours = 12

    #kuinka monta am/pm flippiä
    amPmDict = {"AM" : "PM", "PM" : "AM"}
    amPmFlips = int((startHours + durationHours) / 12)
    finalAmPm = amPmDict[startAmPm] if amPmFlips % 2 == 1 else startAmPm
    #am_and_pm_flip[am_or_pm] if amount_of_am_pm_flips % 2 == 1 else am_or_pm

    #kuluneiden päivien selvitys
    daysPassed = int(durationHours / 24)
    if (startAmPm == "PM" and startHours + (durationHours % 12) >= 12):
        daysPassed += 1

    #viikonpäivän laskufunktio (ei saanut importata päivämäärää, itertoolsia)
    def day_flipper(daysPassed: int, startDay: str) -> str:
        returnDay = ""
        for i in range(daysPassed):
            if startDay.lower() == "monday":
                returnDay = "Tuesday"
            elif startDay.lower() == "tuesday":
                returnDay = "Wednesday"
            elif startDay.lower() == "wednesday":
                returnDay = "Thursday"
            elif startDay.lower() == "thursday":
                returnDay = "Friday"
            elif startDay.lower() == "friday":
                returnDay = "Saturday"
            elif startDay.lower() == "saturday":
                returnDay = "Sunday"
            elif startDay.lower() == "sunday":
                returnDay = "Monday"
            startDay = returnDay
        return returnDay
    

    if startDay and daysPassed > 1:
        return str(endHours) + ":" + str(endMinutes) + " " + finalAmPm + ", " + day_flipper(daysPassed, startDay) + f" ({daysPassed} days later)"
    elif startDay and daysPassed == 0:
        return str(endHours) + ":" + str(endMinutes) + " " + finalAmPm + ", " + startDay
    elif startDay and daysPassed == 1:
        return str(endHours) + ":" + str(endMinutes) + " " + finalAmPm + ", " + day_flipper(daysPassed, startDay) + " (next day)"
    elif daysPassed == 1:
        return str(endHours) + ":" + str(endMinutes) + " " + finalAmPm + " (next day)"
    elif daysPassed > 1:
        return str(endHours) + ":" + str(endMinutes) + " " + finalAmPm + f" ({daysPassed} days later)"
    else:
        return str(endHours) + ":" + str(endMinutes) + " " + finalAmPm
'''
print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
'''


#print(add_time("2:59 AM", "24:00"))
print(add_time("2:59 AM", "24:00", "saturDay"))