# Stage 1: Build stage
FROM python:3.12-slim as builder

# Set environment variables
ENV POETRY_VERSION=1.6.1
ENV POETRY_HOME=/opt/poetry
ENV PATH=$POETRY_HOME/bin:$PATH

# Install Poetry
RUN python -m pip install --upgrade pip \
    && pip install poetry==$POETRY_VERSION

# Create a directory for the application
WORKDIR /app

# Copy only the necessary files to install dependencies
COPY poetry.lock pyproject.toml ./

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Stage 2: Final stage
FROM python:3.12-slim

# Set environment variables
ENV APP_HOME=/app
ENV POETRY_HOME=/opt/poetry
ENV PATH=$POETRY_HOME/bin:$PATH

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a directory for the application
WORKDIR $APP_HOME

# Copy installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn

# Copy the application code
COPY . .

# Set the working directory to src
WORKDIR /app/src

# Expose the application port
EXPOSE 8000

# Run the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
