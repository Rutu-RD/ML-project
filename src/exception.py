import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    #to get exeception at which line and what is it 
    
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename   ##to get filename
    error_message="error occured at python script name [{0}] , in line [{1}] , error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))

    return(error_message)


    

    

class customexception(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message    




if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("divide by zero")
        raise customexception(e,sys)


     