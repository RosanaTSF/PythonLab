c = input('Digite a temperatura em celsius:')
c_temp = eval(c)
f = 1.8 * c_temp + 32
print (f,'em graus Fahrenheit.')


f = input('Digite a temperatura em graus fahrenheit:')
f_temp = eval(f)
c = 5/9 * f_temp - 32
print (c, 'em  graus Celsius.')