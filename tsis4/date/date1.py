from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date - timedelta(days=5)

print("Today's date:", current_date.strftime('%Y-%m-%d'))
print("Five days ago:", new_date.strftime('%Y-%m-%d'))
