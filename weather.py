import requests
import tkinter as tk
from tkinter import messagebox, PhotoImage

def get_weather(city):
    api_key = '6d3495afa8ee2a6dc3f40c2ff66ded67'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def show_weather():
    city = city_entry.get()
    weather_data = get_weather(city)

    if weather_data.get('cod') != 200:
        messagebox.showerror("Error", "City not found.")
        return

    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    conditions = weather_data['weather'][0]['description']

    # Check the selected temperature unit
    if temp_unit.get() == "Celsius":
        temperature_str = f"Temperature: {temperature}°C"
    else:  # Fahrenheit
        temperature = celsius_to_fahrenheit(temperature)
        temperature_str = f"Temperature: {temperature}°F"

    result_label.config(text=f"{temperature_str}\nHumidity: {humidity}%\nConditions: {conditions}")
 
    icon_code = weather_data['weather'][0]['icon']
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
    icon_image = PhotoImage(data=requests.get(icon_url).content)
    weather_icon_label.config(image=icon_image)
    weather_icon_label.image = icon_image

root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.config(bg="#87CEEB")

container = tk.Frame(root, bg="#87CEEB")
container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

input_frame = tk.Frame(container, bg="#87CEEB")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter city name:", font=("Helvetica", 14), bg="#87CEEB").grid(row=0, column=0, padx=10)
city_entry = tk.Entry(input_frame, font=("Helvetica", 14))
city_entry.grid(row=0, column=1, padx=10)

tk.Button(input_frame, text="Get Weather", font=("Helvetica", 14), command=show_weather, bg="#FFA500").grid(row=0, column=2, padx=10)

# Temperature unit selection
temp_unit = tk.StringVar()
temp_unit.set("Celsius")  # Default selection

unit_frame = tk.Frame(container, bg="#87CEEB")
unit_frame.pack(pady=10)

tk.Label(unit_frame, text="Select Temperature Unit:", font=("Helvetica", 12), bg="#87CEEB").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(unit_frame, text="Celsius", variable=temp_unit, value="Celsius", bg="#87CEEB").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(unit_frame, text="Fahrenheit", variable=temp_unit, value="Fahrenheit", bg="#87CEEB").pack(side=tk.LEFT, padx=5)

result_frame = tk.Frame(container, bg="#87CEEB")
result_frame.pack(pady=10)

result_label = tk.Label(result_frame, text="", font=("Helvetica", 14), bg="#87CEEB")
result_label.pack()

weather_icon_label = tk.Label(result_frame, bg="#87CEEB")
weather_icon_label.pack()

root.mainloop()
