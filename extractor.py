import config
import requests


def get(endpoint, params):
    # 1. Validar que el endpoint existe o no
    if endpoint not in config.ENDPOINTS:
        raise ValueError(f"Endpoint '{endpoint}' not found")

    # 2. Combinar parámetros del usuario con DEFAULTS
    if params is None:
        params = {}

    if not isinstance(params, dict):
        raise TypeError("params must be a dictionary")

    params_with_defaults = {**config.DEFAULTS, **params}

    # 3. Construir la URL completa
    final_url = config.base_url + config.ENDPOINTS[endpoint]

    # 4. Manejo de errores al llamar a la API
    try:
        response = requests.get(
            final_url,
            params=params_with_defaults,
            timeout=config.DEFAULTS["timeout"]
        )

        # Lanza excepción si el status HTTP es error
        response.raise_for_status()

        # Intentar parsear JSON de forma segura
        data = response.json()
        return data

    except requests.exceptions.Timeout:
        raise TimeoutError("The request timed out")

    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"HTTP error: {e}")

    except requests.exceptions.ConnectionError:
        raise ConnectionError("Connection error. Check your network or API URL")

    except ValueError:
        raise ValueError("Response was not valid JSON")

    except Exception as e:
        raise RuntimeError(f"Unexpected error: {e}")





