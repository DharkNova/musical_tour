import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from Controllers.Controller_mapa import control_mapa
import Util.generic as utl     
import tkintermapview
import geocoder
class vista_mapa:

    def __init__(self, evento=None):
        self.window=tk.Tk()
        self.window.title("MUSICAL TOUR-MAPA")
        utl.Centre_window(self.window,1300,620)
        self.window.config(bg="#e5e5e5")
        self.window.resizable(width=0, height=0)
        self.controller=control_mapa()
        self.evento=evento
        
        #Frame de barra superior 
        frame_supbar=tk.Frame(self.window, bd=0, height=40, relief=tk.SOLID, padx=10, pady=10, bg="#2f242c")
        frame_supbar.pack(side="top", expand=tk.NO, fill=tk.X)

        #botones
        boton_volver=tk.Button(frame_supbar, text="Volver", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=5, padx=10)
        boton_volver.pack(side="left",expand=tk.NO,padx=5, fill=tk.NONE)
        
        boton_inicio=tk.Button(frame_supbar, text="Inicio", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=5, padx=10)
        boton_inicio.pack(side="left",expand=tk.NO,padx=5, fill=tk.NONE)

        boton_cerrar_sesion=tk.Button(frame_supbar, text="Cerrar sesion", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=10, padx=10)
        boton_cerrar_sesion.pack(side="right",expand=tk.NO,padx=10, fill=tk.NONE)  

        boton_ini_ruta=tk.Button(frame_supbar, text="Iniciar Ruta", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=15, padx=10)
        boton_ini_ruta.pack(side="right",expand=tk.NO,padx=50, fill=tk.NONE)

        boton_fin_ruta=tk.Button(frame_supbar, text="Finalizar Ruta", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=15, padx=10)
        boton_fin_ruta.pack(side="right",expand=tk.NO,padx=50, fill=tk.NONE)

      

        #ventana: rutas y mapa
        frame_rutas=tk.Frame(self.window, bd=10, width=400, relief=tk.SOLID,bg="#e5e5e5")
        frame_rutas.pack(side="left", anchor="w",expand=tk.YES, fill=tk.Y)

        frame_delete_clean_ruta=tk.Frame(frame_rutas, bd=10, width=400, height=50,relief=tk.SOLID,bg="#a1a892")
        frame_delete_clean_ruta.pack(side="top",anchor="n",expand=tk.YES, fill=tk.X)

        boton_elimina_ruta=tk.Button(frame_delete_clean_ruta, text="Eliminar Ruta", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=15, padx=10)
        boton_elimina_ruta.pack(side="right",expand=tk.NO,padx=50,pady=10, fill=tk.NONE)

        boton_elimina_todo=tk.Button(frame_delete_clean_ruta, text="Eliminar Todo", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=15, padx=10)
        boton_elimina_todo.pack(side="right",expand=tk.NO,padx=50,pady=10, fill=tk.NONE)

        frame_lista_rutas=tk.Frame(frame_rutas, bd=0, height=473, relief=tk.SOLID)
        frame_lista_rutas.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        #lista de ruta
        scroll_list=tk.Scrollbar(frame_lista_rutas)
        scroll_list.pack(side="right", fill=tk.Y)

        self.list_rutas=tk.Listbox(frame_lista_rutas,height=600, yscrollcommand=scroll_list.set, activestyle=tk.NONE, bd=0, relief=tk.SOLID, fg="#2f242c", bg="red")
        self.list_rutas.pack(expand=tk.YES, fill=tk.BOTH)
        scroll_list.config(command=self.list_rutas.yview)


        frame_mapa=tk.Frame(self.window, bd=10,width=900, relief=tk.SOLID, bg="#2f242c")
        frame_mapa.pack(side="right",expand=tk.YES, fill=tk.BOTH)

        
        map_widget = tkintermapview.TkinterMapView(frame_mapa, width=800, height=600, corner_radius=0)
        map_widget.pack(anchor="center", padx=20, pady=20)
        coordenadas=geocoder.ip("me")
        latitud=coordenadas.lat
        longitud=coordenadas.lng
        map_widget.set_position(latitud,longitud) 
        map_widget.set_zoom(12)

        marker1=map_widget.set_marker(-24.7763368, -65.4460768)
        marker2=map_widget.set_marker(-24.7951385, -65.4030448)
        marker3=map_widget.set_marker(-24.7622526, -65.3977041)
        marker4=map_widget.set_marker(-24.7828792, -65.4041186)
        marker5=map_widget.set_marker(-24.7327322, -65.4165092)
        lista=[marker1.position, marker2.position, marker3.position, marker4.position, marker5.position]
        map_widget.add_right_click_menu_command(label="Detalles", command=self.Mostrar_detalles, pass_coords=True)


        # set a path
        path_1 = map_widget.set_path(lista)

        # methods
        
        # path_1.add_position(position)
        # path_1.remove_position(position)
        # path_1.delete()


        self.window.mainloop()
        

    def Mostrar_detalles(self, marcador):
        coords, texto=marcador
        id_coords=self.controller.compara_coords(coords)
        evento=self.controller.compara_ids(id_coords)
        self.controller.abre_evento(evento)
        pass

    def Agregar_ruta(self, coords):
        
        pass