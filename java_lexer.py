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
def t_PRIVATE(t):
    r'private'
    return t

def t_PROTECTED(t):
    r'protected'
    return t

def t_PUBLIC(t):
    r'public'
    return t


def t_RETURN(t):
    r'return'
    return t

def t_STATIC(t):
    r'static'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_THROW(t):
    r'throw'


def t_TRY(t):
    r'try'
    return t

def t_IMPORT(t):
    r'import'
    return t

def t_WHILE(t):
    r'while'
    return t


def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_SYSTEM(t):
    r'System'
    return t

def t_OUT(t):
    r'out'
    return t

def t_INT(t):
    r'int'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_DOUBLE(t):
    r'double'
    return t

def t_BOOLEAN(t):
    r'boolean'
    return t

def t_STRING(t):
    r'String'
    return t

def t_CHAR(t):
    r'char'
    return t
    
# simbolos
t_SignoMas      = r'\+'
t_SignoMenos   = r'-'
t_SignoMultiplicar     = r'\*'
t_SignoDividir    = r'/'
t_Asignacion    = r'='
t_Menor     = r'<'
t_Mayor   = r'>'
t_PuntoyComa      = r';'
t_COMA     = r','
t_ParentesisIzquierdo    = r'\('
t_ParentesisDerecho   = r'\)'
t_CorcheteIzquierda  = r'\['
t_CorcheteDerecha  = r'\]'
t_LlaveIzquierda    = r'{'
t_LlaveDerecha    = r'}'
t_DosPuntos     = r':'
t_Punto       = r'\.'
t_ComillasDobles    = r'\"'
t_ComillasSimples = r'\''

def t_MenorIgual(t):
    r'<='
    return t

def t_MayorIgual(t):
    r'>='
    return t

def t_Diferente(t):
    r'!='
    return t

def t_ComparacionIgual(t):
    r'=='
    return t

def t_MenosMenos(t):
    r'--'
    return t

def t_MasMas(t):
    r'\+\+'
    return t
def t_MasIgual(t):
    r'\+='
    return t
def t_MenosIgual(t):
    r'-='
    return t
def t_MultiplicacionIgual(t):
    r'\*='
    return t

def t_DivisionIgual(t):
    r'/='
    return t



def t_COMENTARIOSMULTILINEA(t):
    r'\/\*([^*]|\*[^\/])*(\*)+\/'
    t.lexer.lineno += t.value.count('\n')

def t_COMENTARIOS(t):
    r'(\/\/)(.)*?\n'
    t.lexer.lineno += 1


def t_Numero(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_Identificador(t):
    r'\w+(\w\d)*'
    return t

def t_CADENADECARACTERES(t):
    r'"[^"]*"'
    return t
def t_CARACTER(t):
    r'\'[^\']?\''
    return t

lexer = lex.lex()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        script = sys.argv[1]

        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()
        #print (scriptdata)
        lexer.input(scriptdata)

        print (chr(27)+"[0;36m"+"INICIA ANALISIS LEXICO"+chr(27)+"[0m")
        i = 1
        while True:
            tok = lexer.token()
            if not tok:
                break
            print ("\t"+str(i)+" - "+"Line: "+str(tok.lineno)+"\t"+str(tok.type)+"\t-->  "+str(tok.value))
            i += 1

        print (chr(27)+"[0;36m"+"TERMINA ANALISIS LEXICO"+chr(27)+"[0m")

    else:
        print (chr(27)+"[0;31m"+"Pase el archivo de  JAVA como parametro:")
        print (chr(27)+"[0;36m"+"\t$ python java_lexer.py"+chr(27)+"[1;31m"+" <filename>.java"+chr(27)+"[0m")
