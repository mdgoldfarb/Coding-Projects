import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


medals = pd.read_csv('Summer-Olympic-medals-1976-to-2008.csv', encoding='latin-1')
medals['Medal'] = medals['Medal'].replace({'Bronze': 1, 'Silver': 2, 'Gold': 3}) #medal weights with 3 being gold, 2 silver, 1 bronze
medals.drop_duplicates(subset=['Year', 'Sport', 'Event', 'Country'], keep='first', inplace=True)
medals = medals.drop(['City', 'Sport', 'Discipline', 'Event', 'Athlete', 'Gender', 'Event_gender', 'Country_Code'], axis=1)
medals = medals.groupby(['Year', 'Country']).sum().reset_index() #Combine rows where Year and Country are the same
medals = medals.pivot_table(index='Country', columns='Year', values='Medal', fill_value=0)
medals.columns = medals.columns.astype(int)
medals.columns = [str(col) + 'medals' for col in medals.columns]
medals['Total'] = medals.sum(axis=1) # Add a column named 'Total' that is the sum of the other 'medals' columns

gdp_pc = pd.read_csv('gdp_per_capita.csv', encoding='latin-1')
gdp_pc.rename(columns={'Country Name': 'Country'}, inplace=True)
gdp_pc = gdp_pc.drop('Code', axis=1)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

gdp_pc_medals = pd.merge(gdp_pc, medals, on='Country') # Merge gdp_pc and medals dataframes on 'Country' column
gdp_pc_medals = gdp_pc_medals.fillna(np.nan)

hdi = pd.read_csv('HDI.csv', encoding='latin-1')
hdi = hdi.replace('..', np.nan)
hdi_medals = pd.merge(hdi, medals, on='Country')  # Merge hdi and medals dataframes on 'Country' column
hdi_medals = hdi_medals.fillna(np.nan)
hdi_medals[hdi_medals.columns[2:]] = hdi_medals[hdi_medals.columns[2:]].astype(float)

population = pd.read_csv('world_population.csv', encoding='latin-1')
pop_medals = pd.merge(population, medals, on='Country')  # Merge population and medals dataframes on 'Country' column

gdp = pd.read_csv('gdp.csv', encoding='latin-1')
gdp.rename(columns={'Country Name': 'Country'}, inplace=True)
gdp = gdp.drop('Code', axis=1)
gdp_medals = pd.merge(gdp, medals, on='Country')  # Merge gdp and medals dataframes on 'Country' column
gdp_medals = gdp_medals.fillna(np.nan)

medals_sorted = medals.sort_values(by='Total', ascending=False) #Use the ascending value to make it so it goes from highest to lowest
m=medals_sorted.head(20) #Get the top 20
plt.figure(figsize=(12, 8))
m['Total'].plot(kind='bar', color='blue') #Make plot and colors
plt.xlabel('Country') #All the titles
plt.ylabel('Total Medals')
plt.title('Total Medals Won by Country (Ordered)')
plt.xticks(rotation=90, ha='right') #Rotate numbers so they do not overlap each other
plt.show()

plt.figure(figsize=(12, 8))
plt.pie(m['Total'], labels=m.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Total Medals Among Top 20 Countries')
plt.show()

world_population = pd.read_csv('world_population.csv', index_col=0)
p_sorted = world_population.sort_values(by='2008', ascending=False)
p = p_sorted.iloc[1:21]


plt.figure(figsize=(12, 8))
p['2008'].plot(kind='bar', color='skyblue')
plt.xlabel('Country')
plt.ylabel('Population (2008)')
plt.title('Total Population Won by Country (Ordered)')
plt.xticks(rotation=90, ha='right')
plt.show()

plt.figure(figsize=(12, 8))
plt.pie(p['2008'], labels=p.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Population Among Top 20 Countries')
plt.show()

years = gdp_pc.columns[1:-1] #get all the columns
selected_countries = ['Soviet Union', 'United States', 'China', 'Germany', 'Australia', 'France', 'Italy', 'United Kingdom', 'Romania', 'Japan', 'Cuba', 'Hungary', 'Bulgaria', 'Poland', 'Canada', 'Netherlands', 'Spain', 'Sweden', 'Ukraine', 'New Zealand', 'Brazil', 'Norway', 'Greece', 'Denmark', 'Belarus', 'Finland', 'Switzerland', 'Turkey', 'Kazakhstan', 'Kenya', 'Czechoslovakia', 'Czech Republic', 'Korea, North', 'Jamaica', 'Belgium', 'Austria', 'Mexico', 'Slovakia', 'Iran', 'Thailand', 'Morocco', 'South Africa', 'Argentina', 'Ethiopia', 'West Germany', 'Russia', 'Soviet Union'] #A sample of countries within the top 50 medal countries
plt.figure(figsize=(12, 8))
for country in selected_countries:
    country_data = gdp_pc[gdp_pc['Country'] == country].iloc[:, 16:49].squeeze().interpolate(method='linear')  # the iloc and interpolate get these columns and help with cleaning data.Columns from 1976 to 2008
    if not country_data.empty:
        plt.plot(range(1976, 2009), country_data, label=country) #Take the gdp from all the years from 1976 to 2008
plt.xlabel('Year')
plt.ylabel('GDP per capita Value')
plt.title('GDP per capita Values Over the Years (1976-2008) for Selected Countries')
plt.xticks(rotation=90)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Countries', bbox_transform=plt.gcf().transFigure) #Make a legend and fit it
plt.tight_layout()
plt.show()

#Exact same thing as above but all use the cumsum to make the data progress with adding medals from the current and previous years
selected_countries = ['United States', 'Soviet Union', 'China', 'Russia', 'Germany', 'East Germany', 'Australia', 'France', 'Italy', 'United Kingdom', 'Romania', 'Japan', 'Korea, South', 'Cuba', 'Hungary', 'Bulgaria', 'Poland', 'Canada', 'Netherlands', 'West Germany', 'Spain', 'Unified team', 'Sweden', 'Ukraine', 'New Zealand', 'Brazil', 'Norway', 'Greece', 'Denmark', 'Yugoslavia', 'Belarus', 'Finland', 'Switzerland', 'Turkey', 'Kazakhstan', 'Kenya', 'Czechoslovakia', 'Czech Republic', 'Korea, North', 'Jamaica', 'Belgium', 'Austria', 'Mexico', 'Slovakia', 'Iran', 'Thailand', 'Morocco', 'South Africa', 'Argentina', 'Ethiopia']
plt.figure(figsize=(16, 8))
for country in selected_countries:
    country_data = medals.loc[country, :'2008medals'].cumsum().T
    plt.plot(country_data.index, country_data.values, label=country)
plt.xlabel('Year')
plt.ylabel('Cumulative Medal Count')
plt.title('Cumulative Medal Counts Over the Years for Selected Countries')
plt.xticks(rotation=90)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Countries', bbox_transform=plt.gcf().transFigure)
plt.tight_layout()
plt.show()

#Same as before but with fewer countries to not make it too complicated
world_population = pd.read_csv('world_population.csv', index_col=0)
selected_countries = [
    'United States','China', 'Russian Federation', 'Germany',
    'Australia', 'France', 'Italy', 'United Kingdom', 'Romania',
    'Japan', 'Cuba', 'Hungary', 'Bulgaria', 'Poland',
    'Canada', 'Netherlands', 'Spain', 'Sweden', 'Ukraine',
    'New Zealand', 'Brazil', 'Norway', 'Greece', 'Denmark',
    'Belarus', 'Finland', 'Switzerland', 'Turkiye', 'Kazakhstan',
    'Kenya', 'Czechia', 'Korea, Rep.',
    'Jamaica', 'Belgium', 'Austria', 'Mexico', 'Slovak Republic',
    'Iran, Islamic Rep.', 'Thailand', 'Morocco', 'South Africa', 'Argentina',
    'Ethiopia'
]
population_data = world_population.loc[selected_countries, '1976':'2008'] #the .loc helps with locating all the countries in the df
plt.figure(figsize=(12, 8))
for country in selected_countries:
    country_data = population_data.loc[country].astype(float)
    plt.plot(country_data.index.astype(int), country_data, label=country)
plt.xlabel('Year')
plt.ylabel('Population (Billions)')
plt.title('Population of Selected Countries (1976-2008)')
plt.xticks(rotation=90)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Countries', bbox_transform=plt.gcf().transFigure)
plt.tight_layout()
plt.show()

#Same as before but with the gdp
gdp = pd.read_csv('gdp.csv', index_col=0)
selected_countries = [
    'United States','China', 'Russian Federation', 'Germany',
    'Australia', 'France', 'Italy', 'United Kingdom', 'Romania',
    'Japan', 'Cuba', 'Hungary', 'Bulgaria', 'Poland',
    'Canada', 'Netherlands', 'Spain', 'Sweden', 'Ukraine',
    'New Zealand', 'Brazil', 'Norway', 'Greece', 'Denmark',
    'Belarus', 'Finland', 'Switzerland', 'Turkey', 'Kazakhstan',
    'Kenya', 'Czech Republic', 'Korea, Rep.',
    'Jamaica', 'Belgium', 'Austria', 'Mexico', 'Slovak Republic',
    'Iran, Islamic Rep.', 'Thailand', 'Morocco', 'South Africa', 'Argentina',
    'Ethiopia'
]
gdp_data = gdp.loc[selected_countries, '1976':'2008']
plt.figure(figsize=(12, 8))
for country in selected_countries:
    country_data = gdp_data.loc[country]
    plt.plot(country_data.index.astype(int), country_data, label=country)
plt.xlabel('Year')
plt.ylabel('GDP Value')
plt.title('GDP Values of Selected Countries (1976-2008)')
plt.xticks(rotation=90)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Countries', bbox_transform=plt.gcf().transFigure)
plt.tight_layout()
plt.show()

#Package for heatmap
selected_years = list(range(1976, 2009, 4))  #Make a list of selected years using the syntax of a for loop
common_countries = set(medals.index) & set(gdp.index) & set(world_population.index) #This is so there will be no errors of countries that are spelled differently in different dataframes
for year in selected_years: #Loop for Heatmap for specific years
    common_countries = list(set(medals.index) & set(gdp.index) & set(world_population.index))
    medals_year = medals.loc[common_countries, f'{year}medals'] #Get the info from the specific year column from Pop. GDP and Medals
    gdp_year = gdp.loc[common_countries, f'{year}']
    population_year = world_population.loc[common_countries, f'{year}']
    combined_data_year = pd.concat([medals_year, gdp_year, population_year], axis=1) #Concatinate the data
    combined_data_year.columns = ['Medals', 'GDP', 'Population'] #Make it these 3 variables
    plt.figure(figsize=(10, 8))
    sns.heatmap(combined_data_year.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5) #Blue to red
    plt.title(f'Correlation Heatmap for {year}')
    plt.show()


heatmap_data = hdi_medals[['HDI Rank', 'Total']]
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Heatmap: HDI Rank vs Total Medals')
plt.show()

selected_countries = ['United States','Soviet Union', 'China', 'Russia' ,'Germany', 'Australia', 'France', 'Italy', 'United Kingdom', 'Romania', 'Japan', 'Cuba', 'Hungary', 'Bulgaria', 'Poland', 'Canada', 'Netherlands', 'Spain', 'Sweden', 'Ukraine', 'New Zealand', 'Brazil', 'Norway', 'Greece', 'Denmark', 'Belarus', 'Finland', 'Switzerland', 'Turkey', 'Kazakhstan', 'Kenya', 'Czechoslovakia', 'Czech Republic', 'Korea, North', 'Jamaica', 'Belgium', 'Austria', 'Mexico', 'Slovakia', 'Iran', 'Thailand', 'Morocco', 'South Africa', 'Argentina', 'Ethiopia']
country_continents = {#These are the top 50 countries with the most medals
    'United States': 'North America', 'Soviet Union':'Asia', 'China': 'Asia', 'Russia': 'Asia', 'Germany': 'Europe', 'Australia': 'Oceania',
    'France': 'Europe', 'Italy': 'Europe', 'United Kingdom': 'Europe', 'Romania': 'Europe',
    'Japan': 'Asia', 'Cuba': 'North America', 'Hungary': 'Europe', 'Bulgaria': 'Europe',
    'Poland': 'Europe', 'Canada': 'North America', 'Netherlands': 'Europe', 'Spain': 'Europe',
    'Sweden': 'Europe', 'Ukraine': 'Europe', 'New Zealand': 'Oceania', 'Brazil': 'South America',
    'Norway': 'Europe', 'Greece': 'Europe', 'Denmark': 'Europe', 'Belarus': 'Europe',
    'Finland': 'Europe', 'Switzerland': 'Europe', 'Turkey': 'Asia', 'Kazakhstan': 'Asia',
    'Kenya': 'Africa', 'Czechoslovakia': 'Europe', 'Czech Republic': 'Europe',
    'Korea, North': 'Asia', 'Jamaica': 'North America', 'Belgium': 'Europe', 'Austria': 'Europe',
    'Mexico': 'North America', 'Slovakia': 'Europe', 'Iran': 'Asia', 'Thailand': 'Asia',
    'Morocco': 'Africa', 'South Africa': 'Africa', 'Argentina': 'South America', 'Ethiopia': 'Africa'
}
continent_counts = {}#A dictionary helps, I used ChatGPT to put in all the continents associated with each country because it would take a long time and repetitive for me to type it all
for country in selected_countries:
    continent = country_continents.get(country) #Get the country and the continent
    if continent:
        continent_counts[continent] = continent_counts.get(continent,0)+1 #Get the number of countries from each continent
plt.figure(figsize=(8, 8))
plt.pie(continent_counts.values(), labels=continent_counts.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Selected Countries by Continent')
plt.show()

