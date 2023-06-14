import os
from src.config import Config
from src.apps.logger import Logger
from datetime import datetime
import logging
import json
import time
import glob
from getpass import getpass
import sys
from pymongo import MongoClient
import subprocess

__all__ = ['pyra_connection','pyra_connection_database']

class PyraConnector:
    """
    Description:
    """

    def __init__(self) -> None:
        """
        Constructor Method
        :param: none
        :return: none
        """
        # Version
        self.pyra_version = Config.PYRA_VERSION

        # Mongo Config
        self.__username = Config.MONGO_USERNAME
        self.__password = Config.MONGO_PASSWORD
        self.__host = Config.MONGO_HOST
        self.__port = Config.MONGO_PORT
        self.__db = Config.MONGO_DATABASE
        self.__collection = Config.MONGO_COLLECTION
        # Logger Config
        self.logger = Logger("PyraConnection")


    def pyra_connection(self) -> None:

        print(f"""
(       ) (             
)\ ) ( /( )\ )   (      
(()/( )\()|()/(   )\     
/(_)|(_)\ /(_)|(((_)(   
(_))__ ((_|_))  )\ _ )\  
| _ \ \ / / _ \ (_)_\(_) 
|  _/\ V /|   /  / _ \   
|_|   |_| |_|_\ /_/ \_\  
                Made by mkdemir 
                {self.pyra_version}
        """)

        try:
            if self.__username == '' and self.__password == '':
                client = MongoClient(f"mongodb://{self.__host}:{self.__port}/")
            else:    
                client = MongoClient(f"mongodb://{self.__username}:{self.__password}@{self.__host}:{self.__port}/")

            if client.server_info():
                print("\n**************")
                print("Connecting...")
                print("**************\n")
                return client
            else:
                print("Unable to connect...")

        except Exception as e:
            self.logger.log(logging.ERROR, "An unexpected error occurred => {}".format(e))

    def pyra_connection_database(self, db = None, collection = None):
        try:
            if db == None and collection == None:
                client = self.pyra_connection()
                db = client[f"{self.__db}"]
                collection = db[f"{self.__collection}"]
                return client,db, collection
        
            else:
                client = self.pyra_connection()
                db = client[f"{db}"]
                collection = db[f"{collection}"]
                return client,db, collection

        except ValueError as ve:
            self.logger.log(logging.INFO, "Incorrect data => {}".format(ve))
        except KeyError as ke:
            self.logger.log(logging.INFO, "Invalid key => {}".format(ke))
        except Exception as e:
            self.logger.log(logging.ERROR, "An unexpected error occurred => {}".format(e))