# ============================================================
# Ejemplo 10: Clase Fecha
# Autora: Sara García
# Descripción: Ejemplo del material teórico sobre constructores
#              alternativos con @classmethod.
# ============================================================

import datetime

class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    @classmethod
    def desde_texto(cls, texto):
        """Constructor alternativo: crea una Fecha desde texto DD-MM-AAAA."""
        dia, mes, año = map(int, texto.split('-'))
        return cls(dia, mes, año)

    @classmethod
    def hoy(cls):
        """Constructor alternativo: crea una Fecha con la fecha actual."""
        fecha_actual = datetime.date.today()
        return cls(fecha_actual.day, fecha_actual.month, fecha_actual.year)

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.año}"

    def es_fin_de_semana(self):
        fecha = datetime.date(self.año, self.mes, self.dia)
        return fecha.weekday() >= 5  # 5=sabado, 6=domingo


# Programa principal
fecha1 = Fecha(15, 3, 2025)           # Constructor normal
fecha2 = Fecha.desde_texto("25-12-2025")  # Constructor alternativo
fecha3 = Fecha.hoy()                  # Constructor con fecha actual

print(f"Fecha 1: {fecha1}")
print(f"Fecha 2: {fecha2}")
print(f"Fecha de hoy: {fecha3}")
print()
print(f"¿{fecha1} es fin de semana? {fecha1.es_fin_de_semana()}")
print(f"¿{fecha2} es fin de semana? {fecha2.es_fin_de_semana()}")