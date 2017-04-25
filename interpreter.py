from env import GlobalEnv, LocalEnv
genv = GlobalEnv.empty_env()
result = 0

def eval_tree(tree):
    """ The top level function.
        Args:
            tree (ast.Module): The ast abstract syntax tree- the root is a Module node object. The children are contained in a list.
        Returns:
            integer or float: the result of any value returned by the program, 0 by default.
    """
    global genv
    global result
    children = tree.body
    for node in children:
        values = eval_node(node, genv)
        genv = values[1]
        result = values[0]
    return result

def node_name(node):
    return type(node).__name__

def eval_node(node, env):
    """ Evaluates a Node object in the abstract syntax tree.
        Args:
            node (ast.Node): The node to evaluate.
            env (GlobalEnv | LocalEnv): An environment data type.
        Returns:
            (integer or float, environment): A tuple, where the first element is the result of any
            value computed at this node, and the second value is either a GlobalEnv or LocalEnv object.
    """
    global genv
    global result
    node_type = node_name(node)
    if node_type == 'Expr':
        return eval_node(node.value, env)
    elif node_type == 'Assign':
        variable = node.targets[0].id
        (value, env) = eval_node(node.value, env)
        return (value, env.extend([variable], [value]))
    elif node_type == 'BinOp':
        left = node.left
        right = node.right
        operator = node_name(node.op)
        if(operator == 'Mod'):
            return (eval_node(left, env)[0] % eval_node(right, env)[0], env)
        elif(operator == 'Add'):
            return (eval_node(left, env)[0] + eval_node(right, env)[0], env)
        elif(operator == 'Sub'):
            return (eval_node(left, env)[0] - eval_node(right, env)[0], env)
        elif(operator == 'Mult'):
            return (eval_node(left, env)[0] * eval_node(right, env)[0], env)
        elif(operator == 'Div'):
            return (eval_node(left, env)[0] / eval_node(right, env)[0], env)
    elif node_type == 'FunctionDef':
        name = node.name
        args = node.args
        body = node.body
        return 0, env.extend([name], [[args, body]])
    elif node_type == 'Call':
        if (node_name(node.func) == "Name"):
            name = node.func.id
            func = env.lookup(name)
            lookup = env.lookup(node.func.id)
        else:
            lookup = eval_node(node.func, env)[0]
        param = [i.arg for i in lookup[0].args]
        values = []
        for i in node.args:
            value, env = eval_node(i, env)
            values.append(value)
        localres = 0
        env = LocalEnv(None, env)
        env = env.extend(param, values)
        for n in lookup[1]:
            localres, env = eval_node(n, env)
        return localres, env
    elif node_type == 'Return':
        values = eval_node(node.value, env)
        return values[0], env
    elif node_type == 'Name':
        return env.lookup(node.id), env
    elif node_type == 'Num':
        return node.n, env
