
a = input("Digite uma frase: ")
def reverse(a):
 b = ''
 index = len(a)
 while index:
     index -= 1
     b += a[index]
 return b

print(reverse(a)) 