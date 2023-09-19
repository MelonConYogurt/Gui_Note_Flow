import requests, customtkinter, datetime, webbrowser
import customtkinter as ctk
from BaseDeDatosValores import User, session, func
from BaseDeDatosTokens import UserTokens, session1
from BaseDeDatos import User_values, session_user_values #!pendiente
from tkinter import *
from tkinter import  messagebox
from screeninfo import get_monitors
from googletrans import Translator

contador_row = 0
contador_column = 0
frame_princi = ctk.CTk()
frame_princi.title("NoteFlow")
hora_actual = datetime.datetime.now().time()
customtkinter.set_appearance_mode("dark")

class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.values = values
        self.title = title
        self.row = contador_row  # Guarda la fila
        self.column = contador_column  # Guarda la columna
        self.checkboxes = []
        
        
        self.title_label = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title_label.grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=(10, 10))

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i + 1, column=0, columnspan=2, sticky="w", padx=10, pady=(10, 0))
            self.checkboxes.append(checkbox)

        self.button = customtkinter.CTkButton(self, text="Eliminar", command=self.button_callback)
        self.button.grid(row=len(self.values) + 1, column=0, columnspan=2, padx=10, pady=15)

    def button_callback(self):
        session.query(User).filter((User.Titulo_frame == self.title)).delete()
        session.commit()
        self.destroy()  

    def get_checkbuttons(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append("select")
            else:
                checked_checkboxes.append("deselect")
        return checked_checkboxes
           

class TaskManager:
    def __init__(self, frame_princi):
        self.frame_princi = frame_princi
        self.frame_princi.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.toplevel_window = None
        self.translator = Translator()
            
        self.frame_princi = customtkinter.CTkScrollableFrame(self.frame_princi, fg_color="transparent", width=1000, height=1000)
        self.frame_princi.pack(fill="both")        
    
        self.frame_1 = ctk.CTkFrame(master=self.frame_princi, height=25)
        self.frame_1.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=7)
    
        
        self.frame_princi.grid_rowconfigure(0, weight=0)
        self.frame_princi.grid_columnconfigure(0, weight=1)
       
        self.TituloApp = ctk.CTkLabel(self.frame_1, text="Admistrador de pendientes", font=ctk.CTkFont(size=20, weight="bold"), anchor="w")
        self.TituloApp.pack(side="left", padx=10, pady=10)  # Alinea a la izquierda

        # Crear un contenedor para organizar los labels en la misma fila
        self.mensaje_container = ctk.CTkFrame(self.frame_1, fg_color="transparent")
        self.mensaje_container.pack(side="left", padx=35, pady=10)
        self.welcome_message()
        
        
        self.Configuracion = ctk.CTkFrame(self.frame_1, fg_color="transparent")
        self.Configuracion.pack(side="right")
        
        self.boton_confi = customtkinter.CTkButton(self.Configuracion, text="Configuracion",  command=self.VentanaConfiguracion, width=100)
        self.boton_confi.pack(side="left", padx=10, pady=1)
 
            
        self.scrollable_frame = ctk.CTkScrollableFrame(self.frame_princi, width=500, height=200)
        self.scrollable_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        
        self.TituloLista = ctk.CTkLabel(self.scrollable_frame, text="Notas", font=ctk.CTkFont(size=30, weight="bold"))
        self.TituloLista.pack(fill="x", padx=10, pady=(0, 10))

        self.TareaIngresada = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Agregar nota")
        self.TareaIngresada.pack(fill="x", pady=10, padx=5)

        self.BotonAñadir = ctk.CTkButton(self.scrollable_frame, text="Añadir", command=self.add_Tarea, width=90)
        self.BotonAñadir.pack(pady=10, padx=5, anchor="w")
        
        self.frame_2 = ctk.CTkFrame(master=self.frame_princi, height=400, width=300)
        self.frame_2.grid(row=1, column=1, sticky="ne", padx=10, pady=10)
        self.frame_2.pack_propagate(False)  
        self.TituloFrame2= ctk.CTkLabel(self.frame_2, text="Agregar pendientes", font=ctk.CTkFont(size=20, weight="bold"), anchor="center")
        self.TituloFrame2.pack(fill="x", padx=10, pady=10)
        
        self.TituloTarea = ctk.CTkEntry(self.frame_2, placeholder_text="Titulo del pendiente")
        self.TituloTarea.pack(fill="x", pady=10, padx=5)
        
        
        self.Tareas1 = ctk.CTkEntry(self.frame_2, placeholder_text="Digite una tarea")
        self.Tareas1.pack(fill="x", pady=10, padx=12)
        
        
        self.Tareas2 = ctk.CTkEntry(self.frame_2, placeholder_text="Digite una tarea")
        self.Tareas2.pack(fill="x", pady=10, padx=12)
        
        
        self.Tareas3 = ctk.CTkEntry(self.frame_2, placeholder_text="Digite una tarea")
        self.Tareas3.pack(fill="x", pady=10, padx=12)
        
        
        self.Tareas4 = ctk.CTkEntry(self.frame_2, placeholder_text="Digite una tarea")
        self.Tareas4.pack(fill="x", pady=10, padx=12)
        
        
        self.Tareas5 = ctk.CTkEntry(self.frame_2, placeholder_text="Digite una tarea")
        self.Tareas5.pack(fill="x", pady=10, padx=12)
        
        
        self.BotonGuardar = ctk.CTkButton(self.frame_2, text="Aceptar", command=self.obtener_datos)
        self.BotonGuardar.pack(pady=10)
        
        self.checkbox_frames = []
    
        self.frame_3 = ctk.CTkFrame(master=self.frame_princi, height=400, width=300)
        self.frame_3.grid(row=1, column=2, sticky="ne", padx=10, pady=10)
        self.frame_3.pack_propagate(False)  
        
        self.TituloFrame3= ctk.CTkLabel(self.frame_3, text="Estado climatico", font=ctk.CTkFont(size=20, weight="bold"), anchor="center")
        self.TituloFrame3.pack(fill="x", padx=10, pady=10)
        
        
        self.texto_ciudad = ctk.CTkEntry(self.frame_3, placeholder_text="              Ingresa tu ciudad")
        self.texto_ciudad.pack(fill="x", pady=10, padx=50)
        
        
        self.Nombre_ciudad = ctk.CTkLabel(self.frame_3, text="")
        self.Nombre_ciudad.pack(fill="x", pady=10, padx=12)

        self.Estado_climatico = ctk.CTkLabel(self.frame_3, text="")
        self.Estado_climatico.pack(fill="x", pady=10, padx=12)

        self.Temperatura_actual = ctk.CTkLabel(self.frame_3, text="")
        self.Temperatura_actual.pack(fill="x", pady=10, padx=12)

        self.temperatura_maxima = ctk.CTkLabel(self.frame_3, text="")
        self.temperatura_maxima.pack(fill="x", pady=10, padx=12)


        self.Boton_clima = ctk.CTkButton(self.frame_3, text="Buscar", command=self.get_clima, width=200)
        self.Boton_clima.pack(pady=10, padx=12)
        
        
        self.frame_5 = ctk.CTkFrame(master=self.frame_princi,height=50, width=270 )
        self.frame_5.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=10)
        self.frame_5.pack_propagate(False)  
        
        self.TituloFrame5= ctk.CTkLabel(self.frame_5, text="Lista de pendientes", font=ctk.CTkFont(size=20, weight="bold"), anchor="center")
        self.TituloFrame5.pack(padx=10, pady=10)
        
    
        self.frame_4 = ctk.CTkFrame(master=self.frame_princi, fg_color="transparent")
        self.frame_4.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=3, pady=(20, 10))
        
        self.setear_datos()

        


    def on_closing(self):
        all_checkbox_states = []
        self.numero = 1
        for checkbox_frame in self.checkbox_frames:
            checkbox_states = checkbox_frame.get_checkbuttons()
            all_checkbox_states.append(checkbox_states)
            if len(checkbox_states) == 5:  
                session.query(User).filter(User.Id==self.numero).update(
                    {
                                User.Tarea1_estado:checkbox_states[0],
                                User.Tarea2_estado:checkbox_states[1],
                                User.Tarea3_estado:checkbox_states[2],
                                User.Tarea4_estado:checkbox_states[3],
                                User.Tarea5_estado:checkbox_states[4],
                    }
                )
                session.commit()
                self.numero+=1
            elif len(checkbox_states) == 4:  
                session.query(User).filter(User.Id==self.numero).update(
                    {
                                User.Tarea1_estado:checkbox_states[0],
                                User.Tarea2_estado:checkbox_states[1],
                                User.Tarea3_estado:checkbox_states[2],
                                User.Tarea4_estado:checkbox_states[3]
                    }
                )
                session.commit()
                self.numero+=1
            elif len(checkbox_states) == 3:  
                session.query(User).filter(User.Id==self.numero).update(
                    {
                                User.Tarea1_estado:checkbox_states[0],
                                User.Tarea2_estado:checkbox_states[1],
                                User.Tarea3_estado:checkbox_states[2]
                    }
                )
                session.commit()
                self.numero+=1
            elif len(checkbox_states) == 2:  
                session.query(User).filter(User.Id==self.numero).update(
                    {
                                User.Tarea1_estado:checkbox_states[0],
                                User.Tarea2_estado:checkbox_states[1]
                    }
                )
                session.commit()
                self.numero+=1
            elif len(checkbox_states) == 1:  
                session.query(User).filter(User.Id==self.numero).update(
                    {
                                User.Tarea1_estado:checkbox_states[0]
                    }
                )
                session.commit()
                self.numero+=1
            else:
                pass
            
        result = messagebox.askyesno("Confirmación", "¿Estás seguro de que quieres salir?")
        if result:
            frame_princi.destroy()
        
    def VentanaConfiguracion(self):
        self.toplevel = customtkinter.CTkToplevel(self.frame_princi)
        self.toplevel.geometry("390x480")
        self.toplevel.title("Configuracion")
        
        
        self.frame_4_top = ctk.CTkFrame(master=self.toplevel,height=500, width=500 )
        self.frame_4_top.grid(row=0, column=0, padx=10, pady=10)
        
        self.frame_1_top = ctk.CTkFrame(master=self.toplevel,height=500, width=500 )
        self.frame_1_top.grid(row=1, column=0, padx=10, pady=10)
        
        self.frame_2_top = ctk.CTkFrame(master=self.toplevel,height=300, width=270 )
        self.frame_2_top.grid(row=2, column=0, padx=10, pady=10)
        
        self.frame_3_top = ctk.CTkFrame(master=self.toplevel,height=300, width=270 )
        self.frame_3_top.grid(row=3, column=0, padx=10, pady=10)
        
    
        self.label_problemas= ctk.CTkLabel(self.frame_1_top, text="Si encuentras algún problema, no dudes en ponerte\nen contacto con nosotros. Estamos aquí para\n ayudarte en cualquier momento.", font=ctk.CTkFont(size=12, weight="bold"), anchor="center")
        self.label_problemas.grid(row=0, column=0,padx=20, pady=10, columnspan=4)
        
        self.Boton_contacto1 = ctk.CTkButton(self.frame_1_top, text="Pagina web", command=self.abrir_enlace, width= 20)
        self.Boton_contacto1.grid(row=1, column=1, padx=5, pady=10)
        
        self.Boton_contacto2 = ctk.CTkButton(self.frame_1_top, text="Pagina web1", command=self.abrir_enlace, width= 20)
        self.Boton_contacto2.grid(row=1, column=2, padx=5, pady=10)
        
        self.Boton_contacto3 = ctk.CTkButton(self.frame_1_top, text="Pagina web2", command=self.abrir_enlace, width= 20)
        self.Boton_contacto3.grid(row=1, column=3, padx=5, pady=10)
        
        
        self.label_cerrar= ctk.CTkLabel(self.frame_3_top, text="Si cierras tu sesion perderas todas\nlos pendientes que tengas en la app", font=ctk.CTkFont(size=12, weight="bold"), anchor="center")
        self.label_cerrar.grid(row=0, column=0, padx=65, pady=10, columnspan=2)
        
        self.label_cerrar= ctk.CTkLabel(self.frame_3_top, text="Finalizar sesion", font=ctk.CTkFont(size=20, weight="bold"), anchor="center")
        self.label_cerrar.grid(row=1, column=0, padx=2, pady=10, columnspan=2)
        
        self.Boton_close_session = ctk.CTkButton(self.frame_3_top, text="Salir", command=self.close_seccion, width=100)
        self.Boton_close_session.grid(row=2, column=1, padx=1, pady=10)
        
        self.Boton_close_session = ctk.CTkButton(self.frame_3_top, text="Volver", command=self.close_configuracion, width=100)
        self.Boton_close_session.grid(row=2, column=0, padx=1, pady=10)
        
        self.appearance_mode_label1 = customtkinter.CTkLabel(self.frame_2_top, text="Si deseas, puedes cambiar el color por defecto\ncuyo color es el mismo del sistema (Windows)", font=ctk.CTkFont(size=12, weight="bold"), anchor="center")
        self.appearance_mode_label1.grid(row=0, column=0, padx=35, pady=(10, 0), columnspan=2)
        
        self.appearance_mode_label2 = customtkinter.CTkLabel(self.frame_2_top, text="Apariencia de la app:", font=ctk.CTkFont(size=12, weight="bold"), anchor="center")
        self.appearance_mode_label2.grid(row=1, column=0, padx=10, pady=(10, 0))
        
        self.Set_value_appearance = customtkinter.StringVar(value="Seleccionar")
        
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.frame_2_top, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event, variable=self.Set_value_appearance)
        self.appearance_mode_optionemenu.grid(row=1, column=1, padx=10, pady=(10, 10))
        
        
        self.titulo= ctk.CTkLabel(self.frame_4_top, text="Configuracion", font=ctk.CTkFont(size=22, weight="bold"), anchor="center")
        self.titulo.grid(row=0, column=0,padx=(110, 110), pady=10, columnspan=4)   
        
      
    
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)    
            
    def on_label_enter(self, event):
        self.labelConfiguracion.configure(text_color="#2179bc")  # Cambiar el color del texto al pasar el mouse
        
    def on_label_leave(self, event):
        self.labelConfiguracion.configure(text_color="#dce4ee")  # Restaurar el color original al salir el mouse
           
    def close_configuracion(self):
        self.toplevel.destroy()
        
    
    
    def get_clima(self):
        ciudad = self.texto_ciudad.get()
        self.function_clima(ciudad)
        self.texto_ciudad.delete(0, ctk.END)
        
    def function_clima(self, ciudad):
        try:
            API_KEY = "af08687a387cfa24b274e4f7fc8a066a"
            URL = "https://api.openweathermap.org/data/2.5/weather"
            self.parametros = {"APPID": API_KEY, "q": ciudad, "units": "metric"}
            self.response = requests.get(URL, params= self.parametros)
            self.clima =  self.response.json()

            self.nombre =  self.clima["name"]
            self.desc =  self.clima["weather"][0]["description"]
            self.temp =  self.clima["main"]["temp"]
            self.temp_max =  self.clima["main"]["temp_max"]
            self.estado_climatico_traducido = self.translator.translate(self.desc, dest='es').text

            self.Nombre_ciudad.configure(text=self.nombre, font=ctk.CTkFont(size=28, weight="bold"))
            self.Estado_climatico.configure(text=self.estado_climatico_traducido.capitalize(), font=ctk.CTkFont(size=24, weight="bold"))
            self.Temperatura_actual.configure(text=f"Temperatura promedio: {int(self.temp)}°C", font=ctk.CTkFont(size=19, weight="bold"))
            self.temperatura_maxima.configure(text=f"Temperatura máxima:   {int(self.temp_max)}°C", font=ctk.CTkFont(size=19, weight="bold"))
        except:
            self.Nombre_ciudad.configure(text="Intenta nuevamente")
            self.Estado_climatico.configure(text="")
            self.Temperatura_actual.configure(text="")
            self.temperatura_maxima.configure(text="")    
   
            
    def add_Tarea(self):
        Tarea = self.TareaIngresada.get()
        label = ctk.CTkLabel(self.scrollable_frame, text=Tarea)
        label.pack(anchor="w")
        self.TareaIngresada.delete(0, ctk.END)
          
    def obtener_datos(self):
        global contador_row
        global contador_column
        titulo = self.TituloTarea.get()
        self.TituloTarea.delete(0, ctk.END)
        self.tareas = []
                    
        # Verificar cada Entry de tareas y agregar su contenido si no está vacío
        for tarea_entry in [self.Tareas1, self.Tareas2, self.Tareas3, self.Tareas4, self.Tareas5]:
            contenido_tarea = tarea_entry.get().strip()
            tarea_entry.delete(0, ctk.END)
            if contenido_tarea:
                self.tareas.append(contenido_tarea)


        # Crear una instancia de MyCheckboxFrame con el título y las tareas
        checkbox_frame = MyCheckboxFrame(frame_princi, title=titulo, values=self.tareas)
        if self.checkbox_frames:
            contador_column += 1
            if contador_column >= 5:  # Si hay 3 columnas, pasa a la siguiente fila
                contador_column = 0
                contador_row += 1
        else:
            contador_row += 1
 
        checkbox_frame.grid(row=contador_row, column=contador_column, padx=5, pady=(10, 0), sticky="w", in_=self.frame_4)
       
        if self.tareas:
            new_frame = User(Titulo_frame=titulo,
                            Tarea1_frame=self.tareas[0] if len(self.tareas) > 0 else "",
                            Tarea2_frame=self.tareas[1] if len(self.tareas) > 1 else "",
                            Tarea3_frame=self.tareas[2] if len(self.tareas) > 2 else "",
                            Tarea4_frame=self.tareas[3] if len(self.tareas) > 3 else "",
                            Tarea5_frame=self.tareas[4] if len(self.tareas) > 4 else "",
                            Tarea1_estado="",
                            Tarea2_estado="",
                            Tarea3_estado="",
                            Tarea4_estado="",
                            Tarea5_estado="",
                            Fila_frame=contador_row,
                            Columna_frame=contador_column)
            session.add(new_frame)
            session.commit()
                        
        # Agregar la instancia a la lista
        self.checkbox_frames.append(checkbox_frame)
        
    def close_seccion(self):
        result2 = messagebox.askyesno("Confirmación", "¿Estás seguro de cerrar sesion?")
        if result2:
            session1.query(UserTokens).delete()
            session1.commit()
            frame_princi.destroy()
            
    def abrir_enlace(self):
        webbrowser.open("https://youtu.be/XZp3Mtn-YsI?list=RDGMEMJQXQAmqrnmK1SEjY_rKBGA")    
        
    def setear_datos(self):
        self.count_result = session.query(func.count(User.Id)).scalar()
        print("Cantidad total de registros:", self.count_result)
        
        
        global contador_row
        global contador_column
        last_fila_set = None
        last_columna_set = None

        for numero in range(1, self.count_result + 1):
            Tareas_set = []  # Vaciar la lista en cada iteración
            Estados_tareas_set = []  # Vaciar la lista en cada iteración
            
            
            new_set_frames = session.query(User).filter(User.Id == numero).first()
            if new_set_frames:
                titulo_set = new_set_frames.Titulo_frame
                
                for i in range(1, 6):
                    tarea_frame_attr = getattr(new_set_frames, f"Tarea{i}_frame")
                    tarea_estado_attr = getattr(new_set_frames, f"Tarea{i}_estado")
                    
                    if tarea_frame_attr != "":
                        Tareas_set.append(tarea_frame_attr)
                        Estados_tareas_set.append(tarea_estado_attr)
                
                fila_set = new_set_frames.Fila_frame
                colunma_set = new_set_frames.Columna_frame

                last_fila_set = fila_set
                last_columna_set = colunma_set
                    
                checkbox_frame = MyCheckboxFrame(frame_princi, title=titulo_set, values=Tareas_set)       
                checkbox_frame.grid(row=fila_set, column=colunma_set, padx=5, pady=(10, 0), sticky="w", in_=self.frame_4)
                # Accede a los checkboxes dentro de la instancia actual de MyCheckboxFrame
                for i, estado in enumerate(Estados_tareas_set):
                    if estado == "select":
                        checkbox_frame.checkboxes[i].select()
                    elif estado == "deselect":
                        checkbox_frame.checkboxes[i].deselect()
                    else:
                        pass
                self.checkbox_frames.append(checkbox_frame)
                contador_column = last_columna_set
                contador_row = last_fila_set            

    def welcome_message(self):
        session_user_values.query()
        hora_actual = datetime.datetime.now().time()

        # Definir rangos de horas para personalizar el mensaje de bienvenida
        if hora_actual < datetime.time(12, 0):
            self.mensaje_saludo_obtenido = "¡Buenos días!"
        elif hora_actual < datetime.time(18, 0):
            self.mensaje_saludo_obtenido = "¡Buenas tardes!"
        else:
            self.mensaje_saludo_obtenido = "¡Buenas noches!"
        
        
        self.mensaje_Bienvenida = ctk.CTkLabel(self.mensaje_container, text=self.mensaje_saludo_obtenido, font=ctk.CTkFont(size=20, weight="bold"), anchor="w")
        self.mensaje_Bienvenida.pack(side="right")# Alinea a la derecha
        
        

def get_second_monitor_info(monitors):
    if len(monitors) > 1:
        return monitors[1]  # Assuming the second monitor is at index 1
    return None

def open_app_on_second_monitor(frame_princi, monitor):
    frame_princi.geometry(f"{monitor.width}x{monitor.height}+{monitor.x}+{monitor.y}")

def main():
    
    monitors = get_monitors()
    second_monitor = get_second_monitor_info(monitors)

    if second_monitor:
        open_app_on_second_monitor(frame_princi, second_monitor)

    TaskManager(frame_princi)
    frame_princi.mainloop()

if __name__ == "__main__":
    
    main()
