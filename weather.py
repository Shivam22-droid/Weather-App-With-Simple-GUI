import tkinter as tk
from tkinter import messagebox
from tkinter import font
from PIL import Image, ImageTk
import requests

API_KEY = "db8a0cfb96a3faa06703971ae20b9084"

def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showwarning("Error", "Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        data = requests.get(url).json()
        if data["cod"]!=200:
            messagebox.showerror("Error", f"City not found: {city}")
            return
        temp = data["main"]["temp"]
        weather = data["weather"][0]["main"]
        humidity = data["main"]["humidity"]
        result_label.config(text=f"Temperature: {temp}°C\nWeather: {weather}\nHumidity: {humidity}%")

    except:
        messagebox.showerror("Error", "Check Your Internet Connection.")

#....WINDOW......
root = tk.Tk()
root.title("Weather App")
root.geometry("1000x600")
root.resizable(False,False)

#BACKGROUND IMAGE.......
image = Image.open("bg.jpg")
image = image.resize((1000,600))
background = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#.....TITLE.........
title = tk.Label(root, text="Weather App", font=("ARIAL", 18, "bold"), bg="#E8D1B8", fg="#5D5147")
title.place(x=250, y=130)

#.........CITY ENTRY......
city_entry = tk.Entry(root, font=("ARIAL", 13), width=18, justify="center", bg="white",fg="#4A403A",relief="flat")
city_entry.place(x=520, y=210)

#........SEARCH BUTTON.....
search_button = tk.Button(root, text="Search",command=get_weather, bg="#E8CDB5", font=("ARIAL", 11, "bold"), fg="#4A403A",
                          relief="flat")
search_button.place(x=680, y=207,width=80, height=27)

#.......RESULT LABEL......
result_label = tk.Label(root, text="Enter A City", font=("ARIAL", 15, "bold"), bg="#ffffff", fg="#333333", justify="center")
result_label.place(x=65, y=340, width=210, height=70)

#......INSTRUCTION....
instruction = tk.Label(root, text="SEARCH A CITY TO SEE IT'S WEATHER", bg ="#FFF7E6", fg="#8A7B6D", font=("ARIAL", 11))
instruction.place(x=470, y=450)

#.....ENTER KEY....
city_entry.bind("<Return>", lambda event: get_weather())

root.mainloop()
