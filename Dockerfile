FROM repo.vps.com.vn:8082/proxy/library/python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY pip.conf /etc/pip.conf
RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "main.py"]