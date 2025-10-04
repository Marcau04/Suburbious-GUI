import wx                                                                       #practica hecha por Marcos Alonso Ulloa y Marcos Cámara Vicente
import random
import wx.adv

class Secuencia: #Introduccion de la clase secuencia, que es aquella la cual contiene todos los métodos que alterarán o tendrán que ver con la secuencia de los elementos del juego
    def __init__(self): #introducimos las listas que serán indispensables para el desarrollo de el resto de los métodos de las clase secuencia
        self.sec = [] #lista que usaremos para generar una secuencia aleatoria en caso de que no tengamos una establecida
        for i in range(0, 30):
            self.sec.append('a')
        for i in range(5):
            self.sec.append('b')
        for i in range(1):
            self.sec.append('c')
        for i in range(6):
            self.sec.append('1')
        for i in range(1):
            self.sec.append('W')
        return None

    def crearSecuencia(self, secname, turno): #En este método utilizaremos la lista creada anteriormente para establecer una secuencia aleatoria
        alca = 0
        new = ''
        secu = ""
        num = random.randrange(0, 42) #Generamos un número aleatorio que será el que determinara la posicion de la lista con el elemento que queremos "generar"
        try:    #El método introduce una secuencia predeterminada extraida de un fichero externo
            f = open(f"{secname}", "r")
            fila = f.readline()
            totalfila=len(fila)-1
            if turno>totalfila:
                alca=turno//totalfila
                turno=turno-totalfila*alca
            new = fila[turno - 1]
        except Exception: #Si no existe fichero externo, generará una secuencia aleatoria
            new = self.sec[num]
        return new


class Tablero: #Introduccion de la clase tablero, que es aquella la cual contiene todos los métodos que alterarán o tendrán que ver con el tablero del juego
    def __init__(self,filas,columnas): #Contiene las listas y variables que nos serán necesarias para el resto de metodos
        self.fil=filas
        self.col=columnas
        self.matriz = []
        self.lista = []
        self.age = 0
        self.edadbigfoot = {}
        for i in range(0, 45):
            self.lista.append('.')
        for i in range(18):
            self.lista.append('a')
        for i in range(4):
            self.lista.append('b')
        for i in range(3):
            self.lista.append('c')
        for i in range(2):
            self.lista.append('1')
        # return None

    def crearTablero(self): #Este método crea un tablero de manera aleatoria en caso de que no se introduzca uno predeterminado
        for i in range(self.fil):
            dato = ''
            fila = [dato] * self.col
            self.matriz.append(fila)
        return None

    def copiarTablero(self,fichero): #Este método copia un tablero introducido a través de un fichero
        try:
            f = open(f"{fichero}", "r")
            print('hola')
            fila = f.readlines()[1:]
            for i in range(self.fil):
                palabra = fila[i]
                for j in range(self.col):
                    self.matriz[i][j] = palabra[j]
        except:
             num = 0

             for i in range(self.fil):
                 for j in range(self.col):
                     num = random.randrange(0, 71)
                     self.matriz[i][j] = self.lista[num]
             return None
    def llenarTablero(self): #rellena el tablero con los elementos o bien extraidos del fichero o bien generados aleatoriamente

        num = 0

        for i in range(self.fil):
            for j in range(self.col):
                num = random.randrange(0, 71)
                self.matriz[i][j] = self.lista[num]
        return None

    def dibujarTablero(self, turno, puntos, actual, almacen): #Este método dibuja el teblero en pantalla
        abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R",
                      "S", "T", "U", "V", "W", "X", "Y", "Z"]
        print(end="   ")
        for i in range(self.col):
            print(i + 1, end="   ")
        print("")
        print(end=" ")
        for i in range(self.col):
            print("┌───", end="")
        print("┐")                          #Imprime las líneas que le dan imagen a un tablero, en un principio, 6x6
        for i in range(self.fil):
            print(abecedario[i], end="")
            for j in range(self.col):
                print("│", self.matriz[i][j], end=" ") #Introduce el elemento que tiene que ir dentro de la celda
            print("│", end="")
            print("")
            print(end=" ")
            for h in range(self.col):
                if i < self.fil - 1:
                    print("├───", end="")
            if i < self.fil - 1:
                print("┤")
        for k in range(self.col):
            print("└───", end="")
        print("┘")
        print(end=" ")
        print(f"Turno: {turno}", end=" ") #Imprime en pantalla los puntos, el almacen y el elemento actual
        print(f"Puntos: {puntos}")
        print(f"Almacen: [{almacen}]", end=" ")
        print(f"Actual: [{actual}]")
        return None

    def ocupadaCord(self, coord, actual): #Este método comprueba que las coordenadas introducidas puedan ser ocupadas y, a su vez, que las coordenadas estén bien introducidas
        letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        posicion = 0
        if coord == '*':
            return False
        if coord[0] < 'A' or 'Z' < coord[0]: #Comprueba que el primer elemento sea una letra mayúscula
            return True
        if len(coord) != 2: #Comprueba que las coordenadas tengan longitud 2
            return True
        try:
            num = int(coord[1])
        except:
            return True
        for i in range(len(letras)): #Comprueba que las coordenadas introducidas estén disponibles
            if letras[i] == coord[0]:
                posicion = i
        if num > self.col or posicion + 1 > self.fil:
            return True
        else:
            if actual == 'W': #Comprueba que el Wick no se introduzca en una posicion vacia
                if self.matriz[posicion][num - 1] == '.':
                    return True
                else:
                    return False
            else:
                if self.matriz[posicion][num - 1] != '.':
                    return True
                else:
                    return False

    def colocarCord(self, coord,actual):  # método que recibe las coordenadas y el elemento actual y lo coloca en la matriz
        letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"  # diccionario utilizado para operar con las coordenadas dadas
        posicion = 0  # inicializamos posición en 0
        num = int(coord[1])  # num es el segundo elemento de las coordenadas, es decir las Y de la matriz
        for i in range(len(letras)):  # recorremos letras para que una vez que encuentre una letra que sea igual a la introducida en las coordenadas, nos devuelva su posición(las X de la matriz)
            if letras[i] == coord[0]:
                posicion = i
        if actual == 'W':  # si en actual tenemos un wick hay que operar de manera distinta
            if self.matriz[posicion][num - 1] == '1' or self.matriz[posicion][num - 1] == '2' or self.matriz[posicion][num - 1] == '3' or self.matriz[posicion][num - 1] == '4':  # si el elemento que vamos a quitar es parte de la cadena de los BF, eliminamos su edad del diccionario para evitar errores
                self.edadbigfoot.pop((posicion, num - 1), None)
            self.matriz[posicion][num - 1] = '.'  # introducimos el valor vacío en dicha posición que hemos eliminado

        else:
            self.matriz[posicion][num - 1] = actual  # sino es un wick, introducimos en la matriz el elemento actual
        return None

    def extraercoords(self,coord):  # método usado para obtener las coordenadas del elemento introducido para operar en los siguientes métodod de colapso(se opera igual que en el método anterior)
        letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        posicion = 0
        num = int(coord[1])
        for i in range(len(letras)):
            if letras[i] == coord[0]:
                posicion = i
        j = int(coord[1])
        return posicion, j - 1

    def confirmarcolapso(self, i, j, prox, i2, j2,visitados):  # recibe las coordenadas del elemento introducido, las últimas coordenadas localizadas y la lista de visitados para evitar bucles infinitos
        if self.matriz[i][j] == 'a' or self.matriz[i][j] == 'b' or self.matriz[i][j] == 'c' or self.matriz[i][j] == 'd':  # si el elemento es a,b,c o d operamos
            visitados = list(visitados)  # pasamos visitados  a lista para evitar errores
            visitados.append(f"{i}{j}")  # introducimos las coordenadas actuales a dicha lista

            if i > 0 and (
            f"{i - 1}{j}") not in visitados:  # si puede haber un elemento arriba y además este no está en visitado, comprobamos
                if self.matriz[i][j] == self.matriz[i - 1][j] and i - 1 != i2:  # si el elemento de las coordenadas actuales es igual al de arriba y además ese no lo hemos visto anteriormente procedemos a continuar
                    prox = prox + 1  # aumentamos el número de elementos próximos en 1
                    prox = self.confirmarcolapso(i - 1, j, prox, i, j,
                                                 visitados)  # aplicamos recursividad con las coordenadas del elemento de arriba
            if i < self.fil - 1 and (f"{i + 1}{j}") not in visitados:  # en el resto de direcciones de opera igual
                if self.matriz[i][j] == self.matriz[i + 1][j] and i + 1 != i2:
                    prox = prox + 1
                    prox = self.confirmarcolapso(i + 1, j, prox, i, j, visitados)
            if j > 0 and (f"{i}{j - 1}") not in visitados:
                if self.matriz[i][j] == self.matriz[i][j - 1] and j - 1 != j2:
                    prox = prox + 1
                    prox = self.confirmarcolapso(i, j - 1, prox, i, j, visitados)
            if j < self.col - 1 and (f"{i}{j + 1}") not in visitados:
                if self.matriz[i][j] == self.matriz[i][j + 1] and j + 1 != j2:
                    prox = prox + 1
                    prox = self.confirmarcolapso(i, j + 1, prox, i, j, visitados)
        else:
            prox = 0  # si los elementos son distintos de los que pueden colapsar devolvemos que prox es 0
        return prox

    def colapso1(self, i, j, prox, i2, j2,colapsados):  # método que va a añadir en una lista todos los elementos que pueden colapsar
        colapsados = list(colapsados)  # opera igual que el método anterior, recogiendo los valores ya comprobados en la lista listocolap para evitar bucles infinitos y aplicando recursividad con las nuevas coordenadas
        colapsados.append(f"{i}{j}")
        listcolap = []
        if i > 0 and (f"{i - 1}{j}") not in colapsados:
            if self.matriz[i][j] == self.matriz[i - 1][j] and i - 1 != i2:
                listcolap.append(f"{i - 1}{j}")
                listcolap += self.colapso1(i - 1, j, prox, i, j, colapsados)
        if i < self.fil - 1 and (f"{i + 1}{j}") not in colapsados:
            if self.matriz[i][j] == self.matriz[i + 1][j] and i + 1 != i2:
                listcolap.append(f"{i + 1}{j}")
                listcolap += self.colapso1(i + 1, j, prox, i, j, colapsados)
        if j > 0 and (f"{i}{j - 1}") not in colapsados:
            if self.matriz[i][j] == self.matriz[i][j - 1] and j - 1 != j2:
                listcolap.append(f"{i}{j - 1}")
                listcolap += self.colapso1(i, j - 1, prox, i, j, colapsados)
        if j < self.col - 1 and (f"{i}{j + 1}") not in colapsados:
            if self.matriz[i][j] == self.matriz[i][j + 1] and j + 1 != j2:
                listcolap.append(f"{i}{j + 1}")
                listcolap += self.colapso1(i, j + 1, prox, i, j, colapsados)
        return listcolap

    def colapso2(self,listacoords, ):  # recibe la lista de coordenadas calculada en el anterior apartado y opera en base a ella
        total = len(listacoords)  # el número total de elementos juntos es igual a la longitud de dicha lista
        for i in range(total):  # recorres la lista un número 'total' de veces
            coordenada = listacoords[i]  # das a coordenada cada elemento de la lista que contendrá las coordenadas de los elementos a colapsar y les cambia el valor a un punto
            x = int(coordenada[0])
            y = int(coordenada[1])
            self.matriz[x][y] = "."
        return None

    def cambioelemento(self, i,j):  # método que una vez los elementos que han colapsado de han transformado en un punto, cambia el elemento que hemos introducido a un elemento que lo colapse
        elemento = self.matriz[i][j]  # obtiene el valor del elemento que hemos introducido en la posición dada
        if elemento == 'a':  # en base  a que elemento sea lo transforma en un valor que lo colapse
            self.matriz[i][j] = 'b'
        if elemento == 'b':
            self.matriz[i][j] = 'c'
        if elemento == 'c':
            self.matriz[i][j] = 'd'
        if elemento == 'd':
            self.matriz[i][j] = 'e'
        return None

    def puntosronda(self):  # calculamos los puntos por ronda recorriendo la matriz y sumando el valor exacto al total de puntos según con que valores se vaya encontrando(se actualiza cada ronda)
        puntos = 0
        for i in range(self.fil):
            for j in range(self.col):
                if self.matriz[i][j] == 'a':
                    puntos += 1
                if self.matriz[i][j] == 'b':
                    puntos += 5
                if self.matriz[i][j] == 'c':
                    puntos += 25
                if self.matriz[i][j] == 'd':
                    puntos += 125
                if self.matriz[i][j] == 'e':
                    puntos += 625
                if self.matriz[i][j] == '1':
                    puntos += -25
                if self.matriz[i][j] == '2':
                    puntos += -5
                if self.matriz[i][j] == '3':
                    puntos += 50
                if self.matriz[i][j] == '4':
                    puntos += 500
                if self.matriz[i][j] == 'X':
                    puntos += -50
                if self.matriz[i][j] == '.':
                    puntos += 0
        return puntos

    def colapsoBigFoot(self):  # método para colapsar los BF
        for i in range(self.fil):  # recorremos toda la matriz
            for j in range(self.col):
                encerrado = True  # damos por supuesto que esta encerrado
                if self.matriz[i][j] == '1':  # si encontramos un BF comprobamos
                    if i > 0 and self.matriz[i - 1][
                        j] == '.':  # si en cualquier direccion encontramos un '.' significa que no está encerrado
                        encerrado = False
                    elif j < self.col - 1 and self.matriz[i][j + 1] == '.':
                        encerrado = False
                    elif i < self.fil - 1 and self.matriz[i + 1][j] == '.':
                        encerrado = False
                    elif j > 0 and self.matriz[i][j - 1] == '.':
                        encerrado = False
                    if encerrado == True:  # sino, lo colapsamos en un 2, y aumentamos por última vez su edad
                        self.matriz[i][j] = '2'
                        self.edadbigfoot[(i, j)] = self.edadbigfoot.get((i, j), 0) + 1
        return None

    def movimientoBigfoot(self):  # método para realizar el movimiento de los BF
        unosmovidos = []  # guardamos los unos que hemos movido en esta lista para que un mismo uno no se mueva varias veces

        for i in range(self.fil):  # recorremos la matriz hasta encontrarnos con un uno
            for j in range(self.col):
                if self.matriz[i][j] == '1':
                    if i > 0 and self.matriz[i - 1][j] == '.' and f"{i}{j}" not in unosmovidos:  # si se puede mover hacia arriba, esa posición esta vacía y ademas ese uno todavía no se ha movido seguimos
                        unosmovidos.append(f"{i - 1}{j}")  # añadimos las coordenadas a donde se va a mover en la lista para que no se mueva mas de una vez
                        self.edadbigfoot[(i - 1, j)] = self.edadbigfoot.get((i, j),
                                                                            0) + 1  # incrementamos su edad, en caso de que aún no estuviera en el diccionario, lo añadimos con la edad 1
                        self.edadbigfoot.pop((i, j),None)  # eliminamos en caso de que ya estuviera en el diccionario, el elemento del diccionario que corresponde a su posición vieja
                        self.matriz[i - 1][j] = '1'
                        if self.edadbigfoot[(i - 1, j)] > 10:  # si su edad es mayor o igual que 10, en su posición vieja dejamos un escombro
                            self.matriz[i][j] = 'X'
                        else:
                            self.matriz[i][j] = '.'  # sino, dejamos el espacio vacío('.')

                    elif j < self.col - 1 and self.matriz[i][j + 1] == '.' and f"{i}{j}" not in unosmovidos:  # realizamos el mismo método en todas las direcciones según el orden de prioridad(arriba,derecha,abajo,izquierda)
                        unosmovidos.append(f"{i}{j + 1}")
                        self.edadbigfoot[(i, j + 1)] = self.edadbigfoot.get((i, j), 0) + 1
                        self.edadbigfoot.pop((i, j), None)
                        self.matriz[i][j + 1] = '1'
                        if self.edadbigfoot[(i, j + 1)] > 10:
                            self.matriz[i][j] = 'X'
                        else:
                            self.matriz[i][j] = '.'
                    elif i < self.fil - 1 and self.matriz[i + 1][j] == '.' and f"{i}{j}" not in unosmovidos:
                        unosmovidos.append(f"{i + 1}{j}")
                        self.edadbigfoot[(i + 1, j)] = self.edadbigfoot.get((i, j), 0) + 1
                        self.edadbigfoot.pop((i, j), None)
                        self.matriz[i + 1][j] = '1'
                        if self.edadbigfoot[(i + 1, j)] > 10:
                            self.matriz[i][j] = 'X'
                        else:
                            self.matriz[i][j] = '.'

                    elif j > 0 and self.matriz[i][j - 1] == '.' and f"{i}{j}" not in unosmovidos:
                        unosmovidos.append(f"{i}{j - 1}")
                        self.edadbigfoot[(i, j - 1)] = self.edadbigfoot.get((i, j), 0) + 1
                        self.edadbigfoot.pop((i, j), None)
                        self.matriz[i][j - 1] = '1'
                        if self.edadbigfoot[(i, j - 1)] > 10:
                            self.matriz[i][j] = 'X'
                        else:
                            self.matriz[i][j] = '.'
        return None

    def colapsoBF1(self):  # método colapso de BF
        edadesordenadas = dict(self.edadbigfoot)  # para evitar errores transformamos nuevamente edadesordenadas en un diccionario

        for coordenadas, edades in edadesordenadas.items():  # pasamos cada una de las "claves" del diccionario al valor de coordenadas ya que estas claves son las coordenadas de los BF cuyo valor son las edades de dichos BF
            i, j = coordenadas  # las coordenadas las pasamos a i,j para poder recorrer fácilmente la matriz
            edad = edades
            contador = 0  # contador de cuantos bebes hay juntos
            bbjunto = []  # variable creada para añadir los BF ya comprobados y evitar bucles infinitos
            if (self.matriz[i][j] == '2' and (f"{i}{j}") not in bbjunto):  # si el BF de dicha coordenada ya es un bebe y aún no lo hemos comprobado seguimos
                bbjunto.append(f"{i}{j}")  # lo añadimos a la lista para asegurarnos de no volver a él luego y entrar en un bucle infinito
                contador = contador + 1  # aumentamos el contador de bebes juntos en 1

                def colapsoBF2(i,j):  # entramos en un método anidado para comprobar los vecinos de los vecinos y así obtener todos y cada uno de los bebes que hay juntos
                    nonlocal bbjunto, contador  # nos aseguramos que bbjunto y contador no son variable locales de este método anidado
                    if (i > 0):  # si i es mayor que 0, siginifica que puede haber un bebe en la posición de arriba
                        if (self.matriz[i - 1][j] == '2' and f"{i - 1}{j}" not in bbjunto):  # comprobamos que esto úñtimo sea cierto y en caso de ser cierto:
                            bbjunto.append(f"{i - 1}{j}")  # añadimos sus coordenadas a la lista, incrementamos el contador y aplicamos recursividad con dicho valor
                            contador = contador + 1
                            colapsoBF2(i - 1, j)
                    if (j < self.col - 1):  # repetimos este mismo proceso para todas las direcciones posibles siguiendo el orden de prioridad(arriba,derecha,abajo,izquierda)
                        if (self.matriz[i][j + 1] == '2' and f"{i}{j + 1}" not in bbjunto):
                            bbjunto.append(f"{i}{j + 1}")
                            contador = contador + 1
                            colapsoBF2(i, j + 1)
                    if (i < self.fil - 1):
                        if (self.matriz[i + 1][j] == '2' and f"{i + 1}{j}" not in bbjunto):
                            bbjunto.append(f"{i + 1}{j}")
                            contador = contador + 1
                            colapsoBF2(i + 1, j)
                    if (j > 0):
                        if (self.matriz[i][j - 1] == '2' and f"{i}{j - 1}" not in bbjunto):
                            bbjunto.append(f"{i}{j - 1}")
                            contador = contador + 1
                            colapsoBF2(i, j - 1)
                    return bbjunto, contador  # devolvemos la lista con las coordenadas de los bebesjuntos y el número de bebes juntos que hay

                bbjunto, contador = colapsoBF2(i, j)  # llamamos a la función para obtener ambas variables
                if contador >= 3:  # si hay mas de 3 bebes juntos procedemos a colapsar
                    edadmaxima = 0  # variable que se actualizará para comprobar la edad máxima
                    for x, y in bbjunto:  # extraemos las coordenadas de los bebes
                        edad = edadesordenadas[(int(x),int(y))]  # obtenemos su edad a través del diccionario que la contiene y vamos actualizando la edad máxima en base a cual va siendo la mas alta
                        if edad > edadmaxima:
                            edadmaxima = edad
                    for x, y in bbjunto:  # una vez se tiene la edad máxima recooremos otra vez todos los bebes, en caso de que la edad de dicho bebe sea la máxima lo sustituimos por un 3, y de no ser así desaparecen con un punto y se les elimina del diccionario de edades
                        if edadesordenadas[(int(x), int(y))] == edadmaxima:
                            self.matriz[int(x)][int(y)] = '3'
                        else:
                            self.matriz[int(x)][int(y)] = '.'
                            self.edadbigfoot.pop((int(x), int(y)), None)

        return None

    def colapsoBF4(self):  # este método funciona exactamente igual que el anterior pero cambiando que en lugar de actuar en los '2' para ccolapsar en '3', este colapsa los '3' en '4', pero siguiendo el mismo procedimiento
        edadesordenadas = dict(self.edadbigfoot)

        for coordenadas, edades in edadesordenadas.items():
            i, j = coordenadas
            edad = edades
            contador = 0
            bbjunto = []
            if (self.matriz[i][j] == '3' and (f"{i}{j}") not in bbjunto):
                bbjunto.append(f"{i}{j}")
                contador = contador + 1

                def colapsoBF3(i, j):
                    nonlocal bbjunto, contador
                    if (i > 0):
                        if (self.matriz[i - 1][j] == '3' and f"{i - 1}{j}" not in bbjunto):
                            bbjunto.append(f"{i - 1}{j}")
                            contador = contador + 1
                            colapsoBF3(i - 1, j)
                    if (j < self.col - 1):
                        if (self.matriz[i][j + 1] == '3' and f"{i}{j + 1}" not in bbjunto):
                            bbjunto.append(f"{i}{j + 1}")
                            contador = contador + 1
                            colapsoBF3(i, j + 1)
                    if (i < self.fil - 1):
                        if (self.matriz[i + 1][j] == '3' and f"{i + 1}{j}" not in bbjunto):
                            bbjunto.append(f"{i + 1}{j}")
                            contador = contador + 1
                            colapsoBF3(i + 1, j)
                    if (j > 0):
                        if (self.matriz[i][j - 1] == '3' and f"{i}{j - 1}" not in bbjunto):
                            bbjunto.append(f"{i}{j - 1}")
                            contador = contador + 1
                            colapsoBF3(i, j - 1)
                    return bbjunto, contador

                bbjunto, contador = colapsoBF3(i, j)
                if contador >= 3:
                    edadmaxima = 0
                    for x, y in bbjunto:
                        edad = edadesordenadas[(int(x), int(y))]
                        if edad > edadmaxima:
                            edadmaxima = edad
                    for x, y in bbjunto:
                        if edadesordenadas[(int(x), int(y))] == edadmaxima:
                            self.matriz[int(x)][int(y)] = '4'
                        else:
                            self.matriz[int(x)][int(y)] = '.'
                            self.edadbigfoot.pop((int(x), int(y)), None)
        return None

    def mapalleno(self):  # método comprueba si el mapa está lleno
        num = 0  # contador para comprobar
        for i in range(self.fil):  # recorremos la matriz y en caso de encontrar un '.', el contador se incrementa
            for j in range(self.col):
                if self.matriz[i][j] == '.':
                    num = num + 1
        if num == 0:  # si el contador se ha incrementado, el tablero aún no está lleno, si no se ha incrementado si lo está
            return True
        else:
            return False


class Suburbious(wx.Frame):  #Iniciamos el juego con este primer frame a partir del cual generaremos la primera partida
    def __init__(self, *args, **kwds):
        # begin wxGlade: Suburbious.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((640, 538))
        self.SetTitle("Suburbious")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.panel_1.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)

        self.panel_2 = wx.Panel(self.panel_1, wx.ID_ANY)
        sizer_3.Add(self.panel_2, 0, wx.EXPAND, 0)

        sizer_4 = wx.WrapSizer(wx.HORIZONTAL)

        self.button_1 = wx.Button(self.panel_2, wx.ID_ANY, "Nueva partida")                                                                 #Boton para crear la partida y checkbox para limite de tiempo(en este primer frame que es para crearla este último no hace nada)
        self.button_1.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_4.Add(self.button_1, 0, wx.SHAPED, 0)

        self.checkbox_1 = wx.CheckBox(self.panel_2, wx.ID_ANY, u"Límite de tiempo")
        self.checkbox_1.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_4.Add(self.checkbox_1, 3, wx.LEFT, 8)

        self.panel_3 = wx.Panel(self.panel_1, wx.ID_ANY)
        sizer_3.Add(self.panel_3, 0, wx.EXPAND, 0)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)

        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add(sizer_6, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self.panel_3, wx.ID_ANY, u"Almacén")                                                                #elementos visuales para mostrar como será el formato del juego
        label_1.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_6.Add(label_1, 1, wx.LEFT, 10)

        label_2 = wx.StaticText(self.panel_3, wx.ID_ANY, ".")
        label_2.SetFont(wx.Font(23, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_6.Add(label_2, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM, 7)

        self.button_2 = wx.Button(self.panel_3, wx.ID_ANY, u" ⇆\n")
        self.button_2.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_5.Add(self.button_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.TOP, 0)

        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add(sizer_7, 1, wx.EXPAND, 0)

        label_3 = wx.StaticText(self.panel_3, wx.ID_ANY, "Actual")
        label_3.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_7.Add(label_3, 1, wx.LEFT, 10)

        label_4 = wx.StaticText(self.panel_3, wx.ID_ANY, ".")
        label_4.SetFont(wx.Font(23, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_7.Add(label_4, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM, 7)

        self.panel_4 = wx.Panel(self.panel_1, wx.ID_ANY)
        sizer_3.Add(self.panel_4, 1, wx.EXPAND, 0)

        sizer_8 = wx.BoxSizer(wx.VERTICAL)

        label_5 = wx.StaticText(self.panel_4, wx.ID_ANY, u"Puntuación")
        label_5.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_8.Add(label_5, 1, wx.LEFT, 10)

        label_6 = wx.StaticText(self.panel_4, wx.ID_ANY, "0")
        label_6.SetFont(wx.Font(23, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_8.Add(label_6, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 57)

        self.panel_5 = wx.Panel(self.panel_1, wx.ID_ANY)
        sizer_3.Add(self.panel_5, 1, wx.EXPAND, 0)

        sizer_9 = wx.BoxSizer(wx.VERTICAL)

        label_7 = wx.StaticText(self.panel_5, wx.ID_ANY, "Tiempo restante:")
        label_7.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_9.Add(label_7, 1, wx.LEFT, 10)

        label_8 = wx.StaticText(self.panel_5, wx.ID_ANY, "-")
        label_8.SetFont(wx.Font(23, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_9.Add(label_8, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM, 57)

        label_9 = wx.StaticText(self.panel_1, wx.ID_ANY, "Pulse [Nueva partida] para comenzar a jugar")
        label_9.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_1.Add(label_9, 1, 0, 0)

        self.panel_5.SetSizer(sizer_9)

        self.panel_4.SetSizer(sizer_8)

        self.panel_3.SetSizer(sizer_5)

        self.panel_2.SetSizer(sizer_4)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.NuevaPartida1, self.button_1)             #asociamos cada boton con su evento
        self.Bind(wx.EVT_CHECKBOX, self.LimiteTiempo, self.checkbox_1)
        self.Bind(wx.EVT_BUTTON, self.CambiarActual1, self.button_2)
        # end wxGlade

    def NuevaPartida1(self, event):  # wxGlade: Suburbious.<event_handler>
        self.Hide()                         #Configuramos el boton para que nos abra el menú de Nueva partida cerrandonos el primer frame y abriendonos el menú
        self.frame = NuevaPartida(None, wx.ID_ANY, "")
        self.frame.Show()
        event.Skip()

    def LimiteTiempo(self, event):  # wxGlade: Suburbious.<event_handler>

        event.Skip()

    def CambiarActual1(self, event):  # wxGlade: Suburbious.<event_handler>
        event.Skip()


# end of class Suburbious

class NuevaPartida(wx.Frame):       #Generamos el frame del menú de Nueva Partida
    def __init__(self, *args, **kwds):
        # begin wxGlade: NuevaPartida.__init__
        self.seleccion=0
        self.columnas = 6  #Inicializamos las variables que nos harán falta para la creacion de la Nueva partida
        self.filas = 6
        self.fichero=None
        self.frame = None
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 220))
        self.SetTitle("NuevaPartida")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_4, 1, wx.EXPAND, 0)

        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_4.Add(sizer_5, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Nueva Partida")
        label_1.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))           
        sizer_5.Add(label_1, 0, 0, 0)

        self.radio_box_1 = wx.RadioBox(self.panel_1, wx.ID_ANY, "",                                                             #formatos para crear el tablero de la partida
                                       choices=["Leer de Fichero...", "Crear al azar (6x6)",
                                                u"Crear al azar (Elegir tamaño)"], majorDimension=1,
                                       style=wx.RA_SPECIFY_COLS)
        self.radio_box_1.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.radio_box_1.SetSelection(0)
        sizer_5.Add(self.radio_box_1, 1, wx.ALL, 7)

        self.panel_2 = wx.Panel(self.panel_1, wx.ID_ANY)
        sizer_4.Add(self.panel_2, 1, wx.EXPAND, 0)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)

        label_2 = wx.StaticText(self.panel_2, wx.ID_ANY, u"Tamaño del Tablero")                                                 #opciones para en caso de querer tablero de tamaño personalizado y aleatorio(invisible hasta que se marque la opción 3)
        label_2.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_2.Add(label_2, 0, 0, 0)

        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_6, 1, wx.EXPAND, 0)

        label_3 = wx.StaticText(self.panel_2, wx.ID_ANY, u"Nº Filas=")
        label_3.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_6.Add(label_3, 0, wx.LEFT, 36)

        self.spin_ctrl_1 = wx.SpinCtrl(self.panel_2, wx.ID_ANY, "0", min=0, max=100)
        sizer_6.Add(self.spin_ctrl_1, 0, 0, 0)

        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_7, 1, wx.EXPAND, 0)

        label_4 = wx.StaticText(self.panel_2, wx.ID_ANY, u"Nº Columnas=")
        label_4.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_7.Add(label_4, 0, 0, 0)

        self.spin_ctrl_2 = wx.SpinCtrl(self.panel_2, wx.ID_ANY, "0", min=0, max=100)
        sizer_7.Add(self.spin_ctrl_2, 0, 0, 0)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)

        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_9, 1, wx.EXPAND, 0)
        self.label_5 = wx.StaticText(self.panel_1, wx.ID_ANY, "Nombre de Fichero: ")            #textcontrol para introducir el nombre del fichero deseado
        sizer_9.Add(self.label_5, 0, 0, 0)

        self.text_ctrl_1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        sizer_9.Add(self.text_ctrl_1, 0, 0, 0)

        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_8, 1, wx.EXPAND, 0)

        self.button_3 = wx.Button(self.panel_1, wx.ID_ANY, "OK")                    #botones para ir a la partida o volver al frame1
        sizer_8.Add(self.button_3, 0, wx.ALIGN_BOTTOM | wx.LEFT, 220)

        self.button_4 = wx.Button(self.panel_1, wx.ID_ANY, "Cancel")
        sizer_8.Add(self.button_4, 0, wx.ALIGN_BOTTOM, 0)

        self.panel_2.SetSizer(sizer_2)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()
        self.panel_2.Hide()                                                                     #asociamos los botnes con sus eventos
        self.Bind(wx.EVT_RADIOBOX, self.Elecciontablero, self.radio_box_1)
        self.Bind(wx.EVT_SPINCTRL, self.NFilas, self.spin_ctrl_1)
        self.Bind(wx.EVT_SPINCTRL, self.NColumnas, self.spin_ctrl_2)
        self.Bind(wx.EVT_TEXT, self.NombreFichero, self.text_ctrl_1)
        self.Bind(wx.EVT_BUTTON, self.OK_confirm, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.CancelConfirm, self.button_4)
        # end wxGlade

    def Elecciontablero(self, event):  # wxGlade: NuevaPartida.<event_handler>
        self.seleccion = self.radio_box_1.GetSelection() #Abrimos el selector de partida, si bien por fichero, al azar con 6x6 o con un número de columnas y filas que queramos
        if self.seleccion == 0:
            self.label_5.Show()
            self.text_ctrl_1.Show()
            self.panel_2.Hide()
        if self.seleccion == 1:
            self.columnas = 6
            self.filas = 6
            self.label_5.Hide()
            self.text_ctrl_1.Hide()
            self.panel_2.Hide()
        if self.seleccion == 2:
            self.label_5.Hide()
            self.text_ctrl_1.Hide()
            self.panel_2.Show()
        event.Skip()

    def NFilas(self, event):  # wxGlade: NuevaPartida.<event_handler>
        self.filas = self.spin_ctrl_1.GetValue() #Número de filas según el número seleccionado
        event.Skip()

    def NColumnas(self, event):  # wxGlade: NuevaPartida.<event_handler>
        self.columnas = self.spin_ctrl_2.GetValue() #Número de columnas según el número seleccionado
        event.Skip()

    def NombreFichero(self, event):  # wxGlade: NuevaPartida.<event_handler>
        self.fichero= self.text_ctrl_1.GetLineText(0) #Guardar el nombre de fichero según sea introducido
        event.Skip()

    def OK_confirm(self, event):  # wxGlade: NuevaPartida.<event_handler>
        if self.columnas==0 or self.filas==0:   #Confirmamos el inicio de la partida con el boton ok, pasamos las variables que nos harán falta al siguiente frame y cerraremos este frame
            event.Skip()
        else:
            self.Hide()
            self.frame= Suburbious2(self.filas, self.columnas, self.fichero,self.seleccion ,None, wx.ID_ANY, "")
            self.frame.Show()
            event.Skip()
    def CancelConfirm(self, event):  # wxGlade: NuevaPartida.<event_handler>
        self.Hide()
        self.frame = Suburbious(None, wx.ID_ANY, "")
        self.frame.Show()
        event.Skip()


# end of class NuevaPartida

class Suburbious2(wx.Frame):        #Frame en el que se desarrollará el juego
    def __init__(self, filas, columnas,fichero,seleccion, *args, **kwds):
        # begin wxGlade: Suburbious2.__init_
        self.images={       #Introducimos las imágenes que necesitamos
            'a':wx.Bitmap('./images/Tienda.jpg'),
            'b':wx.Bitmap('./images/casa.jpg'),
            'c':wx.Bitmap('./images/mansion.jpg'),
            'd':wx.Bitmap('./images/edificio.jpg'),
            'e':wx.Bitmap('./images/hospital.jpg'),
            '1':wx.Bitmap('./images/bigfoot.jpg'),
            '2':wx.Bitmap('./images/babybigfoot.jpg'),
            '3':wx.Bitmap('./images/escuela.jpg'),
            '4':wx.Bitmap('./images/universidad.jpg'),
            'W':wx.Bitmap('./images/wick.jpg'),
            '.':wx.Bitmap('./images/vacio.png'),
            'X':wx.Bitmap('./images/escombro.jpg'),
            '5':wx.Bitmap('./images/bigfootmayorde5.jpg'),
            '6':wx.Bitmap('./images/bigfootmayorde10.jpg')

        }
        self.almacen='.' #inicializamos variables
        if seleccion==0:
            try:        #abrimos fichero
                f = open(f"{fichero}", "r")
                fila = f.readlines()[1:]
                self.filas=len(fila)
                if self.filas>0:
                    self.columnas=len(fila[0])-1
                else:
                    self.filas=0
                    self.columnas=0

            except:
                self.filas=filas
                self.columnas=columnas
        if seleccion==1:
            self.filas=6
            self.columnas=6
        if seleccion==2:
            self.filas=filas
            self.columnas=columnas
        for i in range(self.filas):
            for j in range(self.columnas):
                self.boton=wx.Window.FindWindowById(self.columnas*i+j)
                if self.boton is not None:
                    self.boton=wx.Window.FindWindowById(self.columnas*i+j).Destroy()
        self.tablero=Tablero(self.filas,self.columnas)      #Accedemos a los métodos que se utilizan para el tablero y  secuencias
        self.tablero.crearTablero()
        self.tablero.copiarTablero(fichero)
        self.puntos=self.tablero.puntosronda()
        self.fichero=fichero
        self.secuencia=Secuencia()
        self.turno=1
        self.actual=self.secuencia.crearSecuencia(self.fichero,self.turno)
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((750, 600))
        self.SetTitle("Suburbious")
        self.marcado = False
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.panel_1.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)

        self.panel_2 = wx.Panel(self.panel_1, wx.ID_ANY)
        sizer_3.Add(self.panel_2, 0, wx.EXPAND, 0)

        sizer_4 = wx.WrapSizer(wx.HORIZONTAL)

        self.button_1 = wx.Button(self.panel_2, wx.ID_ANY, "Nueva partida")
        self.button_1.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_4.Add(self.button_1, 0, wx.SHAPED, 0)

        self.checkbox_1 = wx.CheckBox(self.panel_2, wx.ID_ANY, u"Límite de tiempo")                 #el limite de tiempo ahora si que funciona
        self.checkbox_1.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_4.Add(self.checkbox_1, 3, wx.LEFT, 8)

        self.panel_3 = wx.Panel(self.panel_1, wx.ID_ANY)
        sizer_3.Add(self.panel_3, 0, wx.EXPAND, 0)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)

        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add(sizer_6, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self.panel_3, wx.ID_ANY, u"Almacén")
        label_1.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_6.Add(label_1, 1, wx.LEFT, 10)
        caracter='.'
        imagen=self.images.get(caracter)                                    #inicializamos el almacen con una imagen vacia correspondiente al '.'
        imagen=wx.Bitmap(imagen)
        imagen = wx.Bitmap.ConvertToImage(imagen).Rescale(100,100).ConvertToBitmap()
        self.bitmap_1 = wx.StaticBitmap(self.panel_3, wx.ID_ANY, imagen)
        self.bitmap_1.SetSize((100,100))
        self.bitmap_1.SetFont(wx.Font(23, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_6.Add(self.bitmap_1, 5, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 1)

        self.button_2 = wx.Button(self.panel_3, wx.ID_ANY, u" ⇆\n")
        self.button_2.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_5.Add(self.button_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.TOP, 0)

        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add(sizer_7, 1, wx.EXPAND, 0)

        label_3 = wx.StaticText(self.panel_3, wx.ID_ANY, "Actual")                                                  #inicializamos actual con la primera imagen de la secuencia
        label_3.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_7.Add(label_3, 1, wx.LEFT, 10)
        caracter=self.actual
        imagen=self.images.get(caracter)
        imagen=wx.Bitmap(imagen)
        imagen = wx.Bitmap.ConvertToImage(imagen).Rescale(100,100).ConvertToBitmap()
        self.bitmap_2 = wx.StaticBitmap(self.panel_3, wx.ID_ANY, imagen)
        self.bitmap_2.SetSize((100,100))
        self.bitmap_2.SetFont(wx.Font(23, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_7.Add(self.bitmap_2, 5, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 1)

        self.panel_4 = wx.Panel(self.panel_1, wx.ID_ANY)
        sizer_3.Add(self.panel_4, 1, wx.EXPAND, 0)

        sizer_8 = wx.BoxSizer(wx.VERTICAL)

        label_5 = wx.StaticText(self.panel_4, wx.ID_ANY, u"Puntuación")
        label_5.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_8.Add(label_5, 1, wx.LEFT, 10)

        self.label_6 = wx.StaticText(self.panel_4, wx.ID_ANY, "0")                              #en el valor de la puntuacion ponemos los puntos
        self.label_6.SetLabel(str(self.puntos))
        self.label_6.SetFont(wx.Font(23, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_8.Add(self.label_6, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 57)

        self.panel_5 = wx.Panel(self.panel_1, wx.ID_ANY)
        sizer_3.Add(self.panel_5, 1, wx.EXPAND, 0)

        sizer_9 = wx.BoxSizer(wx.VERTICAL)

        label_7 = wx.StaticText(self.panel_5, wx.ID_ANY, "Tiempo restante:")
        label_7.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_9.Add(label_7, 1, wx.LEFT, 10)

        self.label_8 = wx.StaticText(self.panel_5, wx.ID_ANY, "-")              #el temporizador empieza apagado
        self.label_8.SetFont(wx.Font(23, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.label_8.SetForegroundColour((0,64,255))
        sizer_9.Add(self.label_8, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM, 57)

        self.Tablero_Panel = wx.Panel(self.panel_1, wx.ID_ANY)
        sizer_2.Add(self.Tablero_Panel, 1, wx.EXPAND, 0)
        grid_sizer_1 = wx.GridSizer(self.filas, self.columnas, 0, 0)
        grid_sizer_1.Clear()
        for i in range(int(self.filas * self.columnas)):        #Introducimos los botones que corresponderan a celdas del tablero
            self.button_3= wx.Button(self.Tablero_Panel,i, "")
            self.button_3.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
            grid_sizer_1.Add(self.button_3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
            self.variable=int(self.button_3.GetId())
            self.Bind(wx.EVT_BUTTON, self.PulsarTablero, self.button_3)

        label_9 = wx.StaticText(self.panel_1, wx.ID_ANY, "Pulse en el tablero para colocar las fichas")
        label_9.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        label_9.SetForegroundColour((0, 64, 255))
        sizer_1.Add(label_9, 1, 0, 0)

        self.Tablero_Panel.SetSizer(grid_sizer_1)

        self.panel_5.SetSizer(sizer_9)

        self.panel_4.SetSizer(sizer_8)

        self.panel_3.SetSizer(sizer_5)

        self.panel_2.SetSizer(sizer_4)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

        for i in range(self.filas):     #Introducimos las imágenes correspondientes en el tablero y ajustamos sus tamaños
            for j in range(self.columnas):
                self.boton=wx.Window.FindWindowById(self.columnas*i+j)
                if self.boton is not None:
                    caracter=self.tablero.matriz[i][j]
                    imagen=self.images.get(caracter)
                    imagen=imagen.ConvertToImage()
                    if imagen is not None:
                        imagen = imagen.Scale(self.boton.GetSize()[0],self.boton.GetSize()[1])
                        imagen = wx.Bitmap(imagen)
                        self.boton.SetBitmap(imagen)

        self.timer = wx.Timer(self)         #creamos el temporizador, inizializamos el contador en 10 y el temporizador lo marcamos para que cambie cada 1000 milisegundos(1 segundo)
        self.contador = 10
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.temporizadorfuncionando, self.timer)           #relacionamos evento y boton
        self.Bind(wx.EVT_BUTTON, self.NuevaPartida2, self.button_1)
        self.Bind(wx.EVT_CHECKBOX, self.Limitedetiempo2, self.checkbox_1)
        self.Bind(wx.EVT_BUTTON, self.Switch, self.button_2)

        # end wxGlade

    def NuevaPartida2(self, event):  # wxGlade: Suburbious2.<event_handler>
        self.Hide()     #Evento para crear una nueva partida desde el juego
        self.frame = NuevaPartida(None, wx.ID_ANY, "")
        self.frame.Show()
        event.Skip()


    def Limitedetiempo2(self, event):  # wxGlade: Suburbious2.<event_handler>
        if not self.checkbox_1.IsChecked(): #Evento para iniciar un contador de diez segundos que se reinicia cada turno y que cuando llega a 0 hace terminar la partida
            self.timer.Stop()
            self.sound.Stop()
            self.contador = 10
            self.label_8.SetLabel('-')
        else:
            self.timer.Start(1000)
        event.Skip()

    def Switch(self, event):  # wxGlade: Suburbious2.<event_handler>
        sound=wx.adv.Sound('./sounds/transicion.wav') #sonido de intercambio de objetos entre almacen y actual
        sound.Play(wx.adv.SOUND_ASYNC)
        temporal=self.almacen       #Evento que intercambia el actual por el almacen e introduce un nuevo objeto en el actual si este es '.'
        if self.almacen=='.':
            self.almacen=self.actual
            self.actual=self.secuencia.crearSecuencia(self.fichero, self.turno)
        else:
            self.almacen=self.actual
            self.actual=temporal
        caracter=self.actual    #Introducimos imágenes correspondientes
        imagen=self.images.get(caracter)
        imagen=wx.Bitmap(imagen)
        imagen = wx.Bitmap.ConvertToImage(imagen).Rescale(100,100).ConvertToBitmap()
        self.bitmap_2.SetBitmap(imagen)
        self.bitmap_2.SetSize((100,100))
        caracter=self.almacen
        imagen=self.images.get(caracter)
        imagen=wx.Bitmap(imagen)
        imagen = wx.Bitmap.ConvertToImage(imagen).Rescale(100,100).ConvertToBitmap()
        self.bitmap_1.SetBitmap(imagen)
        self.bitmap_1.SetSize((100,100))
        event.Skip()
    def temporizadorfuncionando(self, event): #Evento que hara retroceder el contador, si este llega a 0 la partida termina
        self.sound=wx.adv.Sound('./sounds/tiktak.wav') #sonido de intercambio de cuenta atras del reloj
        if self.checkbox_1.IsChecked():
            if self.contador > 0:
                self.sound.Play(wx.adv.SOUND_ASYNC)
                self.contador -= 1                              #en cada ciclo de temporizador  el contador disminuye 1 segundo
                self.label_8.SetLabel(str(self.contador))
            else:
                self.timer.Stop()      #cuando el temporizador sea 0, el tiempo se ha acabado, vamos a pantalla final
                self.Hide()
                self.frame = PantallaFinal(self.turno,self.puntos,None, wx.ID_ANY, "")
                self.frame.Show()

        event.Skip()
    def PulsarTablero(self,event): #Evento que introduce objeto en la matriz y hace pasar de turno
        id=event.GetId()            #obtenemos la id del boton pulsado y en base a esa id calculamos la celda en la que se encuentra
        i=id//self.columnas
        j=id%self.columnas
        boton=wx.Window.FindWindowById(id)
        if self.actual=='W' and self.tablero.matriz[i][j]==".":     #desechamos casos que no se pueden hacer
            sound=wx.adv.Sound('./sounds/error.wav') #Sonido para la introduccion de un objeto en el tablero
            sound.Play(wx.adv.SOUND_ASYNC)
            return None
            
        if self.actual!='W' and self.tablero.matriz[i][j]!=".":
            sound=wx.adv.Sound('./sounds/error.wav') #Sonido para la introduccion de un objeto en el tablero
            sound.Play(wx.adv.SOUND_ASYNC)
            return None

        else:
            self.contador=10
            if self.actual=='W':
                sound=wx.adv.Sound('./sounds/click.wav') #Sonido para la introduccion de un objeto en el tablero
                sound.Play(wx.adv.SOUND_ASYNC)
                self.tablero.matriz[i][j]='.'
                self.tablero.colapsoBigFoot()       #Introducimos los métodos del juego "original" que nos harán pasar de turno
                self.tablero.movimientoBigfoot()
                self.tablero.colapsoBF1()
                self.tablero.colapsoBF4()
                self.turno = self.turno + 1
                self.lleno=self.tablero.mapalleno()
                self.puntos=self.tablero.puntosronda()
                self.label_6.SetLabel(str(self.puntos))
                self.actual=self.secuencia.crearSecuencia(self.fichero, self.turno)
                caracter=self.actual
                imagen=self.images.get(caracter)
                imagen=wx.Bitmap(imagen)
                imagen = wx.Bitmap.ConvertToImage(imagen).Rescale(100,100).ConvertToBitmap()
                self.bitmap_2.SetBitmap(imagen)
                self.bitmap_2.SetSize((100,100))
                for i in range(self.filas):     #intercambiamos por imágenes
                    for j in range(self.columnas):
                        self.boton=wx.Window.FindWindowById(self.columnas*i+j)
                        if self.boton is not None:
                            caracter=self.tablero.matriz[i][j]
                            if caracter=='1':
                                edad=self.tablero.edadbigfoot[(i,j)]
                                if edad>=5 and edad<10:
                                    caracter='5'
                                if edad>=10:
                                    caracter='6'
                            imagen=self.images.get(caracter)
                            imagen=imagen.ConvertToImage()
                            if imagen is not None:
                                imagen = imagen.Scale(self.boton.GetSize()[0],self.boton.GetSize()[1])
                                imagen = wx.Bitmap(imagen)
                                self.boton.SetBitmap(imagen)
                return None
            sound=wx.adv.Sound('./sounds/click.wav') #Sonido para la introduccion de un objeto en el tablero
            sound.Play(wx.adv.SOUND_ASYNC)
            self.tablero.matriz[i][j]=self.actual
            prox=1
            visitados=[]
            nvecinos=self.tablero.confirmarcolapso(i,j,prox,i,j,visitados)
            colapsados=[]
            while nvecinos>=3:
                listacoords=self.tablero.colapso1(i,j,prox,i,j,colapsados)
                self.tablero.colapso2(listacoords)
                self.tablero.cambioelemento(i,j)
                nvecinos=self.tablero.confirmarcolapso(i,j,prox,i,j,visitados)
            self.tablero.colapsoBigFoot()
            self.tablero.movimientoBigfoot()
            self.tablero.colapsoBF1()
            self.tablero.colapsoBF4()
            self.turno = self.turno + 1
            self.lleno=self.tablero.mapalleno()
            self.puntos=self.tablero.puntosronda()
            self.label_6.SetLabel(str(self.puntos))
            self.actual=self.secuencia.crearSecuencia(self.fichero, self.turno)
            caracter=self.actual
            imagen=self.images.get(caracter)
            imagen=wx.Bitmap(imagen)
            imagen = wx.Bitmap.ConvertToImage(imagen).Rescale(100,100).ConvertToBitmap()
            self.bitmap_2.SetBitmap(imagen)
            self.bitmap_2.SetSize((100,100))
            for i in range(self.filas):
                for j in range(self.columnas):
                    self.boton=wx.Window.FindWindowById(self.columnas*i+j)
                    if self.boton is not None:
                        caracter=self.tablero.matriz[i][j]  #Introducimos nuevas imágenes, y para para los bigfoots la imagen segun su edad
                        if caracter=='1':
                            edad=self.tablero.edadbigfoot[(i,j)]
                            if edad>=5 and edad<10:
                                caracter='5'
                            if edad>=10:
                                caracter='6'
                        imagen=self.images.get(caracter)
                        imagen=imagen.ConvertToImage()
                        if imagen is not None:
                            imagen = imagen.Scale(self.boton.GetSize()[0],self.boton.GetSize()[1])
                            imagen = wx.Bitmap(imagen)
                            self.boton.SetBitmap(imagen)
            if self.lleno: #Si el mapa esta lleno la partida se acaba
                self.Hide()
                self.frame = PantallaFinal(self.turno,self.puntos,None, wx.ID_ANY, "")
                self.frame.Show()
            event.Skip()
class PantallaFinal(wx.Frame): #Pantalla de fin de juego con la puntuacion y los turnos
    def __init__(self,turno,puntos, *args, **kwds):
        sound=wx.adv.Sound('./sounds/gameover.wav') #Sonido de fin de juego
        sound.Play(wx.adv.SOUND_ASYNC)
        self.puntos=puntos
        self.turnos=turno
        # begin wxGlade: PantallaFinal.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((512, 330))
        self.SetTitle("TheEnd")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "HAS PERDIDO")         #notificamos que el juego se ha terminado
        label_1.SetFont(wx.Font(39, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_2.Add(label_1, 0, wx.ALL, 10)

        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(sizer_5, 1, wx.EXPAND, 0)

        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Puntuación: ")                   #mostramos la puntuacion final, el numero de turnos y damos la posibilidad de salir o vovler a jugar
        label_2.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_5.Add(label_2, 2, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, "0")
        label_3.SetLabel(str(self.puntos))
        label_3.SetFont(wx.Font(30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_5.Add(label_3, 1, wx.ALIGN_CENTER_VERTICAL, 33)

        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(sizer_6, 1, wx.EXPAND, 0)

        label_4 = wx.StaticText(self.panel_1, wx.ID_ANY, "Turnos:")
        label_4.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_6.Add(label_4, 2, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        label_5 = wx.StaticText(self.panel_1, wx.ID_ANY, "0")
        label_5.SetLabel(str(self.turnos-1))
        label_5.SetFont(wx.Font(30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_6.Add(label_5, 1, wx.ALIGN_CENTER_VERTICAL, 0)

        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_7, 1, wx.EXPAND, 0)

        self.button_1 = wx.Button(self.panel_1, wx.ID_ANY, "Volver a jugar")
        sizer_7.Add(self.button_1, 1, wx.EXPAND, 0)

        self.button_2 = wx.Button(self.panel_1, wx.ID_ANY, "Salir")
        sizer_7.Add(self.button_2, 1, wx.EXPAND, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.VolveraJugar, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.Salir, self.button_2)
        # end wxGlade

    def VolveraJugar(self, event):  # wxGlade: PantallaFinal.<event_handler>                
        self.Hide() #Evento para volver a jugar que abrirá el menú de nueva partida
        self.frame = NuevaPartida(None, wx.ID_ANY, "")
        self.frame.Show()
        event.Skip()

    def Salir(self, event):  # wxGlade: PantallaFinal.<event_handler>
        self.Destroy() #evento para finalizar juego
        event.Skip()

# end of class Suburbious2

class MyApp(wx.App):
    def OnInit(self):
        self.frame = Suburbious(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
