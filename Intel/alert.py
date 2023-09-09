import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('unnati_phase1_data_revised.csv')
alert_counts = df['Alert'].value_counts()
plt.figure(figsize=(10, 5))
alert_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Alert Type')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('alert_type_counts.png')
plt.show()
