#importing os package since we are working with os operations
import os

#importing time package to provide pause 
import time


#Device to be in sleep state and to be connected to Machine where script is run
#Main function defined 
def main():
    i = 0 
    # while loop to perfroming unlock , once from sleep to lock screen and once for lock screen to unlock device
    while i < 2:
	# performing the adb event
	os.system("adb shell input keyevent 82")
	# Program put to sleep for two seconds
	time.sleep(2)
	i = i + 1
	

# Main method to be called
if __name__ == "__main__":
    main()
	