
a ='''
sipush 4
iload 0
imul
iload 2
imul
iload 1
iload 1
imul
isub
'''


b='''
sipush 4
iload 0
iload 2
imul
imul
iload 1
dup
imul
isub
istore 3
'''

b = '''
iload 1
dup
imul
sipush 3
iload 0
imul
iload 2
imul
isub
istore 3
'''

def hi(i):
    u=''
    for v in i.split("\n"):
        if v:
            u+=(v+",")
    print(u[:-1])


hi(b)


