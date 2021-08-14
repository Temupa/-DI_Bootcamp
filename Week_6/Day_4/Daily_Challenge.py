import calendar
from datetime import datetime

# get birthdate and separate year
birthday = input("Enter your birthday (mm/dd/yyyy): ")
x = birthday.split('/')
year = x[2]

currentyear = datetime.now().year
age = currentyear-int(year)
candles=age%10

# if age is multiple of 10, convert 0 to 10 to display 10 candles
# candles=int(candles)
if candles==0:
    candles=10

# calculate the number of dashes surrounding the candles
dash = int((12-candles)/2)

# print cake
cake=[" "*4+"_"*dash +"i"*candles +"_"*dash,"   |:H:a:p:p:y:|"," __|"+"_"*11+"|__", "|"+"^"*17+"|","|:B:i:r:t:h:d:a:y:|","|"+" "*17+"|","~"*19]
print("\n".join(cake[:]))

# if leap year print a second cake
if calendar.isleap(int(year)):
    print('\n'.join(cake[:]))
    print("An extra cake for the leap year.")