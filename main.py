month_list = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

month_numbers = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12
}

days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # days in each month

def get_meal_swipes():
    return int(input("Meal swipes remaining: "))

def leap_year():
    leap = input("Year: ")
    while (not leap.isdigit()):
        print("Invalid year.")
        leap_= input("Year: ")

    if (int(leap) % 4 == 0):
        # it's a leap year
        days_list[1] = 29

def get_date(): 
    month = input("Enter month: ")

    done = False
    while (not done):
        if (month.isdigit()):
            if (int(month) < 1 or int(month) > 12):
                print("Invalid month.")
                month = input("Enter month: ")
            else: 
                month = month_list[int(month) - 1]
                done = True
        else:
            if (month.lower() not in month_list):
                print("Invalid month.")
                month = input("Enter month: ")
            else:
                done = True
                   

    while (month.lower() not in month_list):
        print("Invalid month.")
        month = input("Enter month: ")

    keep_going = True
    day = input("Enter day: ")

    while (keep_going):
        if (day.isdigit() and int(day) <= days_list[month_numbers[month.lower()] - 1] and int(day) > 0):
            keep_going = False
        else: 
            print("Invalid day. ")
            day = input("Enter day: ")
           
    return month, int(day)

def calc_days(month, day, final_month, final_day):
    # convert months into numbers to use as indexes later
    month_num = month_numbers[month.lower()]
    final_month_num = month_numbers[final_month.lower()]

    # start by setting days equal to the number of days left in the current month
    days = days_list[month_num - 1] - day

    for i in range(month_num, final_month_num - 1):
        days += days_list[i]

    days += final_day
    return days

def break_days(days, month):
    more_breaks = input("Are there any more breaks in the semester (y|n)? ").lower()
    if (not more_breaks == 'yes' and not more_breaks == 'y'):
        return days

    if (month_numbers[month.lower()] <= 5):
        remove = input("Remove (8) Spring Break days (y|n)? ").lower()
        if (remove == 'yes' or remove == 'y'):
            days -= 8
    else:
        remove = input("Remove (3) Fall Break days (y|n)? ").lower()
        if (remove == 'yes' or remove == 'y'):
            days -= 3
        remove = input("Remove (8) Thanksgiving Break days (y|n)? ").lower()
        if (remove == 'yes' or remove == 'y'):
            days -= 8
    return days

def farmers_market(meals):
    num = int(input("Estimated swipes to be used on Farmer's Market: "))
    meals -= num
    return meals


def print_results(month, day, final_month, final_day, total_days, meals):
    print('')
    print('Meals per day:', round(meals / total_days, 2))
    print('----------------------------')
    print('Today:', month, day)
    print('Last day:', final_month, final_day)
    print('Days remaning:', total_days)
    print('Meal swipes:', meals)
    print('')
    return

# main
meals = get_meal_swipes()

leap_year()

print("--- Starting Date ---")
month, day = get_date()
print("--- Ending Date ---")
final_month, final_day = get_date()

total_days = calc_days(month, day, final_month, final_day)
total_days = break_days(total_days, month)
meals = farmers_market(meals)

print_results(month, day, final_month, final_day, total_days, meals)