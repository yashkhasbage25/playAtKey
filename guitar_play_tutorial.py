import tkinter as tk
import os

# global declarations

global IMG_GTR_TUT_DIR, IMG_MAIN_DIR

# directory paths

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, 'img')
IMG_MAIN_DIR = os.path.join(IMG_DIR, 'main')
IMG_GTR_TUT_DIR = os.path.join(IMG_DIR, 'guitartutorial')


def guitarCloText(self):

    # global declarations

    global guitar_clo_img

    # photoimages

    guitar_clo_img = tk.PhotoImage(file=os.path.join(IMG_GTR_TUT_DIR, 'clo_chords.gif'))

    # window configurations

    guitar_clo_window = tk.Toplevel()
    guitar_clo_window.geometry('787x691+0+0')
    guitar_clo_window.title('Closer Chords')

    # Tk widgets

    guitar_clo_label = tk.Label(guitar_clo_window, image=guitar_clo_img)

    # packing and mainloop

    guitar_clo_label.pack()
    guitar_clo_window.mainloop()


def guitarBulText(self):

    # global declarations

    global guitar_bul_img

    # photoimages

    guitar_bul_img = tk.PhotoImage(file=os.path.join(IMG_GTR_TUT_DIR, 'bul_chords.gif'))

    # window configurations

    guitar_bul_window = tk.Toplevel()
    guitar_bul_window.geometry('1143x921+0+0')
    guitar_bul_window.title('Bulleya Chords')

    # Tk widgets

    guitar_bul_label = tk.Label(guitar_bul_window, image=guitar_bul_img)

    # packing and mainloop

    guitar_bul_label.pack()
    guitar_bul_window.mainloop()


def guitarIlaText(self):

    # global declarations

    global guitar_ila_img

    # photoimages

    guitar_ila_img = tk.PhotoImage(file=os.path.join(IMG_GTR_TUT_DIR, 'ila_chords.gif'))

    # window configurations

    guitar_ila_window = tk.Toplevel()
    guitar_ila_window.geometry('375x772+0+0')
    guitar_ila_window.title('Ilahi Chords')

    # Tk widgets

    guitar_ila_label = tk.Label(guitar_ila_window, image=guitar_ila_img)

    # packing and mainloop

    guitar_ila_label.pack()
    guitar_ila_window.mainloop()


def guitarKhaText(self):

    # global declarations

    global guitar_kha_img

    # photoimages

    guitar_kha_img = tk.PhotoImage(file=os.path.join(IMG_GTR_TUT_DIR, 'kha_chords.gif'))

    # window configurations

    guitar_kha_window = tk.Toplevel()
    guitar_kha_window.geometry('748x802+0+0')
    guitar_kha_window.title('Khamoshiyan Chords')

    # Tk widgets

    guitar_kha_label = tk.Label(guitar_kha_window, image=guitar_kha_img)

    # packing and mainloop

    guitar_kha_label.pack()
    guitar_kha_window.mainloop()


def guitarFadText(self):

    # global declarations

    global guitar_fad_img

    # photoimages

    guitar_fad_img = tk.PhotoImage(file=os.path.join(IMG_GTR_TUT_DIR, 'fad_chords.gif'))

    # window configurations

    guitar_fad_window = tk.Toplevel()
    guitar_fad_window.geometry('663x936+0+0')
    guitar_fad_window.title('Faded Chords')
    guitar_fad_label = tk.Label(guitar_fad_window, image=guitar_fad_img)
    guitar_fad_label.pack()
    guitar_fad_window.mainloop()


def guitarRaaText(self):

    # global declarations

    global guitar_raa_img

    # photoimages

    guitar_raa_img = tk.PhotoImage(file=os.path.join(IMG_GTR_TUT_DIR, 'raa_chords.gif'))

    # window configurations

    guitar_raa_window = tk.Toplevel()
    guitar_raa_window.geometry('802x703+0+0')
    guitar_raa_window.title('Raabta Chords')

    # Tk widgets

    guitar_raa_label = tk.Label(guitar_raa_window, image=guitar_raa_img)

    # packing and mainloop

    guitar_raa_label.pack()
    guitar_raa_window.mainloop()


def guitarSNSText(self):

    # global declarations

    global guitar_SNS_img

    # photoimages

    guitar_SNS_img = tk.PhotoImage(file=os.path.join(IMG_GTR_TUT_DIR, 'SNS_chords.gif'))

    # window configurations

    guitar_SNS_window = tk.Toplevel()
    guitar_SNS_window.geometry('805x773+0+0')
    guitar_SNS_window.title('Soch Na Sake Chords')

    # Tk widgets

    guitar_SNS_label = tk.Label(guitar_SNS_window, image=guitar_SNS_img)

    # packing and mainloop

    guitar_SNS_label.pack()
    guitar_SNS_window.mainloop()


def guitarSOUText(self):

    # global declarations

    global guitar_SOU_img

    # photoimages

    guitar_SOU_img = tk.PhotoImage(file=os.path.join(IMG_GTR_TUT_DIR, 'SOU_chords.gif'))

    # window configurations

    guitar_SOU_window = tk.Toplevel()
    guitar_SOU_window.geometry('784x814+0+0')
    guitar_SOU_window.title('Shape of You Chords')

    # Tk widgets

    guitar_SOU_label = tk.Label(guitar_SOU_window, image=guitar_SOU_img)

    # packing and mainloop

    guitar_SOU_label.pack()
    guitar_SOU_window.mainloop()


def guitarBolText(self):

    # global declarations

    global guitar_bol_img

    # photoimages

    guitar_bol_img = tk.PhotoImage(file=os.path.join(IMG_GTR_TUT_DIR, 'bol_chords.gif'))

    # window configurations

    guitar_bol_window = tk.Toplevel()
    guitar_bol_window.geometry('701x760+0+0')
    guitar_bol_window.title('Bol Do Na Zara Chords')

    # Tk widgets

    guitar_bol_label = tk.Label(guitar_bol_window, image=guitar_bol_img)

    # packing and mainloop

    guitar_bol_label.pack()
    guitar_bol_window.mainloop()


def guitarStartPlayTutorial(self):

    # global declarations

    global guitar_play_tutorial_window

    # window configurations
    guitar_play_tutorial_window = tk.Toplevel()
    guitar_play_tutorial_window.geometry('480x270+100+100')
    guitar_play_tutorial_window.title('Guitar Tutorial')
    tutorial_icon = tk.Image("photo", file=os.path.join(IMG_MAIN_DIR, 'tutorial_icon.gif'))
    guitar_play_tutorial_window.wm_iconphoto(True, tutorial_icon)
    guitar_play_tutorial_window.configure(background='#ffffff')

    # Tk widgets

    guitar_play_tutorial_frame = tk.Frame(
        guitar_play_tutorial_window, background='#ffffff')
    guitar_play_tutorial_frame.place_configure(relheight=1, relwidth=1, relx=0, rely=0)
    guitar_clo_button = tk.Button(guitar_play_tutorial_frame, text='Closer',
                                  background='#006884', font=('arial', 13))
    guitar_bul_button = tk.Button(guitar_play_tutorial_frame,
                                  text='Bulleya', background='#00909e', font=('arial', 13))
    guitar_ila_button = tk.Button(guitar_play_tutorial_frame, text='Ilahi',
                                  background='#89dbec', font=('arial', 13))
    guitar_kha_button = tk.Button(guitar_play_tutorial_frame,
                                  text='Khamoshiya', background='#fa9d00', font=('arial', 13))
    guitar_fad_button = tk.Button(guitar_play_tutorial_frame, text='Faded',
                                  background='#ffd09d', font=('arial', 13))
    guitar_raa_button = tk.Button(guitar_play_tutorial_frame, text='Raabta',
                                  background='#b00051', font=('arial', 13))
    guitar_SNS_button = tk.Button(guitar_play_tutorial_frame,
                                  text='Soch\nNa Sake', background='#f69370', font=('arial', 13))
    guitar_SOU_button = tk.Button(guitar_play_tutorial_frame,
                                  text='Shape\nOf You', background='#feab80', font=('arial', 13))
    guitar_bol_button = tk.Button(guitar_play_tutorial_frame,
                                  text='Bol Do\nNa Zara', background='#6e006c', font=('arial', 13))

    # place configurations

    guitar_clo_button.place_configure(relheight=0.3, relwidth=0.3, relx=0.025, rely=0.025)
    guitar_bul_button.place_configure(relheight=0.3, relwidth=0.3, relx=0.35, rely=0.025)
    guitar_ila_button.place_configure(relheight=0.3, relwidth=0.3, relx=0.675, rely=0.025)
    guitar_kha_button.place_configure(relheight=0.3, relwidth=0.3, relx=0.025, rely=0.35)
    guitar_fad_button.place_configure(relheight=0.3, relwidth=0.3, relx=0.35, rely=0.35)
    guitar_raa_button.place_configure(relheight=0.3, relwidth=0.3, relx=0.675, rely=0.35)
    guitar_SNS_button.place_configure(relheight=0.3, relwidth=0.3, relx=0.025, rely=0.675)
    guitar_SOU_button.place_configure(relheight=0.3, relwidth=0.3, relx=0.35, rely=0.675)
    guitar_bol_button.place_configure(relheight=0.3, relwidth=0.3, relx=0.675, rely=0.675)

    # event bindings

    guitar_clo_button.bind('<Button-1>', func=guitarCloText)
    guitar_bul_button.bind('<Button-1>', func=guitarBulText)
    guitar_ila_button.bind('<Button-1>', func=guitarIlaText)
    guitar_kha_button.bind('<Button-1>', func=guitarKhaText)
    guitar_fad_button.bind('<Button-1>', func=guitarFadText)
    guitar_raa_button.bind('<Button-1>', func=guitarRaaText)
    guitar_SNS_button.bind('<Button-1>', func=guitarSNSText)
    guitar_SOU_button.bind('<Button-1>', func=guitarSOUText)
    guitar_bol_button.bind('<Button-1>', func=guitarBolText)

    # mainloop

    guitar_play_tutorial_window.mainloop()


# guitarStartPlayTutorial()
