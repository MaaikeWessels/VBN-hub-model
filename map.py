import folium

#Limburg

# Define the locations and route for the example
locations = [(51.36217528421053,6.176075521052632),
(51.19530418947368,6.002218352631578),
(51.248149275,5.722934775),
(51.54315875882353,5.9828779647058825),
(51.33550656981132,5.983188773584906), (50.88782098,6.025938236666667)]

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

locations = [(51.97521735625,5.939923375),(51.815058711111114,5.8197665333333335),(52.17163216692913,5.357915259842519),(51.98449632,6.5845669085714285),(51.963572752380955,5.654869423809524),(52.22193535,5.972595666666667),(51.9664771,6.266678661904762),(51.813632815,5.732678475),(52.36341049761904,5.650807726190476),(51.944211492307694,6.069801007692308),(52.10717397142857,5.180738505357143),(51.774813695999995,5.933115284),(52.086531750000006,5.249007957671885),(52.443114771428576,5.858075514285714),(51.803393675,5.252642829166667),(52.031376225,5.6501037),(52.02460150263158,5.563394555263158),(51.88304585,5.4224755125),(51.93308390833333,6.133909275),(52.0139582525,5.33125643),(52.12733340882353,5.426610682352941),(52.040155389999995,5.300026),(51.88836254705882,5.609285629411764),(52.02629983333333,5.158864606666667)]

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

locations = [(51.56437282222222,5.059543544444445),(51.436445409375,5.4972789875),(51.6957757125,5.28251189375),(51.48338795,4.29881841),(51.59703351935484,4.795428929032258),(51.327605475,3.828160175),(51.64861345714286,4.850118657142858),(51.505156925,3.8823007875),(51.596194002666664,5.322274313333334),(51.500476185714284,3.6407976142857144),(51.75771503650793,5.512279171428571),(51.564810740625,4.6210359125),(51.36189622222222,5.4589322),(51.6840006962963,5.069895648148148),(51.41416228333333,5.398399183333334),(51.588303695238096,4.911455728571428),(51.41465111111111,5.554379522222223),(51.81395038181818,4.962093718181818),(51.645451378260866,4.604022226086956),(51.464661552173915,5.770304382608695),(51.50005128,5.39938953),(51.616409,5.5369154),(51.7410398,5.8686697),(51.39287578333333,5.469990054166667),(51.64962248846154,3.927852826923077),(51.472470360869565,5.5374835434782606), (51.35573833076923,5.222441088461538),(51.64950902105263,5.018251592105264),(51.32379381532258,5.360708442741935)]

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
locations=[(53.1148793875,6.074993),(53.214808604761906,5.78266818095238),(53.17506018461538,5.444323615384615),(52.96874468,5.9113686119999995),(52.88287325384616,5.995202401923077),(53.33303578148148,5.9952906629629625),(53.02110056,5.6855006333333336),(53.00491702045454,6.065337347727272),(53.20227115769231,5.982181851923077),(53.28924928214286,5.985818482142857),(52.836901741803274,5.722666393442624),(52.98723555714286,6.299264069047619),(53.17330801730769,6.180136328846154),(52.966615680000004,5.79453734),(53.06120654583333,5.5344985125),(53.282675160869566,6.156579665217391),(52.89819605909091,5.572688245454545),(53.481990842553195,6.1722936)]
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
locations =[(52.01191714615384,4.288477415384615),(52.160196613636366,4.510807522727273),(51.9844499425,4.371936460000001),(52.16693605454546,4.710036527272727),(52.1841939,4.442593814285714),(51.99450199310345,4.199734303448277),(52.077555784,4.342316740999999),(52.194234490625,4.613536678125),(52.30083542685185,4.585890335185185),(52.24841174444444,4.439412605555555),(52.1452823,4.411407714285714),(52.25795370769231,4.553404384615384),(52.226952215384614,4.529113792307692),(52.12051546285714,4.44941766)]

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
