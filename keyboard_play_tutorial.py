import tkinter as tk
import os

global IMG_KEY_TUT_DIR, IMG_MAIN_DIR

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, 'img')
IMG_MAIN_DIR = os.path.join(IMG_DIR, 'main')
IMG_KEY_TUT_DIR = os.path.join(IMG_DIR, 'keyboardtutorial')


def keyboardGOTLead(self):

    # window

    keyboard_GOT_lead_window = tk.Toplevel()

    # global declarations

    global keyboard_GOT_lead_img

    # photoimages

    keyboard_GOT_lead_img = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'GOT_lead.gif'))

    # window configurations

    keyboard_GOT_lead_window.geometry('424x774+0+0')
    keyboard_GOT_lead_window.title('GOT Lead')

    # Tk widgets

    keyboard_GOT_lead_label = tk.Label(
        keyboard_GOT_lead_window, image=keyboard_GOT_lead_img)

    # packing and mainloop

    keyboard_GOT_lead_label.pack()
    keyboard_GOT_lead_window.mainloop()


def keyboardGOTChords(self):

    # window

    keyboard_GOT_chords_window = tk.Toplevel()

    # global declarations

    global keyboard_GOT_chords_img

    # photoimages
    keyboard_GOT_chords_img = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'GOT_chords.gif'))

    # window configurations

    keyboard_GOT_chords_window.geometry('503x408+0+0')
    keyboard_GOT_chords_window.title('GOT Chords')
    # Tk widgets
    keyboard_GOT_chords_label = tk.Label(
        keyboard_GOT_chords_window, height=1200, width=1600, image=keyboard_GOT_chords_img)
    # packing and mainloop
    keyboard_GOT_chords_label.pack()
    keyboard_GOT_chords_window.mainloop()


def keyboardTHHLead(self):

    # window

    keyboard_THH_lead_window = tk.Toplevel()

    # global

    global keyboard_THH_lead_img

    # photoimages

    keyboard_THH_lead_img = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'THH_lead.gif'))

    # window configurations

    keyboard_THH_lead_window.geometry('666x619+0+0')
    keyboard_THH_lead_window.title('Tum Hi Ho Lead')

    # Tk widgets

    keyboard_THH_lead_label = tk.Label(
        keyboard_THH_lead_window, height=1200, width=1600, image=keyboard_THH_lead_img)

    # packing and mainloop

    keyboard_THH_lead_label.pack()
    keyboard_THH_lead_window.mainloop()


def keyboardTHHChords(self):

    # window

    keyboard_THH_chords_window = tk.Toplevel()

    # global declarations

    global keyboard_THH_chords_img

    # photoimages

    keyboard_THH_chords_img = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'THH_chords.gif'))

    #  window configurations

    keyboard_THH_chords_window.geometry('1020x895+0+0')
    keyboard_THH_chords_window.title('THH Chords')

    # Tk widgets

    keyboard_THH_chords_label = tk.Label(
        keyboard_THH_chords_window, height=1200, width=1600, image=keyboard_THH_chords_img)

    # packing and mainloop

    keyboard_THH_chords_label.pack()
    keyboard_THH_chords_window.mainloop()


def keyboardSSLead(self):

    # window

    keyboard_SS_lead_window = tk.Toplevel()

    # global declarations

    global keyboard_SS_lead_img

    # photoimages

    keyboard_SS_lead_img = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'SS_lead.gif'))

    # window configurations

    keyboard_SS_lead_window.geometry('802x834+0+0')
    keyboard_SS_lead_window.title('Sun Sathiya Lead')

    # Tk widgets

    keyboard_SS_lead_label = tk.Label(
        keyboard_SS_lead_window, height=1200, width=1600, image=keyboard_SS_lead_img)

    # packing and mainloop

    keyboard_SS_lead_label.pack()
    keyboard_SS_lead_window.mainloop()


def keyboardSSChords(self):

    # window
    keyboard_SS_chords_window = tk.Toplevel()

    # global

    global keyboard_SS_chords_img

    # photoimages

    keyboard_SS_chords_img = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'SS_chords.gif'))

    # window configurations

    keyboard_SS_chords_window.geometry('776x660+0+0')
    keyboard_SS_chords_window.title('Sun Sathiya Chords')

    # Tk widgets

    keyboard_SS_chords_label = tk.Label(
        keyboard_SS_chords_window, height=1200, width=1600, image=keyboard_SS_chords_img)

    # packing and mainloop

    keyboard_SS_chords_label.pack()
    keyboard_SS_chords_window.mainloop()


def keyboardDemLead(self):

    # window

    keyboard_dem_lead_window = tk.Toplevel()

    # global declarations

    global keyboard_dem_lead_img

    # photoimages

    keyboard_dem_lead_img = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'dem_lead.gif'))

    # window configurations

    keyboard_dem_lead_window.geometry('558x726+0+0')
    keyboard_dem_lead_window.title('Demons Lead')

    # Tk widgets

    keyboard_dem_lead_label = tk.Label(
        keyboard_dem_lead_window, height=1200, width=1600, image=keyboard_dem_lead_img)

    # packing and mainloop

    keyboard_dem_lead_label.pack()
    keyboard_dem_lead_window.mainloop()


def keyboardDemChords(self):

    # window

    keyboard_dem_chords_window = tk.Toplevel()

    # global declarations

    global keyboard_dem_chords_img

    # photoimages

    keyboard_dem_chords_img = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'dem_chords.gif'))

    # window configurations

    keyboard_dem_chords_window.geometry('519x814+0+0')
    keyboard_dem_chords_window.title('GOT Lead')

    # Tk widgets

    keyboard_dem_chords_label = tk.Label(
        keyboard_dem_chords_window, height=1200, width=1600, image=keyboard_dem_chords_img)

    # packing and mainloop

    keyboard_dem_chords_label.pack()
    keyboard_dem_chords_window.mainloop()


def keyboardGalLead(self):

    # window

    keyboard_gal_lead_window = tk.Toplevel()

    # global declarations

    global keyboard_gal_lead_img

    # photoimages

    keyboard_gal_lead_img = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'gal_lead.gif'))

    # window configurations

    keyboard_gal_lead_window.geometry('1102x890+0+0')
    keyboard_gal_lead_window.title('Galliyan Lead')

    # Tk widgets

    keyboard_gal_lead_label = tk.Label(
        keyboard_gal_lead_window, height=1200, width=1600, image=keyboard_gal_lead_img)

    # packing and mainloop

    keyboard_gal_lead_label.pack()
    keyboard_gal_lead_window.mainloop()


def keyboardGalChords(self):

    # window

    keyboard_gal_chords_window = tk.Toplevel()

    # global

    global keyboard_gal_chords_img

    # photoimages

    keyboard_gal_chords_img = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'gal_chords.gif'))

    # window configurations

    keyboard_gal_chords_window.geometry('606x563+0+0')
    keyboard_gal_chords_window.title('Galliyan Chords')

    # Tk widgets

    keyboard_gal_chords_label = tk.Label(
        keyboard_gal_chords_window, height=1200, width=1600, image=keyboard_gal_chords_img)

    # packing and mainloop

    keyboard_gal_chords_label.pack()
    keyboard_gal_chords_window.mainloop()


def keyboardDesLead(self):

    # window

    keyboard_GOT_lead_window = tk.Toplevel()

    # global declarations

    global keyboard_GOT_lead_img

    # photoimages

    keyboard_GOT_lead_img = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'WDTA_lead.png'))

    # window configurations

    keyboard_GOT_lead_window.geometry('291x710+0+0')
    keyboard_GOT_lead_window.title('We dont tak anymore Lead')

    # Tk widgets

    keyboard_GOT_lead_label = tk.Label(
        keyboard_GOT_lead_window, height=1200, width=1600, image=keyboard_GOT_lead_img)

    # packing and mainloop

    keyboard_GOT_lead_label.pack()
    keyboard_GOT_lead_window.mainloop()


def keyboardDesChords(self):

    # window

    keyboard_GOT_lead_window = tk.Toplevel()

    # global

    global keyboard_GOT_lead_img

    # photoimages

    keyboard_GOT_lead_img = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'WDTA_chords.png'))

    # window configurations

    keyboard_GOT_lead_window.geometry('309x702+0+0')
    keyboard_GOT_lead_window.title('We dont talk anymore Chords')

    # Tk widgets

    keyboard_GOT_lead_label = tk.Label(
        keyboard_GOT_lead_window, height=1200, width=1600, image=keyboard_GOT_lead_img)

    # packing and mainloop

    keyboard_GOT_lead_label.pack()
    keyboard_GOT_lead_window.mainloop()


def keyboardStartPlayTutorial(self):

    # global declarations

    global keyboard_play_tutorial_window

    # window configurations

    keyboard_play_tutorial_window = tk.Toplevel()
    keyboard_play_tutorial_window.geometry("500x350+300+200")
    keyboard_play_tutorial_window.title("Keyboard Tutorial")
    tutorial_icon = tk.Image("photo", file=os.path.join(IMG_MAIN_DIR, 'tutorial_icon.gif'))
    keyboard_play_tutorial_window.wm_iconphoto(True, tutorial_icon)
    keyboard_play_tutorial_window.configure(background='#89ff4d')

    # Tk widgets

    keyboard_play_tutorial_frame = tk.Frame(
        keyboard_play_tutorial_window, background='#89ff4d')
    keyboard_easy_label = tk.Label(
        keyboard_play_tutorial_window, text='Easy', background='#89ff4d', font=('arial', 13))
    keyboard_intermediate_label = tk.Label(
        keyboard_play_tutorial_window, text='Intermediate', background='#89ff4d', font=('arial', 13))
    keyboard_difficult_label = tk.Label(
        keyboard_play_tutorial_window, text='Difficult', background='#89ff4d', font=('arial', 13))
    keyboard_THH_label = tk.Label(keyboard_play_tutorial_window,
                                  text='Tum Hi Ho', background='#89ff4d', font=('arial', 13))
    keyboard_GOT_label = tk.Label(keyboard_play_tutorial_window,
                                  text='GOT theme', background='#89ff4d', font=('arial', 13))
    keyboard_GOT_lead_button = tk.Button(
        keyboard_play_tutorial_window, text='Lead', background='#50c1bf')
    keyboard_GOT_chords_button = tk.Button(
        keyboard_play_tutorial_window, text='Chords', background='#7095e1')
    keyboard_THH_lead_button = tk.Button(
        keyboard_play_tutorial_window, text='Lead', background='#50c1bf')
    keyboard_THH_chords_button = tk.Button(
        keyboard_play_tutorial_window, text='Chords', background='#7095e1')
    keyboard_SS_label = tk.Label(keyboard_play_tutorial_window,
                                 text='Sun Sathiya', background='#89ff4d', font=('arial', 13))
    keyboard_dem_label = tk.Label(keyboard_play_tutorial_window,
                                  text='Demons', background='#89ff4d', font=('arial', 13))
    keyboard_SS_lead_button = tk.Button(
        keyboard_play_tutorial_window, text='Lead', background='#50c1bf')
    keyboard_SS_chords_button = tk.Button(
        keyboard_play_tutorial_window, text='Chords', background='#7095e1')
    keyboard_dem_lead_button = tk.Button(
        keyboard_play_tutorial_window, text='Lead', background='#50c1bf')
    keyboard_dem_chords_button = tk.Button(
        keyboard_play_tutorial_window, text='Chords', background='#7095e1')
    keyboard_gal_label = tk.Label(keyboard_play_tutorial_window,
                                  text='Galliyan', background='#89ff4d', font=('arial', 13))
    keyboard_des_label = tk.Label(keyboard_play_tutorial_window,
                                  text='We Dont\ntalk anymore', background='#89ff4d', font=('arial', 13))
    keyboard_gal_lead_button = tk.Button(
        keyboard_play_tutorial_window, text='Lead', background='#50c1bf')
    keyboard_gal_chords_button = tk.Button(
        keyboard_play_tutorial_window, text='Chords', background='#7095e1')
    keyboard_des_lead_button = tk.Button(
        keyboard_play_tutorial_window, text='Lead', background='#50c1bf')
    keyboard_des_chords_button = tk.Button(
        keyboard_play_tutorial_window, text='Chords', background='#7095e1')

    # place configurations

    keyboard_play_tutorial_frame.place_configure(relheight=1, relwidth=1, relx=0, rely=0)

    keyboard_easy_label.place_configure(relheight=0.1, relwidth=0.4, relx=0.3, rely=0.075)
    keyboard_intermediate_label.place_configure(relheight=0.1, relwidth=0.4, relx=0.3, rely=0.375)
    keyboard_difficult_label.place_configure(relheight=0.1, relwidth=0.4, relx=0.3, rely=0.675)

    keyboard_SS_label.place_configure(relheight=0.1, relwidth=0.3, relx=0.1, rely=0.45)
    keyboard_dem_label.place_configure(relheight=0.1, relwidth=0.3, relx=0.6, rely=0.45)
    keyboard_THH_label.place_configure(relheight=0.1, relwidth=0.3, relx=0.6, rely=0.15)
    keyboard_GOT_label.place_configure(relheight=0.1, relwidth=0.3, relx=0.1, rely=0.15)
    keyboard_GOT_lead_button.place_configure(relheight=0.1, relwidth=0.15, relx=0.1, rely=0.25)
    keyboard_GOT_chords_button.place_configure(relheight=0.1, relwidth=0.15, relx=0.25, rely=0.25)
    keyboard_THH_lead_button.place_configure(relheight=0.1, relwidth=0.15, relx=0.6, rely=0.25)
    keyboard_THH_chords_button.place_configure(relheight=0.1, relwidth=0.15, relx=0.75, rely=0.25)
    keyboard_SS_lead_button.place_configure(relheight=0.1, relwidth=0.15, relx=0.1, rely=0.55)
    keyboard_SS_chords_button.place_configure(relheight=0.1, relwidth=0.15, relx=0.25, rely=0.55)
    keyboard_dem_lead_button.place_configure(relheight=0.1, relwidth=0.15, relx=0.6, rely=0.55)
    keyboard_dem_chords_button.place_configure(relheight=0.1, relwidth=0.15, relx=0.75, rely=0.55)
    keyboard_gal_label.place_configure(relheight=0.1, relwidth=0.3, relx=0.1, rely=0.75)
    keyboard_des_label.place_configure(relheight=0.1, relwidth=0.3, relx=0.6, rely=0.75)
    keyboard_gal_lead_button.place_configure(relheight=0.1, relwidth=0.15, relx=0.1, rely=0.85)
    keyboard_gal_chords_button.place_configure(relheight=0.1, relwidth=0.15, relx=0.25, rely=0.85)
    keyboard_des_lead_button.place_configure(relheight=0.1, relwidth=0.15, relx=0.6, rely=0.85)
    keyboard_des_chords_button.place_configure(relheight=0.1, relwidth=0.15, relx=0.75, rely=0.85)

    # event bindings

    keyboard_GOT_lead_button.bind('<Button-1>', func=keyboardGOTLead)
    keyboard_GOT_chords_button.bind('<Button-1>', func=keyboardGOTChords)
    keyboard_THH_lead_button.bind('<Button-1>', func=keyboardTHHLead)
    keyboard_THH_chords_button.bind('<Button-1>', func=keyboardTHHChords)
    keyboard_SS_lead_button.bind('<Button-1>', func=keyboardSSLead)
    keyboard_SS_chords_button.bind('<Button-1>', func=keyboardSSChords)
    keyboard_dem_lead_button.bind('<Button-1>', func=keyboardDemLead)
    keyboard_dem_chords_button.bind('<Button-1>', func=keyboardDemChords)
    keyboard_gal_lead_button.bind('<Button-1>', func=keyboardGalLead)
    keyboard_gal_chords_button.bind('<Button-1>', func=keyboardGalChords)
    keyboard_des_lead_button.bind('<Button-1>', func=keyboardDesLead)
    keyboard_des_chords_button.bind('<Button-1>', func=keyboardDesChords)

    # mainloop

    keyboard_play_tutorial_window.mainloop()


# keyboardStartPlayTutorial()
