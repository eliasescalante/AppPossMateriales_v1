import logging

def setup_logging():
    """
    Configura el logging para la aplicación.
    """
    logging.basicConfig(
        filename='server.log',  
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Crea un logger
    logger = logging.getLogger(__name__)
    return logger
