import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('unnati_phase1_data_revised.csv')  

vehicle_counts = df['Vehicle'].value_counts()

plt.figure(figsize=(12, 6))
vehicle_counts.plot(kind='bar', color='purple')
plt.xlabel('Vehicle Number')
plt.ylabel('Count')
plt.title('Occurrences of Each Vehicle Number')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
vehicle_data = df[df['vehicle no'] == vehicle_counts.index[0]]

