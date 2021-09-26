def main():
    #escribe tu código abajo de esta línea
    lista=[]
    lista2=[]
    n=int(input())
    if n<=0:
        print ("Error")
    else: 
        for i in range(n):
            dato=input()
            lista.append(dato)
            if dato not in lista2:
                lista2.append(dato)
        print (lista)
        print (lista2)


if __name__=='__main__':
    main()
