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
from email.header import decode_header
import imaplib
import email
import pyttsx3
import pyaudio
import wave
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import mimetypes
import webbrowser
import os
import re


r = sr.Recognizer()

pygame.mixer.init()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def record_audio(respond):

    with sr.Microphone() as source:

        audio = r.listen(source, timeout=5, phrase_time_limit=7)
        voice_data = ''
        try:
            voice_data = r.recognize_google(
                audio, language='am-ET,en-US')
            print(voice_data)
        except sr.UnknownValueError:

            pygame.mixer.music.load("sounds/soryididnotget2.wav")
            pygame.mixer.music.play(loops=0)
            time.sleep(4)

            pygame.mixer.music.load("sounds/speak2.wav")
            pygame.mixer.music.play(loops=0)
            time.sleep(3)

            voice_data = record_audio(respond)
            respond(voice_data)

        except sr.RequestError:

            pygame.mixer.music.load("sounds/spechservicedown2.wav")
            pygame.mixer.music.play(loops=0)
            exit()
        return voice_data


class main(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.geometry("1920x1080")
        # self.geometry("1500x900")

        self.title("በድምጽ ላይ የተመሰረተ የኢሜይል መተግበሪያ")
        """loadd = Image.open("images/8im.jpg")
        resizee = loadd.resize((1920, 1080))

        backGroundImage = ImageTk.PhotoImage(resizee)

        backGroundImageLabel = ctk.CTkLabel(
            self, text="", image=backGroundImage)

        backGroundImageLabel.image = backGroundImage

        backGroundImageLabel.place(x=0, y=0)"""

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
            contact_btn.configure(fg_color=("#2d2d2d", "#393939"))

        def on_leave(e):
            about_btn.configure(fg_color=("#2d2d2d", "#2d2d2d"))
            contact_btn.configure(fg_color=("#2d2d2d", "#2d2d2d"))
            manual_btn.configure(fg_color=("#2d2d2d", "#2d2d2d"))

        about_btn = ctk.CTkButton(frame1, text='ስለ እኛ', font=('Bold', 35),
                                  fg_color=("#2d2d2d", "#2d2d2d"),
                                  )
        about_btn.place(relx=0.2, rely=0.2)

        manual_btn = ctk.CTkButton(frame1, text='መመሪያ', font=('Bold', 35),
                                   fg_color=("#2d2d2d", "#2d2d2d"),
                                   )
        manual_btn.place(relx=0.5, rely=0.2)

        contact_btn = ctk.CTkButton(frame1, text='አግኙን', font=('Bold', 35),
                                    fg_color=("#2d2d2d", "#2d2d2d")
                                    )
        contact_btn.place(relx=0.8, rely=0.2)

        option_frame = ctk.CTkFrame(self)
        option_frame.pack(side=ctk.LEFT, padx=80)
        option_frame.pack_propagate(False)
        option_frame.configure(width=300, height=800)

        # def option():

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

        main_frame = ctk.CTkFrame(self, fg_color=("#c3c3c3", "#2d2d2d"))

        main_lable = ctk.CTkLabel(
            main_frame, text="ይህ በድምጽ ላይ የተመሰረተ የኢሜይል መተግበሪያ ነው", font=('Bold', 35))
        main_lable.pack(padx=10, pady=100)

        main_b1 = ctk.CTkButton(main_frame, text="መግባት", font=('Bold', 35),
                                fg_color=("#c3c3c3"), text_color='#158aff')
        main_b1.pack(pady=20)

        main_b2 = ctk.CTkButton(main_frame, text="መመዝገብ", font=('Bold', 35),
                                fg_color=("#c3c3c3"), text_color='#158aff')
        main_b2.pack(pady=20)

        main_frame.pack(anchor="center", padx=80)
        main_frame.pack_propagate(False)
        main_frame.configure(height=800, width=900)

        def delete_pages():
            for frame in main_frame.winfo_children():
                frame.destroy()

        def login():

            # option()
            show_frame(option_frame)

            def clear():
                user_entry.delete(0, ctk.END)
                user_pass.delete(0, ctk.END)

            def login_user():
                if user_entry.get() == '' or user_pass.get() == '':
                    pygame.mixer.music.load("sounds/allrequired2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(4)
                    clear()
                    pygame.mixer.music.load("sounds/forgate2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(8)
                    pygame.mixer.music.load("sounds/un2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)
                    voice_data = record_audio(respondlg)
                    respondlg(voice_data)

                else:
                    try:
                        con = pymysql.connect(
                            host='localhost', user='root', password='root')
                        mycursor = con.cursor()
                    except:
                        talk('database connectivity issue please try again')
                        clear()
                        pygame.mixer.music.load("sounds/un2.wav")
                        pygame.mixer.music.play(loops=0)
                        time.sleep(3)
                        voice_data = record_audio(respondlg)
                        respondlg(voice_data)

                        return
                    query = 'use userdata'
                    mycursor.execute(query)
                    query = 'select * from data where username=%s and password=%s'
                    mycursor.execute(
                        query, (user_entry.get(), user_pass.get()))
                    row = mycursor.fetchone()
                    if row == None:
                        pygame.mixer.music.load("sounds/invalid2.wav")
                        pygame.mixer.music.play(loops=0)
                        time.sleep(4)
                        clear()
                        pygame.mixer.music.load("sounds/forgate2.wav")
                        pygame.mixer.music.play(loops=0)
                        time.sleep(7)
                        pygame.mixer.music.load("sounds/tryagain2.wav")
                        pygame.mixer.music.play(loops=0)
                        time.sleep(3)
                        voice_data = record_audio(respondlg)
                        respondlg(voice_data)
                    if user_entry.get() and user_pass.get() == 'admin' or 'አድሚን':
                        ind(contactas_indicator, admin)

                    else:

                        ind(contactas_indicator, home)

            def respondlg(voice_data):
                if 'የተጠቃሚ ስም' in voice_data:
                    voice_data = voice_data.replace('የተጠቃሚ ስም', '')
                    u.set(voice_data)
                    time.sleep(4)
                    pygame.mixer.music.load("sounds/pas2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio(respondlg)
                    respondlg(voice_data)
                elif 'የይለፍ ቃል' in voice_data:
                    voice_data = voice_data.replace('የይለፍ ቃል', '')
                    p.set(voice_data)
                    pygame.mixer.music.load("sounds/login2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio(respondlg)
                    respondlg(voice_data)
                elif 'ግባ' in voice_data:
                    # button.invoke()
                    login_user()
                elif 'የይለፍ ቃሌን ረሳሁ' in voice_data:
                    ind(home_indicate, forget)
                elif 'አዲስ account መክፈት' or 'አዲስ አካውንት መክፈት' in voice_data:
                    ind(menu_indicator, signup)

                else:
                    pygame.mixer.music.load("sounds/soryididnotget2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(4)

                    pygame.mixer.music.load("sounds/speak2.wav")

                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio(respondlg)
                    respondlg(voice_data)

            def threads():
                pygame.mixer.music.load("sounds/enkuan2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(4)
                pygame.mixer.music.load("sounds/un2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)
                voice_data = record_audio(respondlg)
                respondlg(voice_data)

            threading.Thread(target=threads).start()

            login_frame = ctk.CTkFrame(master=main_frame)
            login_frame.pack(pady=100, padx=100, fill='both', expand=True)

            label = ctk.CTkLabel(
                master=login_frame, text='እንኳን ደህና መጡ ተጠቃሚያችን', font=('bold', 28))
            label.pack(pady=12, padx=10)

            u = ctk.StringVar()
            p = ctk.StringVar()
            """global userEmail
            userEmail = user_entry.get()"""
            user_entry = ctk.CTkEntry(
                master=login_frame, font=('Arial ', 24), textvariable=u, width=400, )
            user_entry.pack(pady=12, padx=10)

            user_pass = ctk.CTkEntry(
                master=login_frame, show="*", font=('Arial', 24), textvariable=p, width=400,)
            user_pass.pack(pady=12, padx=10)

            button = ctk.CTkButton(master=login_frame,
                                   text='ግባ', command=login_user, font=('bold', 24))
            button.pack(pady=12, padx=10)

            label2 = ctk.CTkLabel(
                master=login_frame, text='የይለፍ ቃል መርሳት?  አዲስ ተጠቃሚ?', )
            label2.pack(pady=12, padx=10)
            return

        def admin():
            show_frame(option_frame)

            def db():
                from tkinter import ttk

                try:
                    con = pymysql.connect(
                        host='localhost', user='root', password='root')
                    mycursor = con.cursor()
                except:
                    talk('database connectivity issue please try again')
                    clear()
                    pygame.mixer.music.load("sounds/un2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)
                    voice_data = record_audio(respondlg)
                    respondlg(voice_data)
                    return
                trv = ttk.Treeview(main_frame, selectmode='browse')
                trv.grid(row=1, column=1, padx=20, pady=20)

                # number of columns
                trv["columns"] = ("1", "2", "3", "4", "5", "6")

                # Defining heading
                trv['show'] = 'headings'

                # width of columns and alignment
                trv.column("1", width=30, anchor='c')
                trv.column("2", width=150, anchor='c')
                trv.column("3", width=150, anchor='c')
                trv.column("4", width=150, anchor='c')
                trv.column("5", width=150, anchor='c')
                trv.column("6", width=150, anchor='c')

               # Headings
                # respective columns
                trv.heading("1", text="id")
                trv.heading("2", text="username")
                trv.heading("3", text="email")
                trv.heading("4", text="epassword")
                trv.heading("5", text="password")
                trv.heading("6", text="birthdate")

                # getting data from MySQL student table
                r_set = mycursor.execute(
                    '''SELECT * from userdata.data LIMIT 0,10''')
                for dt in mycursor.fetchall():
                    trv.insert("", 'end', iid=dt[0], text=dt[0],
                               values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5]))
            db()

        def forget():
            show_frame(option_frame)

            def update_pass():
                if birth_date.get() == '' or new_pass.get() == '' or conf_pass.get() == '':
                    pygame.mixer.music.load("sounds/allrequired2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(4)
                    clear()
                    pygame.mixer.music.load("un2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)
                    voice_data = record_audio(respondsu)
                    respondsu(voice_data)
                elif new_pass.get() != conf_pass.get():
                    pygame.mixer.music.load("sounds/passworddoesnotmutch2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(4)
                    user_pass.delete(0, ctk.END)
                    confirm_pass.delete(0, ctk.END)
                    birth_date.delete(0, ctk.END)
                    pygame.mixer.music.load("sounds/pas2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(4)

                else:
                    try:
                        connection = mysql.connector.connect(host='localhost',
                                                             database='userdata',
                                                             user='root',
                                                             password='root')
                        cursor = connection.cursor()
                        query = 'select * from data where username=%s and birthdate=%s'
                        cursor.execute(
                            query, (user_entry.get(), birth_date.get()))
                        row = mycursor.fetchone()
                        if row == None:
                            pygame.mixer.music.load(
                                "sounds/invalidbirthdate2.wav")
                            pygame.mixer.music.play(loops=0)
                            time.sleep(4)
                            exit()
                        else:

                            ind(contactas_indicator, home)

                        sql_update_query = """Update data set password = %s where username = %s"""
                        cursor.execute(sql_update_query,
                                       (new_pass.get(), user_entry.get()))
                        connection.commit()
                        print("Record Updated successfully ")

                    except mysql.connector.Error as error:
                        print("Failed to update table record: {}".format(error))
                    finally:
                        if connection.is_connected():
                            connection.close()
                            print("MySQL connection is closed")

            def respondf(voice_data):
                if 'የተጠቃሚ ስም' in voice_data:
                    voice_data = voice_data.replace('የተጠቃሚ ስም', '')
                    u.set(voice_data)
                    pygame.mixer.music.load("sounds/birth_date2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio(respondf)
                    respondf(voice_data)
                elif 'የልደት ቀን' in voice_data:
                    voice_data = voice_data.replace('የልደት ቀን', '')
                    b.set(voice_data)
                    pygame.mixer.music.load("sounds/pas2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio(respondf)
                    respondf(voice_data)
                elif 'የይለፍ ቃል' in voice_data:
                    voice_data = voice_data.replace('የይለፍ ቃል', '')

                    np.set(voice_data)
                    pygame.mixer.music.load("sounds/confirmpassword2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio(respondf)
                    respondf(voice_data)
                elif 'ለማረጋገጥ' in voice_data:
                    voice_data = voice_data.replace('ለማረጋገጥ', '')
                    cp.set(voice_data)
                    pygame.mixer.music.load("sounds/changepass2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio(respondf)
                    respondf(voice_data)
                elif 'መቀየር' in voice_data:
                    update_pass()

                else:
                    pygame.mixer.music.load("sounds/soryididnotget2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(4)

                    pygame.mixer.music.load("sounds/speak2.wav")

                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio(respondsu)
                    respondsu(voice_data)

            def threads():
                pygame.mixer.music.load("sounds/new_password2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(4)
                pygame.mixer.music.load("un2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)
                voice_data = record_audio(respondf)
                respondf(voice_data)
            threading.Thread(target=threads).start()
            frame = ctk.CTkFrame(master=main_frame)
            # frame.pack(pady=100, padx=100, fill='both', expand=True)
            frame.pack(pady=90)

            label = ctk.CTkLabel(
                master=frame, text='አዲስ የይለፍ ቃል ለማዘጋጀት እባክዎን ኢሜልዎን እና የልደት ቀንዎን በትክክል ያስገቡ', font=('bold', 28))
            label.pack(pady=12, padx=10)
            u = ctk.StringVar()
            cp = ctk.StringVar()
            np = ctk.StringVar()
            b = ctk.StringVar()

            user_entry = ctk.CTkEntry(
                master=frame, placeholder_text="የተጠቃሚ ስም", font=('Arial', 24), textvariable=u, width=400, height=50)
            user_entry.pack(pady=12, padx=10)

            birth_date = ctk.CTkEntry(
                master=frame, placeholder_text="የልደት ቀን", font=('Arial', 24), textvariable=b, width=400, height=50)
            birth_date.pack(pady=12, padx=10)

            new_pass = ctk.CTkEntry(
                master=frame, placeholder_text="አዲስ የይለፍ ቃል", show="*", font=('Arial', 24), textvariable=np, width=400, height=50)
            new_pass.pack(pady=12, padx=10)
            conf_pass = ctk.CTkEntry(
                master=frame, placeholder_text="አዲስ የይለፍ ቃል ማረጋገጥ", show="*", font=('Arial', 24), textvariable=cp, width=400, height=50)
            conf_pass.pack(pady=12, padx=10)

            button = ctk.CTkButton(master=frame,
                                   text='መቀየር', font=('bold', 24))
            button.pack(pady=12, padx=10)

        def signup():
            show_frame(option_frame)

            def clear():
                user_entry.delete(0, ctk.END)
                email_address.delete(0, ctk.END)
                email_password.delete(0, ctk.END)
                user_pass.delete(0, ctk.END)
                confirm_pass.delete(0, ctk.END)
                birth_date.delete(0, ctk.END)

            def connect_database():

                # check(useremail)
                if user_entry.get() == '' or email_address.get() == '' or email_password.get() == '' or user_pass.get() == '' or confirm_pass.get() == '' or birth_date.get() == '':
                    pygame.mixer.music.load("sounds/allrequired2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(4)
                    clear()
                    pygame.mixer.music.load("un2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)
                    voice_data = record_audio(respondsu)
                    respondsu(voice_data)
                elif user_pass.get() != confirm_pass.get():
                    pygame.mixer.music.load("sounds/passworddoesnotmutch2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(4)
                    user_pass.delete(0, ctk.END)
                    confirm_pass.delete(0, ctk.END)
                    birth_date.delete(0, ctk.END)
                    pygame.mixer.music.load("sounds/pas2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(4)
                    voice_data = record_audio(respondsu)
                    respondsu(voice_data)
                elif not '@' in email_address.get():
                    talk("email not vaid please enter again")
                    clear()
                    pygame.mixer.music.load("sounds/un2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)
                    voice_data = record_audio(respondsu)
                    respondsu(voice_data)
                elif (bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{6,30})', user_pass.get())) == True) or (len(user_pass.get()) < 6):
                    talk("The password is weak")
                    user_pass.delete(0, ctk.END)
                    confirm_pass.delete(0, ctk.END)
                    birth_date.delete(0, ctk.END)
                    pygame.mixer.music.load("sounds/pas2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(4)
                    voice_data = record_audio(respondsu)
                    respondsu(voice_data)
                else:
                    try:
                        con = pymysql.connect(
                            host='localhost', user='root', password='root')
                        mycursor = con.cursor()
                    except:
                        talk('database connectivity issue please try again')
                        clear()
                        pygame.mixer.music.load("sounds/un2.wav")
                        pygame.mixer.music.play(loops=0)
                        time.sleep(3)
                        voice_data = record_audio(respondsu)
                        respondsu(voice_data)

                        return
                    try:

                        query = 'create database userdata'
                        mycursor.execute(query)
                        query = 'use userdata'
                        mycursor.execute(query)
                        query = 'create table data(id int auto_increment primary key not null,  username varchar(100),email varchar(50), epassword varchar(50), password varchar(50), birthdate varchar(100))'
                        mycursor.execute(query)
                    except:
                        mycursor.execute('use userdata')

                    query = 'select * from data where username= %s and email = %s '
                    mycursor.execute(
                        query, (user_entry.get(), email_address.get()))

                    row = mycursor.fetchone()
                    if row != None:
                        pygame.mixer.music.load("sounds/exist2.wav")
                        pygame.mixer.music.play(loops=0)
                        time.sleep(4)
                        pygame.mixer.music.load("sounds/existaccount2.wav")
                        pygame.mixer.music.play(loops=0)
                        time.sleep(4)
                        voice_data = record_audio()

                        if 'አዎ' in voice_data:
                            pygame.mixer.music.load("sounds/navtologin2.wav")
                            pygame.mixer.music.play(loops=0)
                            time.sleep(4)

                        # clear()

                    else:
                        query = 'insert into data(username,email,epassword,password,birthdate) values(%s,%s,%s,%s,%s)'
                        mycursor.execute(query, (user_entry.get(), email_address.get(
                        ), email_password.get(), user_pass.get(), birth_date.get()))
                        con.commit()
                        con.close()
                        ind(contactas_indicator, home)

            def respondsu(voice_data):
                if 'የተጠቃሚ ስም' in voice_data:
                    voice_data = voice_data.replace('የተጠቃሚ ስም', '')
                    u.set(voice_data)
                    time.sleep(4)
                    pygame.mixer.music.load("sounds/email_adress2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio(respondsu)
                    respondsu(voice_data)
                elif 'email' in voice_data:
                    voice_data = voice_data.replace('email', '')
                    e.set(voice_data)
                    pygame.mixer.music.load(
                        "sounds/2stepverificationcode2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio(respondsu)
                    respondsu(voice_data)
                elif 'code' in voice_data:
                    voice_data = voice_data.replace('code', '')
                    ep.set(voice_data)
                    pygame.mixer.music.load("sounds/pas2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio(respondsu)
                    respondsu(voice_data)

                elif 'የይለፍ ቃል' in voice_data:
                    voice_data = voice_data.replace('የይለፍ ቃል', '')

                    p.set(voice_data)
                    pygame.mixer.music.load("sounds/confirmpassword2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio(respondsu)
                    respondsu(voice_data)
                elif 'ለማረጋገጥ' in voice_data:
                    voice_data = voice_data.replace('ለማረጋገጥ', '')
                    cp.set(voice_data)
                    pygame.mixer.music.load("sounds/birth_date2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio(respondsu)
                    respondsu(voice_data)
                elif 'የልደት ቀን' in voice_data:
                    voice_data = voice_data.replace('የልደት ቀን', '')
                    b.set(voice_data)
                    pygame.mixer.music.load("sounds/signup2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio(respondsu)
                    respondsu(voice_data)
                elif 'ይመዝገቡ' in voice_data:
                    connect_database()
                    # button.invoke()

                else:
                    pygame.mixer.music.load("sounds/soryididnotget2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(4)

                    pygame.mixer.music.load("sounds/speak2.wav")

                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio(respondsu)
                    respondsu(voice_data)

            def threads():
                pygame.mixer.music.load("sounds/enkuansignup2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(4)
                pygame.mixer.music.load("sounds/un2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)
                voice_data = record_audio(respondsu)
                respondsu(voice_data)
            threading.Thread(target=threads).start()

            signup_frame = ctk.CTkFrame(master=main_frame)

            # signup_frame.pack(pady=100, padx=100, fill='both', expand=True)
            signup_frame.pack(pady=90)

            label = ctk.CTkLabel(
                master=signup_frame, text='በድምጽ ላይ የተመሰረተ ኢሜል መተግበሪያ እንኳን በደህና መጡ', font=('bold', 28))
            label.pack(pady=12, padx=10)

            u = ctk.StringVar()
            e = ctk.StringVar()
            ep = ctk.StringVar()
            p = ctk.StringVar()
            cp = ctk.StringVar()
            b = ctk.StringVar()

            label = ctk.CTkLabel(
                master=signup_frame, text='የተጠቃሚ ስም', font=('Arial', 24))
            label.pack()

            user_entry = ctk.CTkEntry(
                master=signup_frame, placeholder_text="የተጠቃሚ ስም", font=('Arial ', 24), textvariable=u,  width=400, height=40)
            user_entry.pack(pady=12, padx=10)

            label = ctk.CTkLabel(
                master=signup_frame, text='ኢሜይል', font=('Arial', 24))
            label.pack()

            email_address = ctk.CTkEntry(
                master=signup_frame, placeholder_text=" ኢሜይል",  font=('Arial', 24), textvariable=e,  width=400, height=40)
            email_address.pack(pady=12, padx=10)

            label = ctk.CTkLabel(
                master=signup_frame, text='የኢሜይል የይለፍ ቃል', font=('Arial', 24))
            label.pack()

            email_password = ctk.CTkEntry(
                master=signup_frame, placeholder_text="የኢሜይል የይለፍ ቃል", font=('Arial', 24), textvariable=ep, width=400, height=40)
            email_password.pack(pady=12, padx=10)

            label = ctk.CTkLabel(
                master=signup_frame, text='የይለፍ ቃል', font=('Arial', 24))
            label.pack()

            user_pass = ctk.CTkEntry(
                master=signup_frame, placeholder_text="የይለፍ ቃል", show="*", font=('Arial', 24), textvariable=p, width=400, height=40)
            user_pass.pack(pady=12, padx=10)

            label = ctk.CTkLabel(
                master=signup_frame, text='የይለፍ ቃል ለማረጋገጥ', font=('Arial', 24))
            label.pack()

            confirm_pass = ctk.CTkEntry(
                master=signup_frame, placeholder_text="የይለፍ ቃል ለማረጋገጥ", show="*", font=('Arial', 24), textvariable=cp, width=400, height=40)
            confirm_pass.pack(pady=12, padx=10)

            label = ctk.CTkLabel(
                master=signup_frame, text='የልደት ቀን', font=('Arial', 24))
            label.pack()

            birth_date = ctk.CTkEntry(
                master=signup_frame, placeholder_text="የልደት ቀን",  font=('Arial', 24), textvariable=b, width=400, height=40)
            birth_date.pack(pady=12, padx=10)

            button = ctk.CTkButton(master=signup_frame,
                                   text='ይመዝገብ', font=('bold', 24), command=connect_database)
            button.pack(pady=12, padx=10)

        def home():
            show_frame(option_frame)

            def respondhm(voice_data):
                if 'email ማዘጋጀት' in voice_data:
                    ind(contactas_indicator, compose)

                elif 'የግቢ መልእክት ሳጥን' in voice_data:
                    ind(contactas_indicator, inbox)

                elif 'delete' in voice_data:
                    ind(contactas_indicator, delete)

                else:
                    pygame.mixer.music.load("sounds/soryididnotget2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(4)

                    pygame.mixer.music.load("sounds/speak2.wav")

                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio(respondhm)
                    respondhm(voice_data)

            def threads():
                pygame.mixer.music.load("sounds/home2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(7)
                voice_data = record_audio(respondhm)
                respondhm(voice_data)
            threading.Thread(target=threads).start()

            home_frame = ctk.CTkFrame(master=main_frame)
            # home_frame.pack(pady=80, padx=600, fill='both', expand=True)
            home_frame.pack(pady=90)

            label = ctk.CTkLabel(
                master=home_frame, text='የመነሻ ገጽ ላይ ነዎት', font=('bold', 28))
            label.pack(pady=20, padx=15)

            compose_button = ctk.CTkButton(master=home_frame,
                                           text='ኢሜይል ማዘጋጀት', font=('bold', 24))
            compose_button.pack(pady=20, padx=15)

            inbox_button = ctk.CTkButton(master=home_frame,
                                         text='የግቢ መልእክት ሳጥን', font=('bold', 24))
            inbox_button.pack(pady=20, padx=15)

            delete_button = ctk.CTkButton(master=home_frame,
                                          text="ኢሜይል መሰርዝ", font=('bold', 24))
            delete_button.pack(pady=20, padx=15)

            search_button = ctk.CTkButton(master=home_frame,
                                          text='ኢሜይል መፈለግ', font=('bold', 24))
            search_button.pack(pady=20, padx=15)
            # ind(home_indicate)

        def compose():
            show_frame(option_frame)

            def audio(flage=False):

                # the file name output you want to record into
                filename = "recorded.wav"
                # set the chunk size of 1024 samples
                chunk = 1024
                # sample format
                FORMAT = pyaudio.paInt16
                # mono, change to 2 if you want stereo
                channels = 1
                # 44100 samples per second
                sample_rate = 44100
                record_seconds = 5
                # initialize PyAudio object
                p = pyaudio.PyAudio()
                # open stream object as input & output
                stream = p.open(format=FORMAT,
                                channels=channels,
                                rate=sample_rate,
                                input=True,
                                output=True,
                                frames_per_buffer=chunk)
                frames = []
                pygame.mixer.music.load("sounds/recording2.wav")
                pygame.mixer.music.play(loops=0)
                for i in range(int(sample_rate / chunk * record_seconds)):
                    data = stream.read(chunk)
                    # if you want to hear your voice while recording
                    # stream.write(data)
                    frames.append(data)
                pygame.mixer.music.load("sounds/finishrecording2.wav")
                pygame.mixer.music.play(loops=0)
                # stop and close stream
                stream.stop_stream()
                stream.close()
                # terminate pyaudio object
                p.terminate()
                # save audio file
                # open the file in 'write bytes' mode
                wf = wave.open(filename, "wb")
                # set the channels
                wf.setnchannels(channels)
                # set the sample format
                wf.setsampwidth(p.get_sample_size(FORMAT))
                # set the sample rate
                wf.setframerate(sample_rate)
                # write the frames as bytes
                wf.writeframes(b"".join(frames))
                # close the file
                wf.close()
                time.sleep(4)
                pygame.mixer.music.load("sounds/sendemail2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)
                """voice_data = record_audio(respondc)
                respondc(voice_data)
                
"""
                connect_emailserver(True)

            def connect_emailserver(flage=False):

                em = EmailMessage()
                email_sender = 'forvemailtest@gmail.com'
                # email_pass = 'xeigxqppkyxfmjzp'
                email_pass = 'yntjpvlskkblxxmh'

                s.set(email_sender)
                receiverr = receiver.get()
                subject = emailsubject.get()
                message = emailbody.get()

                em['From'] = email_sender
                em['To'] = receiverr
                em['Subject'] = subject
                em.set_content(message)

                context = ssl.create_default_context()
                if flage:

                    filename = "recorded.wav"

                    ctype, encoding = mimetypes.guess_type(filename)
                    maintype, subtype = ctype.split('/', 1)
                    with open(filename, 'rb') as fp:
                        em.add_attachment(fp.read(), maintype=maintype,
                                          subtype=subtype, filename=filename)

                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(email_sender, email_pass)
                    smtp.sendmail(email_sender, receiverr, em.as_string())

            def respondc(voice_data):

                if 'ለተቀባይ' in voice_data:
                    email_list = {
                        'liya': 'liya@gmail.com',
                        'ገነት': 'etsubsole18@gmail.com'
                    }
                    voice_data = voice_data.replace('ለ', '')
                    voice_data = voice_data.replace(' ', '')
                    if voice_data in email_list:
                        rec = email_list[voice_data]
                        re.set(rec)
                    else:
                        re.set(voice_data)

                    time.sleep(4)
                    pygame.mixer.music.load("sounds/subject2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio(respondc)
                    respondc(voice_data)
                elif 'ርዕሰ ጉዳዩ ' in voice_data:
                    voice_data = voice_data.replace('ርዕሰ ጉዳዩ', '')
                    es.set(voice_data)
                    time.sleep(4)
                    pygame.mixer.music.load("sounds/bodyemail2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)
                    voice_data = record_audio(respondc)
                    respondc(voice_data)
                elif 'ዝርዝር ጉዳዩ ' in voice_data:
                    voice_data = voice_data.replace('ዝርዝር ጉዳዩ', '')
                    eb.set(voice_data)
                    time.sleep(4)
                    pygame.mixer.music.load("sounds/douwantrecordvoice2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    def res(voice_data):
                        if "አዎ" in voice_data:
                            audio()
                        else:
                            time.sleep(4)
                            pygame.mixer.music.load("sounds/sendemail2.wav")
                            pygame.mixer.music.play(loops=0)
                            time.sleep(3)
                            voice_data = record_audio(respondc)
                            respondc(voice_data)

                    voice_data = record_audio(res)
                    res(voice_data)

                elif 'ይላክ' in voice_data:
                    connect_emailserver()
                else:
                    pygame.mixer.music.load("sounds/soryididnotget2.wav")
                    pygame.mixer.music.play(loops=0)
                    time.sleep(4)

                    pygame.mixer.music.load("sounds/speak2.wav")

                    pygame.mixer.music.play(loops=0)
                    time.sleep(3)

                    voice_data = record_audio(respondc)
                    respondc(voice_data)

            def threads():
                pygame.mixer.music.load("sounds/compose2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(7)
                pygame.mixer.music.load("sounds/reciver2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)
                voice_data = record_audio(respondc)
                respondc(voice_data)
            threading.Thread(target=threads).start()

            frame = ctk.CTkFrame(master=main_frame)
            # frame.pack(pady=80, padx=500, fill='both', expand=True)
            frame.pack(pady=90)

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

        def inbox():
            show_frame(option_frame)

            def clear():
                user_entry.delete(0, ctk.END)
                email_address.delete(0, ctk.END)
                email_password.delete(0, ctk.END)
                user_pass.delete(0, ctk.END)
                confirm_pass.delete(0, ctk.END)
                birth_date.delete(0, ctk.END)

            def retrive_email():
                m = imaplib.IMAP4_SSL("imap.gmail.com", 993)
                m.login("forvemailtest@gmail.com", "yntjpvlskkblxxmh")
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
                            subject, encoding = decode_header(
                                msg["Subject"])[0]
                            if isinstance(subject, bytes):
                                # if it's a bytes, decode to str
                                subject = subject.decode(encoding)
                            # decode email sender
                            From, encoding = decode_header(msg.get("From"))[0]
                            if isinstance(From, bytes):
                                From = From.decode(encoding)
                            talk(subject)
                            talk(From)
                            u.set(From)
                            b.set(subject)
                            # if the email message is multipart
                            if msg.is_multipart():
                                # iterate over email parts
                                for part in msg.walk():
                                    # extract content type of email
                                    content_type = part.get_content_type()
                                    content_disposition = str(
                                        part.get("Content-Disposition"))
                                    try:
                                        # get the email body
                                        body = part.get_payload(
                                            decode=True).decode()
                                    except:
                                        pass
                                    if content_type == "text/plain" and "attachment" not in content_disposition:
                                        # print text/plain emails and skip attachments
                                        talk(body)
                                    elif "attachment" in content_disposition:
                                        # download attachment
                                        filename = part.get_filename()
                                        if filename:
                                            folder_name = "files"
                                            if not os.path.isdir(folder_name):
                                                # make a folder for this email (named after the subject)
                                                os.mkdir(folder_name)
                                            filepath = os.path.join(
                                                folder_name, filename)
                                            # download attachment and save it
                                            open(filepath, "wb").write(
                                                part.get_payload(decode=True))
                                            pygame.mixer.music.load(
                                                "files/recorded.wav")
                                            pygame.mixer.music.play(loops=0)
                                            time.sleep(4)

                            else:
                                # extract content type of email
                                content_type = msg.get_content_type()
                                # get the email body
                                body = msg.get_payload(decode=True).decode()
                                if content_type == "text/plain":
                                    # print only text email parts
                                    talk(body)
                            if content_type == "text/html":
                                # if it's HTML, create a new HTML file and open it in browser
                                folder_name = clean(subject)
                                if not os.path.isdir(folder_name):
                                    # make a folder for this email (named after the subject)
                                    os.mkdir(folder_name)
                                filename = "index.html"
                                filepath = os.path.join(folder_name, filename)
                                # write the file
                                open(filepath, "w").write(body)
                                # open in the default browser
                                webbrowser.open(filepath)
                            talk("next email")
                # close the connection and logout

                m.close()
                m.logout()
                pygame.mixer.music.load(
                    "sounds/douwantcont2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)
                voice_data = record_audio(resp)
                resp(voice_data)

                def resp(voice_data):
                    if 'አዎ' in voice_data:
                        pygame.mixer.music.load(
                            "sounds/whichtoread2.wav")
                        pygame.mixer.music.play(loops=0)
                        time.sleep(3)

                    else:
                        ind(contactas_indicator, home)

            def threads():
                pygame.mixer.music.load("sounds/inboxenkuan2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(4)
                pygame.mixer.music.load("sounds/readrecent2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)
                retrive_email()
                """voice_data = record_audio(respondi)
                respondi(voice_data)"""
            threading.Thread(target=threads).start()
            frame = ctk.CTkFrame(master=main_frame)
            # frame.pack(pady=80, padx=600, fill='both', expand=True)
            frame.pack(pady=90)

            label = ctk.CTkLabel(
                master=frame, text='እንኳን ወደ የገቢ መልእክት ሳጥን ኢሜል ገፅ በደህና መጡ\n', font=('bold', 28))
            label.grid(row=0, column=0, columnspan=2, pady=20)

            u = ctk.StringVar()
            e = ctk.StringVar()
            ep = ctk.StringVar()
            b = ctk.StringVar()

            label1 = ctk.CTkLabel(
                master=frame, text='ከ', font=('Arial', 24))
            label1.grid(row=1, column=0, pady=10, padx=10)

            fromemail = ctk.CTkEntry(
                master=frame, placeholder_text="ከ", font=('Arial ', 24), textvariable=u,  width=300, height=50)
            fromemail.grid(row=2, column=0, pady=10)

            label2 = ctk.CTkLabel(
                master=frame, text='ርዕሰ ጉዳይ', font=('Arial', 24))
            label2.grid(row=3, column=0, pady=10)

            subjectpart = ctk.CTkEntry(
                master=frame, placeholder_text=" ርዕሰ ጉዳይ",  font=('Arial', 24), textvariable=b,  height=100, width=400)
            subjectpart.grid(row=4, column=0, pady=10)

            label3 = ctk.CTkLabel(
                master=frame, text='ርዕሰ ጉዳይ', font=('Arial', 24))
            label3.grid(row=5, column=0, pady=10)

            bodypart = ctk.CTkEntry(
                master=frame, placeholder_text=" ዝርዝር ጉዳይ",  font=('Arial', 24), textvariable=b,  height=100, width=400)
            bodypart.grid(row=6, column=0, pady=10)

        def delete():
            pass

        def search():
            pass

        def youtube():
            pass

        def wikipidia():
            pass

        def hide_indi():
            home_indicate.configure(bg_color="#c3c3c3")
            menu_indicator.configure(bg_color="#c3c3c3")
            contactas_indicator.configure(bg_color="#c3c3c3")
            about_indicator.configure(bg_color="#c3c3c3")

        def hide_frame(frame):
            frame.pack_forget()

        def show_frame(frame):
            frame.place(x=50, y=200)
           # frame.pack(anchor="w", padx=80)

        def ind(lb, page):  # (lb)
            hide_indi()
            lb.configure(bg_color="#158aff")
            delete_pages()

            page()
            """voice_data = record_audio()
            indicate(voice_data)"""
        hide_frame(option_frame)

        def indicate(voice_data):
            if "ለመግባት" or "" in voice_data:
                ind(home_indicate, login)
            elif "መመዝገብ" in voice_data:
                ind(menu_indicator, signup)
            elif "contact us" in voice_data:
                ind(contactas_indicator, home)
            elif "email ማዘጋጀት" in voice_data:
                ind(about_indicator, compose)
            elif "inbox" in voice_data:
                ind(about_indicator, inbox)
            elif "መርሳት" in voice_data:
                ind(about_indicator, forget)
            elif "admin" in voice_data:
                ind(about_indicator, admin)

            else:
                pygame.mixer.music.load("sounds/soryididnotget2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(4)

                pygame.mixer.music.load("sounds/speak2.wav")
                pygame.mixer.music.play(loops=0)
                time.sleep(3)

                voice_data = record_audio(indicate)
                indicate(voice_data)

        def threads():

            voice_data = record_audio(indicate)
            indicate(voice_data)

        threading.Thread(target=threads).start()

        more = ctk.CTkFrame(self)

        youtubee = ctk.CTkButton(more, text='youtube', font=('bold', 24))
        youtubee.pack(pady=20)

        wiki = ctk.CTkButton(more, text='wikipidia', font=('bold', 24))
        wiki.pack(pady=20)

        more.place(x=1500, y=200)
        more.pack_propagate(False)
        more.configure(width=300, height=800)

        self.mainloop()


main()
