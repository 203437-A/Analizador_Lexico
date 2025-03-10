from analizador_sintactico import parser
import io
import sys

class TablaDeSimbolos:
    def __init__(self):
        self.simbolos = {}
        self.funciones = {}

    def agregar(self, nombre, tipo):
        if nombre in self.simbolos:
            raise Exception(f"Error semántico: La variable '{tipo}' ya está declarada.")
        self.simbolos[nombre] = tipo

    def agregar_funcion(self, nombre, parametros):
        if nombre in self.funciones:
            raise Exception(f"Error semántico: La función '{nombre}' ya está definida.")
        self.funciones[nombre] = parametros

    def obtener_funcion(self, nombre):
        if nombre not in self.funciones:
            raise Exception(f"Error semántico: La función '{nombre}' no está definida.")
        return self.funciones[nombre]

class IfStatement:
    def __init__(self, condicion, contenido):
        self.condicion = condicion
        self.contenido = contenido

class ForLoop:
    def __init__(self, variable, rango, contenido):
        self.variable = variable
        self.rango = rango
        self.contenido = contenido

class FunctionDefinition:
    def __init__(self, nombre, parametros, contenido):
        self.nombre = nombre
        self.parametros = parametros
        self.contenido = contenido

def analisis_semantico(arbol_sintactico, tabla_simbolos=None):
    if tabla_simbolos is None:
        tabla_simbolos = TablaDeSimbolos()

    if isinstance(arbol_sintactico, tuple):
        if arbol_sintactico[0] == 'declaracion':
            _, tipo, nombre = arbol_sintactico
            tabla_simbolos.agregar(nombre, tipo)
    if isinstance(arbol_sintactico, tuple):
        if arbol_sintactico[0] == 'Funcion':
                _, nombre_funcion, contenido = arbol_sintactico
                tabla_simbolos.agregar_funcion(nombre_funcion, [])    
        elif arbol_sintactico[0] == 'Funcion con FOR':
            _, nombre_funcion, contenido = arbol_sintactico
            tabla_simbolos.agregar_funcion(nombre_funcion, [])  

    elif isinstance(arbol_sintactico, list):
        for nodo in arbol_sintactico:
            analisis_semantico(nodo, tabla_simbolos)

    return "Análisis semántico completado con éxito y el resultado es:\n"

def prueba_semantica(texto):
    old_stdout = sys.stdout  
    try:
        arbol_sintactico = parser.parse(texto)
        resultado = analisis_semantico(arbol_sintactico)
        
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        exec(texto)

        output = new_stdout.getvalue()

        return resultado + '\n' + output
    except SyntaxError as e:
        return f"Hubo un error en el analizador"
    except Exception as e:
        return f"{e}"
    finally:
        sys.stdout = old_stdout 
