# Celery Task for Web Scraping and Database Saving

This project demonstrates the implementation of a Celery task in a Django project to scrape data from a website and save it into a SQLite database. The Celery task is scheduled to run periodically using Celery Beat.

## Setup

- Ensure you have Python and Django installed on your system.
- Install Celery and other dependencies using `pip`.

## Celery Configuration

- Configure Celery in your Django project by creating a `celery.py` file.
- Define the Celery tasks and specify the schedule using Celery Beat.

## Scraping Logic

- Implement the scraping logic using libraries like `requests` and `BeautifulSoup`.
- Fetch HTML content from the website and extract the desired data.
- Ensure error handling and robust parsing.

## Database Configuration

- Configure your Django project to use SQLite as the database backend.
- Define Django models to represent the scraped data.

## Model Definition

- Define a Django model (`ScrapedData`) with fields corresponding to the scraped data.
- Ensure that the model is properly migrated to the database.

## Running the Project

- Start a Celery worker to execute tasks in the background.
- Run the Django development server to serve the application.

## Error Handling

- Test error handling by causing intentional errors in the scraping logic.
- Verify that Celery retries failed tasks according to the configured settings.
- Monitor Celery logs and RabbitMQ logs for any errors or warnings.
