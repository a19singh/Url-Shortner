FROM python:alpine3.6
COPY . /urlShortner
WORKDIR /urlShortner
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]
