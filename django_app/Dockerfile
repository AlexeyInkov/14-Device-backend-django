FROM python:3.11.9-slim
LABEL authors="AlexeyInkov"

WORKDIR backend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY db_device .

COPY script.sh .
RUN chmod +x ./script.sh
CMD ["./script.sh"]



