from re import A


cities_list =[
 "Oakland",
 "Atlanta",
 "New York City",
 "Seattle", 
 "Memphis", 
 "Miami",
 "Boston",
 "Los Angeles",
 "Denver",
 "New Orleans"]

cities_list[5]
print(cities_list[5])
print(cities_list[8])
print(cities_list[3])

#creating my 10 biggest States

Biggest_States = [
 "Alaska",
 "Texas",
 "California",
 "Montana",
 "Nuevo Mexico",
 "Arizona",
 "Nevada",
 "Colorado",
 "Oregon",
 "Wyoming"]
print(Biggest_States [1])
print(Biggest_States [2])  
print(Biggest_States [6])

four_cities = cities_list[0 : 4]
print(four_cities)

four_States = Biggest_States [0 : 4]
print(four_States)


# performing changes 

cities_list[1] = "San Francisco"
cities_list[3] = "Brooklyn"
cities_list[8] = "Hollywood"
cities_list[6] = "Tampa"
print(cities_list)

cities_list.append ("Oakland")
cities_list.extend (["New York City", "Los Angeles"])
cities_list.insert (6, "Miami")
print(cities_list)

#remove items 

del cities_list [2]
cities_list.pop(7)
cities_list.remove("Miami")
print(cities_list [2])
print(cities_list.pop(7))
print(cities_list.remove) 