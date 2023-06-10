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


r = sr.Recognizer()

pygame.mixer.init()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


class forgetPassword_page(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # self.geometry("1920x1080")
        self.geometry("1500x900")

        self.title("በድምጽ ላይ የተመሰረተ የኢሜይል መተግበሪያ")

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
            if 'email' in voice_data:
                voice_data = voice_data.replace('email', '')
                e.set(voice_data)
                pygame.mixer.music.load("birth_date2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)

                voice_data = record_audio()
                respond(voice_data)
            elif 'የልደት ቀን' in voice_data:
                voice_data = voice_data.replace('የልደት ቀን', '')
                b.set(voice_data)
                pygame.mixer.music.load("pas2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)

                voice_data = record_audio()
                respond(voice_data)
            elif 'የይለፍ ቃል' in voice_data:
                voice_data = voice_data.replace('የይለፍ ቃል', '')

                p.set(voice_data)
                pygame.mixer.music.load("confirmpassword2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)

                voice_data = record_audio()
                respond(voice_data)

        def threads():
            pygame.mixer.music.load("new_password2.wav")
            pygame.mixer.music.play(loops=0)
            time.sleep(4)
            pygame.mixer.music.load("email_adress2.wav")
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

        about_btn = ctk.CTkButton(frame1, text='ስለ እኛ', font=('Bold', 35),
                                  fg_color=("#2d2d2d", "#2d2d2d"),
                                  )
        about_btn.place(relx=0.5, rely=0.2)
        about_btn.bind('<Enter>', about_btn.configure(fg_color=("#2d2d2d", "#393939"))
                       )
        about_btn.bind('<Leave>', on_leave)

        contact_btn = ctk.CTkButton(frame1, text='አግኙን', font=('Bold', 35),
                                    fg_color=("#2d2d2d", "#2d2d2d")
                                    )
        contact_btn.place(relx=0.8, rely=0.2)
        contact_btn.bind('<Enter>', on_enter)
        contact_btn.bind('<Leave>', on_leave)

        frame = ctk.CTkFrame(master=self)
        frame.pack(pady=100, padx=100, fill='both', expand=True)

        label = ctk.CTkLabel(
            master=frame, text='አዲስ የይለፍ ቃል ለማዘጋጀት እባክዎን ኢሜልዎን እና የልደት ቀንዎን በትክክል ያስገቡ', font=('bold', 28))
        label.pack(pady=12, padx=10)

        e = ctk.StringVar()
        np = ctk.StringVar()
        b = ctk.StringVar()

        email_address = ctk.CTkEntry(
            master=frame, placeholder_text=" ኢሜይል", font=('Arial', 24), textvariable=e, width=400, height=50)
        email_address.pack(pady=12, padx=10)

        birth_date = ctk.CTkEntry(
            master=frame, placeholder_text="የልደት ቀን", font=('Arial', 24), textvariable=b, width=400, height=50)
        birth_date.pack(pady=12, padx=10)

        new_pass = ctk.CTkEntry(
            master=frame, placeholder_text="አዲስ የይለፍ ቃል", show="*", font=('Arial', 24), textvariable=np, width=400, height=50)
        new_pass.pack(pady=12, padx=10)

        button = ctk.CTkButton(master=frame,
                               text='እሺ', font=('bold', 24))
        button.pack(pady=12, padx=10)

        self.mainloop()


threading.Thread(target=forgetPassword_page).start()
