FROM python:3.12-slim

RUN pip install --upgrade pip 

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV MONGO_URL_ID="mongodb+srv://rohitprabhu:roomstop123@roomstopcluster.w3zqf.mongodb.net/?retryWrites=true&w=majority&appName=RoomStopCluster"
ENV DB_NAME_ID="roomstop"
ENV COLLECTION_NAME_ID="users"

ENTRYPOINT ["python"]

CMD ["app.py"]

