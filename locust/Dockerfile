FROM python:3.6.9

ADD requirements.txt /src/
RUN pip install -r /src/requirements.txt

ADD . /src
WORKDIR /src/

CMD ["server"]
ENTRYPOINT ["/src/boot.sh"]