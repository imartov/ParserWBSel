FROM joyzoursky/python-chromedriver

WORKDIR /src
COPY requirements.txt /src
RUN pip install -r requirements.txt

COPY . /src

CMD ["python", "getpage.py"]