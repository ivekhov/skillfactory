
from bottle import run, route, view
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies


@route("/api/forecast")
def api_forecast():
	prophecies = generate_prophecies(6, 2)
	return {
		"prophecies": prophecies,
	}

run(
	host="localhost",
	port=8090,
	debug=True,
	autoreload=True,
)
