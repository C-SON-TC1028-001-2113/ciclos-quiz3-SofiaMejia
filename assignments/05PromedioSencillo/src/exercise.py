def main():
    #escribe tu código abajo de esta línea
    suma = 0
    n = int(input(""))
    for cont in range(1,n+1):
        nn = float(input(""))
        
        suma += nn 
    promedio = suma / n
    print(promedio)
if __name__=='__main__':
    main()
