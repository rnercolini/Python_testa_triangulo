# Verifica se com o tamanho das retas digitadas é possível construir um triângulo.
print('*' * 20)
print('TESTADOR DE TRIÂNGULOS')
print('*' * 20)
r1 = float(input('Digite o comprimento em cm da primeira reta: '))
r2 = float(input('Digite o comprimento em cm da segunda reta: '))
r3 = float(input('Digite o comprimento em cm da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com estas retas \033[4;34mÉ POSSÍVEL\033[m construir um tirângulo.')
else:
    print('Com estas retas \033[4;31mNÃO É POSSÍVEL\033[m construir um triângulo.')
