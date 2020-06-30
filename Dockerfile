FROM python

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install numpy flask matplotlib

EXPOSE 5001

ENTRYPOINT [ "python"]
 
CMD [ "flaskapp.py" ]