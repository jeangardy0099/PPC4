# 1. Objetivo

O objetivo deste trabalho é implementar e comparar dois métodos de otimização para resolver um problema de maximização de duas variáveis:

1. Método do Aclive Máximo (Steepest Ascent);
2. Método dos Gradientes Conjugados (Fletcher-Reeves).

A função objetivo considerada é:

f(x,y) = 2xy + 2x - x² - 2y²

cujo máximo analítico ocorre em:

(x*,y*) = (2,1)

com valor:

f(x*,y*) = 2

O estudo permite analisar a trajetória de convergência de cada método e comparar sua eficiência.

---

# 2. Formulação Matemática

## Função Objetivo

f(x,y)=2xy+2x−x²−2y²

## Gradiente

∂f/∂x = 2y + 2 − 2x

∂f/∂y = 2x − 4y

Logo,

∇f=(2y+2−2x, 2x−4y)

---

# 3. Métodos Utilizados

## 3.1 Método do Aclive Máximo

O Método do Aclive Máximo utiliza como direção de busca o próprio gradiente da função:

pk = ∇f(xk)

A cada iteração é calculado um passo ótimo h através de uma busca linear unidimensional.

A atualização do ponto é realizada por:

x(k+1)=x(k)+h·pk

Como a direção de busca coincide sempre com o gradiente, o método frequentemente apresenta uma trajetória em zigue-zague até o ponto ótimo.

---

## 3.2 Método dos Gradientes Conjugados (Fletcher-Reeves)

O método Fletcher-Reeves utiliza direções conjugadas definidas por:

pk+1 = ∇f(k+1) + βk pk

onde

βk = ||∇f(k+1)||² / ||∇f(k)||²

Dessa forma, parte da informação das direções anteriores é preservada, reduzindo o efeito de zigue-zague e acelerando a convergência.

---

# 4. Busca Linear

Para determinar o passo ótimo h foi utilizada uma interpolação quadrática de três pontos.

Foram considerados os pontos:

h0 = 0

h1 = 0.5

h2 = 1.0

O vértice da parábola é calculado por:

h* = 1/2 ·
[(h0²-h2²)g(h1)+(h2²-h1²)g(h0)+(h1²-h0²)g(h2)]
/
[(h0-h2)g(h1)+(h2-h1)g(h0)+(h1-h0)g(h2)]

Caso o denominador se torne muito pequeno, utiliza-se como passo o melhor valor entre h0, h1 e h2.

---

# 5. Estrutura do Projeto

PPC4/

├── ppc4.py

├── output1.dat

├── output2.dat

├── function.dat

├── grafico.png

├── README.md

└── relatorio.pdf

---

# 6. Arquivos Gerados

## output1.dat

Histórico do Método do Aclive Máximo.

Formato:

iter erro h x y dfx dfy

---

## output2.dat

Histórico do Método dos Gradientes Conjugados.

Formato:

iter erro h x y dfx dfy

---

## function.dat

Arquivo contendo amostras da função:

x y f(x,y)

Utilizado para geração das curvas de nível.

---

# 7. Requisitos

Python 3.x

Bibliotecas necessárias:

pip install numpy matplotlib

---

# 8. Como Executar

Executar o programa:

python ppc4.py

Informar o ponto inicial desejado.

Exemplo:

x0 = -2

y0 = 3

---

# 9. Resultados Obtidos

O ponto inicial utilizado foi:

(-2,3)

O Método do Aclive Máximo apresentou comportamento característico de zigue-zague, exigindo maior número de iterações para aproximar-se do ponto ótimo.

O Método dos Gradientes Conjugados apresentou convergência mais rápida, utilizando direções conjugadas que reduzem oscilações na trajetória.

Ambos os métodos convergiram para:

x ≈ 2

y ≈ 1

f(x,y) ≈ 2

confirmando o resultado analítico esperado.

---

# 10. Gráfico Comparativo

O gráfico gerado pelo programa apresenta:

* Curvas de nível da função objetivo;
* Trajetória do Método do Aclive Máximo;
* Trajetória do Método Fletcher-Reeves;
* Ponto ótimo analítico (2,1).

A comparação visual evidencia a maior eficiência do método dos Gradientes Conjugados.

---

# 11. Conclusão

Os dois métodos implementados foram capazes de localizar o ponto de máximo da função proposta.

O Método do Aclive Máximo mostrou uma convergência mais lenta devido ao comportamento em zigue-zague provocado pela utilização exclusiva do gradiente como direção de busca.

O Método dos Gradientes Conjugados Fletcher-Reeves apresentou desempenho superior, alcançando o máximo com menos iterações e uma trajetória mais direta.

Os resultados obtidos confirmam a teoria estudada em sala de aula e demonstram a influência da escolha da direção de busca na eficiência de algoritmos de otimização.

