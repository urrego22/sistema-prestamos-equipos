# ============================================================
# Ejemplo 20: Formulario con métodos privados
# Autora: Sara García
# Descripción: Ejemplo del material de encapsulación sobre
#              métodos privados como ayudantes internos.
# ============================================================

class Formulario:
    def __init__(self):
        self._datos = {}
        self._errores = {}

    def validar(self, datos):
        """Metodo publico: coordina todas las validaciones."""
        self._datos = datos.copy()
        self._errores = {}

        # Llama a metodos privados para cada validacion
        self.__validar_campos_requeridos()
        self.__validar_email()
        self.__validar_contrasena()
        self.__validar_edad()

        return len(self._errores) == 0

    def obtener_errores(self):
        """Metodo publico: devuelve los errores encontrados."""
        return self._errores.copy()

    def __validar_campos_requeridos(self):
        """Metodo privado: verifica que los campos obligatorios existan."""
        campos = ['nombre', 'email', 'contrasena']
        for campo in campos:
            if campo not in self._datos or not self._datos[campo]:
                self._errores[campo] = f"El campo '{campo}' es obligatorio"

    def __validar_email(self):
        """Metodo privado: verifica formato del email."""
        import re
        if 'email' in self._datos and self._datos['email']:
            patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(patron, self._datos['email']):
                self._errores['email'] = "El formato del email no es valido"

    def __validar_contrasena(self):
        """Metodo privado: verifica seguridad de la contraseña."""
        if 'contrasena' in self._datos and self._datos['contrasena']:
            c = self._datos['contrasena']
            if len(c) < 8:
                self._errores['contrasena'] = "Debe tener al menos 8 caracteres"
            elif not any(x.isupper() for x in c):
                self._errores['contrasena'] = "Debe tener al menos una mayuscula"
            elif not any(x.isdigit() for x in c):
                self._errores['contrasena'] = "Debe tener al menos un numero"

    def __validar_edad(self):
        """Metodo privado: verifica que la edad sea valida."""
        if 'edad' in self._datos:
            try:
                edad = int(self._datos['edad'])
                if edad < 18:
                    self._errores['edad'] = "Debes ser mayor de edad"
                elif edad > 120:
                    self._errores['edad'] = "La edad ingresada no es valida"
            except ValueError:
                self._errores['edad'] = "La edad debe ser un numero"


# Programa principal
formulario = Formulario()

# Caso 1: datos correctos
datos_ok = {
    "nombre":    "Sara Garcia",
    "email":     "sara@email.com",
    "contrasena": "Segura123",
    "edad":      "18"
}
resultado = formulario.validar(datos_ok)
print(f"Formulario valido: {resultado}")
print(f"Errores: {formulario.obtener_errores()}")
print()

# Caso 2: datos con errores
datos_mal = {
    "nombre":    "Carlos",
    "email":     "correo-invalido",
    "contrasena": "abc",
    "edad":      "15"
}
resultado = formulario.validar(datos_mal)
print(f"Formulario valido: {resultado}")
print("Errores encontrados:")
for campo, error in formulario.obtener_errores().items():
    print(f"  - {campo}: {error}")