import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from matplotlib.ticker import FuncFormatter

# Relative file paths
fp = "world.shp"
csv_file = 'population.csv'
data = 'data.csv'

# fucntion to generate random medal data for each country
def random_data():
    # Load the original csv file into a panda frame
    df_original = pd.read_csv(csv_file)

    # Extract the country name from the first column
    first_column_values = df_original.iloc[:, 0]
    population = df_original['Population']
    continent = df_original['Continent']

    # Generating random medals for each country
    golds = np.random.randint(0, 100, size=len(df_original))
    silver = np.random.randint(0, 100, size=len(df_original))
    bronze = np.random.randint(0, 100, size=len(df_original))
    total = golds+silver+bronze
    male = np.random.randint(0,total,size=len(df_original))
    winter_medals = np.random.randint(0, 200, size=len(df_original))
    female = total-male
    age =  np.random.randint(16, 65, size=len(df_original))
    sprint = np.random.randint(0,10,size=len(df_original))
    archery = np.random.randint(0,10,size=len(df_original))
    high_jump = np.random.randint(0,10,size=len(df_original))
    swimming = np.random.randint(0,10,size=len(df_original))
    javelin = np.random.randint(0,10,size=len(df_original))
    individual_medals = np.random.randint(0, total, size=len(df_original))
    team_medals = total - individual_medals
    medals_per_capita = round(total / (population / 1_000_000))

    # Create a new panda frame with country name and medal data
    data_frame = pd.DataFrame({
        'Countries': first_column_values,
        'Continent': continent,
        'All Medals': total,
        'Winter Medals': winter_medals,
        'Gold Medals': golds,
        'Silver Medals': silver,
        'Bronze Medals': bronze,
        'Male': male,
        'Female':female,
        'Age' : age, 
        '100m Sprint': sprint,
        'Archery':archery,
        'High Jump':high_jump,
        '100m Swimming':swimming,
        'Javelin': javelin,
        'Individual Sports': individual_medals,
        'Team Sports': team_medals,
        'Medals per Capita': medals_per_capita
    })

    # Save the new panda frame to a new CSV file   
    data_frame.to_csv(data, index=False)

def top_countries_by_medals_line():
    df = pd.read_csv(data, header=0)
    top_10_countries = df.nlargest(10, 'All Medals')

    gold = '#FFD700'
    silver = '#C0C0C0'
    bronze = '#CD7F32'

    # Plotting the line graph
    plt.plot(top_10_countries['Countries'], top_10_countries['Gold Medals'], color=gold, label='Gold', marker='o')
    plt.plot(top_10_countries['Countries'], top_10_countries['Silver Medals'], color=silver, label='Silver', marker='o')
    plt.plot(top_10_countries['Countries'], top_10_countries['Bronze Medals'], color=bronze, label='Bronze', marker='o')

    plt.xlabel('Country')
    plt.ylabel('Number of Medals')
    plt.title('Top 10 Countries by Total Medals')
    plt.legend()
    plt.show()

def top_countries_by_medals_area():
    # Get csv into a panda frame
    df = pd.read_csv(data, header=0)

    # Sort the DataFrame by total medals and get the top 10 countries
    top_10_countries = df.nlargest(10, 'All Medals')

    # Getting colours hexcode
    gold = '#FFD700' 
    silver = '#C0C0C0'  
    bronze = '#CD7F32'

    # Plotting the area graph
    plt.stackplot(top_10_countries['Countries'], top_10_countries['Gold Medals'], top_10_countries['Silver Medals'], top_10_countries['Bronze Medals'],
                colors=[gold, silver, bronze],labels=['Gold', 'Silver', 'Bronze'], alpha=0.7)

    # set labels and title
    plt.xlabel('Country')
    plt.ylabel('Number of Medals')
    plt.title('Top 10 Countries by Total Medals')
    # SHow legend
    plt.legend()
    # Display 
    plt.show()

def top_counties_by_gender_line():
    df = pd.read_csv(data, header=0)
    top_10_countries = df.nlargest(10, 'All Medals')

    male = "blue"
    female = "pink"

    # Plotting the line graph
    plt.plot(top_10_countries['Countries'], top_10_countries['Male'], color=male, label='Male', marker='o')
    plt.plot(top_10_countries['Countries'], top_10_countries['Female'], color=female, label='Female', marker='o')

    plt.xlabel('Country')
    plt.ylabel('Number of Medals')
    plt.title('Top 10 Countries by Total Medals for each gender')
    plt.legend()
    plt.show()

def top_counties_by_gender_area():
    # Get csv into a panda frame
    df = pd.read_csv(data, header=0)

    # Sort the DataFrame by total medals and get the top 10 countries
    top_10_countries = df.nlargest(10, 'All Medals')

    # Get colours hexcode
    male = "blue"
    female = "pink"

    # Plotting the area graph
    plt.stackplot(top_10_countries['Countries'], top_10_countries['Male'], top_10_countries['Female'], 
                colors=[male,female],labels=['male','female'], alpha=0.7)

    # set labels and title
    plt.xlabel('Country')
    plt.ylabel('Number of Medals')
    plt.title('Top 10 Countries by Total Medals for each gender')
    # Show legend
    plt.legend()
    # Display 
    plt.show()

def total_medals_by_sport_line():
    df = pd.read_csv(data, header=0)
    top_10_countries = df.nlargest(10, 'All Medals')

    sprint = "#26547D"
    archery = "#EF436B"
    high_jump = "#FFCE5C"
    swimming = "#05C793"
    javelin = "#5C43A9"

    # Plotting the line graph
    plt.plot(top_10_countries['Countries'], top_10_countries['100m Sprint'], color=sprint, label='Sprint', marker='o')
    plt.plot(top_10_countries['Countries'], top_10_countries['Archery'], color=archery, label='Archery', marker='o')
    plt.plot(top_10_countries['Countries'], top_10_countries['High Jump'], color=high_jump, label='High Jump', marker='o')
    plt.plot(top_10_countries['Countries'], top_10_countries['100m Swimming'], color=swimming, label='Swimming', marker='o')
    plt.plot(top_10_countries['Countries'], top_10_countries['Javelin'], color=javelin, label='Javelin', marker='o')

    plt.xlabel('Country')
    plt.ylabel('Number of Medals')
    plt.title('Top 10 Countries by Total Medals for 5 sports')
    plt.legend()
    plt.show()

def total_medals_by_sport_area():
    # Get csv into a panda frame
    df = pd.read_csv(data, header=0)

    # Sort the DataFrame by total medals and get the top 10 countries
    top_10_countries = df.nlargest(10, 'All Medals')

    # get colours hexcode
    sprint = "#26547D"
    archery = "#EF436B"
    high_jump = "#FFCE5C"
    swimming = "#05C793"
    javelin = "#5C43A9"

    # Plotting the area graph
    plt.stackplot(top_10_countries['Countries'],top_10_countries['100m Sprint'], top_10_countries['Archery'],
                  top_10_countries['High Jump'],top_10_countries['100m Swimming'],top_10_countries['Javelin'], 
                colors=[sprint,archery,high_jump,swimming,javelin],labels=['sprint','archery','high_jump','swimming','javelin'], alpha=0.7)
    
    # set labels and title
    plt.xlabel('Country')
    plt.ylabel('Number of Medals')
    plt.title('Top 10 Countries by Total Medals for 5 sports')
    # Show legend
    plt.legend()
    # Display 
    plt.show()

def compare_summer_winter_line():
    df = pd.read_csv(data, header=0)
    top_10_countries = df.nlargest(10, 'All Medals')

    winter = "blue"
    summer = "green"

    # Plotting the line graph
    plt.plot(top_10_countries['Countries'], top_10_countries['Winter Medals'], color=winter, label='Winter Medals', marker='o')
    plt.plot(top_10_countries['Countries'], top_10_countries['All Medals'], color=summer, label='Summer Medals', marker='o')

    plt.xlabel('Country')
    plt.ylabel('Number of Medals')
    plt.title('Top 10 Countries for Winter Medals and Summer Medals')
    plt.legend()
    plt.show()

def compare_summer_winter_area():
    # Get csv into a panda frame
    df = pd.read_csv(data, header=0)

    # Sort the DataFrame by total medals and get the top 10 countries
    top_10_countries = df.nlargest(10, 'All Medals')

    # Get colours hexcode
    winter = "blue"
    summer = "green"

    # Plotting the area graph
    plt.stackplot(top_10_countries['Countries'], top_10_countries['Winter Medals'], top_10_countries['All Medals'], 
                colors=[winter,summer],labels=['Winter Medals','Summer Medals'], alpha=0.7)

    # set labels and title
    plt.xlabel('Country')
    plt.ylabel('Number of Medals')
    plt.title('Top 10 Countries for Winter Medals and Summer Medals')
    # Show legend
    plt.legend()
    # Display 
    plt.show()


# Function to generate hypothetical yearly data
def generate_yearly_data(start_year, end_year, data_points):
    years = list(range(start_year, end_year + 1))
    values = np.random.randint(low=0, high=max(data_points) + 1, size=len(years))
    return years, values

def plot_yearly_medal_count_line_chart(country_name, start_year, end_year):
    df = pd.read_csv(data, header=0)
    country_medals = df[df['Countries'] == country_name]['All Medals'].iloc[0]
    years, country_yearly_medals = generate_yearly_data(start_year, end_year, [country_medals])

    plt.plot(years, country_yearly_medals, color='blue', marker='o')
    plt.title(f'Yearly Medal Count for {country_name} (Line Chart)')
    plt.xlabel('Year')
    plt.ylabel('Medals')
    plt.show()

def plot_yearly_medal_count_area_chart(country_name, start_year, end_year):
    df = pd.read_csv(data, header=0)
    
    country_medals = df[df['Countries'] == country_name]['All Medals'].iloc[0]
    years, country_yearly_medals = generate_yearly_data(start_year, end_year, [country_medals])
    plt.fill_between(years, country_yearly_medals, color='blue', alpha=0.3)
    plt.title(f'Yearly Medal Count for {country_name} (Area Chart)')
    plt.xlabel('Year')
    plt.ylabel('Medals')
    plt.show()

def plot_sport_medal_count_line_chart(sport, start_year, end_year):

    df = pd.read_csv(data, header=0)
    sport_medals = df[sport].sum()
    years, sport_yearly_medals = generate_yearly_data(start_year, end_year, [sport_medals])

    plt.plot(years, sport_yearly_medals, color='green', marker='o')
    plt.title(f'Medal Counts in {sport} Over Time (Line Chart)')
    plt.xlabel('Year')
    plt.ylabel('Medals')
    plt.show()

def plot_sport_medal_count_area_chart(sport, start_year, end_year):

    df = pd.read_csv(data, header=0)
    sport_medals = df[sport].sum()
    years, sport_yearly_medals = generate_yearly_data(start_year, end_year, [sport_medals])

    plt.fill_between(years, sport_yearly_medals, color='green', alpha=0.3)
    plt.title(f'Medal Counts in {sport} Over Time (Area Chart)')
    plt.xlabel('Year')
    plt.ylabel('Medals')
    plt.show()

def plot_age_distribution_line_chart(start_year, end_year):

    df_age = pd.read_csv(data, header=0)['Age']
    min_age, max_age = df_age.min(), df_age.max()
    years, age_yearly_distribution = generate_yearly_data(start_year, end_year, list(range(min_age, max_age + 1)))

    plt.plot(years, age_yearly_distribution, color='red', marker='o')
    plt.title('Age Distribution of Medalists Over Time (Line Chart)')
    plt.xlabel('Year')
    plt.ylabel('Average Age')
    plt.show()

def plot_age_distribution_area_chart(start_year, end_year):

    df_age = pd.read_csv(data, header=0)['Age']
    min_age, max_age = df_age.min(), df_age.max()
    years, age_yearly_distribution = generate_yearly_data(start_year, end_year, list(range(min_age, max_age + 1)))

    plt.fill_between(years, age_yearly_distribution, color='red', alpha=0.3)
    plt.title('Age Distribution of Medalists Over Time (Area Chart)')
    plt.xlabel('Year')
    plt.ylabel('Average Age')
    plt.show()
    
def top_countries_by_individual_team_line():
    df = pd.read_csv(data, header=0)
    top_10_countries = df.nlargest(10, 'All Medals')

    individual = "orange"
    team = "purple"

    # Plotting the line graph
    plt.plot(top_10_countries['Countries'], top_10_countries['Individual Sports'], color=individual, label='Individual Sports', marker='o')
    plt.plot(top_10_countries['Countries'], top_10_countries['Team Sports'], color=team, label='Team Sports', marker='o')

    plt.xlabel('Country')
    plt.ylabel('Number of Medals')
    plt.title('Top 10 Countries by Medals in Individual vs. Team Sports')
    plt.legend()
    plt.show()
    
def top_countries_by_individual_team_area():
    df = pd.read_csv(data, header=0)
    top_10_countries = df.nlargest(10, 'All Medals')

    individual = "orange"
    team = "purple"

    # Plotting the area graph
    plt.stackplot(top_10_countries['Countries'],
                  top_10_countries['Individual Sports'], top_10_countries['Team Sports'],
                  colors=[individual, team], labels=['Individual Sports', 'Team Sports'], alpha=0.7)

    plt.xlabel('Country')
    plt.ylabel('Number of Medals')
    plt.title('Top 10 Countries by Medals in Individual vs. Team Sports')
    plt.legend()
    plt.show()
    
def top_countries_by_medals_per_capita_line():
    # Get csv into a panda frame
    df = pd.read_csv(data, header=0)

    # Sort the DataFrame by medals per capita and get the top 10 countries
    top_10_countries = df.nlargest(10, 'All Medals')

    # Plotting the line chart
    plt.plot(top_10_countries['Countries'], top_10_countries['Medals per Capita'], marker='o')

    plt.xlabel('Country')
    plt.ylabel('Medals per Capita')
    plt.title('Top 10 Countries by Medals per Capita')
    plt.show()
    
def top_countries_by_medals_per_capita_area():
    # Get csv into a panda frame
    df = pd.read_csv(data, header=0)

    # Sort the DataFrame by medals per capita and get the top 10 countries
    top_10_countries = df.nlargest(10, 'All Medals')

    # Plotting the area chart
    plt.fill_between(top_10_countries['Countries'], top_10_countries['Medals per Capita'], color='skyblue', alpha=0.4, label='Medals per Capita')

    plt.xlabel('Country')
    plt.ylabel('Medals per Capita')
    plt.title('Top 10 Countries by Medals per Capita')
    plt.legend()
    plt.show()
    
def medals_by_continent_line():
    df = pd.read_csv(data, header=0)
    
    # Group by continent and sum the medals
    continent_medals = df.groupby('Continent').sum()[['All Medals']]

    # Plotting the line chart
    plt.plot(continent_medals.index, continent_medals['All Medals'], marker='o')

    plt.xlabel('Continent')
    plt.ylabel('Number of Medals')
    plt.title('Medal Counts by Continent')
    plt.show()
    
def medals_by_continent_area():
    df = pd.read_csv(data, header=0)
    
    # Group by continent and sum the medals
    continent_medals = df.groupby('Continent').sum()[['All Medals']]

    # Plotting the area chart
    plt.fill_between(continent_medals.index, continent_medals['All Medals'], color='skyblue', alpha=0.4)

    plt.xlabel('Continent')
    plt.ylabel('Number of Medals')
    plt.title('Medal Counts by Continent')
    plt.show()


if __name__ == "__main__":
    # random_data()
    top_countries_by_medals_line()
    top_countries_by_medals_area()
    top_counties_by_gender_line()
    top_counties_by_gender_area()
    total_medals_by_sport_line()
    total_medals_by_sport_area()
    compare_summer_winter_line()
    compare_summer_winter_area()
    plot_yearly_medal_count_line_chart('United Kingdom', 1960, 2020)
    plot_yearly_medal_count_area_chart('United Kingdom', 1960, 2020)
    plot_sport_medal_count_line_chart('100m Sprint', 1960, 2020)
    plot_sport_medal_count_area_chart('100m Sprint', 1960, 2020)
    plot_age_distribution_line_chart(1960, 2020)
    plot_age_distribution_area_chart(1960, 2020)
    top_countries_by_individual_team_line()
    top_countries_by_individual_team_area()
    top_countries_by_medals_per_capita_line()
    top_countries_by_medals_per_capita_area()
    medals_by_continent_line()
    medals_by_continent_area()
    #show_graph('Gold Medals')
    #show_graph('Silver Medals')
    #show_graph('Bronze Medals')