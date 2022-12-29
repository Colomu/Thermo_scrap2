# Dockerfile, Image, Container

FROM python:3-alpine3.10
WORKDIR  /app
COPY . /app
RUN pip install ${PYTHON_PACKAGES}
EXPOSE 3000
CMD python ./thermo.py

