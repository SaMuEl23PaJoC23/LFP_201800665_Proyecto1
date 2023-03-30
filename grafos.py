from graphviz import render

class CrearGrafo():
    def grafo(self, datos, instrucciones):
        nombreImagenSalida="grafo/Operaciones.dot"
        
        escribirA = open(nombreImagenSalida,'w')
        escribirA.write('digraph errores { \n')
        escribirA.write('rankdir=RL \n')
#---------Propiedades/Instrucciones----------------
        j=1
        colorFondo="darkcyan"
        colorFuente="black"
        forma="house"
        for i in instrucciones:
            if i =="texto":
                pass
            elif i =="color-fondo-nodo":
                colorFondo=instrucciones[j]
            elif i == "color-fuente-nodo":
                colorFuente=instrucciones[j]
            elif i =="forma-nodo":
                forma=instrucciones[j]
            j+=1
#---------------------Nodos------------------------        
        siguiente=0
        lista=[]
        auxLista=[]
        opValidas=["Suma","Resta","Multiplicacion","Division","Potencia","Raiz","Inverso","Seno","Coseno","Tangente","Mod"]
        varTituloOP=""
        for i in datos:
            i=str(i)
            if i in opValidas:    
                varTituloOP=i+'\n '
            elif i =="#":
                lista.append("#")
            else:
                siguiente+=1
                escribirA.write('N'+str(siguiente)+' [label=\"'+varTituloOP+'\n-> '+i+'\", shape='+forma+', color='+colorFondo+', style=filled, fontcolor='+colorFuente+'] \n')
                if varTituloOP == "":
                    auxLista.append('N'+str(siguiente))
                else:
                    lista.append('N'+str(siguiente))
                    lista.append(auxLista)
                    auxLista=[]
                    
                varTituloOP=""
#------------Apuntamiento de NODOS----------------
        j=1
        while j < len(lista):
            for i in lista[j]:
                escribirA.write(lista[j-1]+'->'+i+'; \n')
                
            if j+1 < len(lista) and lista[j+1] !="#":
                escribirA.write(lista[j+1]+'->'+lista[j-1]+'; \n')
                
            elif lista[j+1] =="#":
                j+=1
            j+=2
#-------------------------------------------------------    
        escribirA.write('}\n')
        escribirA.close()
        render('dot','png',nombreImagenSalida)
            
            