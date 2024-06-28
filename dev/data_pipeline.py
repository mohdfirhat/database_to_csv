from functions import *

def main_ETL():
  # Define variables needed here
  db_name = 'cademycode.db'
  expected_table_list=[('cademycode_students',), ('cademycode_courses',), ('cademycode_student_jobs',)]
  sql_query = '''
        SELECT uuid,
            name,
            dob,
            sex,
            contact_info,
            num_course_taken,
            time_spent_hrs,
            hours_to_complete,
            cs.job_id,
            job_category,
            avg_salary,
            current_career_path_id,
            career_path_name
        FROM cademycode_students cs
        LEFT JOIN (
            SELECT DISTINCT job_id,job_category,avg_salary 
            FROM cademycode_student_jobs
            ) as csj
        ON cs.job_id = csj.job_id
        LEFT JOIN cademycode_courses cc
        ON cs.current_career_path_id = cc.career_path_id
    '''
  output_filename='test.csv'
  output_pathname = f'../prod/{output_filename}'

  # Setup logger and db connection. checks if need tablename exist
  logger = logger_setup()
  connection , cursor = db_connection(logger,db_name)
  check_expected_table_exist(logger,cursor,expected_table_list)

  # Query needed data from 3expected table using SQL query
  merged_query = execute_query(logger,connection,sql_query)

  # Close connetion and create output.csv at ../production
  connection.close()
  logger.info('Database connection closed.')
  merged_query.to_csv(output_pathname)
  logger.info(f'{output_filename} created at {output_pathname}')

if __name__ == "__main__":
    main_ETL()