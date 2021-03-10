
class Compilador ():

    #Divide en analisis de sintaxis de linea en linea
    def sintaxis(self, code):
        registro = []
        errorEncontrado = []
        varibles = [('acumulador', None)]
        etiquetas = []

        for linea in range(len(code)):
            registro.append(self.sintaxisPorLinea(code[linea], varibles, etiquetas, code))

        for e in range(len(registro)):
            if registro[e][0] == False:
                errorEncontrado.append(f'linea {e}: {registro[e]}')

        for i in errorEncontrado:
            print(i)
        for v in varibles:
            print(v, 'Variable')
        for e in etiquetas:
            print(e, 'etiqueta')

        return errorEncontrado

    #Hace el analisis de cada linea
    def sintaxisPorLinea (self, linea, variables, etiquetas, code):
        partes = linea.split(' ')

        #Determina la primera instruccion (Operacion) de la linea y envia a su funcion especifica
        if partes[0] == 'nueva':
            return (self.nueva(partes, variables))

        elif partes[0] == 'cargue':
            return (self.cargue(partes, variables))

        elif partes[0]  == 'almacene':
            return (self.almacene(partes, variables))

        elif partes[0]  == 'lea':
            return (self.lea(partes, variables))

        elif partes[0]  == 'sume':
            return (self.sume(partes, variables))

        elif partes[0]  == 'reste':
            return (self.reste(partes, variables))

        elif partes[0]  == 'multiplique':
            return (self.multiplique(partes, variables))

        elif partes[0]  == 'divida':
            return (self.divida(partes, variables))

        elif partes[0]  == 'potencia':
            return (self.potencia(partes, variables))

        elif partes[0]  == 'modulo':
            return (self.modulo(partes, variables))

        elif partes[0]  == 'concatene':
            return (self.concatene(partes, variables))

        elif partes[0]  == 'elimine':
            return (self.elimine(partes, variables))

        elif partes[0]  == 'extraiga':
            return (self.extraiga(partes, variables))

        elif partes[0]  == 'Y':
            return (self.Y(partes, variables))

        elif partes[0]  == 'O':
            return (self.O(partes, variables))

        elif partes[0]  == 'NO':
            return (self.NO(partes, variables))

        elif partes[0]  == 'muestre':
            return (self.muestre(partes, variables))

        elif partes[0]  == 'imprima':
            return (self.imprima(partes, variables))

        elif partes[0]  == 'vaya':
            return (self.vaya(partes, code, etiquetas))

        elif partes[0]  == 'vayasi':
            return (self.vayasi(partes, code, etiquetas, variables))

        elif partes[0]  == 'etiqueta':
            return (self.etiqueta(partes, etiquetas))

        elif partes[0]  == 'retorne':
            return (self.retorne(partes))

        elif partes[0]  == '':
            return (True, 'Ok')

        elif partes[0]  == '//':
            return (True, 'Ok')

        else:
            return (False, 'Comando de operación desconocido')

    #funcion que evalua la cracion de una variable
    def nueva (self, linea, variables):
        # Establece la minima y maxima cantidad de partes para cumplir con la sintaxis de declaracion de variables

    #Evalua el indicativo de que es una cadena
        if len(linea) > 2:
            if linea[2] == 'C':
                #Variable definida con un valor
                if self.existeVariable(variables, linea[1]) == None:
                    if len(linea) >= 4:
                        cadena = ''
                        for contador in range(3, len(linea)):
                            cadena += ' ' + linea[contador]
                        variables.append((linea[1], linea[2], cadena))
                        return (True, 'Ok')
                    #Variable definida sin valoor
                    elif len(linea) == 3:
                        variables.append((linea[1], linea[2],''))
                        return (True, 'Ok')
                else:
                    return (False,'La variable ya existe')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

        if len(linea) > 2 and len(linea) <= 4:
            #Evalua el indicativo I de entero ademas verifica que el valor corresponda a un entero
            if linea[2] == 'I':
                if self.existeVariable(variables, linea[1]) == None:
                    if len(linea) == 4:
                        try:
                            nuevaVar = int(linea[3])
                            variables.append((linea[1], linea[2], nuevaVar))
                            return (True, 'Ok')
                        except Exception as ex:
                            return (False, (ex, 'Error en los datos, el valor ingresado no es entero'))
                    elif len(linea) == 3:
                        variables.append((linea[1], linea[2],0))
                        return (True, 'Ok')
                else:
                    return (False,'La variable y existe')

            #Evalua que el indicativo R de un real y verifica que el valor corresponda a un real
            elif linea[2] == 'R':
                if self.existeVariable(variables, linea[1]) == None:
                    if len(linea) == 4:
                        try:
                            nuevaVar = float(linea[3])
                            variables.append((linea[1], linea[2], nuevaVar))
                            return (True, 'Ok')
                        except Exception as ex:
                            return (False, (ex, 'Error en los datos, el valor ingresado no es real'))
                    elif len(linea) == 3:
                        variables.append((linea[1], linea[2], 0.0))
                        return (True, 'Ok')
                else:
                    return (False,'La variable y existe')

            #Evalua que el indicativo L de un Booleano y verifica que los datos correspondan a los valores booleanos
            elif linea[2] == 'L':
                if self.existeVariable(variables, linea[1]) == None:
                    if len(linea) == 4:
                        try:
                            nuevaVar = int(linea[3])
                            if nuevaVar == 1:
                                variables.append((linea[1], linea[2], True))
                                return (True, 'Ok')
                            elif nuevaVar == 0:
                                variables.append((linea[1], linea[2], False))
                                return (True, 'Ok')
                            else:
                                return (False,'La variable que desea crear no es aceptada')
                        except Exception as ex:
                            return (False, (ex, 'Error en los datos, el valor ingresado no es Booleano'))
                    elif len(linea) == 3:
                        variables.append((linea[1], linea[2], False))
                        return (True, 'Ok')
                else:
                    return (False,'La variable y existe')

            #Evalua cualquier tipo de dato que selecione el usuario y no este desntro de los astablecidos
            else:
                return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

    #Carga el valor de una variable en el acumulador
    def cargue(self, linea, variables):
        #El tamaño que debe tener la linea
        if len(linea) == 2:
            #Si la variable a asignar existe
            variableCarga = self.existeVariable(variables, linea[1])
            if variableCarga:
                #Asigna el nuevo valor a el acumulador
                variables[0] = ('acumulador', variableCarga[1], variableCarga[2])
                return (True, 'Ok')
            else:
                return (False, 'La variable no ha sido creada')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

    #Almacena el valor del acumulador en la variable indicada
    def almacene(self, linea, variables):
        if len(linea) == 2:
            #Si la variable a asignar existe
            variableAsigan = self.existeVariable(variables, linea[1])
            if variableAsigan:
                if variables[0][1] == variableAsigan[1]:
                    index = variables.index(variableAsigan)
                    lista = list(variables[index])
                    lista[2] = variables[0][2]
                    asignar = tuple(lista)
                    variables[index] = asignar
                    return (True, 'OK')
                else:
                    return (False, 'Los tipos de datos no coinciden')
            else:
                return (False, 'La variable a almacenar no existe')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

    #Lee un valor dado por el usurio y lo asigna a una variable definida
    def lea(self, linea, variables):
        if len(linea) == 2:
            #Si la variable a asignar existe
            variableAsigan = self.existeVariable(variables, linea[1])
            if variableAsigan:
                #La funcion lea esta asignada para la segunda entrega del proyecto
                return (True, 'OK')
            else:
                return (False, 'La variable a almacenar el valor leido no existe')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

    #Incremente el valor del acumulador en el valor indicado por la variable señalada por el operando
    def sume(self, linea, variables):
        if len(linea) == 2:
            #Si la variable a asignar existe
            variableSuma = self.existeVariable(variables, linea[1])
            if variableSuma:
                #Intenta realizar la suma, si los datos son compatibles
                try:
                    acumulador = list(variables[0])
                    suma = acumulador[2] + variableSuma[2]
                    #Verefica el tipo de dato resultado de la operacion y lop asigna el valor a la variable acumulador
                    if type(suma) == int:
                        acumulador[2] = suma
                        acumulador[1] = 'I'
                        variables[0] = tuple(acumulador)
                        return (True, 'Ok')
                    elif type(suma) == float:
                        acumulador[2] = suma
                        acumulador[1] = 'R'
                        variables[0] = tuple(acumulador)
                        return (True, 'Ok')

                except Exception as ex:
                    return (False, (ex, 'Los datos no se pueden operar'))
            else:
                return (False, 'La variable a sumar no existe')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

    #Decremente el acumulador en el valor indicado por la variable que señala el operando.
    def reste(self, linea, variables):
        if len(linea) == 2:
            #Si la variable a asignar existe
            variableResta = self.existeVariable(variables, linea[1])
            if variableResta:
                #Intenta realizar la resta, si los datos son compatibles
                try:
                    acumulador = list(variables[0])
                    resta = acumulador[2] - variableResta[2]
                    #Verefica el tipo de dato resultado de la operacion y lop asigna el valor a la variable acumulador
                    if type(resta) == int:
                        acumulador[2] = resta
                        acumulador[1] = 'I'
                        variables[0] = tuple(acumulador)
                        return (True, 'Ok')
                    elif type(resta) == float:
                        acumulador[2] = resta
                        acumulador[1] = 'R'
                        variables[0] = tuple(acumulador)
                        return (True, 'Ok')

                except Exception as ex:
                    return (False, (ex, 'Los datos no se pueden operar'))
            else:
                return (False, 'La variable a restar no existe')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

    #Multiplique el valor del acumulador por el valor indicado por la variable señalada por el operando.
    def multiplique(self, linea, variables):
        if len(linea) == 2:
            #Si la variable a asignar existe
            variableMult = self.existeVariable(variables, linea[1])
            if variableMult:
                #Intenta realizar la Multiplicacion, si los datos son compatibles
                try:
                    acumulador = list(variables[0])
                    multiplica = acumulador[2] * variableMult[2]
                    #Verefica el tipo de dato resultado de la operacion y lop asigna el valor a la variable acumulador
                    if type(multiplica) == int:
                        acumulador[2] = multiplica
                        acumulador[1] = 'I'
                        variables[0] = tuple(acumulador)
                        return (True, 'Ok')
                    elif type(multiplica) == float:
                        acumulador[2] = multiplica
                        acumulador[1] = 'R'
                        variables[0] = tuple(acumulador)
                        return (True, 'Ok')

                except Exception as ex:
                    return (False, (ex, 'Los datos no se pueden operar'))
            else:
                return (False, 'La variable a multiplicar no existe')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

    #Divida el valor del acumulador por el valor indicado por la variable señalada por el operando.
    def divida(self, linea, variables):
        if len(linea) == 2:
            #Si la variable a asignar existe
            variableDiv = self.existeVariable(variables, linea[1])
            if variableDiv:
                #Intenta realizar la División, si los datos son compatibles
                try:
                    acumulador = list(variables[0])
                    divide = acumulador[2] / variableDiv[2]
                    #Verefica el tipo de dato resultado de la operacion y lop asigna el valor a la variable acumulador
                    if type(divide) == int:
                        acumulador[2] = divide
                        acumulador[1] = 'I'
                        variables[0] = tuple(acumulador)
                        return (True, 'Ok')
                    elif type(divide) == float:
                        acumulador[2] = divide
                        acumulador[1] = 'R'
                        variables[0] = tuple(acumulador)
                        return (True, 'Ok')
                # Valida la division entre 0
                except ZeroDivisionError as zero:
                    return (False, (zero, 'Los datos no se pueden operar'))
                # Valida el tipo de datos a operar
                except Exception as ex:
                    return (False, (ex, 'Los datos no se pueden operar'))
            else:
                return (False, 'La variable a dividir no existe')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

    #Eleve el acumulador a la potencia señalada por el operando
    def potencia(self, linea, variables):
        if len(linea) == 2:
            #Si la variable a asignar existe
            variablePoten = self.existeVariable(variables, linea[1])
            if variablePoten:
                #Intenta realizar la Multiplicacion, si los datos son compatibles
                try:
                    if variablePoten[2] >= 0:
                        acumulador = list(variables[0])
                        potencia = acumulador[2] ** variablePoten[2]
                        #Verefica el tipo de dato resultado de la operacion y lop asigna el valor a la variable acumulador
                        if type(potencia) == int:
                            acumulador[2] = potencia
                            acumulador[1] = 'I'
                            variables[0] = tuple(acumulador)
                            return (True, 'Ok')
                        elif type(potencia) == float:
                            acumulador[2] = potencia
                            acumulador[1] = 'R'
                            variables[0] = tuple(acumulador)
                            return (True, 'Ok')
                    else:
                        acumulador = list(variables[0])
                        raiz = 1/(-1 * variablePoten[2])
                        potencia = acumulador[2] ** raiz
                        #Verefica el tipo de dato resultado de la operacion y lop asigna el valor a la variable acumulador
                        acumulador[2] = potencia
                        acumulador[1] = 'R'
                        variables[0] = tuple(acumulador)
                        return (True, 'Ok')

                except Exception as ex:
                    return (False, (ex, 'Los datos no se pueden operar'))
            else:
                return (False, 'La variable de potencia no existe')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

    #Obtenga el modulo al dividir el valor del acumulador por el valor indicado por la variable.
    def modulo(self, linea, variables):
        if len(linea) == 2:
            #Si la variable a asignar existe
            variableMod = self.existeVariable(variables, linea[1])
            if variableMod:
                #Intenta realizar la División, si los datos son compatibles
                try:
                    acumulador = list(variables[0])
                    modulo = acumulador[2] % variableMod[2]
                    #Verefica el tipo de dato resultado de la operacion y lop asigna el valor a la variable acumulador
                    if type(modulo) == int:
                        acumulador[2] = modulo
                        acumulador[1] = 'I'
                        variables[0] = tuple(acumulador)
                        return (True, 'Ok')
                    elif type(modulo) == float:
                        acumulador[2] = modulo
                        acumulador[1] = 'R'
                        variables[0] = tuple(acumulador)
                        return (True, 'Ok')
                # Valida la division entre 0
                except ZeroDivisionError as zero:
                    return (False, (zero, 'Los datos no se pueden operar'))
                # Valida el tipo de datos a operar
                except Exception as ex:
                    return (False, (ex, 'Los datos no se pueden operar'))
            else:
                return (False, 'La variable Para calcular el Modulo no existe')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

    #Genere una cadena que una la cadena dada por el operando a la cadena que hay en el acumulador
    def concatene(self, linea, variables):
        if len(linea) == 2:
            #Si la variable a asignar existe
            variableConc = self.existeVariable(variables, linea[1])
            if variableConc:
                if variableConc[1] == 'C' and variables[0][1] == 'C':
                    acumulador = list(variables[0])
                    nuevaCadena = variables[0][2] + variableConc[2]
                    acumulador[2] = nuevaCadena
                    variables[0] = tuple(acumulador)
                    return (True, 'Ok')
                else:
                    return (False, 'Los datos a concatenar no son de tipo Cadena C')
            else:
                return (False, 'La variable a concatenar no existe')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

    #Genere una subcadena que elimine aparición del conjunto de caracteres dados por el operando del acumulador
    def elimine (self, linea, variables):
        if len(linea) == 2:
            #Si la variable a asignar existe
            variableElimine = self.existeVariable(variables, linea[1])
            if variableElimine:
                #Verifica los tipos de datos de la variable
                if variableElimine[1] == 'C' and variables[0][1] == 'C':
                    acumulador = list(variables[0])
                    cadena = acumulador[2]
                    #Verifica si la cadena a elimar se encuentra en el acumulador
                    if cadena.find(variableElimine[2]) >= 0:
                        nuevaCadena = cadena.replace(variableElimine[2], '')
                        acumulador[2] = nuevaCadena
                        variables[0] = tuple(acumulador)
                        return (True, 'Ok')
                    else:
                        return (False, 'No se encuentran coincidencias en la cadena')
                else:
                    return (False, 'Los datos a concatenar no son de tipo Cadena C')
            else:
                return (False, 'La variable de la cadena a eliminar no existe')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

    # Genere una subcadena que extraiga los primeros caracteres de la cadena que se encuentra en el acumulador
    def extraiga (self, linea, variables):
        if len(linea) == 2:
            # Convierte el dato inglresado en entero y realiza la transformacion de la cadena
            try:
                cantidad = int(linea[1])
                acumulador = list(variables[0])
                cadena = acumulador[2]
                nuevaCadena = cadena[cantidad:]
                acumulador[2] = nuevaCadena
                variables[0] = tuple(acumulador)
                return (True, 'Ok')

            except Exception as Ex:
                return (False, 'Error el dato ingresado no es un numero entero')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

    #Produce una operación lógica Y entre dos operadores y lo almacena en el tercero
    def Y (self, linea, variables):
        #La distacia del comando debe ser de 4
        if len(linea) == 4:
            varComparar1 = self.existeVariable(variables, linea[1])
            varComparar2 = self.existeVariable(variables, linea[2])
            varAlmacena = self.existeVariable(variables, linea[3])

            #Verifica que las variables esten creadas
            if varComparar1 and varComparar2 and varAlmacena:
                #Verifica que todas las variables sean de tipo logicas
                if varComparar1[1] == 'L' and varComparar2[1] == 'L' and varAlmacena[1] == 'L':
                    index = variables.index(varAlmacena)
                    almacena = list(variables[index])
                    #Realiza la opercion logica and
                    logica = varComparar1[2] and varComparar2[2]
                    almacena[2] = logica
                    variables[index] = tuple(almacena)
                    return (True, 'Ok')
                else:
                    return (False, 'Las variables no son del tipo Logico L')
            else:
                return (False, 'Algunas de las variables no han sido declaradas')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

    #Produce uan operacion logica O entre dos operadors y lo almacena en el tercero
    def O (self, linea, variables):
        #La distacia del comando debe ser de 4
        if len(linea) == 4:
            varComparar1 = self.existeVariable(variables, linea[1])
            varComparar2 = self.existeVariable(variables, linea[2])
            varAlmacena = self.existeVariable(variables, linea[3])

            #Verifica que las variables esten creadas
            if varComparar1 and varComparar2 and varAlmacena:
                #Verifica que todas las variables sean de tipo logicas
                if varComparar1[1] == 'L' and varComparar2[1] == 'L' and varAlmacena[1] == 'L':
                    index = variables.index(varAlmacena)
                    almacena = list(variables[index])
                    #Realiza la opercion logica or
                    logica = varComparar1[2] or varComparar2[2]
                    almacena[2] = logica
                    variables[index] = tuple(almacena)
                    return (True, 'Ok')
                else:
                    return (False, 'Las variables no son del tipo Logico L')
            else:
                return (False, 'Algunas de las variables no han sido declaradas')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

    #Produce una operación de negación lógica para el primer operando que es una variable y lo almacena en la seguda.
    def NO (self, linea, variables):
        #La distacia del comando debe ser de 4
        if len(linea) == 3:
            varComparar1 = self.existeVariable(variables, linea[1])
            varAlmacena = self.existeVariable(variables, linea[2])

            #Verifica que las variables esten creadas
            if varComparar1 and varAlmacena:
                #Verifica que todas las variables sean de tipo logicas
                if varComparar1[1] == 'L' and varAlmacena[1] == 'L':
                    index = variables.index(varAlmacena)
                    almacena = list(variables[index])
                    #Realiza la opercion logica or
                    logica = not varComparar1[2]
                    almacena[2] = logica
                    variables[index] = tuple(almacena)
                    return (True, 'Ok')
                else:
                    return (False, 'Las variables no son del tipo Logico L')
            else:
                return (False, 'Algunas de las variables no han sido declaradas')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

    #Presente por pantalla el valor que hay en la variable indicada por el operando.
    def muestre (self, linea, variables):
        if len(linea) == 2:
            #Si la variable a asignar existe
            variableMuestra = self.existeVariable(variables, linea[1])
            if variableMuestra:
                #Metodo funcinal en la seguente fase del proyecto
                return (True, 'OK')
            else:
                return (False, 'La variable a mostrar no existe')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

    #Presente por Impresora el valor que hay en la variable indicada por el operando.
    def imprima (self, linea, variables):
        if len(linea) == 2:
            #Si la variable a asignar existe
            variableImprima = self.existeVariable(variables, linea[1])
            if variableImprima:
                #Metodo funcinal en la seguente fase del proyecto
                return (True, 'OK')
            else:
                return (False, 'La variable a imprimir no existe')
        else:
            return (False, 'Error de sintaxis, la declaracion de variable no cumple con las sintaxis')

    #Salta a la instrucción que corresponde a la etiqueta indicada por el operando
    def vaya (self, linea, code, etiquetas):
        if len(linea) == 2:
            #La etiqueda existe
            etiq = self.existeEtiqueta(etiquetas, linea[1])
            if etiq:
                if etiq[1] <= len(code):
                    return (True, 'Ok')
                else:
                    return (False, 'El valor de la etiqueta sobrepasa las lienas de codigo')
            else:
                return (False, 'La etiqueta no ha sido creada')
        else:
            return (False, 'La declaracion no cumple con la sintaxis')

    #Salta a la instrucción que corresponde a la etiqueta indicada por el operando, bajo las condiciones
    def vayasi (self, linea, code, etiquetas, variables):

        #Crea etiquetas en cualquien posicion del codigo
        for c in code:
            partes = c.split(' ')
            if partes[0] == 'etiqueta':
                respuesta = self.etiqueta(partes, etiquetas)
                if respuesta[0] == True:
                    print('Etiqueta creada exitosamente')
                else:
                    print('Error al crear la tiqueta', respuesta)


        if len(linea) == 3:
            #Si el valor del acumulador es mayor a cero a la instrucción que corresponde la
            # etiqueta indicada por el primer operando
            if variables[0][2] > 0:
                etiq = self.existeEtiqueta(etiquetas, linea[1])
                if etiq:
                    if etiq[1] <= len(code):
                        return (True, 'Ok')
                    else:
                        return (False, 'El valor de la etiqueta sobrepasa las lienas de codigo')
                else:
                    return (False, 'La etiqueta no ha sido creada')
            #Si el valor del acumulador en menor a cero, se asigna la instrucion de la
            # etiqueda indicada en el segundo operando
            elif variables[0][2] < 0:
                etiq = self.existeEtiqueta(etiquetas, linea[2])
                if etiq:
                    if etiq[1] <= len(code):
                        return (True, 'Ok')
                    else:
                        return (False, 'El valor de la etiqueta sobrepasa las lienas de codigo')
                else:
                    return (False, 'La etiqueta no ha sido creada')
            #Si el acumulador es 0, continua su ejecucion
            else:
                return (True, 'Ok')

    #Valida la sitanxis de la linea y crea la etiqueta
    def etiqueta (self, linea, etiquetas):
        if len (linea) == 3:
            try:
                if int(linea[2]) >= 0:
                    if self.existeEtiqueta(etiquetas, linea[1]) == None:
                        etiquetas.append((linea[1], int(linea[2])))
                        return (True, 'Ok')
                    else:
                        return (True, 'Ok')
                else:
                    return (False, 'El valor dado a la etiqueta no es valido')
            except Exception as Ex:
                return (False, 'El valor dado a la etiqueta no es valido')
        else:
            return (False, 'Error de sintaxis, la declaracion de etiquetas no cumple con los parametros')

    # Valida la sintaxis de la linea
    def retorne (self, linea):
        if len(linea) <= 2:
            return (True, 'Ok')
        else:
            return (False, 'Error de sintaxis, el comando no cumple con las normas dadas')

    #Valida si hay una variable con el nombre dado
    def existeVariable(self, variables, nombreVariable):
        for v in variables:
            if nombreVariable == v[0]:
                return v
        return None

    #Valida si hay una etiqueta con el nombre dado
    def existeEtiqueta(self, etiquetas, nombreEtiquetas):
        for e in etiquetas:
            if nombreEtiquetas == e[0]:
                return e
        return None











