import sys
import ply.lex as lex

tokens = (

    # Palabras Reservadas
    'PUBLIC', 'PRIVATE', 'PROTECTED', 'CLASS', 'MAIN', 'STRING', 'INT', 'FLOAT',
    'DOUBLE', 'BOOLEAN', 'CHAR', 'IF', 'ELSE', 'DO', 'WHILE', 'SWITCH', 'CASE',
    'FOR', 'RETURN', 'STATIC', 'TRY', 'EXTENDS', 'PRINT', 'PRINTLN', 'NEW', 'CATCH'
    'TRHOW', 'IMPORT', 'FINAL', 'BREAK', 'DEFAULT', 'IMPLEMENTS', 'SYSTEM', 'OUT', 'ARGS',

    
    'TRUE','FALSE',

    # Simbolos
    'Identificador', 'Numero', 'SignoMas', 'SignoMenos', 'SignoMultiplicar', 'SignoDividir', 'Asignacion',
    'Diferente', 'Mayor', 'MayorIgual', 'Menor', 'MenorIgual', 'ComparacionIgual', 'LlaveIzquierda', 
    'LlaveDerecha', 'CorcheteIzquierda', 'CorcheteDerecha', 'ParentesisIzquierdo', 'ParentesisDerecho', 
    'OR', 'AND', 'COMA', 'PuntoyComa', 'MasIgual', 'MenosIgual', 'MultiplicacionIgual', 'DivisionIgual', 
    'MasMas', 'MenosMenos', 'Punto', 'DosPuntos', "ComillasDobles", "ComillasSimples",

    
    'COMENTARIOSMULTILINEA','VOID','CADENADECARACTERES', 'CARACTER','COMENTARIOS', 
)


t_ignore = " \t"

def t_VOID(t):
    r'VOID|void'
    return t

def t_PRINT(t):
    r'println|print'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print (chr(27)+"[1;31m"+"\t ERROR: Caracter Ilegal"+chr(27)+"[0m")
    print ("\t\tLine: "+str(t.lexer.lineno)+"\t=> " + t.value[0])
    t.lexer.skip(1)

# RE RESERVERD WORDS LIST

def t_MAIN(t):
    r'main'
    return t

def t_ARGS(t):
    r'args'
    return t

def t_AND(t):
    r'\&\&'
    return t

def t_BREAK(t):
    r'break'
    return t


def t_CASE(t):
    r'case'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_DO(t):
    r'do'
    return t


def t_ELSE(t):
    r'else'
    return t

def t_EXTENDS(t):
    r'extends'
    return t


def t_FOR(t):
    r'for'
    return t


def t_IF(t):
    r'if'
    return t

def t_IMPLEMENTS(t):
    r'implements'
    return t

def t_NEW(t):
    r'new'
    return t

def t_OR(t):
    r'\|\|'
    return t
