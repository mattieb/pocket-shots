import re
import ply.lex as lex
import ply.yacc as yacc

tokens = (
    "LPAREN",
    "RPAREN",
    "SYMBOL",
    "NUMBER",
    "STRING",
)


t_LPAREN = r"\("
t_RPAREN = r"\)"
t_SYMBOL = r"[a-z][a-z0-9]+"
t_NUMBER = r"[0-9A-F]+"


def t_STRING(t):
    r"\"([^\\\"]|\\.)*\""
    t.value = t.value[1:-1]
    t.value = re.sub(r"\\(.)", r"\1", t.value)
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


t_ignore = " \t"


def t_error(t):
    raise ValueError("lexer error (%r)" % t.value[0])


def p_objects_addobject(p):
    "objects : objects object"
    objects = p[1].copy()
    objects.append(p[2])
    p[0] = objects


def p_objects_first(p):
    "objects : object"
    p[0] = [p[1]]


def p_object(p):
    "object : SYMBOL LPAREN contents RPAREN"
    p[0] = (p[1], p[3])


def p_property_string(p):
    "property : SYMBOL STRING"
    p[0] = (p[1], p[2])


def p_property_value(p):
    "property : SYMBOL NUMBER"
    p[0] = (p[1], p[2])


def p_contents_addproperty(p):
    "contents : contents property"
    contents = p[1].copy()
    contents.append(p[2])
    p[0] = contents


def p_contents_addobject(p):
    "contents : contents object"
    contents = p[1].copy()
    contents.append(p[2])
    p[0] = contents


def p_contents_empty(p):
    "contents : empty"
    p[0] = []


def p_empty(p):
    "empty :"
    pass


def parse_dat(datfilename):
    lex.lex()
    parser = yacc.yacc(debug=False)
    with open(datfilename, "r") as f:
        return parser.parse(f.read())
