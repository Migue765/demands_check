import tkinter 

# Funcion de prueba
def saludo(text):
    print(text)

def get_text():
    texto1 = input_text.get()
    mostrar_texto["text"] = texto1

# Creamos una ventana
window = tkinter.Tk()
window.geometry("200x200")

# Agregamos texto
tag = tkinter.Label(window, text = "Sistema de gestion de procesos")
tag.pack()

# Manipular texto de una etiqueta
mostrar_texto = tkinter.Label(window)
mostrar_texto.pack()

# entrada de texto
input_text = tkinter.Entry(window)
input_text.pack()

# agregamos botones
botton = tkinter.Button(window, text = "Crear", command = get_text)
botton.pack()

window.mainloop()

