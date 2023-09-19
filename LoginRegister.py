import customtkinter, random, bcrypt, re, string, jwt, datetime, os
import customtkinter as ctk
from PIL import Image
from tkinter import  messagebox
from BaseDeDatos import User_values, session_user_values
from BaseDeDatosTokens import UserTokens, session1
from EnvioMails import EnviarCorreoRecuperacion, EnviarCorreoBienvenida, EnviarSoporte
customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    width = 900
    height = 600
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.secret_key = os.getenv("PASSWORD_TOKENS")
            token_entry = session1.query(UserTokens).first()
            if token_entry and self.verify_token(token_entry.Token):
                from AppIntegrada import main
                main()
                self.destroy()
            else:
                pass
        except Exception as e:
                print(f"Error: {e}")

    
        self.icono_usuario = customtkinter.CTkImage(Image.open("icons8-usuario-24.png"),size=(24,24))
        self.icono_contra = customtkinter.CTkImage(Image.open("icons8-llave-24.png"),size=(24,24))
        self.icono_enviar = customtkinter.CTkImage(Image.open("icons8-aplicación-telegrama-24.png"),size=(24,24))
        self.icono_aceptar = customtkinter.CTkImage(Image.open("icons8-llave-24.png"),size=(24,24))
        self.icono_atras = customtkinter.CTkImage(Image.open("icons8-atrás-24.png"),size=(24,24))
        
        
        self.title("NoteFlow")
        #!self.update_idletasks()  
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.width) // 2
        y = (screen_height - self.height) // 2
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.geometry(f"{self.width}x{self.height}")
       
        self.resizable(False, False)

        # load and create background image
        self.FondoPantalla()
        self.bg_image = customtkinter.CTkImage(Image.open(self.fondo),size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="Reminder\nInicio de sesion",font=customtkinter.CTkFont(size=25, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(130, 15))
        
        self.usuario_login = customtkinter.CTkEntry(self.login_frame, width=200, placeholder_text="Usuario")
        self.usuario_login.grid(row=1, column=0, padx=30, pady=(15, 15))
        
        self.password_login = customtkinter.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="Contraseña")
        self.password_login.grid(row=2, column=0, padx=30, pady=(0, 15))
        
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Iniciar sesion",command=self.verificar, width=200, image=self.icono_usuario, compound="left")
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        
        self.login_button2 = customtkinter.CTkButton(self.login_frame, text="Registarse", command=self.register_event, width=200)
        self.login_button2.grid(row=4, column=0, padx=30, pady=(15, 15))
        
        self.register_label = customtkinter.CTkLabel(self.login_frame, text="¿No recuerdas tu contraseña?",font=customtkinter.CTkFont(size=11, weight="bold"))
        self.register_label.grid(row=5, column=0, padx=30, pady=(15, 25))
        
        self.register_label2 = customtkinter.CTkLabel(self.login_frame, text="Si tinenes problemas\n Contactanos",font=customtkinter.CTkFont(size=11, weight="bold"))
        self.register_label2.grid(row=6, column=0, padx=30, pady=(0,10))
        
        self.register_label2.bind("<Button-1>", self.VentanaConctactanos)
        self.register_label2.bind("<Enter>", self.on_label_enter)  # Enlazar evento de entrada del mouse
        self.register_label2.bind("<Leave>", self.on_label_leave)  # Enlazar evento de salida del mouse
        
        self.register_label.bind("<Button-1>",self.VentanaRecuperacion)
        self.register_label.bind("<Enter>", self.on_label_enter2)  # Enlazar evento de entrada del mouse
        self.register_label.bind("<Leave>", self.on_label_leave2)  # Enlazar evento de salida del mouse
        
    

    def register_event(self): 
        # create main frame
        self.login_frame.grid_forget()
        self.frameDatos1 = customtkinter.CTkFrame(self, corner_radius=0, width=430, height=600)
        self.frameDatos1.grid(row=0, column=0)
        
        self.frameDatos = customtkinter.CTkFrame(self.frameDatos1, corner_radius=0, width=500, height=600 )
        self.frameDatos.grid(row=0, column=1)
        
        self.frameDatos2 = customtkinter.CTkFrame(self.frameDatos1, corner_radius=0, width=500, height=600, fg_color= "#242424" )
        self.frameDatos2.grid(row=0, column=0)
               
        
        self.main_label = customtkinter.CTkLabel(self.frameDatos2, text="¡Bienvenido a nuestra app!", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=20, pady=(5, 15))
        self.main_label2 = customtkinter.CTkLabel(self.frameDatos2, text="\n\nEstamos emocionados de tenerte como parte de nuestra comunidad\nExplora, descubre y disfruta todo lo que nuestra app tiene para ofrecer\n\nGracias por unirte a nosotros y esperamos que disfrutes\n cada momento en nuestra plataforma.", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.main_label2.grid(row=1, column=0, padx=50, pady=(5, 450))
        
        
        self.main_label3 = customtkinter.CTkLabel(self.frameDatos, text="Completa los siguientes campos:", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.main_label3.grid(row=0, column=0, padx=20, pady=(15, 15))
        
        self.usuario = customtkinter.CTkEntry(self.frameDatos, width=200, placeholder_text="Usuario")
        self.usuario.grid(row=2, column=0, padx=30, pady=(15, 15))
        
        self.password = customtkinter.CTkEntry(self.frameDatos, width=200, show="*", placeholder_text="Contraseña")
        self.password.grid(row=3, column=0, padx=30, pady=(15, 15))
        
        self.confirmar = customtkinter.CTkEntry(self.frameDatos, width=200, show="*",placeholder_text="Comfirmar contraseña")
        self.confirmar.grid(row=4, column=0, padx=30, pady=(15, 15))
        
        self.nombre = customtkinter.CTkEntry(self.frameDatos, width=200, placeholder_text="Nombre completo")
        self.nombre.grid(row=5, column=0, padx=30, pady=(15, 15))
        
        self.correo = customtkinter.CTkEntry(self.frameDatos, width=200, placeholder_text="Correo / Email")
        self.correo.grid(row=6, column=0, padx=30, pady=(15, 10))

        
        self.optionmenu_var = customtkinter.StringVar(value="Genero")
        self.optionmenu = customtkinter.CTkOptionMenu(self.frameDatos,values=["Mujer", "Hombre","Helicoptero apache","Prefiero no decirlo"],variable=self.optionmenu_var, width=200)
        self.optionmenu.grid(row=7, column=0, padx=5, pady=(15, 10))
        
        self.optionmenu2_var = customtkinter.StringVar(value="Ocupacion")
        self.optionmenu2 = customtkinter.CTkOptionMenu(self.frameDatos,values=["Estudiante", "Docente","Empleado","Otro"],variable=self.optionmenu2_var, width=200)
        self.optionmenu2.grid(row=8, column=0, padx=5,pady=(15, 10))
        
        
        
        self.back_button = customtkinter.CTkButton(self.frameDatos, text="Continuar", command=self.back_event, width=200)
        self.back_button.grid(row=9, column=0, padx=30, pady=(15, 10))
        self.back_button = customtkinter.CTkButton(self.frameDatos, text="Volver", command=self.atras_event, width=200, image=self.icono_atras, compound="left")
        self.back_button.grid(row=10, column=0, padx=30, pady=(10, 15))
       
        self.register_label2 = customtkinter.CTkLabel(self.frameDatos, text="Si tinenes problemas\n Contactanos",font=customtkinter.CTkFont(size=11, weight="bold"))
        self.register_label2.grid(row=11, column=0, padx=5, pady=(5,25))
        
        self.register_label2.bind("<Button-1>", self.VentanaConctactanos)
        self.register_label2.bind("<Enter>", self.on_label_enter)  # Enlazar evento de entrada del mouse
        self.register_label2.bind("<Leave>", self.on_label_leave)  # Enlazar evento de salida del mouse
        
        

    def VentanaRecuperacion(self, event):
        self.login_frame.grid_forget()  # remove login frame
        self.frame_tempo = customtkinter.CTkFrame(self, height=600, width=300)
        self.frame_tempo.grid(row=0, column=0)

        self.label_tempo = customtkinter.CTkLabel(self.frame_tempo, text="NoteFlow", font=customtkinter.CTkFont(size=35, weight="bold"))
        self.label_tempo.grid(row=0, column=0, padx=15, pady=(2, 55))
        
        self.label_tempo3 = customtkinter.CTkLabel(self.frame_tempo, text="Recuperacion de contraseña", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.label_tempo3.grid(row=1, column=0, padx=10, pady=(10, 20))

        self.label_tempo4 = customtkinter.CTkLabel(self.frame_tempo, text="Si has olvidado tu contraseña, no te preocupes.\nProporciona tu dirección de correo electrónico\n enviaremos un mail con ciertas instrucciones",
                                                   font=customtkinter.CTkFont(size=12, weight="bold"))
        self.label_tempo4.grid(row=2, column=0, padx=15, pady=(10, 22))
        
        self.correo_tempo = customtkinter.CTkEntry(self.frame_tempo, width=200, placeholder_text="     Digite su correo electronico")
        self.correo_tempo.grid(row=3, column=0, padx=10, pady=(15, 15))

        self.boton_tempo = customtkinter.CTkButton(self.frame_tempo, text="Recuperar Contraseña", command=self.RecuperarContra, width=200, image=self.icono_contra, compound="left")
        self.boton_tempo.grid(row=4, column=0, padx=10, pady=(15, 160))

        self.register_label2 = customtkinter.CTkLabel(self.frame_tempo, text="¿Necesitas ayuda?\nContáctanos",font=customtkinter.CTkFont(size=11, weight="bold"))
        self.register_label2.grid(row=6, column=0, padx=10, pady=(0,22))    
        self.register_label2.bind("<Button-1>", self.VentanaConctactanos)
        self.register_label2.bind("<Enter>", self.on_label_enter)  # Enlazar evento de entrada del mouse
        self.register_label2.bind("<Leave>", self.on_label_leave)  # Enlazar evento de salida del mouse
        
        self.back_button2 = customtkinter.CTkButton(self.frame_tempo, text="Volver", command=self.atras_event4, width=50, image=self.icono_atras, compound="left")
        self.back_button2.grid(row=5, column=0, padx=10, pady=(15, 20))

            
    def VentanaConctactanos(self, event):
        try:
            self.login_frame.grid_forget()
        except:
            pass

        try:
            self.frameDatos.grid_forget()
        except:
            pass

        try:
            self.frame_tempo.grid_forget()
        except:
            pass
        try:
            self.frameDatos.grid_forget()
            self.frameDatos1.grid_forget()
            self.frameDatos2.grid_forget()
        except:
            pass
        
        self.tempo1 = customtkinter.CTkFrame(self, height=600, width=300)
        self.tempo1.grid(row=0, column=0)

        self.tempo2 = customtkinter.CTkLabel(self.tempo1, text="NoteFlow", font=customtkinter.CTkFont(size=35, weight="bold"))
        self.tempo2.grid(row=0, column=0, padx=15, pady=(5, 20))
        
        self.tempo3 = customtkinter.CTkLabel(self.tempo1, text="Soporte tecnico", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.tempo3.grid(row=1, column=0, padx=10, pady=(10, 20))

        self.tempo4 = customtkinter.CTkLabel(self.tempo1, text="Si tienes un fallo, bug o problema.\nayudanos proporcionando tu fallo\n asi podremos ayudarte pronto",
                                                   font=customtkinter.CTkFont(size=11, weight="bold"))
        self.tempo4.grid(row=2, column=0, padx=15, pady=(10, 22))
        
        self.textbox = customtkinter.CTkTextbox(self.tempo1, width=100, corner_radius=0)
        self.textbox.grid(row=3, column=0, sticky="nsew")
        self.textbox.insert("0.0", "     Describe tu incoveniente o reporte")
        
        self.nombre_reporte = customtkinter.CTkEntry(self.tempo1, width=200, placeholder_text="Digita tu usuario")
        self.nombre_reporte.grid(row=4, column=0, padx=15, pady=(15, 15))
        
        self.tempo6 = customtkinter.CTkButton(self.tempo1, text="Enviar comentario", command=self.EnvioDeComentarios, width=20, image=self.icono_enviar, compound="right" )
        self.tempo6.grid(row=5, column=0, padx=10, pady=(15, 15))
        
        self.back_button3 = customtkinter.CTkButton(self.tempo1, text="Volver", command=self.atras_event3, width=200, image=self.icono_atras, compound="left")
        self.back_button3.grid(row=6, column=0, padx=10, pady=(15, 45))
        
        
    def atras_event (self):
        self.frameDatos.grid_forget()# remove main frame
        self.frameDatos1.grid_forget()# remove main frame
        self.frameDatos2.grid_forget()# remove main frame
        self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame
        
    def atras_event2 (self):
        self.frame_tempo.grid_forget()  # remove main frame
        self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame   
    
    def atras_event3 (self):
        self.tempo1.grid_forget()  # remove main frame
        self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame 
        
    def atras_event4 (self):
        self.frame_tempo.grid_forget()  # remove main frame
        self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame 
    
    def verificar(self):
        username = self.usuario_login.get()
        password = self.password_login.get()
        if not username or not password:
            messagebox.showerror(message="Por favor, ingresa un usuario y una contraseña.", title="NoteFlow")
            return
        try:
            user = session_user_values.query(User_values).filter_by(username=username).first()
            if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                
                user_data = {
                    "username": username,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(days=365)  
                            }
                self.secret_key = os.getenv("PASSWORD_TOKENS")  
                token_generado = jwt.encode(user_data, self.secret_key, algorithm="HS256")
                
                new_token_entry = UserTokens(Token=token_generado)
                session1.add(new_token_entry)
                session1.commit()
                
                self.destroy()
                from AppIntegrada import main
                main()
            else:
                messagebox.showerror(message="Credenciales incorrectas. Por favor, verifica tu usuario y contraseña.", title="Error de inicio de sesión")    
        except Exception as e:
                print(f"Error: {e}")

    
    def verify_token(self, token):
        try:
            decoded_token = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            exp_timestamp = decoded_token["exp"]
            exp_datetime = datetime.datetime.fromtimestamp(exp_timestamp)
            
            if exp_datetime >= datetime.datetime.utcnow():
                return True
        except jwt.ExpiredSignatureError:
            return False
        except jwt.DecodeError:
            return False
        return False
    
    

    def back_event(self):
        Contra_sin_confirmar = self.password.get()
        contra_confirmada = self.confirmar.get()
        correo = self.correo.get()
        name = self.nombre.get()
        usu = self.usuario.get()
        gen= self.optionmenu.get()
        ocu= self.optionmenu2.get()
        
        if Contra_sin_confirmar == contra_confirmada:
            if re.match(r"[^@]+@[^@]+\.[^@]+", correo):
                user_with_same_email = session_user_values.query(User_values).filter_by(email=correo).first()
                if user_with_same_email:
                    messagebox.showerror(message="El correo electrónico ya está registrado.", title="NoteFlow")
                else:
                    EnviarCorreoBienvenida(correo, usu, contra_confirmada,name)
                    hashed_password = bcrypt.hashpw(contra_confirmada.encode('utf-8'), bcrypt.gensalt())  
                    new_user = User_values(username= usu, password=hashed_password.decode('utf-8'), name=name, email=correo, genero=gen, ocupacion=ocu)
                    session_user_values.add(new_user)
                    session_user_values.commit()
                    self.password.delete(0, ctk.END)
                    self.confirmar.delete(0, ctk.END)
                    self.correo.delete(0, ctk.END)
                    self.nombre.delete(0, ctk.END)
                    self.usuario.delete(0, ctk.END)
                    self.atras_event()
            else:
                messagebox.showerror(message="Correo electrónico no válido.", title="NoteFlow")
        else:
            messagebox.showerror(message="Contraseñas no coinciden", title="NoteFlow")
            
            
    def FondoPantalla(self):
        numero_aleatorio = random.randint(1, 5)

        if numero_aleatorio == 1:
            fondo_aleatorio = "fondo1.jpg"
        elif numero_aleatorio == 2:
            fondo_aleatorio = "fondo6.jpg"
        elif numero_aleatorio == 3:
            fondo_aleatorio = "fondo2.jpg"
        elif numero_aleatorio == 4:
            fondo_aleatorio = "fondo5.jpg"
        elif numero_aleatorio == 5:
            fondo_aleatorio = "fondo4.jpg."

        self.fondo = fondo_aleatorio
            
    
    def EnvioDeComentarios(self):
        Nombre_usuario = self.nombre_reporte.get()
        Comentario_mensaje= self.textbox.get("0.0", "end")
        if Nombre_usuario and Comentario_mensaje:
            EnviarSoporte(Comentario_mensaje, Nombre_usuario)
            messagebox.showinfo(message="Tu reporte se ha realizado con exito. Gracias", title="NoteFlow")
            
        else:
             messagebox.showerror(message="LLena los datos, para continuar", title="NoteFlow")
            
    def GenerarContra(self, length=12):
        characters = string.ascii_letters + string.digits
        self.password_temporal = ''.join(random.choice(characters) for _ in range(length))
        return self.password_temporal
        
        
    def RecuperarContra(self):
        correo= self.correo_tempo.get()
        if correo:
            messagebox.showerror(message="Por favor, asegúrate de revisar la carpeta de spam o correo\n no deseado si no recibes nuestro mensaje de recuperación", title="NoteFlow")
            self.Ventana_tempo.destroy()
            busqueda_correo = session_user_values.query(User_values).filter_by(email=correo).first()
            if busqueda_correo:
                self.GenerarContra()
                EnviarCorreoRecuperacion(correo, self.password_temporal,)
            else:
                messagebox.showerror(message="Hemos tenido un fallo", title="NoteFlow")
                return  # Salir de la función en caso de error 
        else:
            messagebox.showerror(message="No se ha dijitado un correo", title="NoteFlow")
            #return  # Salir de la función en caso de error 
       
    def on_label_enter(self, event):
        self.register_label2.configure(text_color="#2179bc")  # Cambiar el color del texto al pasar el mouse
        
        
    def on_label_leave(self, event):
        self.register_label2.configure(text_color="#dce4ee")  # Restaurar el color original al salir el mouse
        
    def on_label_enter2(self, event):
        self.register_label.configure(text_color="#2179bc")  # Cambiar el color del texto al pasar el mouse

    def on_label_leave2(self, event):
        self.register_label.configure(text_color="#dce4ee")  # Restaurar el color original al salir el mouse
        
        
            
if __name__ == "__main__":
    app = App()
    app.mainloop()
