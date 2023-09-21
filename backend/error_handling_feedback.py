```python
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def handle_error(error):
    """
    Function to handle errors and log them.
    """
    logger.error(f"An error occurred: {error}")

def handle_success(message):
    """
    Function to handle success messages and log them.
    """
    logger.info(f"Success: {message}")

def handle_progress(progress):
    """
    Function to handle progress updates and log them.
    """
    logger.info(f"Progress: {progress}%")
```