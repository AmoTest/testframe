

for i in range(9):
    for j in range(i+1):
        z = (i+1) * (j+1)
        print(str(i+1) + "*" + str(j+1) + "=" + str(z), end=' ')
    print('\n')

for i in range(1, 10):
    for j in range(1, i+1):
        print('{}*{}={}'.format(i, j, i*j), end='\t')
    print('')

i = 1
while i < 10:
    j = 1
    while j <= i:
        print('{}x{}={}\t'.format(i, j, i*j), end='')
        j += 1
    i += 1
    print('')
