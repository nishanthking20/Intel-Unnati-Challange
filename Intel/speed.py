import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('unnati_phase1_data_revised.csv')


average_speed = df['Speed'].mean()
maximum_speed = df['Speed'].max()
minimum_speed = df['Speed'].min()

print(f"Average Speed: {average_speed} km/h")
print(f"Maximum Speed: {maximum_speed} km/h")
print(f"Minimum Speed: {minimum_speed} km/h")

alert_speed = df.groupby('Alert')['Speed'].mean()
plt.figure(figsize=(12, 6))
alert_speed.plot(kind='bar', color='skyblue')
plt.xlabel('Alert Type')
plt.ylabel('Average Speed (km/h)')
plt.title('Average Speed by Alert Type')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
