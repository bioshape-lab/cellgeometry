# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Run APT installs
RUN apt update && apt install -y git build-essential curl

# Set the working directory to /app
WORKDIR /app

# Copy the Poetry files into the container and install dependencies
COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

RUN pip install git+https://github.com/geomstats/geomstats.git && \
    pip install pacmap open3d

# Copy the entire project directory into the container
COPY cellgeometry .

# Expose the port that Streamlit listens on (8501 by default)
EXPOSE 8501

# Set the PYTHONPATH environment variable
ENV PYTHONPATH "${PYTHONPATH}:/app/utils"

# The HEALTHCHECK instruction tells Docker how to test a container to check that it is still working
# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Set the entrypoint command to run the Streamlit app
CMD ["streamlit", "run", "Hello.py", "--server.port=8501"]

