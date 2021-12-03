import pytest
import json

from ticket_viewer.ticket_viewer import *
from ticket_viewer.util import *

@pytest.fixture()
def static_indiv_ticket_data():
  """Fixture that returns static individual ticket data."""
  
  with open("tests/resources/individual_ticket.json") as f:
     return json.load(f)

@pytest.fixture()
def static_tickets_data():
  """Fixture that returns static tickets data."""

  with open("tests/resources/tickets.json") as f:
    return json.load(f)

@pytest.fixture(scope="module")
def vcr_config():
    return {
      "cassette_library_dir": "tests/resources/cassettes",
      "record_mode": "once",
      "filter_headers": ["authorization"]
      }

@pytest.mark.vcr  
def test_count_tickets():
  ticket_viewer = get_ticket_viewer()
  response = ticket_viewer.count_tickets()
  assert response.count == 26

@pytest.mark.vcr  
def test_get_individual_ticket(static_indiv_ticket_data):
  ticket_viewer = get_ticket_viewer()
  response = ticket_viewer.get_individual_ticket("1")
  assert response.tickets[0] == static_indiv_ticket_data

@pytest.mark.vcr  
def test_get_tickets(static_tickets_data):
  ticket_viewer = get_ticket_viewer()
  response = ticket_viewer.get_tickets()
  assert response.tickets == static_tickets_data["tickets"]
  assert response.prev_link == static_tickets_data["links"]["prev"]
  assert response.next_link == static_tickets_data["links"]["next"]

tickets = [
  {
    "id": 23971,
    "updated_at": "2021-12-01T02:35:51Z",
    "status": "new",
    "priority": "urgent",
    "subject": "Unable to access toilet in the office",
    "type": "problem"
  },
  {
    "id": 24,
    "updated_at": "2021-11-30T01:15:51Z",
    "status": "open",
    "priority": "low",
    "subject": "Is Santa going to give me a Christmas gift?",
    "type": "question"
  },
  {
    "id": 9561,
    "updated_at": "2021-11-25T21:35:43Z",
    "status": "solved",
    "priority": "high",
    "subject": "Book a dinner reservation for parents' 25th wedding anniversary",
    "type": "task"
  },
  {
    "id": 7662451,
    "updated_at": "2021-11-27T18:02:10Z",
    "status": "pending",
    "priority": "low",
    "subject": "Can shark eat chocolate?",
    "type": "question"
  },
  {
    "id": 199,
    "updated_at": "2021-11-22T07:30:01Z",
    "status": "solved",
    "priority": "normal",
    "subject": "I accidently dropped my Mom's  flower vase",
    "type": "incident"
  }
]
headers = ["ID", "Updated at (SGT)", "Type", "Priority", "Status", "Subject"]
keys = ["id", "updated_at", "type", "priority", "status", "subject"]

def test_find_column_width():
  col_width = find_column_width(tickets, keys, headers)
  assert col_width == [9, 21, 10, 10, 9, 65]

test_data1 = {
  "col_value": "incident",
  "col_width": 10,
  "is_first_col": True,
  "is_left_indent": True,
  "is_front": True,
  "expected_whitespace": " ",
  "expected_col": " incident "
}
test_data2 = {
  "col_value": "My shoes are missing.",
  "col_width": 40,
  "is_first_col": False,
  "is_left_indent": False,
  "is_front": False,
  "expected_whitespace": "         ",
  "expected_col": "|          My shoes are missing.         "
}

@pytest.mark.parametrize(
  "col_value, col_width, is_front, expected_whitespace",
  [
    pytest.param(
        test_data1["col_value"],
        test_data1["col_width"],
        test_data1["is_front"],
        test_data1["expected_whitespace"]
    ),
    pytest.param(
        test_data2["col_value"],
        test_data2["col_width"],
        test_data2["is_front"],
        test_data2["expected_whitespace"]  
    ),
  ],
)

def test_generate_whitespace(col_value, col_width, is_front, expected_whitespace):
  assert generate_whitespace(col_value, col_width, is_front) == expected_whitespace

@pytest.mark.parametrize(
  "col_value, col_width, is_first_col, is_left_indent, expected_col",
  [
    pytest.param(
        test_data1["col_value"],
        test_data1["col_width"],
        test_data1["is_first_col"],
        test_data1["is_left_indent"],
        test_data1["expected_col"]
    ),
    pytest.param(
        test_data2["col_value"],
        test_data2["col_width"],
        test_data2["is_first_col"],
        test_data2["is_left_indent"],
        test_data2["expected_col"]
    ),
  ],
)

def test_generate_col(
  col_value, 
  col_width, 
  is_first_col, 
  is_left_indent, 
  expected_col
):
  assert generate_cell(col_value, col_width, is_first_col, is_left_indent) == expected_col

def test_convert_to_sgt():
  assert convert_to_sgt("2021-11-25T21:35:43Z") == "26 Nov 2021 05:35AM"

def test_generate_row():
  assert generate_row(tickets[0], keys, [9, 21, 10, 10, 9, 65]) == \
    "  23971  | 01 Dec 2021 10:35AM |  problem |  urgent  |   new   " \
    "| Unable to access toilet in the office                           "
