"""
This module provides Ticket Viewer with the functions to
retrieve all tickets/individual ticket using Zendesk API
"""

import requests
from typing import List, Dict, NamedTuple, Optional

class CountTicketsResponse(NamedTuple):
	status_code: int
	count: Optional[int] = None

class GetTicketsResponse(NamedTuple):
	status_code: int
	tickets: Optional[List[Dict[str, str]]] = None
	prev_link: Optional[str] = None
	next_link: Optional[str] = None

class TicketViewer:
	def __init__(self, url: str, email:str, password: str) -> None:
		self.url: str = url
		self.email: str = email
		self.password: str = password

	def count_tickets(self) -> CountTicketsResponse:
		"""
		Count the number of tickets the account has
		"""

		# In case anything happens, we want to be able to catch the error
		# and send a message to the user
		try:
			response = requests.get(
				f'{self.url}/api/v2/tickets/count.json',
				auth=(self.email, self.password)
			)

			if response.status_code == 200:
				return CountTicketsResponse(
					response.status_code,
					count=response.json()["count"]["value"]
				)

			else:
				return CountTicketsResponse(response.status_code)
		
		except:
			return CountTicketsResponse(-1)
	
	def get_tickets(self, link: Optional[str] = None) -> GetTicketsResponse:
		"""
		List tickets belonging to the account
		"""

		# If no link is given, get 25 most recently updated tickets by default
		if link is None:
			link = f'{self.url}/api/v2/tickets.json?page[size]=25&sort=-updated_at'

		# In case anything happens, we want to be able to catch the error
		# and send a message to the user
		try:
			response = requests.get(link, auth=(self.email, self.password))

			if response.status_code == 200:
				data = response.json()
				tickets = []

				for ticket in data["tickets"]:
					tickets.append(
						{
							"id": ticket["id"],
							"updated_at": ticket["updated_at"],
							"type": ticket["type"],
							"subject": ticket["subject"],
							"priority": ticket["priority"],
							"status": ticket["status"]
						}
					)

				return GetTicketsResponse(
					response.status_code,
					tickets,
					prev_link=data["links"]["prev"],
					next_link=data["links"]["next"]
				)

			else:
				return GetTicketsResponse(response.status_code)
		
		except:
			return GetTicketsResponse(-1)
	
	def get_individual_ticket(self, ticket_number:str) -> GetTicketsResponse:
		"""
		Fetch the properties of a specific ticket by ticket ID
		"""

		# In case anything happens, we want to be able to catch the error
		# and send a message to the user
		try:
			response = requests.get(
				f'{self.url}/api/v2/tickets/{ticket_number}.json', 
				auth=(self.email, self.password)
			)

			if response.status_code == 200:
				ticket_info = response.json()["ticket"]
				ticket = []
				
				ticket.append(
					{
						"id": ticket_info["id"],
						"updated_at": ticket_info["updated_at"],
						"type": ticket_info["type"],
						"subject": ticket_info["subject"],
						"priority": ticket_info["priority"],
						"status": ticket_info["status"]
					}
				)

				return GetTicketsResponse(response.status_code, ticket)
			
			else:
				return GetTicketsResponse(response.status_code)
		
		except:
			return GetTicketsResponse(-1)