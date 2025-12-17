import extractor
import config
import transform_flights

#Llamar a la API
#hay que implementar la vista para poder añadir los valores desde el usuario

params = {
    "access_key": config.API_KEY,
    "dep_iata": "DUB",
    #"airline_name" :"Ryanair Ltd.",
    "limit": 1
}
data = []
data = extractor.get("flights",params)
#print(data)

#enviar los datos a transform

transform_flights.transform_flights(data)