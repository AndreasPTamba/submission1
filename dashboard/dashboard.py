import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit app title
st.title('Air Quality Data Dashboard: Visualizing Pollution Trends and Environmental Factors')

# Attempt to read the CSV file
try:
    df = pd.read_csv('dashboard/main_data.csv')
except FileNotFoundError:
    st.error("The file 'main_data.csv' was not found. Please ensure it is in the correct directory.")
    # Optionally stop further execution
    st.stop()

# Create a pivot table for monthly averages
monthly_avg = df.pivot_table(index='month', 
                              values=['PM2.5', 'PM10', 'SO2', 'NO2'], 
                              aggfunc='mean')

# Display Monthly Average Air Quality Levels Visualization
st.header('Monthly Average Air Quality Levels: A Comprehensive View of Pollutant Concentration Trends')
fig, ax = plt.subplots(figsize=(12, 6))
monthly_avg.plot(kind='bar', ax=ax)
ax.set_title('Monthly Average Air Quality Levels')
ax.set_xlabel('Month')
ax.set_ylabel('Average Concentration (µg/m³)')
ax.grid(True)
st.pyplot(fig)

# Create a pivot table for yearly averages
yearly_avg = df.pivot_table(index='year', 
                             values=['PM2.5', 'PM10', 'TEMP'], 
                             aggfunc='mean')

# Display Yearly Average PM2.5, PM10, and Temperature Visualization
st.header('Yearly Trends in PM2.5, PM10, and Temperature: Long-term Averages Over the Years')
fig, ax = plt.subplots(figsize=(12, 6))
yearly_avg.plot(ax=ax)
ax.set_title('Yearly Average PM2.5, PM10, and Temperature')
ax.set_xlabel('Year')
ax.set_ylabel('Average Concentration / Temperature')
ax.grid(True)
st.pyplot(fig)

# Correlation matrix
correlation_matrix = df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP']].corr()

# Display Correlation Between Air Quality Pollutants and Temperature Visualization
st.header('Correlation Between Air Quality Pollutants and Temperature: Understanding Relationships Among Variables')
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
ax.set_title('Correlation Between Air Quality Pollutants and Temperature')
st.pyplot(fig)

# Create a pivot table for pollutants by station
station_avg = df.pivot_table(index='station', 
                              values=['PM2.5', 'PM10', 'SO2', 'NO2'], 
                              aggfunc='mean')

# Display Average Pollutant Levels by Station Visualization
st.header('Average Pollutant Levels by Station: Comparing Air Quality Across Different Locations')
fig, ax = plt.subplots(figsize=(12, 6))
station_avg.plot(kind='bar', ax=ax)
ax.set_title('Average Pollutant Levels by Station')
ax.set_xlabel('Station')
ax.set_ylabel('Average Concentration (µg/m³)')
ax.grid(True)
st.pyplot(fig)

# Create a pivot table for average pollutants during rain and no rain
rain_effect = df.pivot_table(index='RAIN', 
                              values=['PM2.5', 'PM10', 'SO2', 'NO2'], 
                              aggfunc='mean')

# Display Average Pollutants Levels Based on Rainfall Visualization
st.header('Impact of Rainfall on Pollutant Levels: Average Concentration During Rain and No Rain')
fig, ax = plt.subplots(figsize=(12, 6))
rain_effect.plot(ax=ax)
ax.set_title('Average Pollutants Levels Based on Rainfall')
ax.set_xlabel('Rain (mm)')
ax.set_ylabel('Average Concentration (µg/m³)')
ax.grid(True)
st.pyplot(fig)
