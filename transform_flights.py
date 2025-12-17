def transform_flights(data):
    #validamos que que tengamos datos
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")


    if "data" not in data or not isinstance(data["data"], list):
        raise ValueError("Invalid input: 'data' key not found or not a list")

    records = []

    for flight in data["data"]:
        record = {
            "flight_date": flight.get("flight_date"),
            "flight_status": flight.get("flight_status"),

            "dep_airport": flight.get("departure", {}).get("airport"),
            "dep_timezone": flight.get("departure", {}).get("timezone"),
            "dep_iata": flight.get("departure", {}).get("iata"),
            "dep_terminal": flight.get("departure", {}).get("terminal"),
            "dep_gate": flight.get("departure", {}).get("gate"),
            "dep_scheduled": flight.get("departure", {}).get("scheduled"),
            "dep_estimated": flight.get("departure", {}).get("estimated"),
            "dep_actual": flight.get("departure", {}).get("actual"),
            "dep_delay": flight.get("departure", {}).get("delay"),

            "arr_airport": flight.get("arrival", {}).get("airport"),
            "arr_timezone": flight.get("arrival", {}).get("timezone"),
            "arr_iata": flight.get("arrival", {}).get("iata"),
            "arr_terminal": flight.get("arrival", {}).get("terminal"),
            "arr_gate": flight.get("arrival", {}).get("gate"),
            "arr_scheduled": flight.get("arrival", {}).get("scheduled"),
            "arr_estimated": flight.get("arrival", {}).get("estimated"),
            "arr_actual": flight.get("arrival", {}).get("actual"),
            "arr_delay": flight.get("arrival", {}).get("delay"),

            "airline_name": flight.get("airline", {}).get("name"),
            "airline_iata": flight.get("airline", {}).get("iata"),

            "flight_number": flight.get("flight", {}).get("number"),
            "flight_iata": flight.get("flight", {}).get("iata"),
        }

        records.append(record)

    return records
