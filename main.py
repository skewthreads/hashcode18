

lines = 0
columns = 0
total_vehicles = 0
total_rides = 0
per_ride_bonus = 0
simulation_time = 0
ride_list = []
vehicle_list = []

class Ride:
    def __init__(self, id, start_x, start_y, end_x, end_y, earliest_start, latest_finish):
        self.id = id
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish

class Vehicle:
    def __init__(self, id):
        self.id = id
        self.current_x = 0
        self.current_y = 0
        self.assigned_rides = [] # index of assigned rides

def manhattan(start_x, start_y, end_x, end_y):
    return abs(start_x - end_x) + abs(start_y - end_y)

def main():
    global lines
    global columns
    global total_vehicles
    global total_rides
    global per_ride_bonus
    global simulation_time
    global ride_list
    global vehicle_list
    with open('inputs/a_example.in', 'r') as inputFile:
        header = next(inputFile).split()
        lines = int(header[0])
        columns = int(header[1])
        total_vehicles = int(header[2])
        total_rides = int(header[3])
        per_ride_bonus = int(header[4])
        simulation_time = int(header[5])
        for ride in range(total_rides):
            line = next(inputFile).split()
            ride_list.append(Ride(ride, line[0],line[1],line[2],line[3],line[4],line[5]))
    vehicle_list = [Vehicle(i) for i in range(total_vehicles)]

if __name__ == '__main__':
    main()
