

#Questão 1
#a
def sum(a,b):
    return a+b 
if __name__=='__funcoes__':
        sum() 
# b
def division(a,b):
    if b==0:
        return None
    else: 
        return a/b 
if __name__=='__funcoes__':
        division() 
# c    
def areaTri(a,b):
    return (a*b)/2
if __name__=='__funcoes__':
        areaTri() 
# d
def areaCirc(r):
    pi=3.141592
    return pi*(r**2)
if __name__=='__funcoes__':
        areaCirc() 
# e
def seno(bc,ab):
    if ab==0: 
        return None
    else:
        return bc*ab
if __name__=='__funcoes__':
        seno() 
# f        
def potencia (a,b):
    return a**b 
if __name__=='__funcoes__':
        potencia()     
# Questão 2 
# Resposta Conceito B,C,D
def q2():
    x=8
    if x>=8.5:
        print("Conceito A")
    if x>=7.5:
        print("Conceito B")
    if x>=5.5:
        print("Conceito C")
    if x>=5:
        print("Conceito D") 
if __name__=='__funcoes__':
        q2()    

# Questão 3
# Resposta Conceito B
def q3():
    x=8
    if x>=8.5:
        print("Conceito A")
    elif x>=7.5:
        print("Conceito B")
    elif x>=5.5:
        print("Conceito C")
    elif x>=5:
        print("Conceito D")   
if __name__=='__funcoes__':
        q3()         
# Questão 4
# Resposta: A data de hoje nao é 8/5/13
def q4():
    x=8
    y=5
    z=13
    if x>=1 and x<=31:
        if y>0 and y<13:
            if (x+y)!= z:
                print("A data de hoje é 8/5/2018")
            else:
                print("A data de hoje nao é 8/5/13")
if __name__=='__funcoes__':
    q4() 
#Questão 5
#Resposta
def dvmm(a,b,c,d,e):
    lista = [a,b,c,d,e]
    return max(lista)
    # aux = vet[[0]
    # count=1 
    # while count<len(vet):       
        # if aux<vet[count]:
            # aux=vet[count]
            # aux +=1
# a=int(input())
    # b=int(input())
    # a=int(input())
    # a=int(input())
    # a=int(input())
  # a=int(input())
  
#Questão 6: Exibe SPAM N usando for
def spam(n):
    for i in range(n):
        print("SPAM")
if __name__=='__funcoes__':
        spam()       

#Questão 7: Exibe SPAM N usando while
def spam2(n):
    count=1
    while count<=n:
        print("SPAM")  
        count=count+1   
if __name__=='__funcoes__':
        spam2() 
#Questão 8:Mostrar o números de números impares no intervalo
def nimpar(n):
    for i in range(1,n+1,2):
        print(i)
if __name__=='__impar__':
    nimpar()

#Questão 9: Exibe intervalo,usando for
def intervalo(x,y):
        if x<y:
            for i in range(x,y+1,1):
                print(i)
        else:
            None
 
def intervalo2(x,y): #exibe intervalo usando while
        sum=0
        count=x
        if x<y:
            while count<y:
                sum=sum+1
                print(sum)
                count=count+1
if __name__=='__funcoes__':
    intervalo2()
            
 
#Questão : Determina valor máximo
def detvm(a,b,c,d,e):
    
    if a==b:
        maximo=a
    if a>b:
        maximo=a
    if b>a:
        maximo=b
    if c>maximo:
        maximo=c
    if d>maximo:
        maximo=d
    if e>maximo:
        maximo=e
    print(maximo)
if __name__=='__funcoes__':
    detvm()

#Questão 10: Mostrar os números inteiros em um intervalo[)
def ninteirosx(x,y):
    if x<y:
        for i in range(x,y):
          print(i)
    else:
        print("y não pode ser menor que x")

if __name__=='__funcoes__':
    ninteirosx()

#Questão 11: Mostrar os números inteiros em um intervalo(]
def ninteirosy(x,y):
    if x<y:
        for i in range(x+1,y+1):
            print(i)
    else:
        print("y não pode ser menor que x")

if __name__=='__funcoes__':
    ninteirosy()        

#Questão 12: Calcula a soma das sequência de números inteiros
def sninteirosf(x,y):
    sum=0
    if x<y:
        for i in range(x,y+1,1):
            sum += i
            print(sum)          
    else:
        print("y não pode ser menor que x")

if __name__=='__funcoes__':
    sninteirosf() 
    
#Questão 13: Calcula soma ora negativa,ora positiva n vezes
def nsum(n):
    sum = 0
    for i in range(1, n+1, 1):
        if i % 2 == 0:
            sum += i
        else:
            sum -= i
    print(sum)
if __name__=='__funcoes__':
    nsum() 

#Questão 13.2:Calculo negativo impar ,positivo par
# def nsum2(n):
    # sum = 0
    # aux=0
    # while(aux<=n):
        # if (aux % 2 == 0):
            # sum +=sum+aux
        # else:
            # sum -= sum-aux
        # aux=aux+1
    # print(sum)
# if __name__=='__funcoes__':
    # nsum2() 
#Questão 14: Calcule n sendo n!
def nsump(n):
    dt = 1
    while n > 1:
        dt *= n
        n -= 1     
    return(dt)
if __name__=='__funcoes__':
    nsump() 

#Questão15: Impossível calcular 
    
#Questão 16:Resolvido

# def nlast(a,b):
    # while ((b!=0) and(a%10== b%10)):
        # a=a/10
        # b=b/10
        # if (b==0):
            # return True
        # else:
            # return False

#!/usr/bin/python
# nlast
 
def nlast(a, b):
  if b<a:
    while True:
        print(a, b)
        if 0 == b:
            return True
        elif b % 10 == a % 10:
            b //= 10
            a //= 10
        else:
            return False
if __name__=='__funcoes__':
    nlast() 
def nlaststr(a, b):
    a, b = str(a), str(b)
    return a.endswith(b)
if __name__=='__funcoes__':
    nlaststr() 
 
# def nlast3():
    # from funcoes import nlast
    # print('nlast(12345, 45): {}'.format(nlast(12345, 45)))
    # print('nlast(2026, 2026): {}'.format(nlast(2026, 2026)))
    # print('nlast(45, 12345): {}'.format(nlast(45, 12345)))
 
    # print('nlaststr(12345, 45): {}'.format(nlaststr(12345, 45)))
    # print('nlaststr(2026, 2026): {}'.format(nlaststr(2026, 2026)))
    # print('nlaststr(45, 12345): {}'.format(nlaststr(45, 12345)))
# if __name__ == '__funcoes__':
    # nlast3()                
#Questão 16.3 outras soluções
def encaixa(a,b):
    debug=True
    if debug:
        print("a:
    if (b<a):
        return "Não encaixa"
    if (b==a):
        return "Encaixa"
    elif (a-b)%10==0:
        return "Encaixa"
    else:
        "Não encaixa"
#Questão 17:Fibonacci
def fib(n):
    a, b = 0, 1
    print(a)
    while (b < n):
        a, b = b, a + b
        print(a)
if __name__=='__funcoes__':
    fib()        
def fib2(n):
    sum=1
    a= 0
    b = 1
    print(a)
    while (b<n):
        c=a
        a=b
        b=a+c
        print(a)        
if __name__=='__funcoes__':
    fib2() 

#Questão 18:    
def funcao1(lista):
    temp1 = lista[0] 
    temp2 = lista[len(lista)-1] 
    for elemento in lista:
        if temp1>elemento:
            temp1 = elemento
        if temp2<elemento:
            temp2 = elemento
    print (str(temp1)+str(temp2))
if __name__=='__funcoes__':
    funcao1()     

#Questão 19: Dada uma lista imprima todos os seus elementos   
def ielementos(lista):
    imprima= []
    for i in range(1,lista+1,1):
        imprima.append(i)
    return imprima
if __name__=='__funcoes__':
    ielementos()     
#Questão 20:Dada uma lista some todos os seus elementos
from funcoes import ielementos
def sum_elementos(lista):
    sum=0
    for i in ielementos(lista):
        sum+=i
    return sum 
if __name__=='__funcoes__':
    sum_elementos()      
#obs:ielementos é uma outra função criada por mim, veja a questão 19,para mais detalhes.    
#Questão 21:Crie uma função que permita verificar se 2 listas,dadas como parâmetros, são iguais.    
def equi_lista(lista1,lista2):
    print("Lista1")
    for i in ielementos(lista1):
        print (i)
        n1=i
    print("Lista2")
    for i in ielementos(lista2):
        print (i)
        n2=i
    if n1==n2:
        return "As listas são iguais"
    else:
        return "As listas não são iguais"
if __name__=='__funcoes__':
    equi_lista()      

#Questão 22:Dada a função 'sjakj' indique a saída para n=10.
def sjakj(n):
    if n==0:
        print ("fogo!")
    else:
        print (n)
        sjakj(n-1)
if __name__=='__funcoes__':
    sjakj()     
#Saida 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# fogo!

#Questão 23:Indique a mensagem que apresentará a execução da seguinte função.Considerando como parãmetros: x1=2, y1=3, x2=4, y2=5,ra=112233.

def operacoes(x1, y1, x2, y2, ra):
    p = 0
    while p <(x2-x1)**2 + (y2-y1)**2:
        if x1 < x2:
            print (ra,x1)
        else:
            print(ra,y1)
        p = p+2
if __name__=='__funcoes__':
    operacoes()   
#Saida
# 112233 2
# 112233 2
# 112233 2
# 112233 2

