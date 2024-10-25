FROM ubuntu:latest



WORKDIR /app

COPY requirements.txt .
COPY model.py .
COPY image_converter.cpp .
COPY Makefile .
COPY entrypoint/Makefile ./entrypoint/


RUN apt-get update && apt-get install -y make 
RUN make prereqs
# RUN make build
#RUN make test

# Копируем весь проект в контейнер
COPY . .

# Команда для запуска скрипта
WORKDIR /app/entrypoint
ENTRYPOINT ["make"]

