import customtkinter as ctk
import tkinter.messagebox as tkmb
from PIL import Image, ImageTk
import speech_recognition as sr
import time
import threading
import pygame
import pymysql
# import login
from email.header import decode_header
import imaplib
import email

r = sr.Recognizer()

pygame.mixer.init()


class inbox_page(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.geometry("1920x1080")
        # self.geometry("1500x900")

        self.title("በድምጽ ላይ የተመሰረተ የኢሜይል መተግበሪያ")

        # def clear():
        def clear():
            user_entry.delete(0, ctk.END)
            email_address.delete(0, ctk.END)
            email_password.delete(0, ctk.END)
            user_pass.delete(0, ctk.END)
            confirm_pass.delete(0, ctk.END)
            birth_date.delete(0, ctk.END)

        def loginn():
            import login
            self.withdraw()
            login.run()

        def retrive_email():
            m = imaplib.IMAP4_SSL("imap.gmail.com", 993)
            m.login("forvemailtest@gmail.com", "etbijrjypdxlbdwv")
            status, messages = m.select('"[Gmail]/Sent Mail"')
            # number of top emails to fetch
            N = 5
            # total number of emails
            messages = int(messages[0])
            for i in range(messages, messages-N, -1):
                # fetch the email message by ID
                res, msg = m.fetch(str(i), "(RFC822)")
                for response in msg:
                    if isinstance(response, tuple):
                        # parse a bytes email into a message object
                        msg = email.message_from_bytes(response[1])
                        # decode the email subject
                        subject, encoding = decode_header(msg["Subject"])[0]
                        if isinstance(subject, bytes):
                            # if it's a bytes, decode to str
                            subject = subject.decode(encoding)

                        # decode email sender
                        From, encoding = decode_header(msg.get("From"))[0]
                        if isinstance(From, bytes):
                            From = From.decode(encoding)
                        print("Subject:", subject)
                        print("From:", From)
                    # u.set(email_message.get('From'))
                    return

            m.close()
            m.logout()

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
            if 'አንድ' in voice_data:
                voice_data = voice_data.replace('አንድ', '')
                u.set(voice_data)
                time.sleep(4)
                pygame.mixer.music.load("email_adress2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)

                voice_data = record_audio()
                respond(voice_data)
            elif 'ሁለት' in voice_data:
                voice_data = voice_data.replace('ሁለት', '')
                e.set(voice_data)
                pygame.mixer.music.load("2stepverificationcode2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)

                voice_data = record_audio()
                respond(voice_data)
            elif 'ሶሰት' in voice_data:
                voice_data = voice_data.replace('ሶሰት', '')
                ep.set(voice_data)
                pygame.mixer.music.load("pas2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)

                voice_data = record_audio()
                respond(voice_data)

            elif 'አራት' in voice_data:
                voice_data = voice_data.replace('አራት', '')

                p.set(voice_data)
                pygame.mixer.music.load("confirmpassword2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)

                voice_data = record_audio()
                respond(voice_data)
            elif 'አምስት' in voice_data:
                voice_data = voice_data.replace('አምስት', '')
                cp.set(voice_data)
                pygame.mixer.music.load("birth_date2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)

                voice_data = record_audio()
                respond(voice_data)
            elif 'የልደት ቀን' in voice_data:
                voice_data = voice_data.replace('የልደት ቀን', '')
                b.set(voice_data)
                pygame.mixer.music.load("signup2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)

                voice_data = record_audio()
                respond(voice_data)
            elif 'ወደ' in voice_data:
                connect_database()
                # button.invoke()

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
            pygame.mixer.music.load("inboxenkuan2.wav")
            pygame.mixer.music.play(loops=0)
            time.sleep(4)
            pygame.mixer.music.load("readrecent2.wav")
            pygame.mixer.music.play(loops=0)
            time.sleep(3)
            retrive_email()
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

        frame = ctk.CTkFrame(master=self)
        frame.pack(pady=80, padx=600, fill='both', expand=True)

        label = ctk.CTkLabel(
            master=frame, text='እንኳን ወደ የገቢ መልእክት ሳጥን ኢሜል ገፅ በደህና መጡ\n\n\n\n', font=('bold', 28))
        label.grid(row=0, column=0, columnspan=2)

        u = ctk.StringVar()
        e = ctk.StringVar()
        ep = ctk.StringVar()
        b = ctk.StringVar()

        label = ctk.CTkLabel(
            master=frame, text='ከ', font=('Arial', 24))
        label.grid(row=1, column=0)

        fromemail = ctk.CTkEntry(
            master=frame, placeholder_text="ከ", font=('Arial ', 24), textvariable=u,  width=300, height=200)
        fromemail.grid(row=2, column=0)

        fromemail = ctk.CTkEntry(
            master=frame, placeholder_text="ከ", font=('Arial ', 24), textvariable=ep,  width=300, height=200)
        fromemail.grid(row=3, column=0)

        label = ctk.CTkLabel(
            master=frame, text='ርዕሰ ጉዳይ', font=('Arial', 24))
        label.grid(row=1, column=1)

        subjectpart = ctk.CTkEntry(
            master=frame, placeholder_text=" ርዕሰ ጉዳይ",  font=('Arial', 24), textvariable=e,   width=300, height=200)
        subjectpart.grid(row=2, column=1)
        subjectpart = ctk.CTkEntry(
            master=frame, placeholder_text=" ርዕሰ ጉዳይ",  font=('Arial', 24), textvariable=b,   width=300, height=200)
        subjectpart.grid(row=3, column=1)

        self.mainloop()


threading.Thread(target=inbox_page).start()

# signup_page()
