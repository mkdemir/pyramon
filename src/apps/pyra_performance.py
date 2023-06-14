import os
from src.config import Config
from src.apps.logger import Logger
from src.apps.pyra_connection import PyraConnector
from src.apps.pyra_data import PyraData
from datetime import datetime
import logging
import json
import time
import glob
from getpass import getpass
import sys
from pymongo import MongoClient
import subprocess

__all__ = ['dbstats', 'dbserverStatus','dbcurrentOp']

class PyraPerformance:
    """
    Description:
    """

    def __init__(self) -> None:
        """
        Constructor Method
        :param: none
        :return: none
        """
       
        # Logger Config
        self.logger = Logger("PYRA")

        # Data 
        self.pyra_data = PyraData()

        # Data List
        self.data_list = []
										

    def dbstats(self):

        try:
            client,db, collection = PyraConnector().pyra_connection_database()
            stats = db.command('dbstats')
            print("\ndbstats:")
            print(stats)
            self.pyra_data.pyra_performance_data("dbstats",stats)

        except ValueError as ve:
            self.logger.log(logging.INFO, "Incorrect data => {}".format(ve))
        except KeyError as ke:
            self.logger.log(logging.INFO, "Invalid key => {}".format(ke))
        except Exception as e:
            self.logger.log(logging.ERROR, "An unexpected error occurred => {}".format(e))
        
    def dbserverStatus(self):

        try:
            client,db, collection = PyraConnector().pyra_connection_database()
            server_status = db.command('serverStatus')
            print("\ndbserverStatus:")
            print(server_status)
            self.pyra_data.pyra_performance_data("dbstats",server_status)

        except ValueError as ve:
            self.logger.log(logging.INFO, "Incorrect data => {}".format(ve))
        except KeyError as ke:
            self.logger.log(logging.INFO, "Invalid key => {}".format(ke))
        except Exception as e:
            self.logger.log(logging.ERROR, "An unexpected error occurred => {}".format(e))

    def dbcurrentOp(self):

        try:
            client,db, collection = PyraConnector().pyra_connection_database()
            current_ops = client.admin.command('currentOp')
            print("\ndbcurrentOp:")
            print(current_ops)
            self.pyra_data.pyra_performance_data("dbstats",current_ops)

        except Exception as e:
            self.logger.log(logging.ERROR, "An unexpected error occurred => {}".format(e))
