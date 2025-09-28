#Water intake tracker

#=====================
#     Pseudocode
#=====================
#1. Set recomended glasses of water per day.
#2. Initialize total glasses and number of entries.
#3. Display program instructions to user.
#4. Loop until user types 'done':
#       a. Get user input.
#       b. If input is 'done', break loop
#       c. Try to convert input to intergers:
#           i. If valid number, add to total and count entry.
#           ii. If invalid entry(text, negative), catch error and display message
#       d.In all cases, display "Entry processed. Using finally.
#5. After loop ends:
#       a. If valid entries exist, calculate statistics
#           -Average intake
#           -Percentage of recommended intake
#           -display statistics
#       b. Otherwise, display "No valid data entered."
#6. End with a health reminder message. 



def main():
    recommended = 8  
    total = 0
    entries = 0

    print("Daily Water Intake Tracker")
    print("Enter the number of glasses of water you drank today.")
    print("Type 'done' when finished.\n")

    while True:
        user_input = input("Glasses of water: ")

        if user_input.lower() == "done":
            break

        try:
            glasses = int(user_input)
            if glasses < 0:
                raise ValueError("Negative number not allowed.")
            total += glasses
            entries += 1
        except ValueError as e:
            print(f"Invalid entry: {e}")
        finally:
            print("Entry processed.\n")

    if entries > 0:
        avg = total / entries
        percent = (avg / recommended) * 100
        print("\nWater Intake Statistics ")
        print(f"Total glasses logged: {total}")
        print(f"Days recorded: {entries}")
        print(f"Average per day: {avg:.2f}")
        print(f"Percentage of daily goal: {percent:.1f}%")
    else:
        print("\nNo valid data entered.")

    print("\n Remember: Staying hydrated is good for your health!")
    

if __name__ == "__main__":
    main()
