#Configuration file with API key, endpoints, constants

API_KEY = ""

base_url = "http://api.aviationstack.com"

ENDPOINTS = {
    "flights": "/v1/flights",
    "routes":"/v1/routes",
    "airports": "/v1/airports",
    "airlines": "/v1/airlines",
    "airplanes":"/v1/airplanes",
    "aircraft_types":"/v1/aircraft_types",
    "taxes":"/v1/taxes",
    "cities":"/v1/cities",
    "countries":"/v1/countries",
    "flight_schedules":"/v1/flight_schedules",
    "flight_future_schedules":"/v1/flight_future_schedules"

}


DEFAULTS = {
    "timeout": 10,
    "max_limit": 100
}




