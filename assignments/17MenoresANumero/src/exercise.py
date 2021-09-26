def resultado(m):
    listafinal=[]
    for i in range (len(m)):
       if m[i]<10:
           listafinal.append(m[i])
    return listafinal

def datos(r,c):
    valores=[]
    matriz=[]
    listacompleta=[]
    for i in range(r):
        for i in range (c):
            valor=int(input())
            valores.append(valor)
        matriz.append(valores)
        listacompleta=listacompleta+valores
        valores=[]
    return resultado(listacompleta)

def main():
    renglones=int(input())
    columnas=int(input())
    print (datos(renglones,columnas))
  

if __name__=='__main__':
    main()
