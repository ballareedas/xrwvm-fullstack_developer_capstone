# FROM python:3.9.18-slim-bookworm


# WORKDIR /python-docker

# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt
# COPY . .
# RUN ls
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
FROM python:3.9.18-slim-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "app.py"]

