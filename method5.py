"""
My Part for the project of group 8
"""

import pandas as pd
import matplotlib.pyplot as plt

ag_df = pd.read_csv("file.csv")


def method5(countries):
    """
    This method receives a list of countries or a single country as input and creates a plot of the
    total output quantity over time for the selected countries. The plot includes a line for each 
    country and the x-axis is the year.
    """
    try:
        if isinstance(countries, list):
            df_countries = ag_df[ag_df["Entity"].isin(countries)]
            total_output = (
                df_countries.groupby(["Entity", "Year"])["output_quantity"]
                .sum()
                .reset_index()
            )
            for country in countries:
                country_df = total_output[total_output["Entity"] == country]
                plt.plot(
                    country_df["Year"], country_df["output_quantity"], label=country
                )
            plt.xlabel("Year")
            plt.ylabel("Output Quantity")
            plt.legend()
            plt.show()
        elif isinstance(countries, str):
            df_country = ag_df[ag_df["Entity"] == countries]
            total_output = (
                df_country.groupby("Year")["output_quantity"].sum().reset_index()
            )
            plt.plot(
                total_output["Year"], total_output["output_quantity"], label=countries
            )
            plt.xlabel("Year")
            plt.ylabel("Output Quantity")
            plt.legend()
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


method5(["Germany", "France"])
