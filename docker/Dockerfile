FROM python:3
ARG user=docker
ARG group=docker
ARG uid=1000
ARG gid=1000
ARG WORKINGDIR=/code
ENV PYTHONUNBUFFERED 1
RUN mkdir -p $WORKINGDIR \
  && chown ${uid}:${gid} $WORKINGDIR \
  && addgroup --gid ${gid} ${group} \
  && useradd --home-dir "$WORKINGDIR" --uid ${uid} --gid ${gid} --shell /bin/bash ${user}
WORKDIR $WORKINGDIR
COPY requirements.txt $WORKINGDIR
RUN pip install -r requirements.txt
# COPY code/ /code/