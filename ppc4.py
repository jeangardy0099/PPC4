import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# Função objetivo e gradiente
# ==========================================================

def f(x, y):
    return 2*x*y + 2*x - x**2 - 2*y**2

def gradiente(x, y):
    dfx = 2*y + 2 - 2*x
    dfy = 2*x - 4*y
    return np.array([dfx, dfy])

# ==========================================================
# Busca linear por interpolação quadrática
# ==========================================================

def line_search(x, p):

    def g(h):
        xn = x + h*p
        return f(xn[0], xn[1])

    h0 = 0.0
    h1 = 0.5
    h2 = 1.0

    g0 = g(h0)
    g1 = g(h1)
    g2 = g(h2)

    numerador = (
        (h1**2 - h2**2)*g0 +
        (h2**2 - h0**2)*g1 +
        (h0**2 - h1**2)*g2
    )

    denominador = (
        (h1 - h2)*g0 +
        (h2 - h0)*g1 +
        (h0 - h1)*g2
    )

    if abs(denominador) < 1e-12:
        valores = [g0, g1, g2]
        hs = [h0, h1, h2]
        return hs[np.argmax(valores)]

    h = 0.5 * numerador / denominador

    if h < 0:
        valores = [g0, g1, g2]
        hs = [h0, h1, h2]
        return hs[np.argmax(valores)]

    return h

# ==========================================================
# Método do Aclive Máximo
# ==========================================================

def steepest_ascent(x0, tol=1e-6, max_iter=100):

    x = np.array(x0, dtype=float)

    traj = [x.copy()]

    with open("output1.dat", "w") as arq:

        for k in range(max_iter):

            grad = gradiente(x[0], x[1])
            erro = np.linalg.norm(grad)

            if erro < tol:
                break

            p = grad

            h = line_search(x, p)

            arq.write(
                f"{k} {erro:.8e} {h:.8e} "
                f"{x[0]:.8e} {x[1]:.8e} "
                f"{grad[0]:.8e} {grad[1]:.8e}\n"
            )

            print(
                f"[Aclive] Iter={k:3d} "
                f"x={x[0]:.6f} y={x[1]:.6f} "
                f"f={f(x[0],x[1]):.6f} "
                f"h={h:.6f} erro={erro:.3e}"
            )

            x = x + h*p

            traj.append(x.copy())

    return np.array(traj)

# ==========================================================
# Gradientes Conjugados Fletcher-Reeves
# ==========================================================

def conjugate_gradient_FR(x0, tol=1e-6, max_iter=100):

    x = np.array(x0, dtype=float)

    grad = gradiente(x[0], x[1])

    p = grad.copy()

    traj = [x.copy()]

    with open("output2.dat", "w") as arq:

        for k in range(max_iter):

            erro = np.linalg.norm(grad)

            if erro < tol:
                break

            h = line_search(x, p)

            arq.write(
                f"{k} {erro:.8e} {h:.8e} "
                f"{x[0]:.8e} {x[1]:.8e} "
                f"{grad[0]:.8e} {grad[1]:.8e}\n"
            )

            print(
                f"[FR] Iter={k:3d} "
                f"x={x[0]:.6f} y={x[1]:.6f} "
                f"f={f(x[0],x[1]):.6f} "
                f"h={h:.6f} erro={erro:.3e}"
            )

            x_new = x + h*p

            grad_new = gradiente(x_new[0], x_new[1])

            beta = (
                np.dot(grad_new, grad_new)
                /
                np.dot(grad, grad)
            )

            p = grad_new + beta*p

            x = x_new
            grad = grad_new

            traj.append(x.copy())

    return np.array(traj)

# ==========================================================
# Arquivo para curvas de nível
# ==========================================================

def gerar_function_dat():

    with open("function.dat", "w") as arq:

        for x in np.linspace(-1, 4, 100):
            for y in np.linspace(-1, 3, 100):

                arq.write(
                    f"{x} {y} {f(x,y)}\n"
                )

# ==========================================================
# Programa principal
# ==========================================================

x0 = float(input("x0 = "))
y0 = float(input("y0 = "))

gerar_function_dat()

traj1 = steepest_ascent([x0, y0])
traj2 = conjugate_gradient_FR([x0, y0])

# ==========================================================
# Gráfico
# ==========================================================

X = np.linspace(-1, 4, 200)
Y = np.linspace(-1, 3, 200)

XX, YY = np.meshgrid(X, Y)

ZZ = f(XX, YY)

plt.figure(figsize=(8,6))

plt.contour(XX, YY, ZZ, 20)

plt.plot(
    traj1[:,0],
    traj1[:,1],
    'ro-',
    label='Aclive Máximo'
)

plt.plot(
    traj2[:,0],
    traj2[:,1],
    'bs-',
    label='Gradientes Conjugados FR'
)

plt.plot(
    2,
    1,
    'k*',
    markersize=15,
    label='Ótimo (2,1)'
)

plt.xlabel('x')
plt.ylabel('y')
plt.title('PPC4 - Comparação dos Métodos')
plt.legend()
plt.grid(True)

plt.show()
