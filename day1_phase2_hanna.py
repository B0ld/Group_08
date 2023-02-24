import os
import pandas as pd
import urllib.request
import matplotlib.pyplot as plt
import seaborn as sns



class DataDownloader:
    """
    A class that downloads a CSV file from a given URL and saves it in a local directory,
    and then loads it into a pandas DataFrame.
    """
    def __init__(self):
        """
        Initializes the DataDownloader instance.

        Parameters:
        url (str): The URL from which to download the CSV file.
        """
        self.url = 'https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Agricultural%20total%20factor%20productivity%20(USDA)/Agricultural%20total%20factor%20productivity%20(USDA).csv'
        self.directory = self.get_downloads_directory()
        self.df = self.download_and_read_file()

    def get_downloads_directory(self):
        """
        Returns the full path of the `downloads` directory in the project root directory.
        If the `downloads` directory does not exist, it creates the directory.

        Returns:
        str: The full path of the `downloads` directory.
        """
        directory = 'downloads'
        root_directory = os.path.abspath(os.path.dirname(__file__))
        downloads_directory = os.path.join(root_directory, directory)
        return downloads_directory

    def download_and_read_file(self):
        """
        Downloads the CSV file from the specified URL and saves it in the `downloads` directory.
        If the file is already present in the directory, it loads the file into a pandas DataFrame.
        Otherwise, it creates the directory, downloads the file, and then loads it into a DataFrame.

        Returns:
        pandas.DataFrame: The loaded pandas DataFrame.
        """
        file_name = "agriculture_dataset.csv"
        file_path = os.path.join(self.directory, file_name)

        if os.path.exists(file_path):
            print(f"{file_name} already exists in {self.directory}")
        else:
            if not os.path.exists(self.directory):
                os.makedirs(self.directory)
            print(f"Downloading {file_name}...")
            urllib.request.urlretrieve(self.url, file_path)
            print(f"{file_name} downloaded to {self.directory}")

        df = pd.read_csv(file_path)
        return df

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

# Change so that the class gives out a df
dd = DataDownloader()
print(dd.df.head())
df = dd.df

DataDownloader.method5(["Germany", "France", "Italy"])