'''
Created on Aug 30, 2012

@author: sandeep
'''
import logging
import logging.handlers
import os
import params
def ensureDirectory(folder):
    """
    creates a folder at the path 'folder'
    """
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
    except OSError:
        pass

def loadLoggingDefaults():
    """
    loads the default logger with parameters.
    """
    ensureDirectory(params.LOG_FOLDER)
    logger = logging.getLogger()
    logger.setLevel(params.LOG_LEVEL)
    formatter = logging.Formatter('%(asctime)s  - %(filename)s - %(lineno)d - %(message)s','%m/%d/%Y %I:%M:%S %p')
    #logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG )
    handler = logging.handlers.RotatingFileHandler(params.LOG_FILE, maxBytes = params.LOG_MAX_SIZE, backupCount = params.LOG_BACKUPS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info("logging started")
    
def loadDefaults():
    loadLoggingDefaults()
    logging.info("loaded logging defaults")
    
    