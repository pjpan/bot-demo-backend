FROM rasa/rasa-sdk:latest
WORKDIR /app
COPY requirements.txt requirements.txt
USER root
RUN pip install --verbose -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
EXPOSE 5055
USER 1001