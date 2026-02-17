"""
Author: Nyla Prince
Assignment: #1
"""

# Step b: Create 4 variables

gym_member = "Jordan Hayes" # string 
preferred_weight_kg = 42.5 # floating point number
highest_reps = 30 # int
membership_active = True # boolean

# Step c: Create a dictionary named workout_stats

# Dictionary: used to store data values
workout_stats = {
    "Jordan": (25, 60, 10),   # yoga, running, weightlifting
    "Morgan": (15, 35, 20),
    "Riley": (40, 25, 15)
}
# Step d: Calculate total workout minutes using a loop and add to dictionary

totals_to_add = {}
for friend, workouts in workout_stats.items():
    totals_to_add[friend + "_Total"] = sum(workouts)
workout_stats.update(totals_to_add)

# Step e: Create a 2D nested list called workout_list
#2D nested list stores data in table like format
workout_list = [list(workouts) for friend,
                workouts in workout_stats.items()
                if not friend.endswith("_Total")]

# Step f: Slice the workout_list

yoga_running = [row[:2] for row in workout_list]
print("Minutes fir yoga and running:", yoga_running)

weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Minutes for weightlifting:", weightlifting_last_two)

# Step g: Check if any friend's total >= 120

for friend, total in workout_stats.items():
    if friend.endswith("_Total") and total >= 120:
        friend_name = friend.replace("_Total", "")
        print(f"Great job staying active, {friend_name}!")

# Step h: User input to look up a friend

friend_name = input("Enter a friend's name: ")

if friend_name in workout_stats:
    workouts = workout_stats[friend_name]
    total_minutes = workout_stats.get(friend_name + "_Total", sum(workouts))
    
    print(f"Workout minutes for {friend_name}: Yoga = {workouts[0]}, Running = {workouts[1]}, Weightlifting = {workouts[2]}")
    print(f"Total workout minutes: {total_minutes}")
else:
    print(f"Friend {friend_name} not found in the records.")


# Step i: Friend with highest and lowest total workout minutes

totals = {friend.replace("_Total",""): minutes 
          for friend, minutes in workout_stats.items() 
          if friend.endswith("_Total")}

highest_friend = max(totals, key=totals.get)
highest_minutes = totals[highest_friend]

lowest_friend = min(totals, key=totals.get)
lowest_minutes = totals[lowest_friend]

print(f"Friend with highest total workout minutes: {highest_friend} ({highest_minutes} minutes)")
print(f"Friend with lowest total workout minutes: {lowest_friend} ({lowest_minutes} minutes)")


