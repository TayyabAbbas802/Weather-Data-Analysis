🌦️ Enhanced Weather Data Analysis GUI
This is a Python-based desktop application built using Tkinter, Pandas, Matplotlib, and Seaborn that allows users to load weather datasets in CSV format and perform various types of exploratory analysis such as temperature distributions, humidity trends, air quality correlations, and more.

📊 Features
📁 Load weather data from a CSV file

🌍 Filter data by Country and Location

🔍 Perform various analyses:

Temperature Distribution

Humidity Distribution

Visibility vs Humidity

Wind Speed vs UV Index

Air Quality vs Temperature

📉 Visualizations using Matplotlib & Seaborn

📄 Preview the top 10 rows of the dataset within the GUI

🧠 Displays minimum, maximum, and average temperatures for selected filters

🛠️ Technologies Used
Python 3.x

Tkinter (GUI framework)

Pandas

Matplotlib

Seaborn

📦 Installation
Clone the repository

git clone https://github.com/your-username/enhanced-weather-analysis.git
cd enhanced-weather-analysis

Install dependencies
You can install the required libraries using pip:

pip install pandas matplotlib seaborn

Run the application

python weather_analysis_gui.py

🧪 Sample Data
To get started, use any CSV file that includes weather data with the following (or similar) columns:

country

location_name

temperature_celsius

humidity

visibility_km

uv_index

wind_kph

air_quality_Carbon_Monoxide

air_quality_Ozone

air_quality_Nitrogen_dioxide

air_quality_Sulphur_dioxide

air_quality_PM2.5

air_quality_PM10

Note: The program will auto-detect and utilize available columns in the dataset.

🖼️ GUI Preview
Load & Filter	Analyze & Visualize

Add your own screenshots to the screenshots/ directory for better presentation.

📌 TODO
 Add support for saving plots

 Add CSV export for filtered data

 Support for more chart types and metrics

 Dark mode theme

🤝 Contributing
Contributions are welcome! If you'd like to enhance the tool or fix a bug, feel free to fork the repo and submit a pull request.

📄 License
This project is licensed under the MIT License.
