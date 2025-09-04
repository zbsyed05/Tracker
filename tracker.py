# Zainab Syed
# Program 9 - Tracker
# COP2500C
# April 10, 2024

def load_goals(goals):
    print("Set your goals for the weeks!")

    # Gets 3 goals and their targets and adds them to the goals dictionary
    for i in range(3):
        category = str(input("Enter a category for your goal:\n"))
        goals[category] = int(input("Enter your target for "+category+":\n"))
    return 
                            
def load_data():
    # creates an empty dictionary to store daily
    daily = {}
    
    print("Enter your data with the category and measurment.")
    print("Type \'done\' when done for today.")

    # ask for the category
    category = str(input("Enter category:\n"))

    # while category is not done, it will keep asking for the categories and values
    while( category != "done" ):
        value = int(input("Enter value:\n"))

        # if a value for a category has already been put in daily, it will ask the user to either
        # add to that value or replace the previous value.
        if category in daily:
            print("You have a value for", category, ".")
            add = int(input("Do you want to (1) Add to "+category+",or (2) Replace "+category+"?\n"))
            if(add == 1):
                daily[category] += value
            elif(add == 2):
                daily[category] = value
                
        # if the value isn't in daily, it will just add to the daily dictionary      
        elif value not in daily:
            daily[category] = value
            
        category = str(input("Enter category:\n"))
    return daily

def compare_goals(goals, daily):
    # compares each key for goals and daily, if the category for daily isn't there it will return 0
    for key in goals:
        if(key not in daily):
            return 0
        # if the value of daily is less than the value of goals, it will return 0
        elif(daily[key] < goals[key]):
            return 0
    # if the value of daily is greater than the value of goals, it will return 1
    return 1     

def main():
    # creates empty dictionary for the goals
    goals = { }
    total_met_goals = 0
    
    # Calls load_goals using the paramaters from goals.
    load_goals(goals)

    # Gets the data from everyday of the week.
    print("\nIt's MONDAY!")
    daily = load_data()
    total_met_goals += compare_goals(goals, daily)

    print("\nIt's TUESDAY!")
    daily = load_data()
    total_met_goals += compare_goals(goals, daily)

    print("\nIt's WEDNESDAY!")
    daily = load_data()
    total_met_goals += compare_goals(goals, daily)

    print("\nIt's THURSDAY!")
    daily = load_data()
    total_met_goals += compare_goals(goals, daily)

    print("\nIt's FRIDAY - Happy Friday!")
    daily = load_data()
    total_met_goals += compare_goals(goals, daily)

    print("\nIt's SATURDAY!")
    daily = load_data()
    total_met_goals += compare_goals(goals, daily)

    print("\nIt's SUNDAY!")
    daily = load_data()
    total_met_goals += compare_goals(goals, daily)

    # gets toal amount of goals reached
    print("You hit you goals", total_met_goals, "times this week!")
    
# starts program
main()
