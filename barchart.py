from matplotlib import pyplot as pyp

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
temp_day = [21,25,32,34,23,39,18]
temp_night = [15,25,18,14,23,11,19]

pyp.ylabel("Temperature in celcius")
pyp.xlabel("Days")

pyp.bar(days, temp_day, color="orange")
pyp.bar(days, temp_night, color = "skyblue")

pyp.legend(["Day", "Night"])
pyp.show()

print("Hello")