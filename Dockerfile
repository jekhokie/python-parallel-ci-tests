FROM jenkins/ssh-slave

RUN apt-get update && apt-get install -y software-properties-common
RUN apt-get update && apt-get install -y \
    python-pip
RUN pip install virtualenv
