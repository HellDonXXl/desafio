

k = int(input("Digite o número que vai ser verificado na tabela Fibonacci: "))
anterior = 0
proximo = 0 

vf = False 

while(proximo < k+1):
    print(proximo)
    if(proximo == k):
       vf = True
        
    proximo = proximo + anterior
    anterior = proximo - anterior
    if(proximo == 0):
        proximo = proximo + 1
if(vf == True):
     print("o número informado pertence a sequência de Fibonacci")
else:
    print("o número informado não pertence a sequência de Fibonacci")     
    
    
    