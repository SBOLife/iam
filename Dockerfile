FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip \
    && pip install .

EXPOSE 8000

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
CMD ["/app/entrypoint.sh"]


