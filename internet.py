# importing required module
import http.client as httplib


# function to check internet connectivity
def checkInternetHttplib(url="www.google.com",
						timeout=3):
	connection = httplib.HTTPConnection(url,
										timeout=timeout)
	try:
		# only header requested for fast operation
		connection.request("HEAD", "/")
		connection.close() # connection closed
		print("Internet On")
		return True
	except Exception as exep:
		print("no internet")
		return False



