FROM ubuntu:latest

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y --no-install-recommends make
RUN make prereqs
RUN make build
#RUN make test

# Копируем весь проект в контейнер


# Команда для запуска скрипта
WORKDIR /app/entrypoint
ENTRYPOINT ["make"]

