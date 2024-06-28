import sqlite3
import logging
import sys
import os
import pandas as pd

def logger_setup():
  '''
  creates `logging.log` file to record logging activity and logs to terminal.
  returns `logger` to be used for logging activity
  '''
  logger = logging.getLogger(__name__)
  logging.basicConfig(
    handlers=[logging.FileHandler("logging.log"),
              logging.StreamHandler(sys.stdout)],
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s') 
  
  return logger



def db_connection(logger,db_name:str):
  '''
  establish connection with  `db_name` and returns `connection` and `cursor`.\n\n
  raise Exception if `db_name` does not exist
  '''
  logger.info('Establishing db connection.')
  if os.path.exists(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
  else:
    logger.warning(f'{db_name} does not exist in file.')
    raise Exception(f'{db_name} does not exist in file.')

  return connection , cursor


def check_expected_table_exist(logger,cursor,expected_table_list):
  '''
  check if expected table name is in the database\n\n
  raise `Exception` if expected table is empty or not present
  '''
  logger.info('Checking expected table present in database.')
  table_list = cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'").fetchall()

  if len(expected_table_list) == 0:
      logger.warning('Expected table name is empty.')
      raise Exception("Expected table name is empty.")
  for table in expected_table_list:
    if (table not in table_list):
      logger.warning(f'Table Needed * {table[0]} * is not present in DB.')
      raise Exception(f"Table Needed * {table[0]} * is not present in DB.")
    
def execute_query(logger,connection,sql_query):
  '''
  execute sql query and returns a pd.Dataframe\n\n
  raise `Exception` if found error in SQL statement.
  '''
  logger.info('Executing SQL query on database.')
  try:
    merged_query = pd.read_sql_query(
      sql= sql_query,
      con= connection
    )
  except Exception as e:
     logger.warning(f'Error found in SQL statement:\n{e}')
     raise Exception(f'Error found in SQL statement:\n{e}')
  
  return merged_query