import matplotlib.pyplot as plt
import pandas as pd

years = []
co2 = []
temp = []

# Read csv
df = pd.read_csv('climate.csv')

# append values to list
years = df['Year'].tolist()
co2 = df['CO2'].tolist()
temp = df['Temperature'].tolist()

# for testing
#print("Years:", years)
#print("CO2:", co2)
#print("Temperature:", temp)

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

