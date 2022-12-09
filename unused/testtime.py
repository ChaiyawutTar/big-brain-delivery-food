from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S")
print(current_time)

open_time = 3600*8
close_time = 3600*20
l = current_time.split(":")
s = int(l[0])*60*60 + int(l[1])*60 + int(l[2])
if open_time <= s <= close_time:
    print("open")
else:
    print("closed")





        