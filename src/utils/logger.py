import logging
def logger_setup():
    logging.basicConfig(
        level =logging.INFO,
        force= True,
        format = "%(asctime)s - %(levelname)s - %(message)s",
        handlers = [logging.FileHandler("app.log"), logging.StreamHandler()]
)