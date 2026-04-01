import simplejson as json
from datetime import datetime

# Abrir el archivo JSON
with open("token.json", "r") as f:
    data = json.load(f)

# Cargar en nueva variable
token_info = data

# Imprimir contenido
print("Contenido del JSON:", token_info)

# Mostrar token
print("Token:", token_info["token"])

# Calcular tiempo restante de expiración
expira = datetime.fromisoformat(token_info["expires_at"])
ahora = datetime.now()
restante = expira - ahora

print("Tiempo restante de expiración:", restante)
