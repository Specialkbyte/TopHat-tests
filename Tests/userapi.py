from test import Test

class Userapi(Test):

	short_title = "User API Token Request"
	title = "Attempts to get an user API token from the server."

	def _test(self):
		(self.headers, self.content) = self.h.request(self.args.server + "apitokens" + "/", "POST", 'data={"username":"'+self.args.user+'", "password":"'+self.args.password+'" }', headers={'content-type':'application/x-www-form-urlencoded'})

	def _request_ok(self, content):
		if self._status == 201 and "apitoken" in content:
			self.inform = "API Token Received: "+content['apitoken']
			return True
		elif self._status == 404:
			self._reason = "The details for test user supplied does not exist or are invalid."
			return False
		else:
			self._reason = "Missing JSON or Invalid Status Code."
			return False