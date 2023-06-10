import customtkinter as ctk
import tkinter.messagebox as tkmb
from PIL import Image, ImageTk
import speech_recognition as sr
import time
import threading
import pygame
import pymysql
from email.message import EmailMessage
import ssl
import smtplib


r = sr.Recognizer()

pygame.mixer.init()


class compose_email(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.geometry("1920x1080")
        # self.geometry("1500x900")

        self.title("በድምጽ ላይ የተመሰረተ የኢሜይል መተግበሪያ")

        # def clear():

        def connect_emailserver():
            em = EmailMessage()
            email_sender = 'forvemailtest@gmail.com'
            email_pass = 'xeigxqppkyxfmjzp'
            s.set(email_sender)
            receiverr = receiver.get()
            subject = emailsubject.get()
            message = emailbody.get()

            em['From'] = email_sender
            em['To'] = receiverr
            em['Subject'] = subject
            em.set_content(message)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_pass)
                smtp.sendmail(email_sender, receiverr, em.as_string())

        def record_audio(ask=False, location=False):
            with sr.Microphone() as source:
                audio = r.listen(source, timeout=5, phrase_time_limit=7)
                voice_data = ''
                try:
                    voice_data = r.recognize_google(
                        audio, language='am-ET,en-US')
                    print(voice_data)
                except sr.UnknownValueError:

                    pygame.mixer.music.load("soryididnotget2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(4)

                    pygame.mixer.music.load("speak2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio()
                    respond(voice_data)

                except sr.RequestError:

                    pygame.mixer.music.load("spechservicedown2.wav")
                    pygame.mixer.music.play(loops=0)
                    exit()
                return voice_data

        def respond(voice_data):

            if 'ለ' in voice_data:
                email_list = {
                    'liya': 'liya@gmail.com',
                    'ገነት': 'etsubsole18@gmail.com'
                }
                voice_data = voice_data.replace('ለ', '')
                voice_data = voice_data.replace(' ', '')
                rec = email_list[voice_data]
                re.set(rec)

                time.sleep(4)
                pygame.mixer.music.load("subject2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)

                voice_data = record_audio()
                respond(voice_data)
            elif 'ርዕሰ ጉዳዩ ' in voice_data:
                voice_data = voice_data.replace('ርዕሰ ጉዳዩ', '')
                es.set(voice_data)
                time.sleep(4)
                pygame.mixer.music.load("bodyemail2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)
                voice_data = record_audio()
                respond(voice_data)
            elif 'ዝርዝር ጉዳዩ ' in voice_data:
                voice_data = voice_data.replace('ዝርዝር ጉዳዩ', '')
                eb.set(voice_data)
                time.sleep(4)
                pygame.mixer.music.load("sendemail2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)
                voice_data = record_audio()
                respond(voice_data)
            elif 'ይላክ' in voice_data:
                # tkmb.showinfo('Success', 'successfully send')
                connect_emailserver()
            else:
                pygame.mixer.music.load("soryididnotget2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(4)

                pygame.mixer.music.load("speak2.wav")

                pygame.mixer.music.play(loops=0)
                time.sleep(3)

                voice_data = record_audio()
                respond(voice_data)

        def threads():
            pygame.mixer.music.load("compose2.wav")
            pygame.mixer.music.play(loops=0)
            time.sleep(7)
            pygame.mixer.music.load("reciver2.wav")
            pygame.mixer.music.play(loops=0)
            time.sleep(3)
            voice_data = record_audio()
            respond(voice_data)
        threading.Thread(target=threads).start()
        frame1 = ctk.CTkFrame(master=self,
                              corner_radius=5,
                              height=120)
        frame1.pack(pady=30, padx=10, fill='both')

        load = Image.open("images/amharic1.png")
        img_resized = load.resize((100, 100))  # new width & height

        photo = ImageTk.PhotoImage(img_resized)
        label = ctk.CTkLabel(master=frame1, text="", image=photo)
        label.image = photo
        label.place(x=10, y=10)

        def on_enter(e):
            # about_btn.configure(fg_color=("#2d2d2d", "#393939"))
            contact_btn.configure(fg_color=("#2d2d2d", "#393939"))

        def on_leave(e):
            about_btn.configure(fg_color=("#2d2d2d", "#2d2d2d"))
            contact_btn.configure(fg_color=("#2d2d2d", "#2d2d2d"))
            manual_btn.configure(fg_color=("#2d2d2d", "#2d2d2d"))

        about_btn = ctk.CTkButton(frame1, text='ስለ እኛ', font=('Bold', 35),
                                  fg_color=("#2d2d2d", "#2d2d2d"),
                                  )
        about_btn.place(relx=0.2, rely=0.2)
        """about_btn.bind('<Enter>', about_btn.configure(fg_color=("#2d2d2d", "#393939"))
                       )
        about_btn.bind('<Leave>', on_leave)
"""
        manual_btn = ctk.CTkButton(frame1, text='መመሪያ', font=('Bold', 35),
                                   fg_color=("#2d2d2d", "#2d2d2d"),
                                   )
        manual_btn.place(relx=0.5, rely=0.2)
        """manual_btn.bind('<Enter>', manual_btn.configure(fg_color=("#2d2d2d", "#393939"))
                        )
        manual_btn.bind('<Leave>', on_leave)"""

        contact_btn = ctk.CTkButton(frame1, text='አግኙን', font=('Bold', 35),
                                    fg_color=("#2d2d2d", "#2d2d2d")
                                    )
        contact_btn.place(relx=0.8, rely=0.2)
        """contact_btn.bind('<Enter>', on_enter)
        contact_btn.bind('<Leave>', on_leave)"""
        a = ctk.StringVar()

        """account = ctk.CTkEntry(
            master=frame1, fg_color=("#2d2d2d", "#2d2d2d"), font=('Arial ', 24), textvariable=a,  width=40, height=40)
        account.pack(pady=12, padx=10)"""

        frame = ctk.CTkFrame(master=self)
        frame.pack(pady=80, padx=500, fill='both', expand=True)

        label = ctk.CTkLabel(
            master=frame, text='ኢሜይል ማዘጋጀት', font=('bold', 28))
        label.pack(pady=12, padx=10)
        s = ctk.StringVar()
        re = ctk.StringVar()
        es = ctk.StringVar()
        eb = ctk.StringVar()

        label = ctk.CTkLabel(
            master=frame, text='ከ', font=('Arial', 24))
        label.pack()

        sender = ctk.CTkEntry(
            master=frame, placeholder_text="ከ", font=('Arial ', 24), textvariable=s,  width=800, height=40)
        sender.pack(pady=12, padx=10)

        label = ctk.CTkLabel(
            master=frame, text='ለ', font=('Arial', 24))
        label.pack()

        receiver = ctk.CTkEntry(
            master=frame, placeholder_text=" ለ",  font=('Arial', 24), textvariable=re,  width=800, height=40)
        receiver.pack(pady=12, padx=10)

        label = ctk.CTkLabel(
            master=frame, text='ርዕሰ ጉዳይ', font=('Arial', 24))
        label.pack()

        emailsubject = ctk.CTkEntry(
            master=frame, placeholder_text="ርዕሰ ጉዳይ", font=('Arial', 24), textvariable=es, width=800, height=40)
        emailsubject.pack(pady=12, padx=10)

        label = ctk.CTkLabel(
            master=frame, text='ዝርዝር ጉዳይ', font=('Arial', 24))
        label.pack()
        emailbody = ctk.CTkEntry(
            master=frame, placeholder_text="ዝርዝር ጉዳይ", font=('Arial', 24), textvariable=eb, width=800, height=200)
        emailbody.pack(pady=12, padx=10)

        button = ctk.CTkButton(master=frame,
                               text='ይላክ', font=('bold', 24), command=connect_emailserver)
        button.pack(pady=12, padx=10)

        self.mainloop()


# compose_email()
threading.Thread(target=compose_email).start()
