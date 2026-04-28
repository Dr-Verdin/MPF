import math

def secante(f, x0, x1, e_relativo=None, e_absoluto=None, max_iter=50):
    for k in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)

        # evita divisão por zero
        if f_x1 - f_x0 == 0:
            print("Divisão por zero! Método falhou.")
            return None, k

        x_novo = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        erro_abs = abs(x_novo - x1)

        if x_novo != 0:
            erro_rel = abs((x_novo - x1) / x_novo)
        else:
            erro_rel = erro_abs

        if e_absoluto is not None and erro_abs < e_absoluto:
            return x_novo, k + 1

        if e_relativo is not None and erro_rel < e_relativo:
            return x_novo, k + 1

        x0 = x1
        x1 = x_novo

    return x1, max_iter


expr_f = input("Digite f(x): ")

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

x0 = float(input("Digite x0: "))
x1 = float(input("Digite x1: "))
e_rel = float(input("Digite o erro relativo (ou 0): "))
e_abs = float(input("Digite o erro absoluto (ou 0): "))
max_iter = int(input("Digite o número máximo de iterações: "))

if e_rel == 0:
    e_rel = None
if e_abs == 0:
    e_abs = None


raiz, it = secante(f, x0, x1, e_rel, e_abs, max_iter)

print("\nResultado:")
print("Raiz aproximada:", raiz)
print("Iterações:", it)
