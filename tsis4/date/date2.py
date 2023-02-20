from datetime import datetime, timedelta

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday's date:", yesterday.strftime('%d.%m.%Y'))
print("Today's date:", today.strftime('%d.%m.%Y'))
print("Tomorrow's date:", tomorrow.strftime('%d.%m.%Y'))
