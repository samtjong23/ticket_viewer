"""Helper functions for cli.py"""

import os
import sys
import math
from dotenv import load_dotenv
from datetime import datetime
from pytz import timezone
from typing import List, Dict

from ticket_viewer.ticket_viewer import TicketViewer

def get_ticket_viewer() -> TicketViewer:
  """
  Get url, email and password to connect to Zendesk API
  """

  load_dotenv()
  url = os.environ.get("secretUrl")
  email = os.environ.get("secretEmail")
  password = os.environ.get("secretPassword")

  # Send a message to user if there are missing information
  if not url or not email or not password:
    print("Some values are missing from the .env file." \
          "Please check the file and try again.")
    sys.exit()

  else:
    return TicketViewer(url, email, password)

def find_column_width(
  tickets: List[Dict[str, str]], 
  keys: List[str], 
  headers: List[str]
) -> List[int]:
  """
  Find the width of each column inside the table
  by measuring the lengths of its contents
  """
  
  max_len = list(map(len, headers))
  max_len[1] = 19 # Length of 'Updated at (SGT)' column after conversion to SGT is fixed
  
  for ticket in tickets:
    for idx, key in enumerate(keys):
        # Skip if value is None or if it belongs to "updated_at" key
        # since the length will always be fixed after conversion to SGT
        if ticket[key] is None or key == "updated_at": continue

        if len(str(ticket[key])) > max_len[idx]:
          max_len[idx] = len(str(ticket[key]))

  # To make sure the column is not too tight, add a whitespace before and after the value 
  col_width = list(map(lambda x:x+2, max_len)) 

  return col_width

def generate_whitespace(
  cell_value: str,
  col_width: int,
  is_front: bool
) -> str:
  """
  Generate whitespaces for a cell
  containing a specific property of a ticket
  """

  # For whitespace that comes before the property in the cell
  if is_front:
    return math.ceil((col_width - len(cell_value)) / 2) * " "

  # For whitespace that comes after the property in the cell
  else:
    return int((col_width - len(cell_value)) / 2) * " "

def generate_cell(
  cell_value: str, 
  col_width: int, 
  is_first_col: bool = False, 
  is_left_indent: bool = False
) -> str:
  """
  Generate a cell containing a specific property of a ticket
  """

  front_whitespaces = generate_whitespace(cell_value, col_width, True)
  back_whitespaces = generate_whitespace(cell_value, col_width, False)

  # Since it is first column, we do not need '|' at the start
  if is_first_col:
    # If we want the property to be displayed with left indentation
    if is_left_indent:
      return " " + cell_value + front_whitespaces + back_whitespaces[:-1]
    
    else:
      return front_whitespaces + cell_value + back_whitespaces
  
  else:
    if is_left_indent:
      return "| " + cell_value + front_whitespaces + back_whitespaces[:-1]
    
    else:
      return "|" + front_whitespaces + cell_value + back_whitespaces

def convert_to_sgt(string: str) -> str:
  """
  Convert a ticket's 'updated_at' to SGT
  """
  
  # Convert string to datetime object
  utc_time = datetime.strptime(
    string,
    "%Y-%m-%dT%H:%M:%SZ"
  ).replace(tzinfo=timezone("UTC"))

  # Change timezone to SGT and convert datetime object to string
  sg_time = utc_time \
            .astimezone(timezone("Asia/Singapore")) \
            .strftime("%d %b %Y %I:%M%p")
  
  return sg_time

def generate_row(
  ticket: Dict[str, str], 
  keys: List[str], 
  col_width: List[int]
) -> str:
  """
  Generate a row for tickets table
  """ 

  row = [""] * len(col_width)
  for idx, key in enumerate(keys):
      # Convert None value to empty string
      display_value = ticket[key] if ticket[key] else ""
      
      if key == "updated_at":  # Need to convert 'updated_at' to SGT
        display_value = convert_to_sgt(display_value)
      
      row[idx] = generate_cell(
        str(display_value),
        col_width[idx],
        is_first_col=key == "id",
        is_left_indent=key == "subject"
      )
  
  return "".join(row)