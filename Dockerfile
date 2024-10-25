FROM ubuntu:latest



WORKDIR /app

COPY . .

#COPY requirements.txt .
#COPY model.py .
#COPY Makefile ./
#COPY src/image_converter.cpp  /app/
#COPY entrypoint/Makefile ./entrypoint/
#COPY libs/opencv4 /app/libs
#COPY libs/opencv_contrib4 /app/libs

#COPY opencv4 ./opencv4/


RUN apt-get update && apt-get install -y --no-install-recommends make g++ #git
RUN make prereqs
RUN make build
#RUN make test

# Копируем весь проект в контейнер


# Команда для запуска скрипта
WORKDIR /app/entrypoint
ENTRYPOINT ["make"]

