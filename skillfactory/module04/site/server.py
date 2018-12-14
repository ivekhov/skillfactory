from bottle import run, route

@route("/api/test")
def api_test():
 	return {
 		"test_passed": True
 	}


run(
	host="localhost",
	port=8080,
)