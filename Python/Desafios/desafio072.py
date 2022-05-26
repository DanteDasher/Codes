tn = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
n = int(input('Digite um numero entre 0 e 20: '))
while n < 0 or n > 20:
    n = int(input('Tente novamente digitar um numero entre 0 e 20: '))
print(f'Você digitou o número {tn[n]}')