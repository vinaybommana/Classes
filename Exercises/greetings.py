try:
    hour = int(input("please enter the current hour: ")) # (0-23)
except ValueError:
    print("please enter a valid hour")
    exit()

#  - Use "Good morning" for 5-11,
#  - "Good afternoon" for 12-17,
#  - "Good evening" for 18-21, and
#  - "Good night" otherwise.

if hour > 23:
    print("please enter a valid hour")
elif (hour >= 5 and hour <= 11):
    print(f"Good Morning, its {hour} o'clock")
elif (hour >=12 and hour <= 17): # 13 - 1 o' clock
    print(f"Good Afternoon, its {hour} o'clock")
elif (hour >= 18 and hour <= 21):
    print(f"Good Evening, its {hour} o'clock")
else:
    print(f"Good night, its {hour} o'clock")