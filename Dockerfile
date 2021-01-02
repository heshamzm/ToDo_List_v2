FROM python:3.7-alpine
RUN mkdir /to_do_tasks
WORKDIR /to_do_tasks
ADD requirements.txt .
RUN pip3 install -r requirements.txt
COPY app/ .
ENTRYPOINT ["sh"]