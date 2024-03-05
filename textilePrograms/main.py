from pick_goal import move_to_pose
from place_cotton import move_to_place_cotton

try:
    move_to_pose(-0.55)
    next = input("Press enter to continue to place_cotton.py")
    move_to_place_cotton()
    print("Program finished")

except Exception as e:
    print(f"An error occurred: {e}")