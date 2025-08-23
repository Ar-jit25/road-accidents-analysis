import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

st.title("Road Accidents Analysis in India")

# Fetch data from Flask API
try:
    data = requests.get("http://127.0.0.1:5000/api/data").json()
    df = pd.DataFrame(data)
except:
    st.error("Could not fetch data from Flask API.")
    st.stop()

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(df.head(20))


# Plot 1: Vehicle type distribution
st.subheader("Accidents by Vehicle Type")
vehicle_count = df['Type_of_vehicle'].value_counts()
st.bar_chart(vehicle_count)

# Plot 2: Accidents by Area (Urban/Rural)
if 'Area_accident_occured' in df.columns:
    st.subheader("Accidents by Area")
    area_count = df['Area_accident_occured'].value_counts()
    st.bar_chart(area_count)

# Plot 3: Accidents by Road Surface Condition
if 'Road_surface' in df.columns:
    st.subheader("Accidents by Road Surface Condition")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='Road_surface', order=df['Road_surface'].value_counts().index, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Plot 4: Accidents by Weather Condition
if 'Weather_conditions' in df.columns:
    st.subheader("Accidents by Weather Condition")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='Weather_conditions', order=df['Weather_conditions'].value_counts().index, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Plot 5: Accidents by Day of the Week
if 'Day_of_week' in df.columns:
    st.subheader("Accidents by Day of the Week")
    fig, ax = plt.subplots()
    order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    sns.countplot(data=df, x='Day_of_week', order=order, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Plot 6: Casualties by Vehicle Type
if 'Number_of_casualties' in df.columns:
    st.subheader("Casualties by Vehicle Type")
    casualties = df.groupby('Type_of_vehicle')['Number_of_casualties'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots()
    sns.barplot(x=casualties.index, y=casualties.values, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Plot 7: Accidents by Light Condition
if 'Light_conditions' in df.columns:
    st.subheader("Accidents by Light Conditions")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='Light_conditions', order=df['Light_conditions'].value_counts().index, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Plot 8: Heatmap (Road Surface vs Weather Conditions)
if 'Road_surface' in df.columns and 'Weather_conditions' in df.columns:
    st.subheader("Heatmap: Road Surface vs Weather Conditions")
    cross_tab = pd.crosstab(df['Road_surface'], df['Weather_conditions'])
    fig, ax = plt.subplots(figsize=(10,6))
    sns.heatmap(cross_tab, annot=True, fmt='d', cmap="YlGnBu", ax=ax)
    st.pyplot(fig)


