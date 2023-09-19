import os, ssl, smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
from tkinter import  messagebox
        
"""
#!Envio con Sengrid (Me bloquearon las cuentas)
Apykeys: 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
URl: https://sendgrid.com/

librerias:

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

-Pasos cargando las variables desde un archivo .env 

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Acceder a la clave de API de SendGrid
sendgrid_api_key = os.getenv("SENDGRID_API_KEY")


# Ahora puedes utilizar sendgrid_api_key en tu código

def EnviarCorreoRecuperacion(to_email, password):
    
    message = Mail(
        from_email='GrupoNoteFlow@gmail.com',
        to_emails=to_email,
        subject='Soporte de NoteFlow',
        html_content=f'Tu contraseña es: {password}')
    print("Se intento") 
    try:
        sg = SendGridAPIClient("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")
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        messagebox.showinfo(message="Revisa tu correo electronico.", title="ʕ•́ᴥ•̀ʔっ")
    except Exception as e:
        messagebox.showerror(message="Hemos tenido un problema:\n\nNo se ha encontrado un correo asociado\ncon las cuentas de NoteFlow.", title="ʕ•́ᴥ•̀ʔっ")"""


#Para usar smtplib y email.message para enviar correos electrónicos desde Python:

#-Creamos una cuenta gmail, activamos la verificasion en dos pasos y nos vamos al siguiente apartado url
# - #!https://myaccount.google.com/u/4/apppasswords
#-Estando ahi configuramos las dos opciones que nos piden.


def EnviarCorreoRecuperacion(to_email, new_password):
    try:
        load_dotenv()
        email_sender = "gruponoteflow@gmail.com"
        email_recipient = to_email
        logo_filename = "1.png"
        with open(logo_filename, 'rb') as logo_file:
            logo_content = logo_file.read()
            
        #logo_filename2 = "3.png"
        #with open(logo_filename2, 'rb') as logo_file2:
         #   logo_content2 = logo_file2.read()

        logo_cid = f"logo@{logo_filename}"
        #logo_cid2 = f"logo@{logo_filename2}"
        subject = "Recuperación de contraseña"
        body = f"""\
        <html>
        <body style="font-family: Arial, sans-serif; padding: 20px;">
            <h2 style="color: #8c52ff;">Recuperación de contraseña</h2>
            <p>Estimado usuario,</p>
            <p>Hemos recibido una solicitud para restablecer la contraseña de su cuenta en NoteFlow.</p>
            <p>Su <strong>nueva contraseña</strong> es: <span style="background-color: #FFFF00; padding: 5px; border-radius: 3px;">{new_password}</span></p>
            <p>Le recomendamos que cambie esta contraseña temporal por una personalizada tan pronto como inicie sesión.</p>
            <p>Gracias por ser parte de NoteFlow y no dude en contactarnos si necesita ayuda.</p>
            <p>Atentamente,<br>El equipo de NoteFlow</p>
            <img src="cid:{logo_cid}" alt="Logo" style="max-width: 300px;">
        </body>
        </html>
        """

        em = EmailMessage()
        em.add_alternative(body, subtype='html')
        em["From"] = email_sender
        em["To"] = email_recipient
        em["Subject"] = subject
        em.get_payload()[0].add_related(logo_content, 'image', 'png', cid=logo_cid)
        #em.get_payload()[0].add_related(logo_content2, 'image', 'png', cid=logo_cid2)
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, os.getenv("PASSWORD_API"))
            smtp.sendmail(email_sender, email_recipient, em.as_string())
    except Exception as e:
        messagebox.showerror(message="Hemos tenido un problema:\n\nNo se ha encontrado un correo asociado\ncon las cuentas de NoteFlow.", title="ʕ•́ᴥ•̀ʔっ") 
        
        
def EnviarCorreoBienvenida (to_email, user, password, name):
    try:
        load_dotenv()
        email_sender = "gruponoteflow@gmail.com"
        email_recipient = to_email
        logo_filename = "1.png"
        with open(logo_filename, 'rb') as logo_file:
            logo_content = logo_file.read()

        #logo_filename2 = "3.png"
        #with open(logo_filename2, 'rb') as logo_file2:
        #logo_content2 = logo_file2.read()
        logo_cid = f"logo@{logo_filename}"
        #logo_cid2 = f"logo@{logo_filename2}"
        subject = "Cuenta creada con exito"
        body = f"""\
        <html>
        <body style="font-family: Arial, sans-serif; padding: 20px;">
            <h2 style="color: #8c52ff;">¡Bienvenido a NoteFlow, {name}!</h2>
            <p>Te damos la bienvenida a nuestra comunidad.</p>
            <p>Tu cuenta ha sido creada exitosamente con los siguientes datos:</p>
            <ul>
                <li><strong>Nombre:</strong> {name}</li>
                <li><strong>Usuario:</strong> {user}</li>
                <li><strong>Contraseña:</strong> <span style="background-color: #FFFF00; padding: 5px; border-radius: 3px;">{password}</span></li>
            </ul>
            <p>Es importante que no compartas tu contraseña con nadie. Por parte nuestra tenemos un sistema de seguridad de datos para que estes tranquilo/a.</p>
            <p>Si tienes alguna pregunta o necesitas ayuda, no dudes en contactarnos.</p>
            <p>Gracias por unirte a NoteFlow.</p>
            <p>Atentamente,<br>El equipo de NoteFlow</p>
            <img src="cid:{logo_cid}" alt="Logo" style="max-width: 300px;">
        </body>
        </html>
        """

        em = EmailMessage()
        em.add_alternative(body, subtype='html')
        em["From"] = email_sender
        em["To"] = email_recipient
        em["Subject"] = subject
        em.get_payload()[0].add_related(logo_content, 'image', 'png', cid=logo_cid)
        #em.get_payload()[0].add_related(logo_content2, 'image', 'png', cid=logo_cid2)
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, os.getenv("PASSWORD_API"))
            smtp.sendmail(email_sender, email_recipient, em.as_string())
    except Exception as e:
        messagebox.showerror(message="No hemos podido enviar tus datos\ncomprueba tu dirrecion de correcto electronico.", title="ʕ•́ᴥ•̀ʔっ") 
        
        
def EnviarSoporte(Mensaje, usuario):
    try:
        load_dotenv()
        email_sender = "gruponoteflow@gmail.com"
        email_recipient ="gruponoteflow@gmail.com"
        subject = "Comentario soporte"
        body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; padding: 20px;">
            <h2 style="color: #8c52ff;">Fallo o problema - reportado</h2>
            <p>Estimado equipo de soporte,</p>
            <p>Se ha reportado el siguiente problema:</p>
            <p><span style="background-color: #FFFF00; padding: 5px; border-radius: 3px;">{Mensaje}</span></p>
            <p>Por favor, tomen las medidas necesarias para abordar este problema y brindar la mejor experiencia a los usuarios.</p>
            <p>Gracias por su atención.</p>
            <p>Atentamente,<br> {usuario} </p>
        </body>
        </html>
        """

        em = EmailMessage()
        em.add_alternative(body, subtype='html')
        em["From"] = email_sender
        em["To"] = email_recipient
        em["Subject"] = subject
        
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, os.getenv("PASSWORD_API"))
            smtp.sendmail(email_sender, email_recipient, em.as_string())
    except Exception as e:
        messagebox.showerror(message="Hemos tenido un fallo al enviar tu comentario.", title="NoteFlow") 