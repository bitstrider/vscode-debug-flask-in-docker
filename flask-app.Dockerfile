FROM python:3.6

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

CMD flask run --host=0.0.0.0 --no-debugger --no-reload
