import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from src.logger import logging
from src.exception import customexception

@dataclass
class Data_Trandformation_configuration:
    preprocessor_obj_filrpath=os.path.join("Data_folder",'preprocessor.pkl')

class data_Trandformation:
    def __init__(self):
        self.data_transformation_config=Data_Trandformation_configuration()

    def get_data_transformer_object(self):
        '''
        this function is responsible for data transformation based on different types of data
        '''
        
        
        try:
            numerical_cols=['writing_score','reading_score']
            categorical_cols=["gender",
                              "race_ethinicity",
                              "parental_levle_of_education",
                              "lunch",
                              "test_preparation_course"
                              ]
            numerical_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scalar",StandardScaler()),
                    ]
            )
            logging.info("categorical cols standard scaling completed")
            categorical_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scalar",StandardScaler())
                ]
            )
            logging.info("categorical cols encoding completed")
            preprocessor=ColumnTransformer(
                [
                ("numerical_columns",numerical_pipeline,numerical_cols),
                ("categorical_columns",categorical_pipeline,categorical_cols)

                ]
            )
            return(preprocessor)
        except Exception as e:
            raise customexception(e,sys)

    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("reading test and train data ")

            logging.info("obtaining prepocessing object")
            preprocess_obj=self.get_data_transformer_object()
            target_column="math_score"
            
        except:
            pass