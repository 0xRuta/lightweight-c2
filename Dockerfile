FROM python:3.8-slim

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/0xRuta/lightweight-c2.git

WORKDIR /lightweight-c2

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
