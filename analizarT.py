class analizar():
    def EsLetra(self,caracter):
        if (ord(caracter)>=65 and ord(caracter)<=90) or (ord(caracter)>=97 and ord(caracter)<=122) or ord(caracter)==164 or ord(caracter)==165:
            return True
        else:
            return False
    
    def EsNumero(self,caracter):
        if (ord(caracter) >= 48 and ord(caracter) <=57):
            return True
        else:
            return False
    
    
    def analizarEntrada(self, texto):
        fila=1
        columna=0
        estado=0
        flagLista=False
        texto+="#"
        lexActual=""
        resultado=[]    #0, errores  1,operaciones  2,propiedades
        listaErrores=[]
        lista=[]
        listaOp=[]      # Lista que contendra todas las operaciones detectadas
        listaAux=[]     # Lista que contendra unicamente una operacion y sus valores
        listaProp=[]    # Lista que almacena las propiedades y sus valores detectados
        flagProp=False  # Bandera Propiedades
        flagOp=False    # Bandera Operacion
        Flag_IO=0   # Bandera para indicar si corchetes: abierto(s)/cerrado(os)
        propValidas=["texto","color-fondo-nodo","color-fuente-nodo","forma-nodo"]
        opValidas=["suma","resta","multiplicacion","division","potencia","raiz","inverso","seno","coseno","tangente","mod"]
        simbolosP=["{","}","=","\"",":",".",",","[","]","-"]
        OtrosSimbolos=[" ","\n","\t","#"]
        errorParser=[]
#--------------------------------inicia Automata----------------------------------------
        for caracter in texto:
            columna+=1
            if self.EsLetra(caracter) == False:     #Verificacion si el caracter leido es Permitido o no.
                if self.EsNumero(caracter)==False:  #Si no es Permitido, se marcara como error, lexema.
                    if caracter not in simbolosP:
                        if caracter not in OtrosSimbolos:
                            lista=[caracter, "Error", fila, columna]
                            errorParser.append(lista)
                            print('-----------')
                            print(caracter)
                            print(ord(caracter))
                            print('-----------')
                            continue
            #print("estado:"+str(estado))
            #print(caracter)
#-------------------Estado S0-------------------------------
            if estado==0:
                if caracter=="{":
                    estado=1
                    
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "{", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)
#-------------------Estado S1-------------------------------
            elif estado==1:
                if caracter=="{":
                    estado=2
                    
                elif caracter=="}":
                    estado=20
                
                elif caracter==",":
                    continue
                    
                elif caracter=="\"":
                    estado=14
                    
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "{, }, \"", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)
#-------------------Estado S2-------------------------------
            elif estado==2:
                if caracter=="\"":
                    estado=3
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "\"", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)
#-------------------Estado S3-------------------------------
            elif estado==3:
                if self.EsLetra(caracter):
                    lexActual=caracter.lower()
                    estado=4
                    
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "letra", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)
#-------------------Estado S4-------------------------------
            elif estado==4:
                if self.EsLetra(caracter):
                    lexActual+=caracter.lower()
                    
                elif self.EsNumero(caracter):
                    lexActual+=caracter
                
                elif caracter=="\"":
                    estado=5
                    
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "letra, \"", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)
#-------------------Estado S5-------------------------------
            elif estado==5:
                if lexActual=="operacion":
                    flagOp=True
                else:
                    FlagValor=True
                
                if caracter==":":
                    estado=6
                    
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, ":", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)
#-------------------Estado S6-------------------------------
            elif estado==6:
                if caracter=="\"":
                    estado=7
                    
                elif self.EsNumero(caracter):
                    lexActual=caracter
                    estado=10
                
                elif caracter=="[":
                    Flag_IO+=1
                    estado=2
                
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "\", numero, [", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)
#-------------------Estado S7-------------------------------
            elif estado==7:
                if self.EsLetra(caracter):
                    lexActual=caracter.lower()
                    estado=8
                
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "letra", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)
#-------------------Estado S8-------------------------------
            elif estado==8:
                if self.EsLetra(caracter) or self.EsNumero(caracter):
                    lexActual+=caracter.lower()
                
                elif caracter=="\"":
                    if flagOp==True:
                        if lexActual in opValidas:
                            listaAux.append(lexActual)
                            flagOp=False
                        else:
                            lista=[lexActual, "Operacion Invalida", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                            listaErrores.append(lista)
                    estado=9
                        
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "letra, \"", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)
#-------------------Estado S9-------------------------------
            elif estado==9:
                if caracter==",":
                    estado=2
                    
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "','", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)
#-------------------Estado S10-------------------------------
            elif estado==10:
                if self.EsNumero(caracter):
                    lexActual+=caracter
                
                elif caracter==".":
                    lexActual+=caracter
                    estado==11
                    
                elif caracter==",":
                    listaAux.append(lexActual)
                    estado=2
                    
                elif caracter=="}":
                    if Flag_IO==0:    
                        listaAux.append(lexActual)
                        listaOp.append(listaAux)
                        listaAux=[]
                        estado=1
                        
                    else:
                        lista=[caracter, "]", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                        listaErrores.append(lista)
                        
                elif caracter=="]":
                    listaAux.append(lexActual)
                    listaAux.append("]")
                    Flag_IO-=1
                    estado=13
                    
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "numero, '.', ',', }, ]", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)
#-------------------Estado S11-------------------------------
            elif estado==11:
                if self.EsNumero(caracter):
                    lexActual+=caracter
                    estado=12
                    
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "numero", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)
#-------------------Estado S12-------------------------------
            elif estado==12:
                if self.EsNumero(caracter):
                    lexActual+=caracter
                
                elif caracter==",":
                    listaAux.append(lexActual)
                    estado=2
                
                elif caracter=="}":
                    if Flag_IO==0:    
                        listaAux.append(lexActual)
                        listaOp.append(listaAux)
                        listaAux=[]
                        estado=1
                        
                    else:
                        lista=[caracter, "]", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                        listaErrores.append(lista)
                
                elif caracter=="]":
                    listaAux.append(lexActual)
                    listaAux.append("]")
                    Flag_IO-=1
                    estado=13
                
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "numero, ',', }, ]", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)    
                
#-------------------Estado S13-------------------------------
            elif estado==13:
                if caracter==",":
                    if flagProp==False:
                        estado=2
                    else:
                        estado=1
                    flagProp=False
                
                elif caracter=="}":
                    if flagProp==False:
                        listaOp.append(listaAux)
                        listaAux=[]
                        
                    estado=1
                    flagProp=False
                    
                
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "',', }", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)    
#-------------------Estado S14-------------------------------
            elif estado==14:
                if self.EsLetra(caracter):
                    lexActual=caracter.lower()
                    estado=15
                    
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "letra", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)   
#-------------------Estado S15-------------------------------
            elif estado==15:
                if self.EsLetra(caracter):
                    lexActual+=caracter.lower()
                    
                elif caracter=="-":
                    lexActual+=caracter
                    
                elif caracter=="\"":
                    if lexActual in propValidas:
                        listaProp.append(lexActual)
                        estado=16
                    else:
                        lista=[lexActual, "Propiedad Invalida", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                        listaErrores.append(lista)   
                    
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "letra, '-'", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)   
#-------------------Estado S16-------------------------------
            elif estado==16:
                if caracter==":":
                    estado=17
                
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, ":", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)   
#-------------------Estado S17-------------------------------
            elif estado==17:
                if caracter=="\"":
                    estado=18
                    
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "\"", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)   
#-------------------Estado S18-------------------------------
            elif estado==18:
                if listaProp[-1]=="texto" and caracter!="\"":
                    lexActual=caracter
                    estado=19
                
                elif self.EsLetra(caracter):
                    lexActual=caracter.lower()
                    estado=19
                
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "letra", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista) 
#-------------------Estado S19-------------------------------
            elif estado==19:
                if listaProp[-1]=="texto" and caracter!="\"":
                    lexActual+=caracter
                        
                elif self.EsLetra(caracter):
                    lexActual+=caracter.lower()
                        
                elif caracter=="\"":
                    listaProp.append(lexActual)
                    flagProp=True
                    estado=13
                
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "Texto:cualquier caracter || otraPropiedad:letra, \"", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista) 
#-------------------Estado S20-------------------------------
            elif estado==20:
                if caracter=="#":
                    continue
                
                elif caracter ==" ":
                    continue
                    
                elif caracter =="\n":
                    fila+=1
                    columna=0

                elif caracter == "\t":
                    columna+=3
                else:
                    lista=[caracter, "#", fila, columna, "Est:"+str(estado)]#[seDetecto,seEsperaba,X,Y]
                    listaErrores.append(lista)
#------------------------------------------------------------
        """print("----Operaciones----")
        for i in listaOp:
            print(i)
            
        print("\n----Propiedades----")
        for j in listaProp:
            print(j)"""
            
        print("====== Caractereres detectados fuera de su estado:====== ")
        if listaErrores != []:
            print(">>[ CaracterDetectado, CaracterEsperado(s), Fila, Columna, Estado: ]<<")
            for i in listaErrores:
                print(i)
        else:
            print("\n>>> No se detectaron errores por DESFASE\n")
            
        resultado.append(errorParser)
        resultado.append(listaOp)
        resultado.append(listaProp)
        
        return resultado