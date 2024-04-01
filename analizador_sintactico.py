from ply import  yacc
from analizador_lexico import tokens


def p_declaraciones(p):
    '''
    declaraciones : declaracion declaraciones
                  | declaracion
    '''
    if len(p) == 3:
        p[0] = p[1] + "\n" + p[2]
    else:
        p[0] = p[1]

def p_declaracion(p):
    '''
    declaracion : DECLARATIVO_INT VARIABLE PUNTO_Y_COMA
                | DECLARATIVO_STRING VARIABLE PUNTO_Y_COMA
                | DECLARATIVO_BOOLEAN VARIABLE PUNTO_Y_COMA
    '''
    p[0] = f'\nDeclaracion:\n {p[1]} {p[2]} {p[3]}'

def p_expresion_condicional(p):
    '''
    declaracion : CONDICIONAL_IF DIGITO MAYOR_QUE DIGITO DOS_PUNTOS PRINT PARENTESIS_INICIAL COMILLA VARIABLE COMILLA PARENTESIS_FINAL PUNTO_Y_COMA
                | CONDICIONAL_IF DIGITO MENOR_QUE DIGITO DOS_PUNTOS PRINT PARENTESIS_INICIAL COMILLA VARIABLE COMILLA PARENTESIS_FINAL PUNTO_Y_COMA
                | CONDICIONAL_IF DIGITO MENOR_IGUAL DIGITO DOS_PUNTOS PRINT PARENTESIS_INICIAL COMILLA VARIABLE COMILLA PARENTESIS_FINAL PUNTO_Y_COMA
                | CONDICIONAL_IF DIGITO MAYOR_IGUAL DIGITO DOS_PUNTOS PRINT PARENTESIS_INICIAL COMILLA VARIABLE COMILLA PARENTESIS_FINAL PUNTO_Y_COMA

    '''
    p[0] = f'\nExpresion Condicional:\n {p[1]} {p[2]} {p[3]} {p[4]} {p[5]} {p[6]} {p[7]} {p[8]} {p[9]} {p[10]} {p[11]} {p[12]}'

def p_expresion_condicional_con_for(p):
    '''
    declaracion : CONDICIONAL_IF DIGITO MAYOR_QUE DIGITO DOS_PUNTOS CICLO_FOR VARIABLE IN RANGE PARENTESIS_INICIAL DIGITO PARENTESIS_FINAL DOS_PUNTOS PRINT PARENTESIS_INICIAL COMILLA VARIABLE COMILLA PARENTESIS_FINAL PUNTO_Y_COMA
                | CONDICIONAL_IF DIGITO MENOR_QUE DIGITO DOS_PUNTOS CICLO_FOR VARIABLE IN RANGE PARENTESIS_INICIAL DIGITO PARENTESIS_FINAL DOS_PUNTOS PRINT PARENTESIS_INICIAL COMILLA VARIABLE COMILLA PARENTESIS_FINAL PUNTO_Y_COMA
                | CONDICIONAL_IF DIGITO MENOR_IGUAL DIGITO DOS_PUNTOS CICLO_FOR VARIABLE IN RANGE PARENTESIS_INICIAL DIGITO PARENTESIS_FINAL DOS_PUNTOS PRINT PARENTESIS_INICIAL COMILLA VARIABLE COMILLA PARENTESIS_FINAL PUNTO_Y_COMA
                | CONDICIONAL_IF DIGITO MAYOR_IGUAL DIGITO DOS_PUNTOS CICLO_FOR VARIABLE IN RANGE PARENTESIS_INICIAL DIGITO PARENTESIS_FINAL DOS_PUNTOS PRINT PARENTESIS_INICIAL COMILLA VARIABLE COMILLA PARENTESIS_FINAL PUNTO_Y_COMA
    '''         
    p[0] = f'\nExpresion Condicional con for:\n {p[1]} {p[2]} {p[3]} {p[4]} {p[5]} {p[6]} {p[7]} {p[8]} {p[9]} {p[10]} {p[11]} {p[12]} {p[13]} {p[14]} {p[15]} {p[16]} {p[17]} {p[18]} {p[19]}'

def p_definicion_funcion(p):
    '''
    declaracion : FUNCION_DEF VARIABLE PARENTESIS_INICIAL PARENTESIS_FINAL DOS_PUNTOS PRINT PARENTESIS_INICIAL COMILLA VARIABLE COMILLA PARENTESIS_FINAL PUNTO_Y_COMA
    '''
    p[0] = f'\nDefinicion de Funcion:\n {p[1]} {p[2]} {p[3]} {p[4]} {p[5]} {p[6]} {p[7]} {p[8]} {p[9]} {p[10]} {p[11]} {p[12]}'

def p_definicion_funcion_con_for(p):
    '''
    declaracion : FUNCION_DEF VARIABLE PARENTESIS_INICIAL PARENTESIS_FINAL DOS_PUNTOS CICLO_FOR VARIABLE IN RANGE PARENTESIS_INICIAL DIGITO PARENTESIS_FINAL DOS_PUNTOS PRINT PARENTESIS_INICIAL COMILLA VARIABLE COMILLA PARENTESIS_FINAL PUNTO_Y_COMA
    '''
    p[0] = f'\nDefinicion de Funcion con FOR:\n {p[1]} {p[2]} {p[3]} {p[4]} {p[5]} {p[6]} {p[7]} {p[8]} {p[9]} {p[10]} {p[11]} {p[12]} {p[13]} {p[14]} {p[15]} {p[16]} {p[17]} {p[18]} {p[19]} {p[20]}'

def p_llamada_funcion(p):
    '''
    declaracion :  VARIABLE PARENTESIS_INICIAL PARENTESIS_FINAL PUNTO_Y_COMA
    '''
    p[0] = f'\nLlamada de Funcion:\n {p[1]} {p[2]} {p[3]} {p[4]}'

def p_bucle(p):
    '''
    declaracion : CICLO_FOR VARIABLE IN RANGE PARENTESIS_INICIAL DIGITO PARENTESIS_FINAL DOS_PUNTOS PRINT PARENTESIS_INICIAL COMILLA VARIABLE COMILLA PARENTESIS_FINAL PUNTO_Y_COMA
    '''
    p[0] = f'\nBucle For:\n {p[1]} {p[2]} {p[3]} {p[4]} {p[5]} {p[6]} {p[7]} {p[8]} {p[9]} {p[10]} {p[11]} {p[12]} {p[13]} {p[14]} {p[15]}'

def p_print(p):
    '''
    declaracion : PRINT PARENTESIS_INICIAL COMILLA VARIABLE COMILLA PARENTESIS_FINAL PUNTO_Y_COMA
    '''
    p[0] = f'\nPrint:\n {p[1]} {p[2]} {p[3]} {p[4]} {p[5]} {p[6]} {p[7]}'

def p_error(p):
    if p:
        raise SyntaxError(f"Error de sintaxis en la entrada. Token inesperado: {p.value} en la línea {p.lineno} en la posición {p.lexpos}")
    else:
        raise SyntaxError("Error de sintaxis en la entrada. Final inesperado o token no reconocido.")
 

def prueba(data):
    parser = yacc.yacc(debug=True)
    try:
        result = parser.parse(data)
        if result:
            return result
        else:
            print("El análisis no tuvo éxito.")
            return None
    except Exception as e:
        print(f"Error durante el análisis sintáctico: {str(e)}")
        return None

parser = yacc.yacc(debug=True)