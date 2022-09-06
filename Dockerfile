FROM rasa/rasa:latest
WORKDIR '/app'
COPY requirements.txt /app
USER root
# WORKDIR /app
# COPY . /app
RUN #pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
RUN pip install -r requirements.txt -i http://nexus.nevint.com/repository/pypi-all/simple --trusted-host nexus.nevint.com
RUN curl -fsSL  https://github.com/explosion/spacy-models/releases/download/zh_core_web_md-3.4.0/zh_core_web_md-3.4.0.tar.gz -o zh_core_web_md-3.4.0.tar.gz
# RUN python -m spacy download zh_core_web_md
RUN pip install zh_core_web_md-3.4.0.tar.gz && rm zh_core_web_md-3.4.0.tar.gz
COPY ./data /app/data
#COPY ./models /app/models
COPY ./start.sh /app
RUN rasa train
VOLUME /app
VOLUME /app/data
VOLUME /app/models
ENTRYPOINT ["/bin/bash"]
CMD ["start.sh"]
#CMD ["run","-m","/app/models","--enable-api","--cors","*","--debug" ,"--endpoints", "endpoints.yml", "--log-file", "out.log", "--debug"]
