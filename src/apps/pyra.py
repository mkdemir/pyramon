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

__all__ = ['get_query']

class Pyra:
    """
    Description: this class sends the queries you want to search on the mongo db

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

    def get_query(self, db = None, collection= None) -> json:
        try:
            self.db, self.collection = PyraConnector().pyra_connection_database(db, collection)
            query = {"Key": "Query"}
            
            result = self.collection.find(query).sort("Timestamp",-1).limit(2)

            try:
                for doc in result:
                    timestamp = doc['Timestamp'].time 
                    timestamp_dt = datetime.fromtimestamp(timestamp) 
                    timestamp_str = timestamp_dt.strftime('%Y-%m-%d %H:%M:%S') 

                    data = f"{timestamp_str},{doc['Key']},{doc['Name']},{doc['Author']}\n"
                    self.data_list.append(data)
                self.pyra_data.pyra_data("Query",self.data_list)
               
            
            except ValueError as ve:
                self.logger.log(logging.INFO, "Incorrect data => {}".format(ve))
            except KeyError as ke:
                self.logger.log(logging.INFO, "Invalid key => {}".format(ke))
            except Exception as e:
                self.logger.log(logging.ERROR, "An unexpected error occurred => {}".format(e))

        except ValueError as ve:
            self.logger.log(logging.INFO, "Incorrect data => {}".format(ve))
        except KeyError as ke:
            self.logger.log(logging.INFO, "Invalid key => {}".format(ke))
        except Exception as e:
            self.logger.log(logging.ERROR, "An unexpected error occurred => {}".format(e))
