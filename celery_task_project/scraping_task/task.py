# your_app_name/tasks.py

from celery import shared_task
from .models import ScrapedData
import requests
from bs4 import BeautifulSoup

@shared_task
def scrape_and_save_data():
    # Scrape data
    response = requests.get('https://geonode.com/free-proxy-list')
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        data_elements = soup.find_all('div', class_='data')
        scraped_data = []

        for element in data_elements:
            ip = element.find('span', class_='ip').text.strip()
            port = element.find('span', class_='port').text.strip()
            protocol = element.find('span', class_='protocol').text.strip()
            country = element.find('span', class_='country').text.strip()
            uptime = element.find('span', class_='uptime').text.strip()

            scraped_data.append((ip, port, protocol, country, uptime))

        # Save data to database
        for ip, port, protocol, country, uptime in scraped_data:
            ScrapedData.objects.create(ip=ip, port=port, protocol=protocol, country=country, uptime=uptime)
