FROM python:3.8
RUN pip install requests
WORKDIR /main
COPY sender.py /main/sender.py
CMD ["python", "/main/sender.py"]