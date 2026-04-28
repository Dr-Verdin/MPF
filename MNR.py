import math

def newton_raphson(f, df, x0, e_relativo=None, e_absoluto=None, max_iter=50):
    x = x0

    for k in range(max_iter):
        fx = f(x)
        dfx = df(x)

        # evita divisão por zero
        if dfx == 0:
            print("Derivada zero! Método falhou.")
            return None, k

        x_novo = x - fx / dfx

        erro_abs = abs(x_novo - x)

        if x_novo != 0:
            erro_rel = abs((x_novo - x) / x_novo)
        else:
            erro_rel = erro_abs

        if e_absoluto is not None and erro_abs < e_absoluto:
            return x_novo, k + 1

        if e_relativo is not None and erro_rel < e_relativo:
            return x_novo, k + 1

        x = x_novo

    return x, max_iter


expr_f = input("Digite f(x): ")
expr_df = input("Digite f'(x): ")

f = lambda x: eval(expr_f, {
    "x": x,
    "log": math.log,
    "ln": math.log,
    "exp": math.exp,
    "e": math.e,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan
})

df = lambda x: eval(expr_df, {
    "x": x,
    "log": math.log,
    "ln": math.log,
    "exp": math.exp,
    "e": math.e,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan
})

x0 = float(input("Digite o chute inicial: "))
e_rel = float(input("Digite o erro relativo (ou 0): "))
e_abs = float(input("Digite o erro absoluto (ou 0): "))
max_iter = int(input("Digite o número máximo de iterações: "))

if e_rel == 0:
    e_rel = None
if e_abs == 0:
    e_abs = None


raiz, it = newton_raphson(f, df, x0, e_rel, e_abs, max_iter)

print("\nResultado:")
print("Raiz aproximada:", raiz)
print("Iterações:", it)
