import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from Controllers.Controller_mapa import control_mapa
import Util.generic as utl     
import tkintermapview
import geocoder
class vista_mapa:

    def __init__(self,controller=None, band=None, ubicacion=None, ):
        self.window=tk.Tk()
        self.window.title("MUSICAL TOUR-MAPA")
        utl.Centre_window(self.window,1300,620)
        self.window.config(bg="#e5e5e5")
        self.window.resizable(width=0, height=0)
        self.controller=controller
        self.band=band
        self.ubicacion=ubicacion
        
        #Frame de barra superior 
        frame_supbar=tk.Frame(self.window, bd=0, height=40, relief=tk.SOLID, padx=10, pady=10, bg="#2f242c")
        frame_supbar.pack(side="top", expand=tk.NO, fill=tk.X)

        #botones
        boton_volver=tk.Button(frame_supbar, text="Volver", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=5, padx=10, command=self.volver_atras)
        boton_volver.pack(side="left",expand=tk.NO,padx=5, fill=tk.NONE)
        
        boton_inicio=tk.Button(frame_supbar, text="Inicio", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=5, padx=10) #self.controller.volver_inicio
        boton_inicio.pack(side="left",expand=tk.NO,padx=5, fill=tk.NONE)

        self.boton_del_ubi=tk.Button(frame_supbar, text="Quitar del recorrido",state="disabled", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=15, padx=10, command=self.eliminar_ruta)
        self.boton_del_ubi.pack(side="left",expand=tk.NO,padx=5, fill=tk.NONE)

        boton_cerrar_sesion=tk.Button(frame_supbar, text="Cerrar sesion", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=10, padx=10)
        boton_cerrar_sesion.pack(side="right",expand=tk.NO,padx=10, fill=tk.NONE)  

        boton_ini_ruta=tk.Button(frame_supbar, text="Iniciar Ruta", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=15, padx=10, command=self.iniciar_ruta)
        boton_ini_ruta.pack(side="right",expand=tk.NO,padx=50, fill=tk.NONE)

        self.boton_fin_ruta=tk.Button(frame_supbar, text="Finalizar Ruta", font=("Roboto, 13"),state="disabled", fg="#2f242c", bg="#e6d884", width=15, padx=10, command=self.finaliza_ruta)
        self.boton_fin_ruta.pack(side="right",expand=tk.NO,padx=50, fill=tk.NONE)

      

        #ventana: rutas y mapa
        frame_rutas=tk.Frame(self.window, bd=10, width=400, relief=tk.SOLID,bg="#e5e5e5")
        frame_rutas.pack(side="left", anchor="w",expand=tk.YES, fill=tk.Y)

        frame_delete_clean_ruta=tk.Frame(frame_rutas, bd=10, width=400, height=50,relief=tk.SOLID,bg="#a1a892")
        frame_delete_clean_ruta.pack(side="top",anchor="n",expand=tk.YES, fill=tk.X)

        boton_elimina_ruta=tk.Button(frame_delete_clean_ruta, text="Eliminar Ruta", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=15, padx=10, command=self.quitar_de_lista)
        boton_elimina_ruta.pack(side="right",expand=tk.NO,padx=50,pady=10, fill=tk.NONE)

        boton_elimina_todo=tk.Button(frame_delete_clean_ruta, text="Eliminar Todo", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=15, padx=10, command=self.elimna_todo)
        boton_elimina_todo.pack(side="right",expand=tk.NO,padx=50,pady=10, fill=tk.NONE)

        frame_lista_rutas=tk.Frame(frame_rutas, bd=0, height=473, relief=tk.SOLID)
        frame_lista_rutas.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        #lista de ruta
        scroll_list=tk.Scrollbar(frame_lista_rutas)
        scroll_list.pack(side="right", fill=tk.Y)

        self.list_rutas=tk.Listbox(frame_lista_rutas,height=600, yscrollcommand=scroll_list.set, activestyle=tk.NONE, bd=0, relief=tk.SOLID, fg="#2f242c", bg="#e5e5e5")
        self.list_rutas.pack(expand=tk.YES, fill=tk.BOTH)
        scroll_list.config(command=self.list_rutas.yview)


        frame_mapa=tk.Frame(self.window, bd=10,width=900, relief=tk.SOLID, bg="#2f242c")
        frame_mapa.pack(side="right",expand=tk.YES, fill=tk.BOTH)

        self.map_widget = tkintermapview.TkinterMapView(frame_mapa, width=800, height=600, corner_radius=0)
        self.map_widget.pack(anchor="center", padx=20, pady=20)

        if self.ubicacion is None:
            coordenadas=geocoder.ip("me")
            latitud=coordenadas.lat
            longitud=coordenadas.lng
            self.map_widget.set_position(latitud,longitud) 
            self.map_widget.set_zoom(12)

        else:
            self.map_widget.set_position(self.ubicacion.coordenadas)
            self.map_widget.set_zoom(12)
            
        self.markerMe=self.map_widget.set_marker(-24.7967267, -65.4175023, text="Me", marker_color_circle="#a1a892", marker_color_outside="#2f242c", text_color="white")
        imagen1=utl.redefine_imagen(".\\images\\consoladj1.jpg", (50,50))
        imagen2=utl.redefine_imagen(".\\images\\festival_rock.jpg", (50,50))
        imagen3=utl.redefine_imagen(".\\images\\rolling.jpeg", (50,50))
        marker1=self.map_widget.set_marker(-24.7763368, -65.4460768, text="Pool Party-David Guetta", image=imagen1, command=self.Mostrar_detalles)
        marker2=self.map_widget.set_marker(-24.7951385, -65.4030448, text="Festival de rock-Artistas Varios", image=imagen2, command=self.Mostrar_detalles)
        marker3=self.map_widget.set_marker(-24.7327322, -65.4165092, text="Concierto estelar de los rolling stones-Rolling Stones", image=imagen3, command=self.Mostrar_detalles)

        self.corredor=None

        self.window.mainloop()
        

    def Mostrar_detalles(self, marcador):
        coords, texto=marcador
        id_coords=self.controller.compara_coords(coords)
        evento=self.controller.compara_ids(id_coords)
        self.controller.abre_evento(evento)
        pass

    def iniciar_ruta(self):
        if self.boton_fin_ruta.state=="disabled" and self.list_rutas.curselection():
            self.boton_fin_ruta.state="normal"
            self.boton_del_ubi.state="normal"
            elementos_box=list(self.list_rutas.get(0, tk.END))
            lista=[self.markerMe]
            for i in elementos_box:
                lista.append(i)
            recorrido=self.map_widget.set_path(lista)
            self.corredor=recorrido
        elif not self.list_rutas.curselection():
            messagebox.showerror(title="Error", message="La lista se encuentra vacía, por favor seleccione uno de los eventos que hay en mapa y dentro de los detalles añada el evento a la ruta")
        else:
            messagebox.showinfo(message="El recorrido ya está en ejecución")

    def agrega_ruta_vista(self, coords):
        self.list_rutas.insert(tk.END, coords)

    def agregar_event_ini(self, coords):
        self.corredor.add_position(coords)

    def eliminar_ruta(self):
        eleccion=self.list_rutas.get()
        self.controller.quita_ruta(eleccion)
        index=self.list_rutas.curselection()
        self.corredor.remove_position(eleccion)
        self.list_rutas.delete(index)

    def volver_atras(self):
        if self.band==1:
            self.controller.Volver_inicio()
        else:
            self.controller.Volver_evento(self.ubicacion.id)

    def finaliza_ruta(self):
        self.corredor.delete()

    def quitar_de_lista(self):
        eleccion=self.list_rutas.get()
        self.controller.quita_ruta(eleccion)
        index=self.list_rutas.curselection()
        self.list_rutas.delete(index)

    def elimna_todo(self):
        self.controller.limpia_lista()
        self.list_rutas.delete(0, tk.END)




