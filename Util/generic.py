from PIL import ImageTk, Image

def redefine_imagen(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size)) 
    

def Centre_window(window, App_ancho, App_largo):
    win_ancho=window.winfo_screenwidth()
    win_largo=window.winfo_screenheight()
    x=int((win_ancho/2)-(App_ancho/2))
    y=int((win_largo/2)-(App_largo/2))
    return window.geometry(f"{App_ancho}x{App_largo}+{x}+{y}")