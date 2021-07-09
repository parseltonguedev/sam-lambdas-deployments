FROM jenkins/jenkins:alpine
USER root
RUN apk add docker
RUN apk add py-pip
RUN apk add python3-dev libffi-dev openssl-dev gcc libc-dev make