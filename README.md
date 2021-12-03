# **Ticket Viewer**
Ticket Viewer is a CLI app built with Python to help access your Zendek support tickets.

## **Installation**
1. Clone the application's source code into a `ticket-viewer/` directory by typing the following command:
```
ticket-viewer$ git clone https://github.com/samtjong23/ticket_viewer
```
2. Create a Python 3 (I personally used Python 3.9.5) virtual environment and activate it:
```
ticket-viewer$ python -m venv ./venv
ticket-viewer$ source venv/bin/activate
(venv) ticket-viewer$
```
3. Create a .env file containing url, email and password inside `ticket-viewer/ticket_viewer/` directory to access Zendesk API:
```
secretUrl = "https://{subdomain}.zendesk.com"
secretEmail = "{email_address}"
secretPassword = "{password}"
```
4. Install all the dependencies:
```
(venv) ticket-viewer/ticket_viewer$ python -m pip install -r requirements.txt
```

## **Usage**
1. Once you have run the installation steps, you can type `python -m ticket_viewer` to run the application:
```
(venv) ticket-viewer/ticket_viewer$ python -m ticket_viewer

Welcome to the Ticket Viewer.

Select view options:
* Type '1' to view all tickets
* Type '2' to view a specific ticket
* Type 'quit' to exit
``` 
2. The app has two main features and you can access them by following the given intructions and typing the right option.
3. If you want to view all the tickets your account has, you can type `1`:
```
Select view options:
* Type '1' to view all tickets
* Type '2' to view a specific ticket
* Type 'quit' to exit

1

 ID |   Updated at (SGT)  |   Type   | Priority | Status |                    Subject                    
---------------------------------------------------------------------------------------------------------
  5 | 03 Dec 2021 11:49AM |  problem |  urgent  |   new  | aliquip mollit quis laborum incididunt        
  4 | 03 Dec 2021 08:21AM |   task   |   high   | solved | ad sunt qui aute ullamco                      
  3 | 02 Dec 2021 10:13PM | question |    low   |  open  | excepteur laborum ex occaecat Lorem           
  1 | 02 Dec 2021 06:55PM | incident |  normal  |  open  | Sample ticket: Meet the ticket                
  2 | 02 Dec 2021 09:01AM |   task   |   high   | closed | velit eiusmod reprehenderit officia cupidatat
```
4. If more than 25 tickets are returned, you can page through them by typing `prev` or `next`:
```
Select view options:
* Type '1' to view all tickets
* Type '2' to view a specific ticket
* Type 'quit' to exit

1

 ID |   Updated at (SGT)  | Type | Priority | Status |                  Subject                  
-------------------------------------------------------------------------------------------------
 30 | 03 Dec 2021 02:46PM |      |          |        | officia esse nostrud est exercitation     
 29 | 03 Dec 2021 02:46PM |      |          |        | irure pariatur aliquip dolore esse        
 28 | 03 Dec 2021 02:46PM |      |          |        | magna consequat ut ullamco magna          
 27 | 03 Dec 2021 02:46PM |      |          |        | ut magna eiusmod magna nostrud            
 26 | 03 Dec 2021 02:46PM |      |          |        | in labore quis mollit mollit              
 25 | 03 Dec 2021 02:46PM |      |          |        | voluptate dolor deserunt ea deserunt      
 24 | 03 Dec 2021 02:46PM |      |          |        | et ad ut enim labore                      
 23 | 03 Dec 2021 02:46PM |      |          |        | sunt enim pariatur id id                  
 22 | 03 Dec 2021 02:46PM |      |          |        | esse adipisicing consectetur sunt tempor  
 21 | 03 Dec 2021 02:46PM |      |          |        | laboris sint Lorem ex Lorem               
 20 | 03 Dec 2021 02:46PM |      |          |        | commodo sint laboris est et               
 19 | 03 Dec 2021 02:46PM |      |          |        | est fugiat labore pariatur esse           
 18 | 03 Dec 2021 02:46PM |      |          |        | laborum ea ut in cupidatat                
 17 | 03 Dec 2021 02:46PM |      |          |        | exercitation sit incididunt magna laboris 
 16 | 03 Dec 2021 02:46PM |      |          |        | tempor magna anim ea id                   
 15 | 03 Dec 2021 02:46PM |      |          |        | do incididunt incididunt quis anim        
 14 | 03 Dec 2021 02:46PM |      |          |        | officia mollit aliqua eu nostrud          
 13 | 03 Dec 2021 02:46PM |      |          |        | labore pariatur ut laboris laboris        
 12 | 03 Dec 2021 02:46PM |      |          |        | tempor aliquip sint dolore incididunt     
 11 | 03 Dec 2021 02:46PM |      |          |        | quis veniam ad sunt non                   
 10 | 03 Dec 2021 02:46PM |      |          |        | magna reprehenderit nisi est cillum       
  9 | 03 Dec 2021 02:46PM |      |          |        | veniam ea eu minim aute                   
  8 | 03 Dec 2021 02:46PM |      |          |        | proident est nisi non irure               
  7 | 03 Dec 2021 02:46PM |      |          |        | cillum quis nostrud labore amet           
  6 | 03 Dec 2021 02:46PM |      |          |        | nisi aliquip ipsum nostrud amet           

Select view options:
* Type 'next' or 'prev' to see other tickets
* Type 'menu' to go back to the main menu
* Type 'quit' to exit

next

 ID |   Updated at (SGT)  |   Type   | Priority | Status |                    Subject                    
---------------------------------------------------------------------------------------------------------
  5 | 03 Dec 2021 11:49AM |          |          |        | aliquip mollit quis laborum incididunt        
  4 | 03 Dec 2021 11:49AM |          |          |        | ad sunt qui aute ullamco                      
  3 | 03 Dec 2021 11:49AM |          |          |        | excepteur laborum ex occaecat Lorem                         
  2 | 03 Dec 2021 11:49AM |          |          |        | velit eiusmod reprehenderit officia cupidatat 

It seems that you have reached the end of the table. You may choose to go in the opposite direction.

Select view options:
* Type 'prev' to see other tickets
* Type 'menu' to go back to the main menu
* Type 'quit' to exit
```
5. If you want to view a single ticket, you can type `2`:
```
Select view options:
* Type '1' to view all tickets
* Type '2' to view a specific ticket
* Type 'quit' to exit

2

Enter ticket ID:
1

 ID |   Updated at (SGT)  |   Type   | Priority | Status |             Subject            
------------------------------------------------------------------------------------------
  1 | 03 Dec 2021 11:49AM | incident |  normal  |  open  | Sample ticket: Meet the ticket 
```
6. No worries if you provide the wrong input or if the API is unavailable, the app will send you a message to let you know what is happening.
```
Select view options:
* Type '1' to view all tickets
* Type '2' to view a specific ticket
* Type 'quit' to exit

quitt

Invalid input. Please try again.

Select view options:
* Type '1' to view all tickets
* Type '2' to view a specific ticket
* Type 'quit' to exit

2

Enter ticket ID:
1

Oops it seems that something is wrong.
We could not authenticate you.
Please check your credentials in the .env file and restart the app.
```
7. Finally, once you are done you may type `quit` to exit the app:
```
Select view options:
* Type '1' to view all tickets
* Type '2' to view a specific ticket
* Type 'quit' to exit

quit

Thank you for using Ticket Viewer. Bye. :D
```

## **Unit Tests**
### Using **my subdomain**
* If you are using **my subdomain**, just make sure that `secretUrl = "https://zccsamueltjong.zendesk.com"` can be found inside the .env file.
* **Only for unit tests**, `secretEmail` and `secretPassword` values can be anything so long as they are not empty and the unit tests should still be able to pass.
### Using **other subdomains**
* Before running the tests, you need to make some changes to files inside `tests/resources/` and `tests/test_ticket_viewer.py`.
 * `tests/resources/individual_ticket.json` should contain (replace values inside curly brackets with results returned when calling `https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_number}.json`): 
```
{
  "id": {ticket_id},
  "updated_at": {updated_at},
  "type": {type},
  "subject": {subject},
  "priority": {priority},
  "status": {status}
}
```
 * `tests/resources/tickets.json` should contain (replace values inside curly brackets with results returned when calling `https://{subdomain}.zendesk.com/api/v2/tickets.json?page[size]=25&sort=-updated_at`)
```
{
  "tickets": [
    {
      "id": {ticket_id_1},
      "updated_at": {updated_at_1},
      "type": {type_1},
      "subject": {subject_1},
      "priority": {priority_1},
      "status": {status_1}
    },
    ...
    ...
    },
    {
      "id": {ticket_id_x},
      "updated_at": {updated_at_x},
      "type": {type_x},
      "subject": {subject_x},
      "priority": {priority_x},
      "status": {status_x}
    }
  ],
  "links": {
    "prev": {prev_link},
    "next": {next_link}
  }
}
```
 * `tests/test_ticket_viewer.py` should contain:
```
...
@pytest.mark.vcr  
def test_count_tickets():
  ticket_viewer = get_ticket_viewer()
  response = ticket_viewer.count_tickets()
  assert response.count == {count returned when calling https://{subdomain}.zendesk.com/api/v2/tickets/count.json}

@pytest.mark.vcr  
def test_get_individual_ticket(static_indiv_ticket_data):
  ticket_viewer = get_ticket_viewer()
  response = ticket_viewer.get_individual_ticket({the same ticket number as the one inside tests/resources/individual_ticket.json})
  assert response.tickets[0] == static_indiv_ticket_data
...
```
 * Also make sure that your .env file contains the right credentials.
### Running the tests
Finally you can type `python -m pytest` to run unit tests.
```
(venv) ticket-viewer/ticket_viewer$ python -m pytest
============================================================================ test session starts ============================================================================
platform linux -- Python 3.9.5, pytest-6.2.4, py-1.11.0, pluggy-0.13.1
rootdir: /home/samtjong/ticket-viewer/ticket_viewer
plugins: recording-0.12.0
collected 10 items                                                                                                                                                                                                              

tests/test_ticket_viewer.py ..........                                                                                                                                                                                    [100%]

============================================================================ 10 passed in 0.17s =============================================================================
```

## **Additional Comments**
1. I used cursor pagination to paginate through the list of tickets. Since the `has_more` attribute can occasionally return `True` even though there are actually no more tickets to see, likewise the app will not know if it has reached the end of the list unless:
 * The current page contains less than 25 tickets OR
 * The user requests to get more tickets and the API returns 0 tickets.

When any of these 2 scenario happens the app will tell the user that he/she has reached the end of the table and he/she can try the other option to see more tickets.
```
ID |   Updated at (SGT)  |   Type   | Priority | Status |                    Subject                    
---------------------------------------------------------------------------------------------------------
 25 | 03 Dec 2021 02:46PM |          |          |  open  | voluptate dolor deserunt ea deserunt          
 24 | 03 Dec 2021 02:46PM |          |          |  open  | et ad ut enim labore                          
 23 | 03 Dec 2021 02:46PM |          |          |  open  | sunt enim pariatur id id                      
 22 | 03 Dec 2021 02:46PM |          |          |  open  | esse adipisicing consectetur sunt tempor      
 21 | 03 Dec 2021 02:46PM |          |          |  open  | laboris sint Lorem ex Lorem                   
 20 | 03 Dec 2021 02:46PM |          |          |  open  | commodo sint laboris est et                   
 19 | 03 Dec 2021 02:46PM |          |          |  open  | est fugiat labore pariatur esse               
 18 | 03 Dec 2021 02:46PM |          |          |  open  | laborum ea ut in cupidatat                    
 17 | 03 Dec 2021 02:46PM |          |          |  open  | exercitation sit incididunt magna laboris     
 16 | 03 Dec 2021 02:46PM |          |          |  open  | tempor magna anim ea id                       
 15 | 03 Dec 2021 02:46PM |          |          |  open  | do incididunt incididunt quis anim            
 14 | 03 Dec 2021 02:46PM |          |          |  open  | officia mollit aliqua eu nostrud              
 13 | 03 Dec 2021 02:46PM |          |          |  open  | labore pariatur ut laboris laboris            
 12 | 03 Dec 2021 02:46PM |          |          |  open  | tempor aliquip sint dolore incididunt         
 11 | 03 Dec 2021 02:46PM |          |          |  open  | quis veniam ad sunt non                       
 10 | 03 Dec 2021 02:46PM |          |          |  open  | magna reprehenderit nisi est cillum           
  9 | 03 Dec 2021 02:46PM |          |          |  open  | veniam ea eu minim aute                       
  8 | 03 Dec 2021 02:46PM |          |          |  open  | proident est nisi non irure                   
  7 | 03 Dec 2021 02:46PM |          |          |  open  | cillum quis nostrud labore amet               
  6 | 03 Dec 2021 02:46PM |          |          |  open  | nisi aliquip ipsum nostrud amet               
  5 | 03 Dec 2021 11:49AM |          |          |  open  | aliquip mollit quis laborum incididunt        
  4 | 03 Dec 2021 11:49AM |          |          |  open  | ad sunt qui aute ullamco                      
  3 | 03 Dec 2021 11:49AM |          |          |  open  | excepteur laborum ex occaecat Lorem           
  1 | 03 Dec 2021 11:49AM |          |          |  open  | excepteur Lorem anim adipisicing deserunt               
  2 | 03 Dec 2021 11:49AM |          |          |  open  | velit eiusmod reprehenderit officia cupidatat 

Select view options:
* Type 'next' or 'prev' to see other tickets
* Type 'menu' to go back to the main menu
* Type 'quit' to exit

next

It seems that you have reached the end of the table. You may choose to go in the opposite direction.

Select view options:
* Type 'prev' to see other tickets
* Type 'menu' to go back to the main menu
* Type 'quit' to exit
```
2. One possible area of improvement is the unit tests. In the future I can write tests for functions that return `None` to check if the they behave correctly in different scenarios. This is something that I am still not familiar with it yet and I have identified to be a growth opportunity.

## **About the Author**
Samuel Tjong - Email: [samtjong23@gmail.com](mailto:samtjong23@gmail.com)
