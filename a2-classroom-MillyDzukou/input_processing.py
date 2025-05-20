# input_processing.py
# MILLY VITAL DZUKOU TASSE, ENSF 692 Spring 2025
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# Definition of the sensor class
class Sensor:

    # Constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self, trafficLight = 'green', pedStat='yes', vehiStat='yes'):
        self.trafficLight = trafficLight
        self.pedStat = pedStat
        self.vehiStat = vehiStat

    # Replace these comments with your function commenting
    def update_status(self): # You may decide how to implement the arguments for this function
        while True:
            print("Are changes are detected for the visual input?")
            updateChange = input("Select 1 for light, 2 for pedestrian, 3 for vehicule or 0 to end the program: ")
            # print("This is update change ", updateChange)
            if updateChange == '1':
                # print("I am the first update change")
                while True:
                    self.trafficLight = input("What change has been identified?")
                    if (self.trafficLight == "green" or self.trafficLight == "red" or self.trafficLight =="yellow"):
                        break
                break

            elif updateChange =='2':
                # print("I am the second update change")
                while True:
                    self.pedStat = input("What change has been identified?")
                    if (self.pedStat == "yes" or self.pedstat =="no"):
                        break
                break

            elif updateChange == '3':
                while True:
                    self.vehiStat = input("What change has been identified?\n")
                    if (self.vehiStat == "yes" or self.vehiStat =="no"):
                        break
                break
            
            elif updateChange == '0':
                print("End of the program")
                break
            else:
                self.update_status()
                print("This is the else")
            print("This is update change 2", updateChange)




# This function check the status of the sensor
# It has 3 conditional statements representing the 3 different states
def print_message(sensor):
    if (sensor.trafficLight == "red" and sensor.pedStat == "yes" and sensor.vehiStat == "yes" ):
        print("STOP")
    if (sensor.trafficLight == "green" and sensor.pedStat == "no" and sensor.vehiStat == "no" ):
        print("Proceed")
    if (sensor.trafficLight == "yellow" and sensor.pedStat == "no" and sensor.vehiStat == "no" ):
        print("Caution")
    print("\n")
    
    print("Light = {0}, Pedestrian = {1}, Vehicule = {2}.".format(sensor.trafficLight, sensor.pedStat, sensor.vehiStat))




# Main function call, will call all the function in the required order.
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sensor1 = Sensor()
    print_message(sensor1)
    sensor1.update_status()
    print_message(sensor1)





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

