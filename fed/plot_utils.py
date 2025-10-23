import matplotlib.pyplot as plt
import pandas as pd

def plot_gdp_trends(df):
    """
    Plot GDP trends over time for all countries in the dataframe.
    
    Parameters:
    df : pandas DataFrame with columns ['Country Name', 'Year', 'GDP']
         (after reshaping from wide to long format)
    """
    plt.figure(figsize=(14, 8))
    
    # Get all unique countries
    countries = df['Country Name'].unique()
    
    # Convert Year to numeric (in case it's a string)
    df['Year'] = pd.to_numeric(df['Year'])
    
    # Plot each country
    for country in countries:
        country_data = df[df['Country Name'] == country].sort_values('Year')
        plt.plot(country_data['Year'], country_data['GDP'], 
                marker='o', linewidth=2, label=country)
    
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('GDP (current US$)', fontsize=12)
    plt.title('GDP Development Over Time (2000-2022)', fontsize=14, fontweight='bold')
    plt.legend(loc='best', fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()