from datetime import datetime, timedelta

today = datetime.now()
yest = today - timedelta(days=1)
tommo = today + timedelta(days=1)
print("yesterday:", yest)
print("today:", today)
print("tommorow:", tommo)