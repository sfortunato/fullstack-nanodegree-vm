from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer 
import cgi

#handler 
class webserverHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith("/hello"):
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()

				output = ""
				output += "<html><body>Hello!"
				output += "<form method='POST' enctype='multipart/form-data' action ='/hello'><h2>Whatwould you like me to say></h2><input name='message' type='text' ><input type = 'submit' value='Submit'> </form>"
				output += "</body></html>"

				self.wfile.write(output) #sends output to client
				print output
				return

			if self.path.endswith("/hola"):
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()

				output = ""
				output += "<html><body>&#161Hola <a href = '/hello'>Back to Hello</a>"
				output += "<form method='POST' enctype='multipart/form-data' action ='/hello'><h2>Whatwould you like me to say></h2><input name='message' type='text' ><input type = 'submit' value='Submit'> </form>"
				output += "</body></html>"

				self.wfile.write(output) #sends output to client
				print output
				return

		except IOError:
			self.send_error(404, "File Not Found")

	def do_POST(self):
		try:
			self.send_response(301)
			self.end_headers()

			ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
			if ctype == "multipart/form-data":
				fields = cgi.parse_multipart(self.rfile, pdict)
				messagecontent = fields.get("message")

			output = ""
			output += "<html><body>"
			output += " <h2> %s </h2>" % messagecontent[0]
			output += "<form method='POST' enctype='multipart/form-data' action ='/hello'><h2>What would you like me to say</h2><input name='message' type='text' ><input type = 'submit' value='Submit'> </form>"
			output += "</body></html>"
			self.wfile.write(output)
			print output

		except:
			pass


#main function (spins up server)
def main():
	try:
		port = 8080
		server = HTTPServer(("", port), webserverHandler)
		print "Web server running on port 8080"
		server.serve_forever()
	except KeyboardInterrupt:
		print "^C entered, stopping webserver..."
		server.socket.close()

if __name__ == '__main__':
	main()