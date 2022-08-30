#FROM rasa/rasa:latest
FROM ubuntu:20.04
# USER root  # 权限不足时打开

COPY . /app
WORKDIR /app
RUN apt-get install -y gcc && RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

ENTRYPOINT ["rasa"]
CMD ["run", "--cors", "*"]
