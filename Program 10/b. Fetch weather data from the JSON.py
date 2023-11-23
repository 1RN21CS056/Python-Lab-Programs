import json

with open(r'C:\\Users\\Eshwar K\\OneDrive\Desktop\\Python-Lab-Programs\\Program 10\\weather_data.json','rb') as f :
    data = json.load(f)

current_temp = data['main']['temp']
humidity = data['main']['humidity']
des = data['weather']['des'] 

print(f"Current Temperature :{current_temp}°C")
print(f"Humidity :{humidity}%")
print(f"Weather Description :{des}")