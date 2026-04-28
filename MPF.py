import math

def ponto_fixo (g, x0, e_relativo=None, e_absoluto=None, max_inter = 50):
    x = x0
    
    # 3. loop até atender um critério de parada (criterio inserido)
    for k in range(max_inter):
        x_novo = g(x)

        # erro absoluto
        erro_abs = abs(x_novo - x)

        # erro relativo (evita divisão por zero)
        if x_novo != 0:
            erro_rel = abs((x_novo - x) / x_novo)
        else:
            erro_rel = erro_abs

        # critério de parada
        if e_absoluto is not None and erro_abs < e_absoluto:
            return x_novo, k + 1

        if e_relativo is not None and erro_rel < e_relativo:
            return x_novo, k + 1
        
        x = x_novo
    
    return x, max_inter

# 1. Escolher função de interação
expr = input("Digite g(x): ")
g = lambda x: eval(expr, {
    "x": x,
    "log": math.log,   # log natural
    "ln": math.log,    # ln = log natural
    "exp": math.exp,
    "e": math.e,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan
})

# 1.5. Conferir se a função converge


# 2. Escolher um Chute Inicial
x0 = float(input("Digite o chute inicial: "))
e_rel = float(input("Digite o erro relativo: "))
e_abs = float(input("Digite o erro absoluto: "))
max_iter = int(input("Digite o número máximo de iterações: "))

if e_rel == 0:
    e_rel = None
if e_abs == 0:
    e_abs = None

raiz, it = ponto_fixo(g, x0, e_rel, e_abs, max_iter)

print("\nResultado:")
print("Raiz aproximada:", raiz)
print("Iterações:", it)