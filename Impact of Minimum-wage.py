import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'MinWage': [8.0, 8.0, 8.0, 8.0, 9.0, 9.0, 10.5, 12.0, 13.25, 14.25, 15.0, 15.0, 16.04, 16.78, 17.28],
    'Unemployment': [12.5, 12.2, 10.9, 8.9, 8.2, 5.9, 5.2, 4.8, 4.6, 4.4, 12.8, 8.9, 4.9, 5.1, 5.4]
}

df = pd.DataFrame(data)

#graph
fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.bar(df['Year'], df['MinWage'], color='lightgray', label='Minimum Wage ($)')
ax1.set_ylabel('Minimum Wage ($)')

ax2 = ax1.twinx()
ax2.plot(df['Year'], df['Unemployment'], color='red', marker='o', linewidth=2, label='Unemployment Rate (%)')
ax2.set_ylabel('Unemployment Rate (%)')

plt.title('Does Minimum Wage Hurt Employment in LA?', fontsize=16)
plt.annotate('COVID-19 Shock', xy=(2020, 12.8), xytext=(2017, 13),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()