import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog, ttk

# Function to load and display the CSV file
def load_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        global data
        data = pd.read_csv(file_path)
        filter_country['values'] = data['country'].dropna().unique().tolist()
        filter_location['values'] = []
        display_data_preview(data)

# Function to display data preview
def display_data_preview(data):
    for widget in preview_frame.winfo_children():
        widget.destroy()

    text_area = tk.Text(preview_frame, wrap='none', height=10)
    text_area.insert(tk.END, data.head(10).to_string(index=False))
    text_area.pack(side='left', fill='both', expand=True)

    scrollbar = ttk.Scrollbar(preview_frame, orient='vertical', command=text_area.yview)
    scrollbar.pack(side='right', fill='y')
    text_area.config(yscrollcommand=scrollbar.set)

# Function to filter locations based on country
def update_locations(event):
    selected_country = filter_country.get()
    if selected_country:
        locations = data[data['country'] == selected_country]['location_name'].dropna().unique().tolist()
        filter_location['values'] = locations

# Function to perform analysis and display temperature statistics
def perform_analysis():
    analysis_type = analysis_combo.get()
    selected_country = filter_country.get()
    selected_location = filter_location.get()

    filtered_data = data.copy()
    if selected_country:
        filtered_data = filtered_data[filtered_data['country'] == selected_country]
    if selected_location:
        filtered_data = filtered_data[filtered_data['location_name'] == selected_location]

    # Calculate min, max, and average temperature
    if 'temperature_celsius' in filtered_data.columns and not filtered_data.empty:
        min_temp = filtered_data['temperature_celsius'].min()
        max_temp = filtered_data['temperature_celsius'].max()
        avg_temp = filtered_data['temperature_celsius'].mean()
        temp_stats_label.config(text=f"Min: {min_temp:.2f}°C, Max: {max_temp:.2f}°C, Avg: {avg_temp:.2f}°C")
    else:
        temp_stats_label.config(text="No temperature data available")

    # Analysis options
    if analysis_type == "Temperature Distribution":
        plt.figure(figsize=(10, 6))
        sns.histplot(filtered_data['temperature_celsius'], kde=True, color="orange")
        plt.title('Temperature Distribution (Celsius)')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Frequency')
        plt.show()
    elif analysis_type == "Humidity Distribution":
        plt.figure(figsize=(10, 6))
        sns.histplot(filtered_data['humidity'], kde=True, color="blue")
        plt.title('Humidity Distribution')
        plt.xlabel('Humidity (%)')
        plt.ylabel('Frequency')
        plt.show()
    elif analysis_type == "Visibility vs Humidity":
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='visibility_km', y='humidity', data=filtered_data, color="green")
        plt.title('Visibility vs Humidity')
        plt.xlabel('Visibility (km)')
        plt.ylabel('Humidity (%)')
        plt.show()
    elif analysis_type == "Wind Speed vs UV Index":
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='wind_kph', y='uv_index', data=filtered_data, color="purple")
        plt.title('Wind Speed vs UV Index')
        plt.xlabel('Wind Speed (KPH)')
        plt.ylabel('UV Index')
        plt.show()
    elif analysis_type == "Air Quality vs Temperature":
        air_quality_cols = [
            'air_quality_Carbon_Monoxide', 'air_quality_Ozone',
            'air_quality_Nitrogen_dioxide', 'air_quality_Sulphur_dioxide',
            'air_quality_PM2.5', 'air_quality_PM10'
        ]
        for col in air_quality_cols:
            if col in filtered_data.columns:
                plt.figure(figsize=(10, 6))
                sns.scatterplot(x='temperature_celsius', y=col, data=filtered_data)
                plt.title(f'{col} vs Temperature')
                plt.xlabel('Temperature (°C)')
                plt.ylabel(col)
                plt.show()

# Main GUI setup
root = tk.Tk()
root.title("Enhanced Weather Data Analysis")
root.geometry("1920x1080")
root.configure(bg='sky blue')

# Frames
control_frame = ttk.Frame(root)
control_frame.pack(fill='x', pady=20)

preview_frame = ttk.Frame(root)
preview_frame.pack(fill='both', expand=True, pady=10)

# Control Widgets
load_button = ttk.Button(control_frame, text="Load CSV File", command=load_csv)
load_button.grid(row=0, column=0, padx=10)

filter_country_label = ttk.Label(control_frame, text="Filter by Country:")
filter_country_label.grid(row=0, column=1, padx=10)

filter_country = ttk.Combobox(control_frame, state='readonly', width=20)
filter_country.grid(row=0, column=2, padx=10)
filter_country.bind("<<ComboboxSelected>>", update_locations)

filter_location_label = ttk.Label(control_frame, text="Filter by Location:")
filter_location_label.grid(row=0, column=3, padx=10)

filter_location = ttk.Combobox(control_frame, state='readonly', width=20)
filter_location.grid(row=0, column=4, padx=10)

analysis_label = ttk.Label(control_frame, text="Analysis Type:")
analysis_label.grid(row=0, column=5, padx=10)

analysis_combo = ttk.Combobox(control_frame, state='readonly', width=30, values=[
    "Temperature Distribution",
    "Humidity Distribution",
    "Visibility vs Humidity",
    "Wind Speed vs UV Index",
    "Air Quality vs Temperature"
])
analysis_combo.grid(row=0, column=6, padx=10)

analyze_button = ttk.Button(control_frame, text="Perform Analysis", command=perform_analysis)
analyze_button.grid(row=0, column=7, padx=10)

# Temperature statistics display
temp_stats_label = ttk.Label(control_frame, text="Min: --°C, Max: --°C, Avg: --°C", font=('Arial', 12, 'bold'))
temp_stats_label.grid(row=1, column=0, columnspan=8, pady=10)

root.mainloop()



