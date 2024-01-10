#know the number of weeks left for you on the earth
#assuming we all are die at 90 years
#then you minus your current age with the year you are dieing (90)
#then multiply the remaining years with the weeks in a year (52)
age = "18"
years = 90 - int(age)
weeks = years * 52
#f-string
print(f"You have {weeks} weeks left.")