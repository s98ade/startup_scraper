import logging
from logging.handlers import RotatingFileHandler


class Logging:
    def __init__(self, log_file='data/logs/log_entries.log', max_bytes=5*1024*1024):
        self.log_file = log_file
        self.max_bytes = max_bytes
        
        self.log = logging.getLogger('ScrapyLog') # create log object
        
        self.log.setLevel(logging.DEBUG) #set log level for log object
        
        # defining log format
        format = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
       
        # defining log file handler (max amount) 
        log_handler = RotatingFileHandler(
            self.log_file,
            maxBytes=self.max_bytes
        )
        
        log_handler.setFormatter(format)
        
        self.log.addHandler(log_handler)
        
    
    def get_logger(self):
        return self.log