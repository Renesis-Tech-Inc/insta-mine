from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings

# Initialize FastAPI application
app = FastAPI(
    title="InstaMiner - Instagram User Profile Data Miner",
    description="A tool to fetch Instagram user details using their username or Instagram URL. This project helps you gather basic information about an Instagram profile quickly and efficiently.",
    version="1.0.0",
    docs_url="/docs",  # Endpoint for Swagger UI documentation
    redoc_url=None,  # Disable ReDoc documentation
)


async def startup() -> None:
    """Event handler for application startup."""
    print("Starting up...")


async def shutdown() -> None:
    """Event handler for application shutdown."""
    print("Shutting down...")


# Register startup and shutdown event handlers
app.add_event_handler("startup", startup)
app.add_event_handler("shutdown", shutdown)

# CORS middleware configuration
origins = ["*"]  # Replace with your allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Base route for application health check
@app.get("/")
async def health_check():
    """
    Endpoint for checking the health status of the application.

    Returns:
        dict: A dictionary with application metadata and health status.
    """
    try:
        return {
            "app": settings.APP_TITLE,
            "description": settings.APP_DESCRIPTION,
            "version": settings.APP_VERSION,
            "environment": settings.APP_ENV,
        }
    except Exception as e:
        return {"status": "unhealthy", "message": str(e)}


# Health Check Route
@app.get("/health")
async def health_check():
    """
    Endpoint for checking the health status of the application.

    Returns:
        dict: A dictionary indicating the health status of the application.
    """
    try:
        return {"status": "healthy"}
    except Exception as e:
        return {"status": "unhealthy", "message": str(e)}


# Import routers from domain functionalities
from modules.miner.endpoints import router

# Mount routers onto the main application
app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI application using Uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.PORT,
        reload=settings.APP_ENV == "development",
        log_level="info",
    )
