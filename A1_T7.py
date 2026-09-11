print("Calculate fuel consumtion.")
Feed = input("Enter travel distance(kilometers): ")
Distance = int(Feed)
Feed = input("Enter fuel usage(liters): ")
FuelUsage = int(Feed)

concumption_per_km = float(FuelUsage) / float(Distance)
Consumption = int(concumption_per_km * 100)

print("Fuel consumption is {Consumption} l per 100 km".format(Consumption=Consumption))
