FROM ubuntu:16.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    curl \
    apt-transport-https \
    ca-certificates \
    sudo \
    gnupg-agent \
    software-properties-common \
    build-essential \
    zlib1g-dev \
    zstd \
    gettext \
    liblttng-ust0 \
    libcurl4-openssl-dev \
    inetutils-ping \
    jq \
    wget \
    dirmngr \
    openssh-client \
    python3-pip \
  && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg \
  && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null \
  && apt-get update \
  && apt-get install -y docker-ce docker-ce-cli containerd.io --no-install-recommends --allow-unauthenticated \
  && curl -L "https://github.com/docker/compose/releases/download/1.29.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
  && chmod +x /usr/local/bin/docker-compose \
  && ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /tmp/*


RUN useradd -rm -d /home/runner -s /bin/bash -u 1000 -p "$(openssl passwd -1 runner)" runner

WORKDIR /home/runner

COPY ./setup-runner.sh .

COPY ./ie-app-publisher-linux /usr/bin/

RUN usermod -aG docker runner

USER runner

CMD ["/bin/sh", "/home/runner/setup-runner.sh"]
#CMD ["tail", "-f", "/dev/null"]




