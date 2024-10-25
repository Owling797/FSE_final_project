FROM python:3.9-slim as compiler
ENV PYTHONUNBUFFERED 1

WORKDIR /app
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -Ur requirements.txt


# Копируем весь проект в контейнер
# пока убрал

FROM python:3.9-slim as runner
WORKDIR /app/
COPY --from=compiler /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY . /app/

# Команда для запуска скрипта
CMD ["python3", "model.py", "./tresh", "./out.fuck", "./ft_resnet_10e.pt"]
