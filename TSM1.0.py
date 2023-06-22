import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming
import pandas as pd
import csv

#distance matrix Limburg

distance_matrix = np.array([
    [0, 78, 55, 61, 102 ,81],
    [79, 0, 28, 46, 27, 18],
    [54	,29, 0 ,22	,52	,25],
    [60,47 ,22 ,0 ,59 ,24],
    [102,28	,51,58 ,0, 37],
    [81	,21, 38, 24, 38, 0]
])
#Arnhem
file = open("C:/Users/maaik/OneDrive/Documents/Econometrics year 3/thesis/python/test arnhem for python.csv", "r")
data = list(csv.reader(file, delimiter=";"))
file.close()
distance_matrix2 = np.array(data).astype(np.int)

#Brabant-Zeeland
file = open("C:/Users/maaik/OneDrive/Documents/Econometrics year 3/thesis/python/test brabant zeeland for python.csv", "r")
data = list(csv.reader(file, delimiter=";"))
file.close()
distance_matrix1 = np.array(data).astype(np.int)

#Friesland
file = open("C:/Users/maaik/OneDrive/Documents/Econometrics year 3/thesis/python/test friesland for python.csv", "r")
data = list(csv.reader(file, delimiter=";"))
file.close()
distance_matrix3 = np.array(data).astype(np.int)

#Haaglanden
file = open("C:/Users/maaik/OneDrive/Documents/Econometrics year 3/thesis/python/test haaglanden for python.csv", "r")
data = list(csv.reader(file, delimiter=";"))
file.close()
distance_matrix4 = np.array(data).astype(np.int)

#Rotterdam
file = open("C:/Users/maaik/OneDrive/Documents/Econometrics year 3/thesis/python/test rotterdam for python.csv", "r")
data = list(csv.reader(file, delimiter=";"))
file.close()
distance_matrix6 = np.array(data).astype(np.int)

#Salland-Twente
file = open("C:/Users/maaik/OneDrive/Documents/Econometrics year 3/thesis/python/test salland twente for python.csv", "r")
data = list(csv.reader(file, delimiter=";"))
file.close()
distance_matrix7 = np.array(data).astype(np.int)

#Noord Holland
file = open("C:/Users/maaik/OneDrive/Documents/Econometrics year 3/thesis/python/test noord holland for python.csv", "r")
data = list(csv.reader(file, delimiter=";"))
file.close()
distance_matrix8 = np.array(data).astype(np.int)

Limburg_distances =distance_matrix
Arnhem_distances = distance_matrix2
Brabant_Zeeland_distances = distance_matrix1
Friesland_distances=distance_matrix3
Haaglanden_distances=distance_matrix4
Rotterdam_distances=distance_matrix6
Salland_Twente_distances=distance_matrix7
Noord_Holland_distances=distance_matrix8


# Starting points for each region
region_starting_points = {
    'Arnhem': np.array([0, 1, 2]),
    'Limburg': np.array([0, 1]),
    'Brabant_Zeeland': np.array([0, 1, 2,3]),
    'Haaglanden': np.array([0,1,2]),
    'Rotterdam': np.array([0,1,2,3,4]),
    'Salland_Twente': np.array([0,1]),
    'Friesland': np.array([0,1]),
    'Noord_Holland': np.array([0,1,2])
}
region_clusters = {}
region_points = {
    'Arnhem': ['Arnhem','Nijmegen','Amersfoort','Oost-Achterhoek','Neder-Veluwe','Apeldoorn','Doetinchem','Wijchen & Beuningen','Harderwijk','Zevenaar en Rijnwaarden','De Bilt', 'Groesbeek e.o.', 'Zeist', 'Elburg-Oldebroek','Bommelerwaard (Zaltbommel)', 'Ede', 'Veenendaal','Rivierenland (Tiel)','Montferland','Kromme Rijn (Wijk bij Duurstede)','Leusden', 'Utrechtse Heuvelrug','Druten','Houten'],
    'Limburg': ['Limburg-Zuid (Landgraaf)', 'Venlo','Midden-Limburg (Roermond)','Weert','Limburg-Noord (Venray)','Peel en Maas'],
    'Brabant_Zeeland': ['Tilburg','Eindhoven', 'Den Bosch','Goed Ontmoet (Bergen op Zoom)','Breda','Zeeuws-Vlaanderen (Terneuzen)','De Baronie (Oosterhout)','Bevelanden','Boxtel','Walcheren','Oss','Etten-Leur','De Boodschappenmand (Valkenswaard)','Waalwijk "De Rijglaars"','Veldhoven','Gilze-Rijen','Geldrop-Mierlo','Altena','Moerdijk','Deurne','Best','Veghel','Land van Cuijk','Aalst-Waalre','Schouwen Duiveland','Nuenen','Bladel','Loon op Zand','Bergeijk'],
    'Haaglanden': ['Haaglanden','Leiden','Delft','Alphen a/d Rijn','Katwijk','Westland','Voorburg / Leidschendam','Alkemade/Jacobswoude/ KBEO','Hillegom','Noordwijk/ Noorwijkerhout','Wassenaar','Lisse','Teylingen','Voorschoten'],
    'Rotterdam' : ['Rotterdam','Utrecht','Dordrecht','Spijkenisse','Gouda','Maassluis','Hellevoetsluis','Vlaardingen','Hoeksche Waard (Oud-Beijerland)','Zwijndrecht','Capelle a/d Ijssel','Schiedam','Gorinchem','Papendrecht','Stichtse Vecht (Maarssen)','Woerden','De Ronde Venen','Leerdam', 'Sliedrecht','Ijssel en Lek','Giessenlanden-Zederik','Alblasserdam','Barendrecht','Brielle','Hardinxveld-Giessendam','Nieuwegein-Ijsselstein','Oudewater','Montfoort / Linschoten'],
    'Salland_Twente':  ['Deventer','Enschede', 'Midden Twente (Hengelo)','Almelo','Raalte','Oost Twente (Oldenzaal)','Zutphen','Hellendoorn','Vaassen / Epe / Heerde','West-Twente (Rijssen Holten)','Losser'],
    'Friesland' : ['Smallingerland (Drachten)','Leeuwarden','Harlingen/Franeker (Helpende Hand)','Heerenveen','Weststellingwerf','Dongeradeel/Dokkum','Sneek-Wymbritseradiel','Opsterland','Tietjerksteradeel ','Dantumadiel','Lemsterland (Lemmer)','Ooststellingwerf','Achtkarspelen', 'Utjouwer, De (Joure)','Bolsward','Kollumerland','Zuidwest Friesland','Schiermonnikoog'],
    'Noord_Holland': ['Amsterdam','Gooi en omstreken','Alkmaar','Almere','Haarlemmermeer','Lelystad (De Korenaar)','Zaanstreek','Haarlem','Purmerend','West-Friesland','Amstelveen','IJmond Noord','Kop van Noord (Anna Paulowna)','Den Helder','Naarden/Bussum/Hilversumse Meent','Langedijk','Uithoorn-De Kwakel','Diemen','Velsen','Zeewolde (de Kostmand)','Aalsmeer','Texel']
}
# Loop through each region
for region, distances in zip(['Arnhem', 'Limburg', 'Brabant_Zeeland', 'Haaglanden', 'Rotterdam', 'Salland_Twente', 'Friesland', 'Noord_Holland'], [Arnhem_distances, Limburg_distances, Brabant_Zeeland_distances, Haaglanden_distances, Rotterdam_distances, Salland_Twente_distances, Friesland_distances, Noord_Holland_distances]):

    labels=[]
    # Loop through each row of the distance matrix
    for i in range(distances.shape[0]):

        # Find the index of the closest starting point
        closest_starting_point = region_starting_points[region][np.argmin(distances[i][region_starting_points[region]])]

        # Add the label to the list
        labels.append(closest_starting_point)

    # Create clusters based on labels
    clusters = [[] for _ in range(len(set(labels)))]
    cluster_names = [[] for _ in range(len(set(labels)))]

    for i, label in enumerate(labels):
        clusters[label].append(i)
        cluster_names[label].append(f"{region_points[region][i]}")
    k = 0
    for j in clusters:
        globals()[f"{region}_{k}"] = j
        k += 1
    region_points[region]
    globals()[f"{region}_names"] = cluster_names
    globals()[f"distance_matrices_{region}"] = []

    for i in range(len(clusters)):
        clusterall = []
        for j, c in enumerate(clusters):
            if j != i:
                clusterall.extend(c)
        distance_matrix = np.delete(globals()[f"{region}_distances"], clusterall, 1)
        distance_matrix = np.delete(distance_matrix, clusterall, 0)
        globals()[f"distance_matrices_{region}"].append(distance_matrix)
        #print(distance_matrix)
regions = {
    'Limburg': {
        'distances': Limburg_distances,
        'distance_matrices': distance_matrices_Limburg,
        'names': Limburg_names
    },
    'Arnhem': {
        'distances': Arnhem_distances,
        'distance_matrices': distance_matrices_Arnhem,
        'names': Arnhem_names
    },
    'Brabant_Zeeland': {
        'distances': Brabant_Zeeland_distances,
        'distance_matrices': distance_matrices_Brabant_Zeeland,
        'names': Brabant_Zeeland_names
        },
    'Haaglanden': {
        'distances': Haaglanden_distances,
        'distance_matrices': distance_matrices_Haaglanden,
        'names': Haaglanden_names
        },
    'Rotterdam': {
        'distances': Rotterdam_distances,
        'distance_matrices': distance_matrices_Rotterdam,
        'names': Rotterdam_names
        },
    'Salland_Twente': {
        'distances': Salland_Twente_distances,
        'distance_matrices': distance_matrices_Salland_Twente,
        'names': Salland_Twente_names
        },
    'Friesland': {
        'distances': Friesland_distances,
        'distance_matrices': distance_matrices_Friesland,
        'names': Friesland_names
        },
    'Noord_Holland': {
        'distances': Noord_Holland_distances,
        'distance_matrices': distance_matrices_Noord_Holland,
        'names': Noord_Holland_names
        }
}
# distances and routes
for region, data in regions.items():
    distances = data['distances']
    distance_matrices = data['distance_matrices']
    names = data['names']
    
    print("Total distance of {} from all FB to RDCs and back:".format(region), distances[:, 0].sum() + distances[0].sum())
    
    hubs = region_starting_points[region]
    hub_distances = [distances[0, i] + distances[i, 0] for i in range(1, len(hubs))]
    hub_fb_distances = [distance_matrices[i][:, 0].sum() + distance_matrices[i][0].sum() for i in range(len(hubs))]
    total_distance = sum(hub_distances) + sum(hub_fb_distances)
    print("Total distance of {} with HUB(s) {}:".format(region, ', '.join(map(str, hubs))), total_distance)
    
    permutations = []
    distances = []
    for i in range(len(hubs)):
        permutation, distance = solve_tsp_dynamic_programming(distance_matrices[i])
        permutations.append(permutation)
        distances.append(distance)
    
    total_distance = sum(distances) + sum(hub_distances)
    print("Total distance of {} with HUB(s) {} with route:".format(region, ', '.join(map(str, hubs))), total_distance)
    
    for i in range(len(hubs)):
        permutation_cluster_names = [names[i][j] for j in permutations[i]]
        print(permutation_cluster_names)
