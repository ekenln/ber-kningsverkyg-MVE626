import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('CO2.csv', sep = ';')

regioner = {
	"south_asia" : 'C9',
	"europe_central_asia" : 'r',
	"middle_east_north_africa" : 'b',
	"sub_saharan_africa" : 'y',
	"america" : 'm',
	"east_asia_pacific" : 'purple',
}

colors = df['Region'].map(regioner)
colors[df['Stat'] == "Sweden"] = 'black'
df['Befolkningsmängd'] = np.floor(np.sqrt(df['Befolkningsmängd']) / 100)

plt.scatter(x = df["BNP/capita"], y = df["CO2"], s=df["Befolkningsmängd"], color=colors, alpha=0.5) # Scatter plot
plt.xscale('log') # Ändrar x-skalan till log10 för lättläst graf
plt.yscale('log') # Ändrar x-skalan till log10 för lättläst graf

plt.ylabel('koldioxidutsläpp/capita') # y-rubrik
plt.xlabel('BNP/capita') # x-rubrik
plt.title('BNP/capita kontra CO2 utsläpp/capita') # Titel

plt.show()