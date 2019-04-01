#!\Users\Charli\AppData\Local\Programs\Python\Python37\python
"""
      Operaciones con tuplas
"""

wow = 1, 0, 0

"""
    niega el valor booleano de una tupla en el indice index
"""
def not_Binario( t ):
    index = 0
    b = bool( t[index])  #Acotamos que es estamos trabajando con booleanos
    """
        #   para debuguear
        print ( str(b) )
    """
    new = not b  # lo negamos
    st = str ( new) #lo convertimos a string
    print( st ) #imprimimos


"""
    Actividad principal
"""
def main():
    not_Binario( wow )


main() #iniciamos el programa
