FROM python:3

ADD test.py /

RUN pip install web3 py-solc

CMD [ "python", "./test.py" ]
