import matplotlib.pyplot as plt
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('climate.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a query to select data from the ClimateData table
cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData")

# Fetch all rows from the table
rows = cursor.fetchall()

years = []
co2 = []
temp = []

# add to lists
for row in rows:
    year, co2_value, temp_value = row
    years.append(year)
    co2.append(co2_value)
    temp.append(temp_value)

# Close cursor and database conn
cursor.close()
conn.close()

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
plt.savefig("co2_temp_1.png") 
