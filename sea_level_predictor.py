import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(
    df['Year'],
    df['CSIRO Adjusted Sea Level']
)
    slope, intercept, r_value, p_value, std_err = linregress(
    df['Year'],
    df['CSIRO Adjusted Sea Level']
)
    years = range(1880, 2051)
    predicted_sea_levels = [
    slope * year + intercept
    for year in years
]
    plt.plot(years, predicted_sea_levels)
    # Create first line of best fit
    recent_df = df[df['Year'] >= 2000]


    # Create second line of best fit
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
    recent_df['Year'],
    recent_df['CSIRO Adjusted Sea Level']
)
    recent_years = range(2000, 2051)
    recent_predicted_sea_levels = [
    slope_recent * year + intercept_recent
    for year in recent_years
]
    plt.plot(recent_years, recent_predicted_sea_levels)


    # Add labels and title

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()