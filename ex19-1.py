def myfunc(journey_distance, journey_time, fuel_usage):
    print("How far did you travel in miles?")
    journey_distance = float(input(">"))
    print("How long did you travel for in hours?")
    journey_time = float(input(">"))
    print("How much fuel did your journey use in litres?")
    fuel_usage = float(input(">"))

    average_speed = journey_distance/journey_time
    print(f"Your average speed was {average_speed} miles per hour")
    average_fuel = journey_distance/fuel_usage
    print(f"Your average fuel consumption was {average_fuel} miles per litre")

myfunc(0,0,0)
