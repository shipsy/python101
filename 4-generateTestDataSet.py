import random
from random import randint

#Select Random Data from list
random.choice([1,2,3,4,4,5])
#Select random value between integers
randint(1,5)

def generateData(minLat=28.301493, maxLat=28.543555, minLng=76.889479, maxLng=77.046961, numberOfPoints=30):
    req = []
    for i in range(numberOfPoints):
        factor = 10000.0
        scaledMinLat = int(minLat*factor)
        scaledMaxLat = int(maxLat*factor)
        scaledMinLng = int(minLng*factor)
        scaledMaxLng = int(maxLng*factor)
        obj = {
            'lat' : float(random.randint(scaledMinLat, scaledMaxLat)/factor),
            'lng': float(random.randint(scaledMinLng, scaledMaxLng)/factor)
        }
        req.append(obj)
    return req

def generateRandomDataSet(minLat=28.5951643,maxLat=28.5991643,minLng=77.328135,maxLng=77.338135,\
    numberOfCNs=100,numberOfVehicles=5):

    factor = 10000.0
    hubLat = float(randint(int(minLat*factor), int(maxLat*factor))/factor)
    hubLng = float(randint(int(minLng*factor), int(maxLng*factor))/factor)
    CNs = []
    for i in range(numberOfCNs):
        lat = float(randint(int(minLat*factor), int(maxLat*factor))/factor)
        lng = float(randint(int(minLng*factor), int(maxLng*factor))/factor)
        consignments_count = randint(1,3)
        weight = randint(1,10)
        volume = randint(1,10)
        fuelType = random.choice(['CNG', 'DIESEL'])
        cn = {
            'delivery_lat' : lat,
            'delivery_lng' : lng,
            'pickup_lat' : hubLat,
            'pickup_lng' : hubLng,
            'lat' : lat,
            'lng' : lng,
            'weight' : weight,
            'volume' : volume,
            'consignments_count' : consignments_count,
            'fuel_type' : fuelType,
            'type' : 'delivery',
            'tw_open' : 28800,
            'tw_close' : 72000,
            'service_time_per_demand' : randint(100,1000)
        }
        CNs.append(cn)
    Vehicles = []
    for i in range(numberOfVehicles):
        weightCapacity = randint(100,150)
        volumeCapacity = randint(100,150)
        consignment_capacity = randint(100,150)
        worker_id = i
        fuelFlag = randint(0,1)
        if fuelFlag == 0:
            fuelType ='CNG'
        else:
            fuelType = 'DIESEL'
        veh = {
            'weight' : weightCapacity,
            'volume' : volumeCapacity,
            'consignment_capacity' : consignment_capacity,
            'worker_id' : worker_id,
            'priority' : randint(1,3),
            'fuel_type' : fuelType,
            'cost': randint(1, 3),
            'perKmCost': randint(1, 3),
            'delivery_time_start': 28800,
            'delivery_time_end' : 72000
        }
        Vehicles.append(veh)
    start_depot = [[hubLat,hubLng]]
    end_depot = [[hubLat,hubLng]]
    service_time_per_demand = [randint(60,1000) for i in range(numberOfCNs)]
    constraint_type = [
        "weight","volume","number",'time'
    ]
    reqFinal = {
        'constraint_type' : constraint_type,
        'service_time_per_demand' : service_time_per_demand,
        'end_depot' : end_depot,
        'start_depot' : start_depot,
        'vehicles' : Vehicles,
        'task_list' : CNs
    }
    return reqFinal
