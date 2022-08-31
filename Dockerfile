FROM rasa/rasa:latest
WORKDIR '/app'
COPY . /app
USER root
# WORKDIR /app
# COPY . /app
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
RUN curl -fsSL  https://github.com/explosion/spacy-models/releases/download/zh_core_web_md-3.4.0/zh_core_web_md-3.4.0.tar.gz -o zh_core_web_md-3.4.0.tar.gz
# RUN python -m spacy download zh_core_web_md
RUN pip install zh_core_web_md-3.4.0.tar.gz
COPY ./data /app/data
RUN rasa train
VOLUME /app
VOLUME /app/data
VOLUME /app/models
CMD ["run","-m","/app/models","--enable-api","--cors","*","--debug" ,"--endpoints", "endpoints.yml", "--log-file", "out.log", "--debug"]
