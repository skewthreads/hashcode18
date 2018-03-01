
current_time = 0
lines = 0
columns = 0
total_vehicles = 0
total_rides = 0
per_ride_bonus = 0
simulation_time = 0
ride_list = []
ride_dict = {}
# free_rides = []
vehicle_dict = {}
vehicle_list = []
free_vehicles = {}
all_rides_assigned = False
time_dict = {} # when its time to update a vehicle

class Ride:
    def __init__(self, id, start_x, start_y, end_x, end_y, earliest_start, latest_finish):
        self.id = id
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish
        self.distance = manhattan(self.start_x, self.start_y, self.end_x , self.end_y)
        self.free = True

class Vehicle:
    def __init__(self, id):
        self.id = id
        self.current_x = 0
        self.current_y = 0
        self.assigned_rides = [] # index of assigned rides
        self.free = True



def manhattan(start_x, start_y, end_x, end_y):
    return abs(start_x - end_x) + abs(start_y - end_y)

def score(vehicle, ride):
    score = 0
    distance_to_starting_point = manhattan(vehicle.current_x, vehicle.current_y, ride.start_x, ride.start_y)
    ride_distance = ride.distance
    starting_time = max(current_time + distance_to_starting_point, ride.earliest_start)
    # starting_time = current_time + distance_to_starting_point
    total_time = starting_time + ride_distance
    if starting_time <= ride.earliest_start:
        score += per_ride_bonus
    if total_time < ride.latest_finish:
        score += ride.distance
    # waiting_time = max(current_time - ride.earliest_start, 0)
    waiting_time = max(current_time + distance_to_starting_point - ride.earliest_start, 0)
    return score - waiting_time # maybe subtract distance_to_starting_point*some_factor


def main():
    global lines
    global columns
    global total_vehicles
    global total_rides
    global per_ride_bonus
    global simulation_time
    global ride_list
    global ride_dict
    global vehicle_list
    global vehicle_dict
    global free_vehicles
    global all_rides_assigned
    # with open('./inputs/a_example.in', 'r') as inputFile:
    # with open('./inputs/b_should_be_easy.in', 'r') as inputFile:
    # with open('./inputs/c_no_hurry.in', 'r') as inputFile:
    # with open('./inputs/d_metropolis.in', 'r') as inputFile:
    with open('./inputs/e_high_bonus.in', 'r') as inputFile:
        header = next(inputFile).split()
        lines = int(header[0])
        columns = int(header[1])
        total_vehicles = int(header[2])
        total_rides = int(header[3])
        per_ride_bonus = int(header[4])
        simulation_time = int(header[5])
        for ride in range(total_rides):
            line = next(inputFile).split()
            ride_dict[ride] = Ride(ride, int(line[0]),int(line[1]),int(line[2]),int(line[3]),int(line[4]),int(line[5]))
            ride_list.append(Ride(ride, int(line[0]),int(line[1]),int(line[2]),int(line[3]),int(line[4]),int(line[5])))

    vehicle_list = [Vehicle(v) for v in range(total_vehicles)]
    for v in range(total_vehicles):
        vehicle_dict[v] = Vehicle(v)
        free_vehicles[v] = True

    for current_time in range(simulation_time):
        if current_time in time_dict: # if its time to update a vehicle
            for vehicle in time_dict[current_time]:
                vehicle.free = True
                last_ride = vehicle.assigned_rides[-1]
                vehicle.current_x = last_ride.end_x
                vehicle.current_y = last_ride.end_y
        if all_rides_assigned:
            break
        for vehicle in vehicle_list:
            scores = []
            if vehicle.free == False:
                continue
            for ride in ride_list:
                if ride.free == False:
                    continue
                scores.append([ride, score(vehicle, ride)])
            if len(scores) == 0: # No free rides left
                all_rides_assigned = True
                break
            best_ride = max(scores, key=lambda x: x[1])[0]
            best_ride.free = False
            vehicle.assigned_rides.append(best_ride)
            vehicle.free = False
            distance_to_starting_point = manhattan(vehicle.current_x, vehicle.current_y, ride.start_x, ride.start_y)
            ending_time = current_time + distance_to_starting_point + ride.distance
            if ending_time in time_dict:
                time_dict[ending_time].append(vehicle)
            else:
                time_dict[ending_time] = [vehicle]

def output():
    # with open('outputs/a_example.out', 'w') as outputFile:
    # with open('outputs/b_example.out', 'w') as outputFile:
    # with open('outputs/c_example.out', 'w') as outputFile:
    # with open('outputs/d_example.out', 'w') as outputFile:
    with open('outputs/e_example.out', 'w') as outputFile:
        for vehicle in vehicle_list:
            rides = ''
            for ride in vehicle.assigned_rides:
                rides += ' ' + str(ride.id)
            outputFile.write(str(len(vehicle.assigned_rides)) + rides + '\n' )


if __name__ == '__main__':
    main()
    output()