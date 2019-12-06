import sys
import ply.yacc as yacc
from java_lexer import tokens
VERBOSE = 1
precedence = (
	('left', 'IMPLEMENTS', 'IMPORT'),
	('left', 'COMA'),
    ('left', 'Asignacion', 'MasIgual', 'MenosIgual', 'MultiplicacionIgual', 'DivisionIgual'),
	('left', 'PuntoyComa'),
	('left', 'OR'),
	('left', 'AND'),
	('nonassoc', 'ComparacionIgual', 'Diferente'),
    ('nonassoc', 'SignoMenos', 'MenorIgual', 'Mayor', 'MayorIgual'),
	('left', 'SignoMas', 'SignoMenos'),
    ('left', 'ELSE'),
	('right', 'CorcheteIzquierda'),
    ('right', 'PRIVATE', 'PROTECTED', 'PUBLIC', 'FINAL'),
)

def p_program(p):
    'program : PUBLIC CLASS Identificador LlaveIzquierda instrucciones  LlaveDerecha'
	
def p_instrucciones(p):
	'''instrucciones : metodo_main LlaveIzquierda declaration_list LlaveDerecha
					 | declaration_list
					 '''
	pass
def p_metodo_main(p):
	'''metodo_main : PUBLIC STATIC VOID MAIN ParentesisIzquierdo STRING CorcheteIzquierda CorcheteDerecha ARGS ParentesisDerecho
					'''
	pass
def p_declaration_list(p):
   '''declaration_list : declaration_list  declaration
   					   | declaration 
					   
					   
   '''
   pass

def p_declaration(p):
	'''declaration : linea
				   | sentencia_while
				   | sentencia_if'''
	pass


def p_linea(p):
	'''linea : tipado PuntoyComa
			 | mensaje PuntoyComa
			 '''
	pass
def p_tipado(p):
	'''tipado : FLOAT assigment
			  | STRING Identificador Asignacion expression_cadena
			  | INT assigment 
			  | DOUBLE assigment
			  | BOOLEAN assigment
			  | CHAR Identificador Asignacion expression_caracter'''
	pass


def p_mensaje(p):
	'''mensaje : SYSTEM Punto OUT Punto PRINT ParentesisIzquierdo expression_cadena ParentesisDerecho
			   | SYSTEM Punto OUT Punto PRINT ParentesisIzquierdo Identificador ParentesisDerecho 
			   | SYSTEM Punto OUT Punto PRINT ParentesisIzquierdo expression_cadena SignoMas expression ParentesisDerecho
			   | SYSTEM Punto OUT Punto PRINT ParentesisIzquierdo ParentesisDerecho '''
	pass
def p_sentencia_while(p):
	'''sentencia_while : DO LlaveIzquierda declaration_list LlaveDerecha cabecera_do_while PuntoyComa
					   | cabecera_while LlaveIzquierda declaration_list LlaveDerecha'''
	pass
def p_sentencia_if(p):
	'''sentencia_if : cabecera_if ELSE LlaveIzquierda declaration_list LlaveDerecha
					| cabecera_if ELSE cabecera_if
					| cabecera_if'''
	pass 
def p_cabecera_do_while(p):
	'''cabecera_do_while : WHILE ParentesisIzquierdo expression_comparacion ParentesisDerecho
				         | WHILE ParentesisIzquierdo double_expression_comparacion ParentesisDerecho'''
	pass
def p_cabecera_while(p):
	'''cabecera_while : WHILE ParentesisIzquierdo expression_comparacion ParentesisDerecho
				        | WHILE ParentesisIzquierdo double_expression_comparacion ParentesisDerecho'''
	pass

def p_cabecera_if(p):
	'''cabecera_if : IF ParentesisIzquierdo expression_comparacion ParentesisDerecho LlaveIzquierda declaration_list LlaveDerecha
				   | IF ParentesisIzquierdo double_expression_comparacion ParentesisDerecho LlaveIzquierda declaration_list LlaveDerecha'''
	pass
def p_assignment(p):
	'''assigment : Identificador Asignacion expression   
				| Identificador MasIgual expression 
				| Identificador MenosIgual expression 
				| Identificador DivisionIgual expression
				| Identificador'''
	pass
def p_expression_cadena(p):
	'''expression_cadena : CADENADECARACTERES'''
	pass
def p_expression_caracter(p):
	'''expression_caracter : CARACTER'''
	pass

def p_empty(p):
	'empty :'
	pass
def p_double_expression_comparacion(p):
	'''double_expression_comparacion : expression_comparacion OR expression_comparacion
									 | expression_comparacion AND expression_comparacion'''
	pass