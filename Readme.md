Here is the updated README file with added Docker instructions:

---

# InstaMiner - Instagram User Profile Data Miner

## Project Overview

InstaMiner is a tool to fetch Instagram user details using their username or Instagram URL. This project helps you gather basic information about an Instagram profile quickly and efficiently. The application is built using FastAPI, a modern web framework for building APIs with Python.

## Features

- Fetch Instagram user details by providing a username or URL
- Retrieve information such as profile picture, bio, followers count, following count, and more
- API endpoints for easy integration with other applications

## API Endpoints

- `GET /`: Fetch Project description and details 
- `GET /health`: Health check endpoint to check the application status
- `GET /insta/profile?username_or_url=`: Fetch Instagram user details by providing the username

## Project Structure

```
insta-mine/
├── .env.example
├── .gitignore
├── Makefile
├── pyproject.toml
├── README.md
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── utils.py
│   │   └── base_model.py
│   ├── modules/
│   │   └── miner/
│   │       ├── __init__.py
│   │       ├── endpoints.py
│   │       ├── models.py
│   │       └── services.py
│   └── main.py

```

- `.env.example`: Example environment variables file
- `Makefile`: Makefile for running common commands
- `pyproject.toml`: Poetry configuration file for managing dependencies
- `src/`: Source code directory
  - `core/`: Core functionality modules
    - `config.py`: Application configuration management
    - `utils.py`: Utility functions
    - `base_model.py`: Base Pydantic model for responses
  - `modules/miner/`: Instagram user data fetching module
    - `endpoints.py`: API endpoints for fetching user data
    - `models.py`: Pydantic models for representing user data
    - `services.py`: Service layer for fetching user data from Instagram API
  - `main.py`: Main FastAPI application

## Development

### Running the Development Server

To run the development server:

```bash
make run-local
```

This will start the FastAPI server on `http://localhost:3000`.

### Formatting

To run the code formatting:

```bash
make format
```

This will format code using Black.

### Environment Variables

Before running the application, create a `.env` file based on the `.env.example` file and fill in the required environment variables.

## Docker

### Building the Docker Image

To build the Docker image:

```bash
make docker-build
```

### Running the Docker Container

To run the Docker container:

```bash
make docker-run
```

This command will start the container and expose it on port 3000.

### Stopping the Docker Container

To stop the Docker container:

```bash
make docker-stop
```

### Removing the Docker Container

To remove the Docker container:

```bash
make docker-remove
```

### Cleaning Docker Images

To remove the Docker image:

```bash
make docker-clean
```

### Rebuilding and Running the Docker Container

To rebuild and run the Docker container:

```bash
make docker-rebuild
```

## Contributing

Contributions are welcome! Please follow the existing code style and patterns. Ensure that all tests pass before submitting a pull request.
