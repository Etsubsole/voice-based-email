import customtkinter as ctk
import tkinter.messagebox as tkmb
from PIL import Image, ImageTk
import speech_recognition as sr
import time
import threading
import pygame


r = sr.Recognizer()

pygame.mixer.init()


class home_page(ctk.CTk):
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
                    exit()
                return voice_data

        def respond(voice_data):
            if 'የተጠቃሚ ስም' in voice_data:
                setText(voice_data)
                time.sleep(1)
                play_music3("pas2.wav")

            if 'exit' in voice_data:
                exit()

        def play_music(file):
            pygame.mixer.music.load(file)
            pygame.mixer.music.play(loops=0)
            time.sleep(3)

        def play_music2(file):
            pygame.mixer.music.load(file)
            pygame.mixer.music.play(loops=0)
            time.sleep(3)

        def play_music3(file):
            pygame.mixer.music.load(file)
            pygame.mixer.music.play(loops=0)
            # time.sleep(3)

        def threads():
            play_music("enkuan2.wav")
            play_music2("un2.wav")
            voice_data = record_audio()
            respond(voice_data)
        threading.Thread(target=threads).start()
        frame1 = ctk.CTkFrame(master=self,
                              corner_radius=5,
                              height=120)
        frame1.pack(pady=30, padx=10, fill='both')
        about_btn = ctk.CTkButton(frame1, text='ስለ እኛ', font=('Bold', 35),
                                  fg_color=("#2d2d2d", "#2d2d2d"),
                                  )
        about_btn.place(relx=0.5, rely=0.2)

        def on_enter(e):
            # about_btn.configure(fg_color=("#2d2d2d", "#393939"))
            contact_btn.configure(fg_color=("#2d2d2d", "#393939"))

        def on_leave(e):
            about_btn.configure(fg_color=("#2d2d2d", "#2d2d2d"))
            contact_btn.configure(fg_color=("#2d2d2d", "#2d2d2d"))

        about_btn.bind('<Enter>', about_btn.configure(fg_color=("#2d2d2d", "#393939"))
                       )
        about_btn.bind('<Leave>', on_leave)

        contact_btn = ctk.CTkButton(frame1, text='አግኙን', font=('Bold', 35),
                                    fg_color=("#2d2d2d", "#2d2d2d")
                                    )
        contact_btn.place(relx=0.8, rely=0.2)
        contact_btn.bind('<Enter>', contact_btn.configure(fg_color=("#2d2d2d", "#393939"))
                         )
        contact_btn.bind('<Leave>', on_leave)

        frame = ctk.CTkFrame(master=self)
        frame.pack(pady=100, padx=100, fill='both', expand=True)

        button = ctk.CTkButton(master=frame,
                               text='ግባ', font=('bold', 24), width=400, height=50)
        button.pack(pady=12, padx=10)

        self.mainloop()


threading.Thread(target=home_page).start()
