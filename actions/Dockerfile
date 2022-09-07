FROM rasa/rasa-sdk:latest
WORKDIR /app
COPY requirements.txt requirements.txt
USER root
RUN pip install --verbose -r requirements.txt -i http://nexus.nevint.com/repository/pypi-all/simple --trusted-host nexus.nevint.com
COPY ./actions /app/actions
EXPOSE 5055
USER 1001
#ENTRYPOINT ["/bin/bash"]
#CMD ["rasa run actions"]