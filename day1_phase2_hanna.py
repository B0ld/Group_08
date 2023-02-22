import os
import pandas as pd
import urllib.request

class DataDownloader:
    def __init__(self, url):
        self.url = url
        self.directory = self.get_downloads_directory()
        self.df = self.download_and_read_file()

    def get_downloads_directory(self):
        directory = 'downloads'
        root_directory = os.path.abspath(os.path.dirname(__file__))
        downloads_directory = os.path.join(root_directory, directory)
        return downloads_directory

    def download_and_read_file(self):
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

url = 'https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Agricultural%20total%20factor%20productivity%20(USDA)/Agricultural%20total%20factor%20productivity%20(USDA).csv'
dd = DataDownloader(url)
print(dd.df.head())