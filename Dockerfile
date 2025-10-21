FROM python:3.13-slim

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
run pip install "django<6"
copy src /src
WORKDIR src

CMD ["python", "manage.py","runserver"]