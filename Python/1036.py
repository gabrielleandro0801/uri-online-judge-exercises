a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

delta = pow(b, 2) - 4 * a * c

if (delta <= 0) or (a == 0):
    print('Impossivel calcular')
else:
    r1 = ((b * -1) + pow(delta, 0.5)) / (2 * a)
    r2 = ((b * -1) - pow(delta, 0.5)) / (2 * a)
    print('R1 = {:.5f}' .format(r1))
    print('R2 = {:.5f}' .format(r2)) 
    
