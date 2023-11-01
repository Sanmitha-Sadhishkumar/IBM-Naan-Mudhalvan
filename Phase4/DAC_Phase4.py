import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("/content/modified_transportation_data.csv")

# Calculate average SO2, NO2, and RSPM/PM10 levels across different monitoring stations
average_levels = data.groupby('Location of Monitoring Station')[['SO2', 'NO2', 'RSPM/PM10']].mean()

# Create a bar plot to visualize average SO2 levels by monitoring station
sns.barplot(x=average_levels.index, y=average_levels['SO2'])
plt.xlabel('Monitoring Station')
plt.ylabel('Average SO2 Level')
plt.title('Average SO2 Levels by Monitoring Station')
plt.xticks(rotation=90)
plt.show()

# Create a bar plot to visualize average NO2 levels by monitoring station
sns.barplot(x=average_levels.index, y=average_levels['NO2'])
plt.xlabel('Monitoring Station')
plt.ylabel('Average NO2 Level')
plt.title('Average NO2 Levels by Monitoring Station')
plt.xticks(rotation=90)
plt.show()

# Create a bar plot to visualize average RSPM/PM10 levels by monitoring station
sns.barplot(x=average_levels.index, y=average_levels['RSPM/PM10'])
plt.xlabel('Monitoring Station')
plt.ylabel('Average RSPM/PM10 Level')
plt.title('Average RSPM/PM10 Levels by Monitoring Station')
plt.xticks(rotation=90)
plt.show()

# Calculate average levels by city/town/village/area
average_city_levels = data.groupby('City/Town/Village/Area')[['SO2', 'NO2', 'RSPM/PM10']].mean()

# Create a bar plot to visualize average SO2 levels by city/town/village/area
sns.barplot(x=average_city_levels.index, y=average_city_levels['SO2'])
plt.xlabel('City/Town/Village/Area')
plt.ylabel('Average SO2 Level')
plt.title('Average SO2 Levels by City/Town/Village/Area')
plt.xticks(rotation=90)
plt.show()

# Time-series plot for SO2 levels
sns.lineplot(x="Sampling Date", y="SO2", data=data)
plt.xlabel('Sampling Date')
plt.ylabel('SO2 Level')
plt.title('SO2 Level Over Time')
plt.xticks(rotation=45)
plt.show()
# Create similar plots for NO2 and RSPM/PM10.

# Heatmap for SO2 levels by monitoring station
sns.heatmap(data.pivot_table(values='SO2', index='Location of Monitoring Station', columns='Sampling Date'), cmap='YlGnBu')
plt.xlabel('Sampling Date')
plt.ylabel('Monitoring Station')
plt.title('SO2 Levels by Monitoring Station Over Time')
plt.xticks(rotation=45)
plt.show()
# Create similar heatmaps for NO2 and RSPM/PM10.

# Sort by average SO2 levels
sorted_city_so2 = average_city_levels.sort_values(by='SO2', ascending=False)
print("Areas with highest average SO2 levels:")
print(sorted_city_so2.head(10))

# Create similar analyses for NO2 and RSPM/PM10.
correlation_matrix = data[['SO2', 'NO2', 'RSPM/PM10']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Between Pollutants')
plt.show()

sns.lineplot(x="Sampling Date", y="NO2", data=data)
plt.xlabel('Sampling Date')
plt.ylabel('NO2 Level')
plt.title('NO2 Level Over Time')
plt.xticks(rotation=45)
plt.show()

sns.heatmap(data.pivot_table(values='NO2', index='Location of Monitoring Station', columns='Sampling Date'), cmap='YlGnBu')
plt.xlabel('Sampling Date')
plt.ylabel('Monitoring Station')
plt.title('NO2 Levels by Monitoring Station Over Time')
plt.xticks(rotation=45)
plt.show()

# Sort by average NO2 levels
sorted_city_no2 = average_city_levels.sort_values(by='NO2', ascending=False)
print("Areas with highest average NO2 levels:")
print(sorted_city_no2.head(10))

correlation_matrix = data[['NO2', 'SO2', 'RSPM/PM10']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Between NO2 and Other Pollutants')
plt.show()

