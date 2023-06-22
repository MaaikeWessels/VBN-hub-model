import folium

#Limburg

# Define the locations and route for the example
locations = [(#coordinates of food banks, for security reasons not shown]

route = [5,0, 5, 3,5, 4, 5, 2,5, 1,5]

# Create a map centered on the first location in the route
map_center = locations[0]
route_map = folium.Map(location=map_center, zoom_start=6)

# Add a marker for each location in the route
for i, location in enumerate(locations):
    marker = folium.Marker(location=location, popup=f"Location {i}")
    marker.add_to(route_map)

# Create a list of line segments connecting the locations in the route
route_segments = []
for i in range(len(route) - 1):
    start_location = locations[route[i]]
    end_location = locations[route[i+1]]
    segment = (start_location, end_location)
    route_segments.append(segment)

# Add a polyline to the map representing the route
route_line = folium.PolyLine(locations=route_segments, weight=8, color='blue')
route_line.add_to(route_map)

# Display the map in a web browser
route_map.save('limburg_nohub_route_map.html')

#Arnhem

locations = [#coordinates of food banks, for security reasons not shown]
labels = [0, 1, 2, 0, 0, 0, 0, 1, 2, 0, 2, 1, 2, 2, 1, 0, 0, 1, 0, 2, 2, 2, 1, 2]

# Create empty lists for each label

unique_labels = set(labels)
label_lists = {label: [] for label in unique_labels}

for i, label in enumerate(labels):
    label_lists[label].append(locations[i])

# Assign location lists to dynamically named variables
for label, locations_list in label_lists.items():
    variable_name = f"locations{label}"
    globals()[variable_name] = locations_list

# Define the locations and routes
route=[0,1,0,2]
route0 = [0, 1, 4, 8, 5, 3, 2, 7, 6,0]
route1 = [0, 1, 3, 4, 5, 2,0]
route2=[0, 7, 5, 8, 2, 3, 6, 1, 4,0]

# Create a folium map centered on the first location
map_center = locations1[0]
map_zoom = 4
m = folium.Map(location=map_center, zoom_start=map_zoom)

# Add a PolyLine for the first route
route_points = [locations[i] for i in route]
route_line = folium.PolyLine(locations=route_points, color='black')
m.add_child(route_line)

route0_points = [locations0[i] for i in route0]
route0_line = folium.PolyLine(locations=route0_points, color='purple')
m.add_child(route0_line)

route1_points = [locations1[i] for i in route1]
route1_line = folium.PolyLine(locations=route1_points, color='red')
m.add_child(route1_line)

# Add a PolyLine for the second route
route2_points = [locations2[i] for i in route2]
route2_line = folium.PolyLine(locations=route2_points, color='blue')
m.add_child(route2_line)

# Display the map
m.save("Arnhem.html")

#map route with opening days considered
# Define the locations and routes
route=[0,1,0,2]
route0 = [0,1,4,8,5,6,7,2,0,3,0]
route1 = [0, 1, 3, 4, 5, 0, 2]
route2=[0, 7, 5, 8, 2, 3, 6, 1, 4,0]

# Create a folium map centered on the first location
map_center = locations1[0]
map_zoom = 4
m = folium.Map(location=map_center, zoom_start=map_zoom)

# Add a PolyLine for the first route
route_points = [locations[i] for i in route]
route_line = folium.PolyLine(locations=route_points, color='black')
m.add_child(route_line)

route0_points = [locations0[i] for i in route0]
route0_line = folium.PolyLine(locations=route0_points, color='purple')
m.add_child(route0_line)

route1_points = [locations1[i] for i in route1]
route1_line = folium.PolyLine(locations=route1_points, color='red')
m.add_child(route1_line)

# Add a PolyLine for the second route
route2_points = [locations2[i] for i in route2]
route2_line = folium.PolyLine(locations=route2_points, color='blue')
m.add_child(route2_line)

# Display the map
m.save("Arnhem_opening_days.html")

#map FB to HUBs only

# Define the locations and routes
route0 = [0, 1, 0, 4, 0,8, 0,5, 0,3, 0,2, 0,7, 0,6,0]
route1 = [0, 1, 0,3, 0,4, 0,5, 0,2, 0]
route2=[0, 7, 0,5, 0, 8, 0,2, 0,3,0, 6, 0,1, 0,4,0]

# Create a folium map centered on the first location
map_center = locations1[0]
map_zoom = 4
m = folium.Map(location=map_center, zoom_start=map_zoom)

# Add a PolyLine for the first route
route_points = [locations[i] for i in route]
route_line = folium.PolyLine(locations=route_points, color='black')
m.add_child(route_line)

route0_points = [locations0[i] for i in route0]
route0_line = folium.PolyLine(locations=route0_points, color='purple')
m.add_child(route0_line)

route1_points = [locations1[i] for i in route1]
route1_line = folium.PolyLine(locations=route1_points, color='red')
m.add_child(route1_line)

# Add a PolyLine for the second route
route2_points = [locations2[i] for i in route2]
route2_line = folium.PolyLine(locations=route2_points, color='blue')
m.add_child(route2_line)

# Display the map
m.save("Arnhem_ONLY HUB.html")

#map FB to RDC only

#Brabant-Zeeland

locations = [#coordinates of food banks, for security reasons not shown]
labels = [0, 1, 2, 3, 0, 3, 0, 3, 2, 3, 2, 3, 1, 0, 1, 0, 1, 2, 3, 1, 1, 1, 2, 1, 3, 1, 1, 0, 1]

unique_labels = set(labels)
label_lists = {label: [] for label in unique_labels}

for i, label in enumerate(labels):
    label_lists[label].append(locations[i])

# Assign location lists to dynamically named variables
for label, locations_list in label_lists.items():
    variable_name = f"locations{label}"
    globals()[variable_name] = locations_list     

# Define the locations and routes
route=[0,1,0,2,0,3]
route0 = [0, 4, 1, 2, 5, 3,0]
route1 = [0, 8, 4, 6, 5, 2, 9, 10, 1, 7, 3,0]
route2=[0, 1, 4, 2, 3,0]
route3=[0, 3, 1, 2, 6, 5, 4,0]

# Create a folium map centered on the first location
map_center = locations1[0]
map_zoom = 4
m = folium.Map(location=map_center, zoom_start=map_zoom)

# Add a PolyLine for the first route
route_points = [locations[i] for i in route]
route_line = folium.PolyLine(locations=route_points, color='black')
m.add_child(route_line)

route0_points = [locations0[i] for i in route0]
route0_line = folium.PolyLine(locations=route0_points, color='purple')
m.add_child(route0_line)

route1_points = [locations1[i] for i in route1]
route1_line = folium.PolyLine(locations=route1_points, color='red')
m.add_child(route1_line)

route2_points = [locations2[i] for i in route2]
route2_line = folium.PolyLine(locations=route2_points, color='blue')
m.add_child(route2_line)

route3_points = [locations3[i] for i in route3]
route3_line = folium.PolyLine(locations=route3_points, color='orange')
m.add_child(route3_line)

# Display the map
m.save("Brabant-Zeeland.html")

#map FB to HUBs only

# Define the locations and routes
route=[0,1,0,2,0,3]
route0 = [0, 4, 0, 1, 0, 2, 0,5, 0,3,0]
route1 = [0, 8, 0,4, 0,6, 0,5, 0,2, 0,9, 0,10, 0,1, 0,7, 0,3,0]
route2=[0, 1, 0, 4,0,  2, 0, 3,0]
route3=[0, 3, 0,1, 0,2, 0,6, 0,5, 0,4,0]

# Create a folium map centered on the first location
map_center = locations1[0]
map_zoom = 4
m = folium.Map(location=map_center, zoom_start=map_zoom)

# Add a PolyLine for the first route
route_points = [locations[i] for i in route]
route_line = folium.PolyLine(locations=route_points, color='black')
m.add_child(route_line)

route0_points = [locations0[i] for i in route0]
route0_line = folium.PolyLine(locations=route0_points, color='purple')
m.add_child(route0_line)

route1_points = [locations1[i] for i in route1]
route1_line = folium.PolyLine(locations=route1_points, color='red')
m.add_child(route1_line)

route2_points = [locations2[i] for i in route2]
route2_line = folium.PolyLine(locations=route2_points, color='blue')
m.add_child(route2_line)

route3_points = [locations3[i] for i in route3]
route3_line = folium.PolyLine(locations=route3_points, color='orange')
m.add_child(route3_line)

# Display the map
m.save("Brabant-Zeeland_ONLY HUB.html")

#Friesland
locations=[#coordinates of food banks, for security reasons not shown]
labels = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1,0,0,1]

# Create empty lists for each label

unique_labels = set(labels)
label_lists = {label: [] for label in unique_labels}

for i, label in enumerate(labels):
    label_lists[label].append(locations[i])

# Assign location lists to dynamically named variables
for label, locations_list in label_lists.items():
    variable_name = f"locations{label}"
    globals()[variable_name] = locations_list

# Define the locations and routes
route=[0,1]
route0 = [0, 3, 8, 10, 5, 1, 2, 6, 7, 9, 4,0]
route1 = [0, 6, 2, 4, 3, 5, 1,0]

# Create a folium map centered on the first location
map_center = locations1[0]
map_zoom = 4
m = folium.Map(location=map_center, zoom_start=map_zoom)

# Add a PolyLine for the first route
route_points = [locations[i] for i in route]
route_line = folium.PolyLine(locations=route_points, color='black')
m.add_child(route_line)

route0_points = [locations0[i] for i in route0]
route0_line = folium.PolyLine(locations=route0_points, color='purple')
m.add_child(route0_line)

route1_points = [locations1[i] for i in route1]
route1_line = folium.PolyLine(locations=route1_points, color='red')
m.add_child(route1_line)

# Display the map
m.save("Friesland.html")

#map FB to HUBs only

# Define the locations and routes
route0 = [0, 3, 0, 8, 0,10, 0,5, 0,1, 0,2, 0,6,0, 7, 0,9, 0,4]
route1 = [0, 0,6, 0,2, 0,4, 0,3, 0,5, 0,1]

# Create a folium map centered on the first location
map_center = locations1[0]
map_zoom = 4
m = folium.Map(location=map_center, zoom_start=map_zoom)

# Add a PolyLine for the first route
route_points = [locations[i] for i in route]
route_line = folium.PolyLine(locations=route_points, color='black')
m.add_child(route_line)

route0_points = [locations0[i] for i in route0]
route0_line = folium.PolyLine(locations=route0_points, color='purple')
m.add_child(route0_line)

route1_points = [locations1[i] for i in route1]
route1_line = folium.PolyLine(locations=route1_points, color='red')
m.add_child(route1_line)

# Display the map
m.save("Friesland_ONLY HUB.html")

#Haaglanden 
locations =[#coordinates of food banks, for security reasons not shown]
labels = [0, 1, 2, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1]

# Create empty lists for each label

unique_labels = set(labels)
label_lists = {label: [] for label in unique_labels}

for i, label in enumerate(labels):
    label_lists[label].append(locations[i])

# Assign location lists to dynamically named variables
for label, locations_list in label_lists.items():
    variable_name = f"locations{label}"
    globals()[variable_name] = locations_list

# Define the locations and routes
route=[0,1,0,2]
route0 = [0, 1, 2,0]
route1 = [0, 3, 1, 4, 7, 8, 5, 2, 6, 9,0]
route2=[0]

# Create a folium map centered on the first location
map_center = locations1[0]
map_zoom = 4
m = folium.Map(location=map_center, zoom_start=map_zoom)

# Add a PolyLine for the first route
route_points = [locations[i] for i in route]
route_line = folium.PolyLine(locations=route_points, color='black')
m.add_child(route_line)

route0_points = [locations0[i] for i in route0]
route0_line = folium.PolyLine(locations=route0_points, color='purple')
m.add_child(route0_line)

route1_points = [locations1[i] for i in route1]
route1_line = folium.PolyLine(locations=route1_points, color='red')
m.add_child(route1_line)

# Add a PolyLine for the second route
route2_points = [locations2[i] for i in route2]
route2_line = folium.PolyLine(locations=route2_points, color='blue')
m.add_child(route2_line)

# Display the map
m.save("Haaglanden.html")

#map FB to HUBs only

# Define the locations and routes
route0 = [0, 1, 0, 2]
route1 = [0, 3, 0,1, 0,4, 0,7, 0,8, 0,5, 0,2, 0,6, 0,9]
route2=[0]

# Create a folium map centered on the first location
map_center = locations1[0]
map_zoom = 4
m = folium.Map(location=map_center, zoom_start=map_zoom)

# Add a PolyLine for the first route
route_points = [locations[i] for i in route]
route_line = folium.PolyLine(locations=route_points, color='black')
m.add_child(route_line)

route0_points = [locations0[i] for i in route0]
route0_line = folium.PolyLine(locations=route0_points, color='purple')
m.add_child(route0_line)

route1_points = [locations1[i] for i in route1]
route1_line = folium.PolyLine(locations=route1_points, color='red')
m.add_child(route1_line)

# Add a PolyLine for the second route
route2_points = [locations2[i] for i in route2]
route2_line = folium.PolyLine(locations=route2_points, color='blue')
m.add_child(route2_line)

# Display the map
m.save("Haaglanden_ONLY HUB.html")
