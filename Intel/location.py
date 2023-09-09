import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('unnati_phase1_data_revised.csv') 
coordinates_counts = df.groupby(['Lat', 'Long']).size().reset_index(name='count')
most_frequent_coordinates = coordinates_counts.loc[coordinates_counts['count'].idxmax()]
print(f"Most Frequent Coordinates (Latitude, Longitude): ({most_frequent_coordinates['Lat']}, {most_frequent_coordinates['Long']})")
print(f"Occurrence Count: {most_frequent_coordinates['count']} times")
top_coordinates = coordinates_counts.nlargest(7, 'count')  
print(top_coordinates)
plt.figure(figsize=(12, 6))
plt.scatter(top_coordinates['Long'], top_coordinates['Lat'], s=top_coordinates['count'], alpha=0.5)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title(f'Top {7} Most Frequent Coordinates')
plt.grid(True)
plt.show()
