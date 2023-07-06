# [1]
FROM python:3.8-slim-buster 

WORKDIR /app

COPY . .

COPY assignment-391215-firebase-adminsdk-5prid-8874894646.json /app/assignment-391215-firebase-adminsdk-5prid-8874894646.json

ENV GOOGLE_APPLICATION_CREDENTIALS /app/assignment-391215-firebase-adminsdk-5prid-8874894646.json qq

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5002

CMD ["python3", "-m", "c3", "run", "--host=0.0.0.0","--port=5002"] 

# References 
# [1] 	Docker Inc, "Build your Python image," Docker Inc, [Online]. Available: https://docs.docker.com/language/python/build-images/. [Accessed 04 July 2023].