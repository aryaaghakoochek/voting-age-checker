import datetime

#variables that arent changing
#todays date
TD = datetime.datetime.today()
#elcetion date
ELECTION_DATE = datetime.date(2007, 2, 27)
#number of days in 18 years
DAYS_IN_18_YEARS = 18 * 365

number_of_birthdays = round(float(input("please enter the number of voters (between 1-100):")))
#only allows up to 100 birthdays
while float(round(number_of_birthdays)) > 100 or float(round(number_of_birthdays)) < 1:
    number_of_birthdays = float(round(input("please enter the number of voters  (between 1-100):")))
#asks for birthdays same nimber of times as satted earleir
list_birthdays = []

N = int(number_of_birthdays)

for i in range(N):
    year = int(input("please enter your birthday year"))
#allows only dates between 1900 to current date
    while year < 1900 or year > TD.year:
        year = int(input("please enter your birthday year"))

    month = int(input("please enter your birthday month"))
#checks that month is not bigger than 12
    while month < 1 or month > 12:
        month = int(input("please enter your birthday month"))

    day = int(input("please enter your birthday day"))

    while day < 1 or day > 31:
        day = int(input("please enter your birthday day"))

#checks the number of days in each month
    if month == 1:
        while (day <1 or day >31):
             day = int(input("please enter birthday day"))

    if month == 2:
         while (day < 1 or day > 29):
             day = int(input("please enter birthday day"))

    if month == 3:
         while (day <1 or day >31):
             day = int(input("please enter birthday day"))

    if month == 4:
         while (day <1 or day >30):
             day = int(input("please enter birthday day"))

    if month == 5:
         while (day <1 or day >31):
             day = int(input("please enter birthday day"))

    if month == 6:
         while (day <1 or day >30):
             day = int(input("please enter birthday day"))

    if month == 7:
         while (day <1 or day >31):
             day = int(input("please enter birthday day"))

    if month == 8:
         while (day <1 or day >31):
             day = int(input("please enter birthday day"))

    if month == 9:
         while (day <1 or day >30):
             day = int(input("please enter birthday day"))

    if month == 10:
         while (day <1 or day >31):
             day = int(input("please enter birthday day"))

    if month == 11:
         while (day <1 or day >30):
             day = int(input("please enter birthday day"))

    if month == 12:
         while (day <1 or day >31):
             day = int(input("please enter birthday day"))

#puts input into a list in yyyy-mm-dd format
    birthday_date = datetime.date(year, month, day)
    list_birthdays.append(birthday_date)

#checks if the age is above 18
for birthday in list_birthdays:
    if (ELECTION_DATE - birthday).days >= DAYS_IN_18_YEARS:
        print(birthday)
        print("YES, you may vote")
    else:
        print(birthday)
        print("NO, you are not old enough to vote")
