"""Top level package for Ticket Viewer"""

from collections import defaultdict

# Preparing messages to be displayed for different HTTP status codes
STATUS_CODE = (401, 403, 404, 429)
MESSAGE = (
	"\nOops it seems that something is wrong." \
	"\nWe could not authenticate you." \
	"\nPlease check your credentials in the .env file and restart the app.",

	"\nOops it seems that something is wrong." \
	"\nYou do not seem to have the required persmission to perform this action." \
	"\nPlease try other options.",

	"\nOops the ticket number you provided does not exist.",

	"\nYou hit the rate limit. Please get a coffee and retry after some time."
)
STATUS_CODE_MESSAGE = defaultdict(
	lambda: "\nSomething seems off." \
		"\nPlease get a coffee and retry after some time while we are figuring things out." \
		"\nYou might want to check your .env file too to make sure the inputs are correct."	,
	{
		status_code: message for status_code, message in zip(STATUS_CODE, MESSAGE)
	} 
)