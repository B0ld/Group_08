"""
Method 5
"""
import seaborn as sns
import matplotlib.pyplot as plt
from day1_phase2_hanna import DataDownloader

dd = DataDownloader()
df = dd.df

def method5(countries):
    """
    Receives a list of countries or a single country as input and creates a plot of the
    total output quantity over time for the selected countries.

    Parameters
    ---------------
    countries: str, list of str
        Countries of which a plot is created
        
    Returns
    ---------------
    Graph of the selected countries

    """
    try:
        if isinstance(countries, list):
            df_countries = df[df['Entity'].isin(countries)]
            total_output = df_countries.groupby(['Entity', 'Year'])['output_quantity']\
                .sum().reset_index()
            #Create the plot for each country
            plt.figure(figsize=(10, 6))
            ax_output = sns.lineplot(x='Year', y='output_quantity', hue='Entity', data=total_output)
            ax_output.set(xlabel='Year', ylabel='Output Quantity')
            ax_output.legend(loc='upper left', bbox_to_anchor=(1, 1))
            plt.show()
        elif isinstance(countries, str):
            df_country = df[df['Entity'] == countries]
            total_output = df_country.groupby('Year')['output_quantity'].sum().reset_index()
            #Create the plot for each country
            plt.figure(figsize=(10, 6))
            ax_output = sns.lineplot(x='Year', y='output_quantity', data=total_output)
            ax_output.set(xlabel='Year', ylabel='Output Quantity')
            ax_output.legend([countries], loc='upper left', bbox_to_anchor=(1, 1))
            plt.show()
        else:
            raise ValueError("Input should be a string or a list of strings")
    except ValueError as val_err:
        print(val_err)
    except FileNotFoundError:
        print("File not found")
    except Exception as ex:
        print(f"An error occurred: {ex}")
    else:
        print("Plot created successfully")
    finally:
        print("Execution complete\n")

method5(["Germany", "France", "United States"])
