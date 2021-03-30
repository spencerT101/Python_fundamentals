stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
#2. Add "Glasgow Queen St" to the start of the list
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
#4. Print out the index position of "Linlithgow"
#5. Remove "Livingston" from the list using its name
#6. Delete "Cumbernauld" from the list by index
#7. Print the number of stops there are in the list
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop


Waverly = stops.append("Edinburgh Waverly")
print(stops)

Glasgow_queen = stops.insert(0,"Glasgow Queen st")
print(stops)

Polmont = stops.insert(4, "Polmont")
print(stops)

Linlithgow = stops.index("Linlithgow")
print(Linlithgow)

Livingston = stops.remove("Livingston")
print(stops)

del stops[2]
print(stops)

num_stops = len(stops)
print (num_stops)

alpha_order = sorted(stops)
print(alpha_order)

rever_order = sorted(stops, reverse = True)
print(rever_order)

for stop in stops:
    print(stop)


    


# print(Linlithgow)
# #print(alpha_order)
# print(num_stops)

