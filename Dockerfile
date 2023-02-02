FROM python:3.10

ADD client.py .

EXPOSE 9898

CMD ["python", "client.py"]
