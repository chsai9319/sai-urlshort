#init a base image (Alpine -> Small Linux distro)
FROM python:3.6.7-alpine
#define the present working directory
WORKDIR /sai-urlshort
#copy contents into present working dir
COPY .  /sai-urlshort
#installing dependencies of Flask
RUN pip install -r requirements.txt
#define command to start container


EXPOSE 5000
CMD ["python","app.py","--host=0.0.0.0"]
