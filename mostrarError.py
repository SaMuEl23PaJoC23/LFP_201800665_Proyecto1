from graphviz import render
class mostrarErroresLex():
    def escrituraArchivoError(self, datos):
        #lista=[[caracter, "Error", fila, columna],[....]]
        escribirA = open('erroresLex/ERRORES_201800665.lfp','w')
        escribirA.write('{\n')
        contar=len(datos)
        indice=1
        for elemento in datos:
            escribirA.write('\t{ \n')    
            escribirA.write('\t\t\"No.\": '+str(indice)+'\n')
            escribirA.write('\t\t\"Descripcion-Token\": {\n')
            escribirA.write('\t\t\t\"Lexema\": '+elemento[0]+'\n')
            escribirA.write('\t\t\t\"Tipo\": Error\n')
            escribirA.write('\t\t\t\"Fila\": '+str(elemento[2])+'\n')
            escribirA.write('\t\t\t\"Columna\": '+str(elemento[3])+'\n')
            escribirA.write('\t\t}\n')
            escribirA.write('\t}')
            contar-=1
            indice+=1
            if contar >0:
                escribirA.write(',\n')
        
        escribirA.write('\n}')
        escribirA.close()