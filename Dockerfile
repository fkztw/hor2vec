FROM python:3.8-alpine

RUN pip3 install flit

RUN addgroup -S hor2vec && adduser -S -G hor2vec hor2vec
USER hor2vec

WORKDIR /home/hor2vec
ENV PATH="/home/hor2vec/.local/bin:${PATH}"
ADD . /home/hor2vec
RUN flit install

WORKDIR /srv/work/

ENTRYPOINT ["hor2vec"]
