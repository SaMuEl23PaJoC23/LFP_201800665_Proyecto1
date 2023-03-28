class OperacionYgrafo():
    def calcular(self,datos):
        opValidas=["suma","resta","multiplicacion","division","potencia","raiz","inverso","seno","coseno","tangente","mod"]
        for op in datos:
            AuxOp=[]
            VarOp=0
            siguiente=0
            while True:
                i=-1
                if op[i]=="suma":    #Se realiza una suma negativa entre la longitud de "op" e "i", para poder iniciar con la pocision del primer numero
                    j=len(op)+i+1    #   de la operacion mas interna, unicamente se le suma un 1 mas. 
                    AuxOp=op[:len(op)+i]    #Se duplica la lista "op", hasta donde se encontro el tipo de operacion
                    
                    for numero in op[j+1:]: #Se recorre todos los valores, hasta finalizar o encontrar "]"
                        siguiente+=1
                        if numero !="]":
                            VarOp+=float(numero)
                        else:
                            break
                    siguiente=0
                    AuxOp.append(VarOp)
                    VarOp=0
                    AuxOp+=op[siguiente:]
                       
                           
                
                elif op[i]=="resta": 
                    pass
                else:
                    i-=1
                    if (i*-1)>len(op):
                        break
                    
                    