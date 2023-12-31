sys_template_loader = "You are excel loader"
human_template_loader = "You will extract the zeroth row with headers from the {doc} and return the keys and find out the data type. Display in form of a dictionary"

snake_case_instruction = """Make sure that all field names are in SNAKE Case.
SNAKE Case means all field names are in LOWER CASE and spaces are converted to underscores(_) """

system_template_create = "you create SQL tables in database"
human_template_create = """Create a table {table_name} using {header_type} with the specified data type in {db}. Use Create statement with if not exists. 
Make sure that all field names are in SNAKE Case.
SNAKE Case means all field names are in LOWER CASE and spaces are converted to underscores(_)"""

sys_template_data_loader = "You will load the data from excel file"
human_template_data_loader = """"convert {doc} into tuples of data.
"""


sys_template_data_loader_1 = "You are an expert SQL coder"
human_template_data_loader_1 = """" Please generate a postgreSQL query to insert data into {table_name} according to {headers} with these values = {docs}. 
generate DOCS according to {data_type}
Headers should not have any quotes(" ` ') in it 
Example of the query:
INSERT INTO {table_name} {headers} values {docs};
"""

system_template_python_coder_load = """You generate PYTHON CODE"""
human_template_python_coder_load = """ Please generate Python Code to Load {excel} sheet into the {db} by creating a table with this name : {table_name}
Use the database connection as mentioned. 
Make sure that the connection is always made, use password as {pwd}

Example code:

import pandas as pd

# Load the Excel file
df = pd.read_excel('path')

# Convert field names to snake case
snake_case_columns = [col.lower().replace(' ', '_') for col in df.columns]
df.columns = snake_case_columns

# Create a table in the database
from sqlalchemy import create_engine

# Replace 'xxx' with the actual password
engine = create_engine('postgresql://postgres:12345@localhost:5432/test')

df.to_sql('employee', engine, if_exists='replace', index=False)
"""