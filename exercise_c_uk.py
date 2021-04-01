united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.

capital_city = united_kingdom[2]["capital"] = "Cardiff"

wales_capital = capital_city

print(wales_capital)

# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
united_kingdom.append(
  {
    "name": "Northern Ireland",
    "population": 1885000,
    "capital": "Belfast"
  })

print(united_kingdom)

# 3. Use a loop to print the names of all the countries in the UK.

# REMEMBER KEEP IT SIMPLE!

for countries in united_kingdom:
    print(countries["name"])

# 4. Use a loop to find the total population of the UK.

total_population = 0 #create variable to populate value

for population_value in united_kingdom:
  total_population += population_value["population"] # reference string parameter at end of loop.

print(total_population)

