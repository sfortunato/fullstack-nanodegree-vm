from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer 

#handler 



def main():
	try:
		port = 8080
		server = HTTPServer(("", port), webserverHandler)
		print "Web server running on port " + port
		server.serve_forever()
	except KeyboardInterrupt:

	#stuff

if __name__ == '__main__':
	main()