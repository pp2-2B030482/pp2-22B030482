from datetime import datetime

date1 = datetime(2022, 1, 15, 0, 0, 0) #any times
date2 = datetime(2022, 2, 1, 0, 0, 0) 

difference_seconds = (date2 - date1).total_seconds()
print("Difference in seconds:", difference_seconds)
