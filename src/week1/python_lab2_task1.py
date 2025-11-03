"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# Create the datasets
temperatures = [15.2, 16.5, 14.8, 17.0, 16.1, 15.9, 16.7]

city_population = {
    "Riga": 632614,
    "Daugavpils": 82064,
    "Liepaja": 68590,
    "Jelgava": 54694,
    "Jurmala": 49500,
}

# Compute aggregates
average_temperature = sum(temperatures) / len(temperatures)
largest_city = max(city_population, key=city_population.get) # type: ignore
largest_population = city_population[largest_city]
smallest_city = min(city_population, key=city_population.get) # type: ignore
smallest_population = city_population[smallest_city]
total_population = sum(city_population.values())

# Print results
print(f"Temperatures (week): {temperatures}")
print(f"Average temperature: {average_temperature:.2f} °C\n")
print(f"Total population (all cities): {total_population:,}")
print(f"Largest city: {largest_city} - {largest_population:,}")
print(f"Smallest city: {smallest_city} - {smallest_population:,}")
