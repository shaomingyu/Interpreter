
expr1 = """
res = 7 + 5
res
"""

expr2 = """
res = 8 / 3
res
"""

expr3 = """
res = 8 - 3
res
"""

expr4 = """
res = 8 * 3
res
"""

expr5 = """
res = 8 % 3
res
"""

expr6 = """
num1 = 5
num2 = 6
res = num1 + num2
res
"""

expr7 = """
def foo(arg1, arg2):
    return arg1 * arg2
res = foo(6, 7)
res
"""

expr8 = """
def f_to_celsius(f):
    c = (f - 32) * (5/9)
    return c

ftemp = 68
res = f_to_celsius(ftemp)
"""

expr9 = """
def foo():
    return 25
res = foo()
res
"""

expr10 = """
def foo(arg1, arg2):
    return arg1 * arg2

def bar(x, y):
    return x + y

res = foo(6, 7) + bar(3,4)
res
"""

expr11 = """
num1 = 5
num2 = 16
def foo(arg1, arg2):
   return arg1 * arg2

res = foo(num1, num2 + 6)
res
"""

expr12 = """
num1 = 5
num2 = 6

def bar(x):
    return 20 + x

def foo(arg1, arg2):
    return arg1 * arg2

res = foo(num1, bar(num2))
res
"""

expr13 = """
def foo():
    def bar(x):
        return 20 + x
    return bar
res = foo()(3)
res
"""

expr14 = """
def foo():
    def bar(x):
        return 20 + x
    return bar
res = foo()
z = res(3)
z
"""

if __name__ == '__main__':
    import ast
    import interpreter

    tree = ast.parse(expr13)
    expr_val = interpreter.eval_tree(tree)
    print(expr_val)
