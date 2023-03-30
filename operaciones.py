import math

class Operacion():
    def calcular(self,datos):
        paraGrafo=[]
        #opValidas=["suma","resta","multiplicacion","division","potencia","raiz","inverso","seno","coseno","tangente","mod"]
        for op in datos:
            #print("operacion: ")
            #print(op)
            AuxOp=[]
            siguiente=0
            i=0
            while True:    
                VarOp=0
                i-=1    #permite retroceder posicion dentro de la lista a operar
                #print("elementos")
                #print(op[i])
#---------------------------------------------------------------------  
                if op[i]=="suma":    #Se realiza una suma negativa entre la longitud de "op" e "i", para poder iniciar con la pocision del primer numero de la operacion mas interna, unicamente se le suma un 1 mas. 
                    j=len(op)+i+1    #Se busca donde inicial los numeros despues de la operacion encontrada
                    AuxOp=op[:len(op)+i]    #Se duplica la lista "op", hasta donde se encontro el tipo de operacion
                    #print("lista Duplicada")
                    #print(AuxOp)
                    #print(op[j:])
                    
                    for numero in op[j:]: #Se recorre todos los valores, hasta finalizar o encontrar "]"
                        siguiente+=1
                        if numero !="]":
                            paraGrafo.append(numero)    #Almacena el numero en la lista paraGrafo
                            VarOp+=float(numero)
                        else:
                            break
                        
                    paraGrafo.append("Suma")    #Almacena el tipo de operacion que se realizo en lista paraGrafo
                    paraGrafo.append(VarOp)     #Almacena el resultado de la operacion en lista paraGrafo
                    
                    AuxOp.append(VarOp)
                    AuxOp+=op[j+siguiente:]
                    #print("lista aux:")
                    #print(AuxOp)
                    
                    op=AuxOp[:]
                    AuxOp=[]
                    siguiente=0
                    VarOp=0
                    i=0
                    
                    #print("nueva lista OPERACION:")
                    #print(op)
#---------------------------------------------------------------------
                elif op[i]=="resta":
                    j=len(op)+i+1 
                    AuxOp=op[:len(op)+i]
                    
                    for numero in op[j:]:
                        siguiente+=1        
                        
                        if numero !="]":
                            if siguiente==1:
                                paraGrafo.append(numero)
                                VarOp=float(numero)
                            else:
                                paraGrafo.append(numero)
                                VarOp-=float(numero)
                        else:
                            break
                    
                    paraGrafo.append("Resta")
                    paraGrafo.append(VarOp)
                    
                    AuxOp.append(VarOp)
                    AuxOp+=op[j+siguiente:]
                    op=AuxOp[:]
                    AuxOp=[]
                    siguiente=0
                    VarOp=0     
                    i=0
#---------------------------------------------------------------------    
                elif op[i]=="multiplicacion":
                    VarOp=1
                    j=len(op)+i+1
                    AuxOp=op[:len(op)+i]
                    
                    for numero in op[j:]:
                        siguiente+=1
                        if numero !="]":
                            paraGrafo.append(numero)
                            VarOp*=float(numero)
                        else:
                            break
                    
                    paraGrafo.append("Multiplicacion")
                    paraGrafo.append(VarOp)
                    
                    AuxOp.append(VarOp)
                    AuxOp+=op[j+siguiente:]
                    op=AuxOp[:]
                    AuxOp=[]
                    siguiente=0
                    VarOp=0
                    i=0
#---------------------------------------------------------------------                
                elif op[i]=="division": #solo funciona si la operacion contiene 2 numeros.
                    j=len(op)+i+1
                    AuxOp=op[:len(op)+i]
                    
                    for numero in op[j:]:
                        siguiente+=1
                        if numero !="]":
                            if siguiente==1:
                                paraGrafo.append(numero)
                                VarOp=float(numero)
                            else:
                                paraGrafo.append(numero)
                                VarOp/=float(numero)
                        else:
                            break
                        
                    paraGrafo.append("Division")
                    paraGrafo.append(VarOp)
                    
                    AuxOp.append(VarOp)
                    AuxOp+=op[j+siguiente:]
                    op=AuxOp[:]
                    AuxOp=[]
                    siguiente=0
                    VarOp=0
                    i=0
#---------------------------------------------------------------------   
                elif op[i]=="potencia": #solo funciona si la operacion contiene 2 numeros.
                    VarOp1=1
                    VarOp2=1
                    j=len(op)+i+1
                    AuxOp=op[:len(op)+i]
                    
                    for numero in op[j:]:
                        siguiente+=1
                        if numero !="]":
                            if siguiente==1:
                                paraGrafo.append(numero)
                                VarOp1=float(numero)    #Base
                                
                            elif siguiente==2:
                                paraGrafo.append(numero)
                                VarOp2=float(numero)    #Exponente
                        else:
                            break
                        
                    VarOp=VarOp1**VarOp2
                    paraGrafo.append("Potencia")
                    paraGrafo.append(VarOp)
                    
                    AuxOp.append(VarOp)
                    AuxOp+=op[j+siguiente:]
                    op=AuxOp[:]
                    AuxOp=[]
                    siguiente=0
                    VarOp=0    
                    i=0
#---------------------------------------------------------------------   
                elif op[i]=="raiz": #solo funciona si la operacion contiene 2 numeros.
                    VarOp1=1
                    VarOp2=1
                    j=len(op)+i+1
                    AuxOp=op[:len(op)+i]
                    
                    for numero in op[j:]:
                        siguiente+=1
                        if numero !="]":
                            if siguiente==1:
                                paraGrafo.append(numero)
                                VarOp1=float(numero)    #Numero
                                
                            elif siguiente==2:
                                paraGrafo.append(numero)
                                VarOp2=float(numero)    #Grado raiz-N
                        else:
                            break
                    
                    VarOp=VarOp1**(1/VarOp2)
                    paraGrafo.append("Raiz")
                    paraGrafo.append(VarOp)
                    
                    AuxOp.append(VarOp)
                    AuxOp+=op[j+siguiente:]
                    op=AuxOp[:]
                    AuxOp=[]
                    siguiente=0
                    VarOp=0    
                    i=0
#---------------------------------------------------------------------   
                elif op[i]=="inverso": #solo realiza la operacion para 1 numero, el primero que detecte.
                    j=len(op)+i+1
                    AuxOp=op[:len(op)+i]
                    
                    for numero in op[j:]:
                        siguiente+=1
                        if numero !="]":
                            if siguiente==1:
                                paraGrafo.append(numero)
                                VarOp=1/float(numero)    #Numero
                        else:
                            break
                        
                    paraGrafo.append("Inverso")
                    paraGrafo.append(VarOp)
                    
                    AuxOp.append(VarOp)
                    AuxOp+=op[j+siguiente:]
                    op=AuxOp[:]
                    AuxOp=[]
                    siguiente=0
                    VarOp=0
                    i=0
#---------------------------------------------------------------------   
                elif op[i]=="seno": #solo realiza la operacion para 1 numero, el primero que detecte.
                    VarOp1=1
                    j=len(op)+i+1
                    AuxOp=op[:len(op)+i]
                    
                    for numero in op[j:]:
                        siguiente+=1
                        if numero !="]":
                            if siguiente==1:
                                paraGrafo.append(numero)
                                VarOp1=float(numero)    #Numero
                                VarOp1=math.radians(VarOp1)
                        else:
                            break
                        
                    VarOp=math.sin(VarOp1)
                    paraGrafo.append("Seno")
                    paraGrafo.append(VarOp)
                    
                    AuxOp.append(VarOp)
                    AuxOp+=op[j+siguiente:]
                    op=AuxOp[:]
                    AuxOp=[]
                    siguiente=0
                    VarOp=0
                    i=0
#---------------------------------------------------------------------   
                elif op[i]=="coseno": #solo realiza la operacion para 1 numero, el primero que detecte.
                    VarOp1=1
                    j=len(op)+i+1
                    AuxOp=op[:len(op)+i]
                    
                    for numero in op[j:]:
                        siguiente+=1
                        if numero !="]":
                            if siguiente==1:
                                paraGrafo.append(numero)
                                VarOp1=float(numero)    #Numero
                                VarOp1=math.radians(VarOp1)
                        else:
                            break
                        
                    VarOp=math.cos(VarOp1)
                    paraGrafo.append("Coseno")
                    paraGrafo.append(VarOp)
                    
                    AuxOp.append(VarOp)
                    AuxOp+=op[j+siguiente:]
                    op=AuxOp[:]
                    AuxOp=[]
                    siguiente=0
                    VarOp=0
                    i=0
#---------------------------------------------------------------------   
                elif op[i]=="tangente": #solo realiza la operacion para 1 numero, el primero que detecte.
                    VarOp1=1
                    j=len(op)+i+1
                    AuxOp=op[:len(op)+i]
                    
                    for numero in op[j:]:
                        siguiente+=1
                        if numero !="]":
                            if siguiente==1:
                                paraGrafo.append(numero)
                                VarOp1=float(numero)    #Numero
                                VarOp1=math.radians(VarOp1)
                        else:
                            break
                        
                    VarOp=math.tan(VarOp1)
                    paraGrafo.append("Tangente")
                    paraGrafo.append(VarOp)
                    
                    AuxOp.append(VarOp)
                    AuxOp+=op[j+siguiente:]
                    op=AuxOp[:]
                    AuxOp=[]
                    siguiente=0
                    VarOp=0
                    i=0
#---------------------------------------------------------------------   
                elif op[i]=="mod": #solo funciona si la operacion contiene 2 numeros.
                    j=len(op)+i+1
                    AuxOp=op[:len(op)+i]
                    
                    for numero in op[j:]:
                        siguiente+=1
                        if numero !="]":
                            if siguiente==1:
                                paraGrafo.append(numero)
                                VarOp=float(numero)    #Numero 1
                            else:
                                paraGrafo.append(numero)
                                VarOp%=float(numero)    #numero 2
                        else:
                            break
                        
                    paraGrafo.append("Mod")
                    paraGrafo.append(VarOp)    
                        
                    AuxOp.append(VarOp)
                    AuxOp+=op[j+siguiente:]
                    op=AuxOp[:]
                    AuxOp=[]
                    siguiente=0
                    VarOp=0 
                    i=0
#---------------------------------------------------------------------   
                if len(op)==1:
                    paraGrafo.append("#")
                    #print("Resultado")
                    #print(op[0])    #muestra el resultado final de cada lista operacion completada
                    break
        return paraGrafo
