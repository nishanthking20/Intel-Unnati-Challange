import pandas as pd
import matplotlib.pyplot as plt
csv_file = 'unnati_phase1_data_revised.csv'
df = pd.read_csv(csv_file)
latitude = df['Lat']  
longitude = df['Long']
speed = df['Speed']
plt.figure(figsize=(10, 6))
scatter = plt.scatter(longitude, latitude, c=speed, cmap='viridis', marker='o', edgecolor='k', alpha=0.7)
cbar = plt.colorbar(scatter)
cbar.set_label('Speed (km/h)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Scatter Plot of Speed vs. Location')
plt.grid(True)
plt.show()
