import tkinter as tk
import os

# global

global IMG_DRM_TUT_DIR, IMG_MAIN_DIR

# directory paths

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, 'img')
IMG_MAIN_DIR = os.path.join(IMG_DIR, 'main')
IMG_DRM_TUT_DIR = os.path.join(IMG_DIR, 'drumstutorial')

# button functions


def drumsBelieverSheet(self):

    # global declarations

    global believer_sheet_img

    # photoimages

    believer_sheet_img = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_23.gif'))

    # window configurations

    believer_sheet_window = tk.Toplevel()
    believer_sheet_window.geometry('900x403+0+0')
    believer_sheet_window.title('Sheet')

    # Tk widgets

    believer_sheet_Label = tk.Label(believer_sheet_window, image=believer_sheet_img)

    # packing and mainloop

    believer_sheet_Label.pack()
    believer_sheet_window.mainloop()


def drumsBOBDSheet(self):

    # global declarations

    global BOBD_sheet_img

    # photoimages

    BOBD_sheet_img = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_24.gif'))

    # window configurations

    BOBD_sheet_window = tk.Toplevel()
    BOBD_sheet_window.geometry('1541x854+0+0')
    BOBD_sheet_window.title('Chord Sheet')

    # Tk widgets

    BOBD_sheet_Label = tk.Label(BOBD_sheet_window, image=BOBD_sheet_img)

    # packing and mainloop

    BOBD_sheet_Label.pack()
    BOBD_sheet_window.mainloop()


def drumsIDSheet(self):

    # global declarations

    global ID_sheet_img

    # photoimages

    ID_sheet_img = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_25.gif'))

    # window configurations

    ID_sheet_window = tk.Toplevel()
    ID_sheet_window.geometry('1305x674+0+0')
    ID_sheet_window.title('Chord Sheet')

    # Tk widgets

    ID_sheet_Label = tk.Label(ID_sheet_window, image=ID_sheet_img)

    # packing and mainloop

    ID_sheet_Label.pack()
    ID_sheet_window.mainloop()


def drumsUFSheet(self):

    # global declarations

    global UF_sheet_img

    # photoimages

    UF_sheet_img = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_26.gif'))

    # window configurations

    UF_sheet_window = tk.Toplevel()
    UF_sheet_window.geometry('1460x863+0+0')
    UF_sheet_window.title('Chord Sheet')

    # Tk widgets

    UF_sheet_Label = tk.Label(UF_sheet_window, image=UF_sheet_img)

    # packing and mainloop

    UF_sheet_Label.pack()
    UF_sheet_window.mainloop()


def drumsShowSheet(self):

    # global declarations

    global drums_sheet_window

    # window configurations

    drums_sheet_window = tk.Toplevel()
    drums_sheet_window.geometry("400x300+300+200")
    drums_sheet_window.title("Keyboard Tutorial")
    tutorial_icon = tk.Image("photo", file=os.path.join(IMG_MAIN_DIR, 'tutorial_icon.gif'))
    drums_sheet_window.wm_iconphoto(True, tutorial_icon)

    # Tk widgets

    drums_sheet_frame = tk.Frame(drums_sheet_window, height=180, width=320, background='#8f16b2')
    drums_believer_button = tk.Button(
        drums_sheet_frame, text='Believer', bg='#f65314', font=('arial', 15))
    drums_BOBD_button = tk.Button(
        drums_sheet_frame, text='Boulevard of\nBroken Dreams', bg='#7cbb00', font=('arial', 15))
    drums_ID_button = tk.Button(drums_sheet_frame, text='Imagine Dragons',
                                bg='#00a1f1', font=('arial', 15))
    drums_UF_button = tk.Button(drums_sheet_frame, text='Uptown Funk',
                                bg='#ffbb00', font=('arial', 15))

    # place configurations

    drums_sheet_frame.place_configure(relheight=1, relwidth=1, relx=0, rely=0)
    drums_believer_button.place_configure(relheight=0.44, relwidth=0.44, relx=0.04, rely=0.04)
    drums_BOBD_button.place_configure(relheight=0.44, relwidth=0.44, relx=0.52, rely=0.04)
    drums_ID_button.place_configure(relheight=0.44, relwidth=0.44, relx=0.04, rely=0.52)
    drums_UF_button.place_configure(relheight=0.44, relwidth=0.44, relx=0.52, rely=0.52)

    # event bindings

    drums_believer_button.bind('<Button-1>', func=drumsBelieverSheet)
    drums_BOBD_button.bind('<Button-1>', func=drumsBOBDSheet)
    drums_ID_button.bind('<Button-1>', func=drumsIDSheet)
    drums_UF_button.bind('<Button-1>', func=drumsUFSheet)
    drums_sheet_window.mainloop()


# drumsShowSheet()
