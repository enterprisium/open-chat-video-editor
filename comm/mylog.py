import logging
def build_logger():
    
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    return logging.getLogger(__name__)

logger = build_logger()
