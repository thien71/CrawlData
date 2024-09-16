FROM python:3.9-slim
COPY . ./scraping
RUN pip install mysql-connector-python requests
WORKDIR ./scraping
CMD ["python", "crawl_data.py"]