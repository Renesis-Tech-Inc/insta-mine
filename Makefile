# Makefile for Python project

# Command to format Python code using Black
format:
	@echo "Formatting Python code using Black..."
	black .

# Command to run the main Python script
run:
	@echo "Running the Python application..."
	python -B src/main.py
 