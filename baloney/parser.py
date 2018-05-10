
from lark import Lark

parser = Lark(r"""
        start: command*
        command: [declaration|print|incr|decr|if|aug_assign] _NL
        declaration: NAME " is a " TYPE [" with a value of " VALUE]
        print: print_value|print_literal
        print_value: "print the value of " NAME
        print_literal: "print " STRING
        incr: "increment " NAME
        decr: "decrement " NAME
        if: "if the value of " NAME eq|neq|lt|gt|nn|nu _NL command+ _NL
        eq: " is equal to " NAME
        neq: " isnt equal to " NAME
        lt: " is less than " NAME
        gt: " is greater than " NAME
        nn: " has a value"
        nu: " does not have a value"
        aug_assign: aug_value_assign|aug_literal_assign
        aug_value_assign: OPERATOR " the value of " NUMBER " to " NAME
        aug_literal_assign: OPERATOR " " NUMBER " to " NAME
        OPERATOR: ADD_OPERATOR|SUBTRACT_OPERATOR
        ADD_OPERATOR: "add"
        SUBTRACT_OPERATOR: "subtract"
        VALUE: STRING|NUMBER
        TYPE: "string"|"number"
        %import common.CNAME -> NAME
        %import common.NEWLINE -> _NL
        %import common.ESCAPED_STRING -> STRING
        %import common.NUMBER
        %import common.WS_INLINE
    """, lexer='dynamic')

def parse(code: str):
    r = parser.parse(code)
    return r
