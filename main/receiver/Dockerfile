FROM python:3.8
RUN pip install flask
RUN pip install Flask-SQLAlchemy
WORKDIR /main
COPY receiver.py /main/receiver.py
EXPOSE 5000
CMD ["python", "/main/receiver.py"]