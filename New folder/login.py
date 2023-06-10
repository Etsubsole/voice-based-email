import customtkinter as ctk
import tkinter.messagebox as tkmb
from PIL import Image, ImageTk
import speech_recognition as sr
import pyttsx3
import pyaudio
import wave
import time
import threading
import pygame
import pymysql
import tkinter as tk

r = sr.Recognizer()

pygame.mixer.init()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


class login_page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        # tk.set_appearance_mode("light")
        # tk.set_default_color_theme("blue")
        # self.geometry("1920x1080")
        # self.geometry("1500x900")
        # self.title("በድምጽ ላይ የተመሰረተ የኢሜይል መተግበሪያ")

        def clear():
            user_entry.delete(0, ctk.END)
            user_pass.delete(0, ctk.END)

        def signupp():
            import signup

        def forgate():
            import forgetPassword

        def login_user():
            if user_entry.get() == '' or user_pass.get() == '':
                pygame.mixer.music.load("allrequired2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(4)
                clear()
                pygame.mixer.music.load("forgate2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(5)
                pygame.mixer.music.load("un2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)
                voice_data = record_audio()
                respond(voice_data)
            else:
                try:
                    con = pymysql.connect(
                        host='localhost', user='root', password='root')
                    mycursor = con.cursor()
                except:
                    tkmb.showerror('Error', 'database connectivity issue')
                    return
                query = 'use userdata'
                mycursor.execute(query)
                query = 'select * from data where username=%s and password=%s'
                mycursor.execute(query, (user_entry.get(), user_pass.get()))
                row = mycursor.fetchone()
                if row == None:
                    pygame.mixer.music.load("invalid2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(4)
                    clear()
                    pygame.mixer.music.load("un2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(4)
                    time.sleep(3)
                    voice_data = record_audio()
                    respond(voice_data)
                else:

                    self.destroy()
                    # exit()
                    # tkmb.showerror('Error', 'something went wrong')
                    # import signup

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
                    # exit()
                return voice_data

        def respond(voice_data):
            if 'የተጠቃሚ ስም' in voice_data:
                voice_data = voice_data.replace('የተጠቃሚ ስም', '')
                u.set(voice_data)
                time.sleep(4)
                pygame.mixer.music.load("pas2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)

                voice_data = record_audio()
                respond(voice_data)
            elif 'የይለፍ ቃል' in voice_data:
                voice_data = voice_data.replace('የይለፍ ቃል', '')

                p.set(voice_data)
                pygame.mixer.music.load("login2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)

                voice_data = record_audio()
                respond(voice_data)
            elif 'ግባ' in voice_data:
                button.invoke()
            elif 'የይለፍ ቃሌን ረሳሁ' in voice_data:
                forgate()
            else:
                pygame.mixer.music.load("soryididnotget2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(4)

                pygame.mixer.music.load("speak2.wav")

                pygame.mixer.music.play(loops=0)
                time.sleep(3)

                voice_data = record_audio()

        def threads():
            pygame.mixer.music.load("enkuan2.wav")
            pygame.mixer.music.play(loops=0)
            time.sleep(4)
            pygame.mixer.music.load("un2.wav")
            pygame.mixer.music.play(loops=0)
            time.sleep(3)
            voice_data = record_audio()
            respond(voice_data)
        threading.Thread(target=threads).start()

        """frame1 = tk.CTkFrame(master=self,
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

        about_btn = ctk.CTkButton(frame1, text='ስለ እኛ', font=('Bold', 35),
                                  fg_color=("#2d2d2d", "#2d2d2d"), )
        about_btn.place(relx=0.5, rely=0.2)
        about_btn.bind('<Enter>', about_btn.configure(
            fg_color=("#2d2d2d", "#393939")))
        about_btn.bind('<Leave>', on_leave)

        contact_btn = ctk.CTkButton(frame1, text='አግኙን', font=('Bold', 35),
                                    fg_color=("#2d2d2d", "#2d2d2d"))
        contact_btn.place(relx=0.8, rely=0.2)
        contact_btn.bind('<Enter>', on_enter)
        contact_btn.bind('<Leave>', on_leave)"""

        frame = tk.Frame(master=self)
        frame.pack(pady=100, padx=100, fill='both', expand=True)

        label = tk.Label(
            master=frame, text='እንኳን ደህና መጡ ተጠቃሚያችን', font=('bold', 28))
        label.pack(pady=12, padx=10)

        u = ctk.StringVar()
        p = ctk.StringVar()

        user_entry = tk.Entry(
            master=frame, font=('Arial ', 24), textvariable=u, width=400, )
        user_entry.pack(pady=12, padx=10)

        user_pass = tk.Entry(
            master=frame, show="*", font=('Arial', 24), textvariable=p, width=400,)
        user_pass.pack(pady=12, padx=10)

        button = tk.Button(master=frame,
                           text='ግባ', command=login_user, font=('bold', 24))
        button.pack(pady=12, padx=10)

        label2 = tk.Label(
            master=frame, text='የይለፍ ቃል መርሳት?  አዲስ ተጠቃሚ?', )
        label2.pack(pady=12, padx=10)

        # self.mainloop()


# threading.Thread(target=login_page).start()
login_page()
# app.mainloop()


def s():
    import signup


# s()
