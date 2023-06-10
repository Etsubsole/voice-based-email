import customtkinter as ctk
import speech_recognition as sr
import pygame
import threading
import time


root = ctk.CTk()
root.geometry('500x400')
root.title('practice')
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

r = sr.Recognizer()
pygame.mixer.init()


def record_audio(ask=False, location=False):

    with sr.Microphone() as source:

        audio = r.listen(source, timeout=5, phrase_time_limit=7)
        voice_data = ''
        try:
            voice_data = r.recognize_google(
                audio, language='en-US')
            print(voice_data)
        except sr.UnknownValueError:

            pygame.mixer.music.load("sounds/soryididnotget2.wav")
            pygame.mixer.music.play(loops=0)
            time.sleep(4)

            pygame.mixer.music.load("sounds/speak2.wav")
            pygame.mixer.music.play(loops=0)
            time.sleep(3)

            voice_data = record_audio()
            indicate(voice_data)

        except sr.RequestError:

            pygame.mixer.music.load("sounds/spechservicedown2.wav")
            pygame.mixer.music.play(loops=0)
            exit()
        return voice_data


def home_page():
    home_frame = ctk.CTkFrame(main_frame)

    lb = ctk.CTkLabel(home_frame, text="laa home", font=('Bold', 24))
    lb.pack()

    home_frame.pack(pady=20)


def menu_page():
    menu_frame = ctk.CTkFrame(main_frame)

    lb = ctk.CTkLabel(menu_frame, text="laa menu", font=('Bold', 24))
    lb.pack()

    menu_frame.pack(pady=20)


def contactas_page():
    contact_frame = ctk.CTkFrame(main_frame)

    lb = ctk.CTkLabel(contact_frame, text="laa contact us", font=('Bold', 24))
    lb.pack()

    contact_frame.pack(pady=20)


def about_page():
    about_frame = ctk.CTkFrame(main_frame)

    lb = ctk.CTkLabel(about_frame, text="laa about", font=('Bold', 24))
    lb.pack()

    about_frame.pack(pady=20)


option_frame = ctk.CTkFrame(root)

home_btn = ctk.CTkButton(option_frame, text="Home", font=('Bold', 24),
                         fg_color=("#c3c3c3"), text_color='#158aff')
home_btn.place(x=10, y=50)

home_indicate = ctk.CTkLabel(
    option_frame, text='', bg_color='#c3c3c3', width=5, height=40)
home_indicate.place(x=3, y=50)

menu_btn = ctk.CTkButton(option_frame, text="menu", font=('Bold', 24),
                         fg_color=("#c3c3c3"), text_color='#158aff')
menu_btn.place(x=10, y=100)

menu_indicator = ctk.CTkLabel(
    option_frame, text='', bg_color='#c3c3c3', width=5, height=40)
menu_indicator.place(x=3, y=100)


contactas = ctk.CTkButton(option_frame, text="contact", font=('Bold', 24),
                          fg_color=("#c3c3c3"), text_color='#158aff')
contactas.place(x=10, y=150)

contactas_indicator = ctk.CTkLabel(
    option_frame, text='', bg_color='#c3c3c3', width=5, height=40)
contactas_indicator.place(x=3, y=150)

about_btn = ctk.CTkButton(option_frame, text="about", font=('Bold', 24),
                          fg_color=("#c3c3c3"), text_color='#158aff')
about_btn.place(x=10, y=200)

about_indicator = ctk.CTkLabel(
    option_frame, text='', bg_color='#c3c3c3', width=5, height=40)
about_indicator.place(x=3, y=200)


option_frame.pack(side=ctk.LEFT)
option_frame.pack_propagate(False)
option_frame.configure(width=150, height=400)

main_frame = ctk.CTkFrame(root, fg_color=("#c3c3c3", "#2d2d2d"))

main_frame.pack(side=ctk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400, width=500)


def hide_indi():
    home_indicate.configure(bg_color="#c3c3c3")
    menu_indicator.configure(bg_color="#c3c3c3")
    contactas_indicator.configure(bg_color="#c3c3c3")
    about_indicator.configure(bg_color="#c3c3c3")


def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()


def ind(lb, page):
    hide_indi()
    lb.configure(bg_color="#158aff")
    delete_pages()
    page()
    voice_data = record_audio()
    indicate(voice_data)


def indicate(voice_data):
    if "home" in voice_data:
        ind(home_indicate, home_page)
    elif "menu" in voice_data:
        ind(menu_indicator, menu_page)
    elif "contact us" in voice_data:
        ind(contactas_indicator, contactas_page)
    elif "about" in voice_data:
        ind(about_indicator, about_page)
    else:
        pygame.mixer.music.load("sounds/soryididnotget2.wav")
        pygame.mixer.music.play(loops=0)
        time.sleep(4)

        pygame.mixer.music.load("sounds/speak2.wav")
        pygame.mixer.music.play(loops=0)
        time.sleep(3)

        voice_data = record_audio()
        indicate(voice_data)


def threads():
    voice_data = record_audio()
    indicate(voice_data)


threading.Thread(target=threads).start()
root.mainloop()
