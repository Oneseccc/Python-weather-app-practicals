import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap


def get_weather(city):
    API_KEY = "dce51922cde99fb001896aef4c47ba97"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    res = requests.get(url)
    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None

    weather = res.json()

    # Check if 'weather' key is present in the response
    if 'weather' not in weather:
        messagebox.showerror("Error", "Weather information not available for this city")
        return None

    icon_id = weather["weather"][0]["icon"]
    temperature = weather["main"]["temp"] - 273.15
    description = weather["weather"][0]["description"]
    city = weather["name"]
    country = weather["sys"]["country"]

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)


def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return

    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    temperature_label.configure(text=f"{temperature:.2f}°C")
    description_label.configure(text=f"{description}")

root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("600x500")

city_entry = ttkbootstrap.Entry(root, font="helvetica, 15")
city_entry.pack(pady=20)

search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=20)


location_label = tk.Label(root, font="helvetica, 20")
location_label.pack(pady=20)

icon_label = tk.Label(root)
icon_label.pack()

temperature_label = tk.Label(root, font="helvetica, 30")
temperature_label.pack()

description_label = tk.Label(root, font="helvetica, 20")
description_label.pack()

root.mainloop()