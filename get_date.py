
#https://stackoverflow.com/questions/50639415/attributeerror-module-datetime-has-no-attribute-now

from datetime import datetime

now = datetime.now()

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Time Now : ", dt_string)	

#Datetime to ISO8601 and viceversa

#my_date = datetime.now()
#print(my_date.isoformat())
#now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#print(now)
#timestamp = time.mktime(datetime.strptime(now, "%d/%m/%Y %H:%M:%S").timetuple())
#print(timestamp)
