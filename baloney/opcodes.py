
# Constant type mappings
C_TYPE_MAP = {
        'number': 'int',
        'string': 'char*'
    }


def command_to_op(command, scope):
    if command.data == 'declaration':
        return inst_declr(command, scope)
    elif command.data == 'print':
        return inst_print(command, scope)
    elif command.data == 'if':
        return inst_if(command, scope)
    elif command.data == 'incr':
        return inst_incr(command, scope)
    elif command.data == 'decr':
        return inst_decr(command, scope)
    elif command.data == 'aug_assign':
        return inst_augassign(command, scope)
    else:
        raise ValueError(f"{command.data} not recognised")


def inst_augassign(command, scope):
    command = command.children[0]
    operator, number, name = command.children
    if operator == 'add':
        c_str = f"{name} += {number};\n"
    elif operator == 'subtract':
        c_str = f"{name} -= {number};\n"
    
    return (c_str, scope)


def inst_decr(command, scope):
    name, *_ = command.children
    c_str = f"{name}--;\n"
    return (c_str, scope)


def inst_incr(command, scope):
    name, *_ = command.children
    c_str = f"{name}++;\n"
    return (c_str, scope)


def inst_declr(command, scope):
    name, type_name, value = command.children
    scope[name] = (type_name, value)
    c_type = C_TYPE_MAP[type_name]
    if value:
        c_str = f"{c_type} {name} = {value};\n"
    else:
        c_str = f"{c_type} {name};\n"
    return (c_str, scope)


def inst_print(command, scope):
    name, *_ = command.children
    if name.data == 'print_value':
        name, *_ = name.children
        if name in scope:
            c_type, value = scope[name]
        else:
            raise ValueError(f"Can't find {name} in scope")
        if c_type == 'string':
            c_str = f"printf(\"%s\", {name});\n"
        elif c_type == 'number':
            c_str = f"printf(\"%d\", {name});\n"
    elif name.data == "print_literal":
        name, *_ = name.children
        c_str = f"printf({name});\n"

    return (c_str, scope)


def inst_if(command, scope):
    name, comparison = command.children
    if comparison.data == 'eq':
        c_operator = '=='
        target, *_ = comparison.children
        lh_ctype, *_ = scope[name]
        rh_ctype, *_ = scope[target]
        if lh_ctype != rh_ctype:
            if lh_ctype == 'number' and rh_ctype == 'string':
                c_str = f"if (to_str({name}) {c_operator} {target})"
            elif lh_ctype == 'string' and rh_ctype == 'number':
                c_str = f"if ({name} {c_operator} to_str({target}))"
        else:
            c_str = f"if ({name} {c_operator} {target})"
    return (c_str, scope)
