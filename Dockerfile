# Use an official Python runtime as an image
FROM python:3.8-slim

# The EXPOSE instruction indicates the ports on which a container 
# will listen for connections
# Since Flask apps listen to port 5000 by default, we expose it
EXPOSE 7000

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction 
# creates a directory with this name if it doesn’t exist

RUN apt-get update && apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev gcc

WORKDIR /app1

### these two steps are in order to activate the virtual environment where poetry installed everything
ENV VIRTUAL_ENV=/app1/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY pyproject.toml poetry.lock /app1/
RUN pip install poetry
RUN pip install pyOpenSSL
RUN poetry install --no-root

# # Install any needed packages specified in requirements.txt
# COPY poetry.lock pyproject.toml /app/
# RUN pip install poetry
# RUN poetry install
# # these two steps arein order to activate the virtual environment where poetry installed everything
# ENV VIRTUAL_ENV=/root/.cache/pypoetry/virtualenvs/fa-preds-hYuym2R--py3.8
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"


# Run app.py when the container launches
COPY  .  /app1/
ENV PYTHONUNBUFFERED=1
CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=7000"]