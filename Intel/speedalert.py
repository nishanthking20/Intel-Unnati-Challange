import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('unnati_phase1_data_revised.csv')

df['Speed'] = df['Speed'].apply(lambda x: int(x) if str(x).isdigit() else None)

df.dropna(subset=['Speed'], inplace=True)

speed_counts = df['Speed'].value_counts()

plt.figure(figsize=(10, 6))
speed_counts.plot(kind='bar')
plt.xlabel('Speed')
plt.ylabel('Number of Accidents')
plt.title('Number of Accidents by Speed')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

alerts_with_speed_58 = df[df['Speed'] == 58]['Alert'].value_counts()

print("Alert counts with Speed 58:")
print(alerts_with_speed_58)
