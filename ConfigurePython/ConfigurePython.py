def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
	output = '<html>'
	output += '<h1>This is a demo for basic python running on WAWS</h1>'
	output += '</html>'
	return [output]