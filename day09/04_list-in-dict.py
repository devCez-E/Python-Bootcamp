travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, total_visits, cities):
    new_log = {}
    new_log["country"] = country
    new_log["visits"] = total_visits
    new_log["cities"] = cities
    
    travel_log.append(new_log)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])