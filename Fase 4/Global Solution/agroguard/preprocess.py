
import json

def classificar_alerta(sensor_data):
    umidade = sensor_data["umidade"]
    temperatura = sensor_data["temperatura"]
    ph = sensor_data["ph"]
    condutividade = sensor_data["condutividade"]

    if (
        umidade < 10 or umidade > 80 or
        temperatura < 8 or temperatura > 40 or
        ph < 4.5 or ph > 8.5 or
        condutividade < 0.2 or condutividade > 5.0
    ):
        return "critico"
    elif (
        (10 <= umidade < 25 or 50 < umidade <= 80) or
        (8 <= temperatura < 12 or 32 < temperatura <= 38) or
        (4.5 <= ph < 5.5 or 7.5 < ph <= 8.5) or
        (0.2 <= condutividade < 0.5 or 3.5 < condutividade <= 5.0)
    ):
        return "atencao"
    else:
        return "normal"
