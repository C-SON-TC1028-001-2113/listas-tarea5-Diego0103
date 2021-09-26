def main():
    #escribe tu código abajo de esta línea
    lista=[]
    n=int(input())
    if n<=0:
        print ("Error")
    else: 
        for i in range(n):
            dato=input()
            lista.append(dato)
        print (lista)
        
        for i in len(lista):
            if lista[i] in lista[i+1:]:
                del lista[i]
        print (lista)



if __name__=='__main__':
    main()
