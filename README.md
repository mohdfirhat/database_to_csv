# Project Description

This projects allow user to read a local SQlite database file and extract data and create a csv file with the data required. This project has logging, exception handling to help user when an issue arises(more details below). User has to update the variables such as `db_name`, `expected_table_list`, `sql_query`, `output_pathname` and `output_filename`.

# How to use

1. Open `data_pipeline.py` and update the variables `db_name`, `expected_table_list`, `sql_query` `output_pathname` and `output_filename` as required.
2. If user needs to test the SQL query, user is able to use the Data_Pipeline.ipynb to test the sql_query.(Optional)
3. Run the `bash_script.sh` in Terminal/Command Prompt using `bash bash_script.sh`. The bash script would run the unit-testing on the variables provided and log any errors encountered(logged at console and ).
4. If there are no error, user could continue by pressing y/Y to create the output file in `output_pathname`

# File Structure

.
├── README.md
├── dev
│ ├── Data_Pipeline.ipynb
│ ├── bash_script.sh
│ ├── cademycode.db
│ ├── data_pipeline.py
│ ├── functions.py
│ ├── logging.log
│ └── test.py
└── prod

- dev folder - contains all the codes.
  - bash_script.sh - main file to run the test.py and data_pipeline.py.
  - Data_Pipeline.ipynb - jupyter notebook for user to test the output of the DB.
  - cademycode.db - local SQlite database used for the data extraction.
  - data_pipeline.py - the python code to read the database, execute the SQL query and create the csv file. User needs to update the variable if necessary.
  - functions.py - contains all the functions and logic used in the data_pipeline.py
  - test.py - test the data_pipeline.py using the unittesting library.
  - logging.log - contains all the logs for troubleshooting
- prod folder - for the output csv file

# Project Features

## Logging

This project logs the information and error in the console and `logging.log`.

## Exception Handling

The pipeline handles the following errors.

- Local db file does not exist.
- `expected_table_list` is empty.
- The table in `expected_table_list` is not found in the db.
- SQL query error which will log the SQL error encountered.

## Bash Scripting

The project has a Bash script where the user can run both the test and pipeline in one place. User can decide not to run the pipeline when the test run into the error.

## SQL query using sqlite3

User is able to enter their SQL query into the data_pipeline.py
