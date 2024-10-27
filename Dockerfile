FROM ubuntu:latest



WORKDIR /app

COPY . .


RUN apt-get update && apt-get install -y --no-install-recommends make g++ #git
RUN make prereqs
RUN make build
RUN make test


WORKDIR /app/entrypoint
ENTRYPOINT ["make"]
