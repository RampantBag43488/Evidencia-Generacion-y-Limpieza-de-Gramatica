import nltk
from nltk import CFG
from nltk.parse import ChartParser


grammatica = CFG.fromstring("""
S -> ID IGUAL E PCOMA

E -> T E_TAIL
E_TAIL -> MAS T E_TAIL
E_TAIL -> MENOS T E_TAIL
E_TAIL ->

T -> F T_TAIL
T_TAIL -> MULT F T_TAIL
T_TAIL -> DIV F T_TAIL
T_TAIL ->

F -> IZPAREN E DERPAREN
F -> ID
F -> NUM

ID -> 'id'
NUM -> 'num'
IGUAL -> '='
PCOMA -> ';'
MAS -> '+'
MENOS -> '-'
MULT -> '*'
DIV -> '/'
IZPAREN -> '('
DERPAREN -> ')'
""")


parser = ChartParser(grammatica)


def tokenizador(oracion):
    cadena = []

    for token in oracion.split():
        if token.isidentifier():
            cadena.append("id")
        elif token.isnumeric():
            cadena.append("num")
        elif token in ["=", ";", "+", "-", "*", "/", "(", ")"]:
            cadena.append(token)
        else:
            cadena.append("invalido")

    return cadena


def parsear_oracion(oracion):
    """
    Recibe una cadena, la tokeniza y busca arboles.
    Si trees tiene al menos un arbol, la cadena se acepta.
    Si arboles esta vacia, la cadena se rechaza.
    """
    tokens = tokenizador(oracion)

    if "invalido" in tokens:
        return tokens, []

    arboles = list(parser.parse(tokens))
    return tokens, arboles
