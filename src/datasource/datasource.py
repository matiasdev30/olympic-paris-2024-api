from bs4 import BeautifulSoup
import requests
from exceptions.exceptions import DataSourceError

class DataSource:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
    
    def fetch_html(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            raise DataSourceError(f"Failed to retrieve the page: {e}")

    def parse_html_games(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        container = soup.find('div', id='results-container')
        if not container:
            raise DataSourceError("Container with id 'results-container' not found.")
        return container
    
    def parse_html_records(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find("table", class_="medals olympics has-team-logos")
        if not table:
            raise DataSourceError("Table with class 'medals olympics has-team-logos' not found.")
        return table
