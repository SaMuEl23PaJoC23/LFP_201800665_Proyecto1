import tkinter
import tkinter.font as tkFont
import easygui
from tkinter import DISABLED, END, NORMAL, StringVar, messagebox

Mensaje="Esperando Archivo..."
ruta=""

#------------Ventana Principal--------
VentanaRaiz = tkinter.Tk()
VentanaRaiz.config(bg="chartreuse")
VentanaRaiz.geometry("335x50")
VentanaRaiz.resizable(0,0)
VentanaRaiz.title("Proyecto No.1 - Menu Principal")
#----------- Funcion abrir archivo --------
def Abrir():
    global ruta
    ruta=easygui.fileopenbox()
    
    
    if ruta != None:
        messagebox.showinfo("ALERT",">>Archivo cargado exitosamente<<")
        archivoSeleccionado=open(ruta)
        textoArchivo=archivoSeleccionado.read()
        archivoSeleccionado.close()
        
        areaTexto.delete("1.0",END)
        areaTexto.insert("1.0",textoArchivo)
        botonGuardar.config(state=NORMAL)
    else:
        messagebox.showerror("ALERT","!!Archivo no seleccionado!!")

def analizarTextoPantalla():
    pass

def errores():
    pass

def guardar():
    archivoGuardar=open(ruta, 'w')
    archivoGuardar.write(areaTexto.get("1.0",END))
    archivoGuardar.close()
    messagebox.showinfo("ALERT",">>Archivo -Guardado- <<")

def guardarComo():
    VentanaGuardarC = tkinter.Tk()
    VentanaGuardarC.config(bg="chartreuse")
    VentanaGuardarC.geometry("335x120")
    #VentanaGuardarC.resizable(0,0)
    VentanaGuardarC.title("Guardar como....")
    
    fontStyle = tkFont.Font(family="Times", size=14)
    subTitulo = tkinter.Label(VentanaGuardarC, text="Nombre del nuevo archivo:", bg="orange", font=fontStyle)
    subTitulo.place(x=50, y=10)
    
    global nombreArchivoN
    nombreArchivoN = StringVar()
    inputNombreArchivo = tkinter.Entry(VentanaGuardarC, textvariable=nombreArchivoN, font=fontStyle)
    inputNombreArchivo.place(x=45, y=80)
    
    #agregar un boton para guardar/crear el archivo
    #limpiar la entrada del nombre a guardar
    
        
        
    


#------------Ventana Menu Archivo--------
def ventanaMenuArchivo():
    ventanaArchivo = tkinter.Tk()
    ventanaArchivo.config(bg="mediumturquoise")
    ventanaArchivo.geometry("930x530")
    ventanaArchivo.resizable(0,0)
    ventanaArchivo.title(">> Archivo <<")
    
    #--------- Componentes (Ventana Menu Archivo) ---------
    fontStyle = tkFont.Font(family="Times", size=14)
    
    global areaTexto, botonGuardar, botonGuardarC, botonAnalizar, botonErrores
    
    areaTexto=tkinter.Text(ventanaArchivo, width=100, height=24, font=fontStyle, bg="lightgray")
    areaTexto.insert("1.0",Mensaje)
    areaTexto.place(x=10,y=70)
    
    botonAbrir = tkinter.Button(ventanaArchivo, text="Abrir", bg="chartreuse", font=fontStyle, command=Abrir)
    botonAbrir.place(x=10,y=10)
    
    botonGuardar = tkinter.Button(ventanaArchivo, text="Guardar", bg="gold", font=fontStyle, command=guardar, state=DISABLED)
    botonGuardar.place(x=90,y=10)

    botonGuardarC = tkinter.Button(ventanaArchivo, text="Guardar Como...", bg="yellow", font=fontStyle, command=guardarComo)
    botonGuardarC.place(x=170,y=10)
    
    botonAnalizar = tkinter.Button(ventanaArchivo, text="Analizar", bg="teal", font=fontStyle, state=DISABLED)
    botonAnalizar.place(x=670,y=10)
    
    botonErrores = tkinter.Button(ventanaArchivo, text="Errores", bg="purple", font=fontStyle, state=DISABLED)
    botonErrores.place(x=750,y=10)
    
#------------Ventana Ayuda--------
def ventanaAyuda():
    
    ventanaAyuda = tkinter.Tk()
    ventanaAyuda.config(bg="lightseagreen")
    ventanaAyuda.geometry("240x140")
    ventanaAyuda.resizable(0,0)
    ventanaAyuda.title(">> Ayuda <<")
    
    #--------- Componentes (Ventana Menu Archivo) ---------
    fontStyle = tkFont.Font(family="Times", size=14)
    
    botonManUsuario = tkinter.Button(ventanaAyuda, text="Manual Usuario", bg="chartreuse", font=fontStyle)
    botonManUsuario.place(x=50,y=10)
    
    botonManTecnico = tkinter.Button(ventanaAyuda, text="Manual Tecnico", bg="chartreuse", font=fontStyle)
    botonManTecnico.place(x=50,y=50)
    
    botonInfo = tkinter.Button(ventanaAyuda, text="Temas de Ayuda", bg="red", font=fontStyle)
    botonInfo.place(x=45,y=90)
    


#--------- Componentes (Ventana Principal) ---------
fontStyle = tkFont.Font(family="Times", size=12)

botonArchivo = tkinter.Button(VentanaRaiz, text="Menu Archivo", bg="orange", font=fontStyle, command=ventanaMenuArchivo)
botonArchivo.place(x=10,y=10)
botonAyuda = tkinter.Button(VentanaRaiz, text="Ayuda", bg="yellow", font=fontStyle, command=ventanaAyuda)
botonAyuda.place(x=270,y=10)

#--------------------------------
VentanaRaiz.mainloop()