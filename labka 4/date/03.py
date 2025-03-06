from datetime import datetime

current = datetime.now()
now = current.replace(microsecond=0)
print(now)
#print(current.strftime("%Y-%B-%d %H:%M:%S"))