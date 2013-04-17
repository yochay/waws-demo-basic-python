def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
	output = '<html>'
	output += '<h1>This is a demo for basic python running on WAWS</h1>'
	output += '</html>'
	start_response('200 OK', [('Content-type', 'text/html')])
	yield output