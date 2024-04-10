# Use the official Python image as the base image
FROM python:3.11.9-bullseye

# Set the working directory in the container
WORKDIR /backend-fastapi
# Copy the poetry.lock and pyproject.toml files to the container
COPY poetry.lock pyproject.toml /backend-fastapi/
COPY . /backend-fastapi
# Install Poetry
RUN pip install poetry
# Install project dependencies
RUN poetry install --no-interaction --no-ansi


# Copy the rest of the application code to the container
EXPOSE ${PORT}

# Start the FastAPI application
CMD ["poetry", "run", "start"]
