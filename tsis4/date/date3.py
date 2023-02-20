from datetime import datetime

dt_with_microseconds = datetime.now()
dt_without_microseconds = dt_with_microseconds.replace(microsecond=0)

print("Original datetime:", dt_with_microseconds)
print("Datetime without microseconds:", dt_without_microseconds)
