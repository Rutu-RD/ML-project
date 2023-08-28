import os
import sys
from src.exception import customexception
from src.logger import logging
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass 
@dataclass
class dataingestionconfiguration:
    train_data_path : str =os.path.join('Data_folder',"train.csv")
    test_data_path : str =os.path.join('Data_folder',"test.csv")
    raw_data_path : str =os.path.join('Data_folder',"raw_data.csv")
    
class dataingestion:
    def __init__(self):
        self.ingestion_config=dataingestionconfiguration()

    def begin_data_Ingestion(self):
        logging.info("entered Data Ingestion Method")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info("reading the dataset")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train Test split begins")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("ingestion is completed")

            return(self.ingestion_config.train_data_path,
                   self.ingestion_config.test_data_path)

        except Exception as e:
            raise customexception(e,sys)

if __name__=="__main__":
    obj=dataingestion()
    obj.begin_data_Ingestion()

