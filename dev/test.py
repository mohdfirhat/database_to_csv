import unittest
from data_pipeline import *

class TestDataPipeline(unittest.TestCase):
  def setUp(self) -> None:
    self.logger = logger_setup()
    self.db_name = 'cademycode.db'
    self.expected_table_list=[('cademycode_students',), ('cademycode_courses',), ('cademycode_student_jobs',)]
    self.connection , self.cursor = db_connection(self.logger,self.db_name)
    self.sql_query = '''
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
  
  def tearDown(self) -> None:
     self.connection.close()
  

  def test_db_name_not_exist(self):
    wrong_db_name='hello_world'
    with self.assertRaises(Exception):
            db_connection(self.logger,wrong_db_name)

  def test_table_name_not_exist(self):
    wrong_expected_table_list = [('cademycode_student',), ('cademycode_courses',), ('cademycode_student_job',)]
    empty_list = []

    test_cases = [wrong_expected_table_list,empty_list]
    for test_case in test_cases:
      with self.subTest(test_case):
        with self.assertRaises(Exception):
          check_expected_table_exist(self.logger,self.cursor,test_case)

  def test_query_handle_exception(self):
      with self.assertRaises(Exception):
            execute_query(self.logger,self.connection,self.sql_query[-5:])


if __name__ == '__main__':
  unittest.main()