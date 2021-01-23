
# 乘法表
def mut9_9():
    for i in range(1, 10):
        for j in range(1, i+1):
            print('{}x{}={}\t'.format(j, i, i*j), end='')
        print()


print(mut9_9())