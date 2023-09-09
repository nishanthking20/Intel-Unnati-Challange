import pandas as pd
import folium


df = pd.read_csv('unnati_phase1_data(1).csv') 

coordinates_counts = df.groupby(['Lat', 'Long']).size().reset_index(name='count')

most_frequent_coordinates = coordinates_counts.loc[coordinates_counts['count'].idxmax()]

print(f"Most Frequent Coordinates (Latitude, Longitude): ({most_frequent_coordinates['Lat']}, {most_frequent_coordinates['Long']})")
print(f"Occurrence Count: {most_frequent_coordinates['count']} times")

N = 7  
top_coordinates = coordinates_counts.nlargest(N, 'count')

map_center = (most_frequent_coordinates['Lat'], most_frequent_coordinates['Long'])
m = folium.Map(location=map_center, zoom_start=10)

for index, row in top_coordinates.iterrows():
    lat, long, count = row['Lat'], row['Long'], row['count']
    folium.CircleMarker(
        location=(lat, long),
        radius=count / 50, 
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6,
        popup=f'Count: {count}',
    ).add_to(m)

m.save('map.html') 
m
