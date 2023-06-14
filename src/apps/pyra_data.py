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
import subprocess
import json

__all__ = ['is_there_dir', 'pyra_data']

class PyraData:
    """
    Description:
    """

    def __init__(self) -> None:
        """
        Constructor Method
        :param: none
        :return: none
        """

        # Data Config
        self.__data_dir = Config.DATA_DIR
        
        # Logger Config
        self.logger = Logger("pyra_data")

        # Date
        self.date = datetime.today().strftime('%Y-%m-%d')

    def is_there_data_dir(self):

        try:
            directory_path = self.__data_dir
            if not os.path.exists(directory_path):
                os.makedirs(directory_path )
                print("Data Directory created:", directory_path)
        except Exception as e:
            self.logger.log(logging.ERROR, "An unexpected error occurred => {}".format(e))
                
    def pyra_data(self, type, data_list):
        try:
            self.is_there_data_dir()
            file_name = self.__data_dir + f"{type}" + "-" + self.date +  ".log"
            
            existing_data_set = set()
            if os.path.exists(file_name):
                with open(file_name, "r", encoding="utf-8") as f:
                    existing_data = f.read()
                    existing_data_set = set(existing_data.split("\n"))

            with open(file_name, "a", encoding="utf-8") as f:
                for data in data_list:
                    if data not in existing_data_set:
                        f.write(data)
                        existing_data_set.add(data)

        except Exception as e:
            self.logger.log(logging.ERROR, "An unexpected error occurred => {}".format(e))

    def pyra_performance_data(self, type, data):
        try:
            self.is_there_data_dir()
            file_name = self.__data_dir + "Performance" + "-" +  f"{type}" + "-" + self.date +  ".log"
            
            with open(file_name, "a", encoding="utf-8") as f:
                f.write(type + "\n")
                json.dump(data, f, default=str)
                f.write("\n")

        except Exception as e:
            self.logger.log(logging.ERROR, "An unexpected error occurred => {}".format(e))

