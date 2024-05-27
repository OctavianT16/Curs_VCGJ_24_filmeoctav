FROM python:3.10-alpine

ENV FLASK_APP main
#ENV FLASK_CONFIG = docker

#3.8 booster
#RUN useradd -rm -d /home/site -s /bin/bash -g root -G sudo -u 1001 site

#3.8 alpine
RUN adduser -D main

USER main

WORKDIR /home/filme/

COPY app app
COPY static static
COPY templates templates
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY main.py main.py
USER root   
RUN chmod -R 777 static

RUN python3 -m venv .venv
RUN chmod -R g+x .venv
RUN .venv/bin/pip install -r quickrequirements.txt


# runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
#CMD sh
