from helpers.test import expect, runAllTests

'''
Design a parking lot system
- The parking lot has one level with multiple rows of spots.
- The parking lot can park motorcycles, cars, and buses.
- The parking lot has motorcycle spots, compact spots, and large spots.
- A motorcycle can park in any spot.
- A car can park in either a single compact spot or a single large spot.
- A bus can park in five large spots that are consecutive and within the same row. It cannot park in small spots.
- Someone should be able to find where their vehicle is parked via an ID
- You need to display open spots in the garage on a board outside at all times

Class Spot
    Variables
        - size: 1 | 2 | 3
        - vehicleId?: string

Class ParkingGarage
    Variables
        - garage: Spot[][]
        - locations: dict(vehicleId, number[][])
    Functions
        private create(n)
            - should create a garage where there is a an equal number of spots of the three given sizes
        public park(vehicleId): number[]
        public getLocation(vehicleId): number[]
        public openSpots(): number[][]

Class Vehicle
    Variables
        size: 1 | 2 | 3
        id: string

Class Motorcycle extends Vehicle
    Variables
        size: 1
        id: string

Class Car extends Vehicle
    Variables
        size: 2
        id: string

Class Truck extends Vehicle
    Variables
        size: 3
        id: string
'''
class VehicleDirectory:
    directory = dict()

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(VehicleDirectory, self).__new__(self)
        return self.instance

    def add(self, vehicle):
        if vehicle.id in self.directory:
            raise ValueError("cannot add a vehicle that has already been added")
        self.directory[vehicle.id] = vehicle

    def clear(self):
        self.directory.clear()


class Vehicle:
    def __init__(self, id):
        self.id = id
        self.size = None
        self.location = None
        VehicleDirectory().add(self)

    def assignLocation(self, row, column):
        self.location = [row, column]
        return self.location


class Motorcycle(Vehicle):
    def __init__(self, id):
        super().__init__(id)
        self.size = 1

class Car(Vehicle):
    def __init__(self, id):
        super().__init__(id)
        self.size = 2

class Truck(Vehicle):
    def __init__(self, id):
        super().__init__(id)
        self.size = 3

class Spot:
    def __init__(self, size, row, col):
        self.size = size
        self.vehicleId = None
        self.location = [row, col]

    def assign(self, vehicle):
        if not self.isEmpty():
            return False
        self.vehicleId = vehicle.id
        vehicle.assignLocation(*self.location)
        return True

    def remove(self):
        if self.isEmpty():
            return False
        self.vehicleId = None
        return True

    def isEmpty(self):
        return not bool(self.vehicleId)

class ParkingGarage:
    def __init__(self, size):
        self.size = size
        self.garage = self.__create()
        self.__vehicles = VehicleDirectory().directory

    def __create(self):
        levels = [0] * self.size
        last = 3
        nextSizes = [2, 3, 1]
        leftToRight = True
        row = 1
        for r in reversed(range(self.size)):
            columns = range(self.size) if leftToRight else reversed(range(self.size))
            level = [0] * self.size
            col = 1
            for c in columns:
                nextSize = nextSizes[last - 1]
                level[c] = Spot(nextSize, row, col)
                last = nextSize
                col += 1
            levels[r] = level
            leftToRight = not leftToRight
            row += 1
        return levels

    def printSizes(self):
        results = []
        for i in range(self.size):
            level = []
            for spot in self.garage[i]:
                level.append(spot.size)
            results.append(level)
        return results

    def park(self, vehicleId):
        if vehicleId not in self.__vehicles:
            return []
        leftToRight = True
        for x in reversed(range(self.size)):
            columns = range(self.size) if leftToRight else reversed(range(self.size))
            for y in columns:
                spot = self.garage[x][y]
                vehicle = self.__vehicles[vehicleId]
                if spot.isEmpty() and spot.size >= vehicle.size:
                    spot.assign(vehicle)
                    return vehicle.location
            leftToRight = not leftToRight
        return []

    def getLocation(self, vehicleId):
        if vehicleId not in self.__vehicles:
            return []
        vehicleLocation = self.__vehicles[vehicleId].location
        return vehicleLocation if vehicleLocation else []

    def openSpots(self):
        leftToRight = True
        results = []
        for x in reversed(range(self.size)):
            columns = range(self.size) if leftToRight else reversed(range(self.size))
            for y in columns:
                spot = self.garage[x][y]
                if spot.isEmpty():
                    results.append(spot.location)
            leftToRight = not leftToRight
        return results


def test1():
    truck = Truck("t1")
    expect("truck should have correct variables", ["t1", 3], [truck.id, truck.size])


def test2():
    expect("parking garage of size 2 is generated correctly", [[1, 3], [1, 2]], ParkingGarage(2).printSizes())
    expect("parking garage should of size 3 is generated correctly", [[1, 3, 2, 1], [3, 1, 2, 3], [2, 1, 3 ,2], [1, 2, 3, 1]], ParkingGarage(4).printSizes())

def test3():
    VehicleDirectory().clear()
    pg = ParkingGarage(2)
    pg.park(Truck("t1").id)
    pg.park(Truck("t2").id)
    pg.park(Motorcycle("m1").id)
    pg.park(Car("c1").id)
    expect("park and getLocation methods work correctly", [[2, 1], [], [1, 1], [1, 2]] , [pg.getLocation("t1"), pg.getLocation("t2"), pg.getLocation("m1"), pg.getLocation("c1")])

def test4():
    VehicleDirectory().clear()
    pg = ParkingGarage(3)
    pg.park(Truck("t1").id)
    pg.park(Truck("t2").id)
    pg.park(Motorcycle("m1").id)
    pg.park(Car("c1").id)
    expect("openSpots method works correctly", [[2, 1], [2, 2], [3, 1], [3, 2], [3, 3]] , pg.openSpots())

runAllTests([test1, test2, test3, test4])