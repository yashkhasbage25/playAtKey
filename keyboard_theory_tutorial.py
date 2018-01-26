import tkinter as tk
import tkinter.scrolledtext as tkst
import os

# global declarations

global IMG_KEY_TUT_DIR, IMG_MAIN_DIR

# dirctory paths

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, 'img')
IMG_MAIN_DIR = os.path.join(IMG_DIR, 'main')
IMG_KEY_TUT_DIR = os.path.join(IMG_DIR, 'keyboardtutorial')

# button functions


def gettingStartedText(self):

    # global declarations

    global keyboard_img_2

    # photoimages

    keyboard_img_2 = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'piano_2.gif'))

    # Tk widgets

    text_frame = tk.Frame(keyboard_tutorial_window, borderwidth=5, relief='ridge')
    text_widget = tkst.ScrolledText(text_frame, font='arial 15', wrap='word')

    # place configurations

    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)

    # fit text

    text_widget.insert('current', """
    Getting Started


    What every person that’s thinking about learning a new instrument """
                       """should know is that instruments are no cake-walk. Every now and then """
                       """there will be someone who comes across as somewhat of a prodigy, but """
                       """most of us will have to be willing to put in work.


            """)
    text_widget.image_create('current', image=keyboard_img_2)
    text_widget.insert('current', """


    One of the first questions people wanting to learn the piano/keyboard """
                       """want to know is just how much time it takes to learn and master the """
                       """keyboard. Well, when it comes to mastery, the time it takes to become """
                       """“fluent” in keyboard is subjective. """
                       """Many people take years— some people sound as if they’ve been playing """
                       """for a decade within a few months’ time. How quickly you reach your """
                       """musical goals depends solely on you and how much time, practice and """
                       """effort you put into mastering your instrument. """
                       """We recommend that you practice for at least 30 minutes each day. This """
                       """is enough time to play scales, practice chords and do position changes. """
                       """You don’t have to allot hours to your keyboard each day but you do have """
                       """to stay consistent.


                       """)
    text_widget.tag_config('head', font='times 20 bold')
    text_widget.tag_add('head', '2.0', '2.20')


def learningNotesText(self):

    # global declarations

    global keyboard_img_3

    # photoimages

    keyboard_img_3 = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'piano_3.gif'))

    # Tk widgets

    text_frame = tk.Frame(keyboard_tutorial_window, borderwidth=5, relief='ridge')
    text_widget = tkst.ScrolledText(text_frame, wrap='word', font='arial 15')

    # place configurations

    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)
    text_widget.insert('current', """
      Learning Notes


    The white keys are whole notes. These notes do not """
                       """contain any accidentals— that is sharps or flats. The white keys represent 7 """
                       """natural notes. C, D, E, F, G, A and B. In that order.


            """)
    text_widget.image_create('current', image=keyboard_img_3)
    text_widget.insert('current', """


    These notes, in the sequence above, are actually the key of C. All of the notes: """
                       """C, D, E, F, G, A, B and C are the notes that comprise the key. Keys tell us which"""
                       """notes to play in any given song. Now you know that if a song is in the key of C"""
                       """you will only play the keys of your keyboard.


""")

    # fonts

    text_widget.tag_add('head', '2.0', '2.20')
    text_widget.tag_config('head', font='times 25 bold')


def whiteKeysText(self):

    # global declarations

    global keyboard_img_4

    # photoimages

    keyboard_img_4 = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'piano_4.gif'))

    # Tk widgets

    text_frame = tk.Frame(keyboard_tutorial_window, borderwidth=5, relief='ridge')
    text_widget = tkst.ScrolledText(text_frame, font='arial 15', wrap='word')

    # place configurations

    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)
    text_widget.insert('current', """
     White Keys


    The white keys are whole notes. These notes do not"""
                       """contain any accidentals— that is sharps or flats. The white keys"""
                       """represent 7 natural notes. C, D, E, F, G, A and B. In that order.


             """)
    text_widget.image_create('current', image=keyboard_img_4)
    text_widget.insert('current', """


    These notes, in the sequence above, are actually the key of C."""
                       """All of the notes: C, D, E, F, G, A, B and C are the notes that"""
                       """comprise the key. Keys tell us which notes to play in any given"""
                       """song. Now you know that if a song is in the key of C you will"""
                       """only play the keys of your keyboard.


""")
    text_widget.tag_add('head', '2.0', '2.20')
    text_widget.tag_config('head', font='times 20 bold')


def blackKeysText(self):

    # global declarations

    global keyboard_img_5

    # photoimages

    keyboard_img_5 = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'piano_4.gif'))

    # Tk widgets

    text_frame = tk.Frame(keyboard_tutorial_window, borderwidth=5, relief='ridge')
    text_widget = tkst.ScrolledText(text_frame, font='arial 15', wrap='word')

    # place configurations

    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)

    # insert text

    text_widget.insert('current', """
    Black Keys


    These keys are sharps and flats. The black keys can """
                       """be a bit complicated to explain since they aren’t always sharps. """
                       """Speaking of sharps and flats, there are two notes in western music """
                       """that do not have sharps/flats. Those notes are E and B, which is why """
                       """there is no black key separating them from the other keys. """
                       """The two black keys next to each other are C# and D#. In the sequence """
                       """of three black keys the notes are F#, G# and A#.


        """)
    text_widget.image_create('current', image=keyboard_img_5)
    text_widget.insert('current', """


    While you can avoid the black keys sometimes, don’t think that you can """
                       """learn to play chords without them. You will quickly learn that they are """
                       """very necessary in most chord voicings. """
                       """Just look at A major whose triad is A, C# and E or even D whose triad """
                       """is D, F# and A. Fortunately there are plenty of songs that you can learn """
                       """without jumping into chords using the black keys so much.""")

    # fonts

    text_widget.tag_add('head', '2.0', '2.20')
    text_widget.tag_config('head', font='times 25')


def firstScaleText(self):

    # global declarations

    global keyboard_img_6

    # photoimages

    keyboard_img_6 = tk.PhotoImage(file=os.path.join(
        IMG_KEY_TUT_DIR, 'piano_6.gif'), height=400, width=600)

    # Tk widgets

    text_frame = tk.Frame(keyboard_tutorial_window, borderwidth=5, relief='ridge')
    text_widget = tkst.ScrolledText(text_frame, wrap='word', font='arial 15')

    # place configurations

    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)

    # insert text

    text_widget.insert('current', """
    Your first scale


    Remember those white keys that I told you about earlier? """
                       """C, D, E, F, G, A, B and C? That is your first scale. The """
                       """C major scale. Simply by using this scale you can play """
                       """chords, a melody or even arpeggios.


    Using the key of C you can learn your first position which """
                       """is, you guessed it, C positon. Start with your right thumb """
                       """on middle C (this key is normally indicated on your keyboard), """
                       """place your index finger on D, middle finger on E, ring finger """
                       """on F and pinky on G.

           """)
    text_widget.image_create('current', image=keyboard_img_6)
    text_widget.insert('current', """


    If you’d like to play C position on your left hand, you will """
                       """play C2 with you pinky, D with your ring finger, E with your """
                       """middle finger, F with your index finger and G with your thumb. """
                       """Notice that the only finger playing the same note is the middle """
                       """finger. All of the other fingers play different notes. """
                       """Learning how to control your fingers and move around the """
                       """keyboard takes time. Don’t get discouraged! Practice moving """
                       """forward and backwards with this scale using the same notes. """
                       """Scales are vital to learning the keyboard because they allow """
                       """for you to “jam” or solo over chord voicings and other """
                       """instruments. This technique also helps familiarize you with """
                       """the notes on the keyboard and their various locations and octaves.


""")
    text_widget.tag_config('head', font='Times 20 bold')
    text_widget.tag_add('head', '2.0', '2.20')


def majorChordsText(self):

    # global

    global keyboard_img_7, keyboard_img_8, keyboard_img_9

    # photoimages

    keyboard_img_7 = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'piano_7.gif'))
    keyboard_img_8 = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'piano_8.gif'))
    keyboard_img_9 = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'piano_9.gif'))

    # Tk widget

    text_frame = tk.Frame(keyboard_tutorial_window, borderwidth=5, relief='ridge')
    text_widget = tkst.ScrolledText(text_frame, wrap='word', font='arial 15')

    # place configurations

    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)

    # insert text

    text_widget.insert('current', """
    Major Chords


     1. Understand what a chord is. A chord is three or more notes. """
                       """Complex chords may have many notes, but you need a minimum of three. """
                       """The chords discussed here will all be composed of """
                       """three notes: a root, a third and a fifth.


      """)
    text_widget.image_create('current', image=keyboard_img_7)
    text_widget.insert('current', """


    2. Find the root of the chord. Every major chord is """
                       """built on a note called the tonic, or root of the chord. """
                       """This is the note that the chord is named after and will """
                       """be the lowest note in the chord. """
                       """For a C major chord, C is the tonic. It will be the """
                       """bottom note of your chord. """
                       """You will play the tonic note with your thumb in your """
                       """right hand, or with your pinkie in your left hand.


       """)
    text_widget.insert('current', """


    3. Find the major third. The second note in a major chord """
                       """is the major third, which gives the chord its character. It will """
                       """be four semitones, or half-steps, above the root. It is called a """
                       """third because when you play a scale in that key, it will be the """
                       """third note that you hit. """
                       """

    For a C major chord, E is the third. It is four half steps above """
                       """C. You can count them on your piano (C#, D, D#, E). """
                       """You will play the third with your middle finger, regardless of """
                       """which hand you’re using. """
                       """Try playing the root and the third together, to get a sense of """
                       """how that interval is supposed to sound.

      """)
    text_widget.image_create('current', image=keyboard_img_8)
    text_widget.insert('current', """


    4. Find the fifth. The top note in a major chord is """
                       """called the fifth because if you play a scale it will be """
                       """the fifth note that you hit. It anchors the chord and makes """
                       """it complete. It is seven semi-tones above the root. """
                       """For a C major chord, G is the fifth. You can count the """
                       """seven semi-tones up from the root on your piano. """
                       """(C#, D, D#, E, F, F#, G.) """
                       """You play the fifth with your pinkie in your right """
                       """hand, or your thumb in your left.

     """)
    text_widget.insert('current', """


    5. Understand that there are at least two ways to """
                       """spell a chord. All notes can be written at least two """
                       """different ways, for example Eb and D# are the same """
                       """note. Therefore, an Eb major chord would sound the """
                       """same as D# major chord. """
                       """The notes Eb, G, Bb create an Eb chord. The notes D#, """
                       """F##, A# create a D# Major chord, which sounds """
                       """exactly like an Eb chord. """
                       """The two chords are called enharmonic equivalents because """
                       """they sound exactly the same but are written differently. """
                       """A few of the common enharmonic equivalents are noted below, """
                       """but otherwise the article presents only the most common """
                       """notation of a major chord.


     """)
    text_widget.image_create('current', image=keyboard_img_9)
    text_widget.insert('current', """


    6. Review proper hand position. In order to play a piece"""
                       """of piano music well, you need to consistently use """
                       """the correct hand position, even when you’re just """
                       """practicing chords. """
                       """Keep your fingers tall and curved, as if they are """
                       """diving into the keys. Use the natural curve of your """
                       """fingers. """
                       """Use the weight of your arms rather than the strength """
                       """of your fingers to push on the keys. """
                       """Play on the tips of your fingers, including if """
                       """possible the pinkie and thumb which tend to lie flat """
                       """if you’re not paying attention. """
                       """Keep your fingernails trimmed close so that you can """
                       """play using the tips of your fingers.


     """)

    # fonts
    text_widget.tag_add('head', '2.0', '2.20')
    text_widget.tag_config('head', font='times 20 bold')


def minorChordsText(self):

    # global declaeations

    global keyboard_img_10

    # photoimages

    keyboard_img_10 = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'piano_10.gif'))

    # Tk widgets

    text_frame = tk.Frame(keyboard_tutorial_window, borderwidth=5, relief='ridge')
    text_widget = tkst.ScrolledText(text_frame, wrap='word', font='arial 15')

    # place configurations

    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)

    # insert text

    text_widget.insert('current', """
    Minor Chords


    Piano and keyboard players need to know how to build """
                       """a minor chord. Like the major chord, a minor chord """
                       """is a triad comprised of a root note, a third interval, """
                       """and a fifth interval. Written as a chord symbol, minor """
                       """chords get the suffix m, or sometimes min. Songs in """
                       """minor keys give you lots of opportunities to play """
                       """minor chords.


          """)
    text_widget.image_create('current', image=keyboard_img_10)
    text_widget.insert('current', """


You can make a minor chord two different ways:

    Play the root note, and add the third and fifth notes """
                       """of the minor scale on top. For example, play A as the """
                       """root note, and add the third note (C) and fifth note """
                       """(E) of the A minor scale.

"""
                       """Play a major chord and lower the middle note, or third """
                       """interval, by one half step. For example, a C major chord """
                       """has the notes C-E-G. To play a C minor chord, lower """
                       """the E to E flat.


        """)

    # fonts

    text_widget.tag_config('head', font='times 20 bold')
    text_widget.tag_add('head', '2.0', '2.20')


def keyboardChordSheet(self):

    # window configurations

    keyboard_sheet_window = tk.Toplevel()
    keyboard_sheet_window.geometry('1200x960+0+0')
    keyboard_sheet_window.title('Chord Sheet')

    # global declarations

    global keyboard_sheet_img

    # photoimages

    keyboard_sheet_img = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'piano_12.gif'))

    # Tk widgets

    keyboard_sheet_Label = tk.Label(keyboard_sheet_window, image=keyboard_sheet_img)

    # packing and mainloop

    keyboard_sheet_Label.pack()
    keyboard_sheet_window.mainloop()


def keyboardTwoOctaveImg(self):

    # window configurations

    keyboard_two_octave_img_window = tk.Toplevel()
    keyboard_two_octave_img_window.geometry('1000x500+200+100')
    keyboard_two_octave_img_window.title('Two Octave Keyboard')

    # global declarations

    keyboard_two_octave_img = tk.PhotoImage(
        file=os.path.join(IMG_KEY_TUT_DIR, 'two_octave_keyboard.gif'))

    # Tk widgets

    keyboard_two_octave_img_label = tk.Label(
        keyboard_two_octave_img_window, image=keyboard_two_octave_img)

    # packings and mainloop

    keyboard_two_octave_img_label.pack()
    keyboard_two_octave_img_window.mainloop()


def keyboardThreeOctaveImg(self):

    # window configurations

    keyboard_three_octave_img_window = tk.Toplevel()
    keyboard_three_octave_img_window.geometry('1000x500+200+100')
    keyboard_three_octave_img_window.title('Three Octave Keyboard')

    # global declarations

    keyboard_three_octave_img = tk.PhotoImage(
        file=os.path.join(IMG_KEY_TUT_DIR, 'three_octave_keyboard.png'))

    # Tk widgets

    keyboard_three_octave_img_label = tk.Label(
        keyboard_three_octave_img_window, image=keyboard_three_octave_img)

    # packings and mainloop

    keyboard_three_octave_img_label.pack()
    keyboard_three_octave_img_window.mainloop()


def keyboardStartTheoryTutorial(self):

    # global declarations

    global keyboard_tutorial_window, text_frame, getting_started_button

    # window configurations

    keyboard_tutorial_window = tk.Toplevel()
    keyboard_tutorial_window.geometry("1000x750+200+100")
    keyboard_tutorial_window.title("Keyboard Tutorial")
    tutorial_icon = tk.Image("photo", file=os.path.join(IMG_MAIN_DIR, 'tutorial_icon.gif'))
    keyboard_tutorial_window.wm_iconphoto(True, tutorial_icon)

    # Tk widgets

    getting_started_button = tk.Button(
        keyboard_tutorial_window, text='Getting\nStarted', background='#62bd18', font=('arial', 13))
    learning_notes_button = tk.Button(keyboard_tutorial_window,
                                      text='Learning\nnotes', background='#8ddd00', font=('arial', 13))
    white_keys_button = tk.Button(keyboard_tutorial_window,
                                  text='White\nkeys', background='#a3ee3f', font=('arial', 13))
    black_keys_button = tk.Button(keyboard_tutorial_window,
                                  text='Black\nkeys', background='#ffbb00', font=('arial', 13))
    first_scale_button = tk.Button(keyboard_tutorial_window,
                                   text='Learning\nyour\nfirst\nscale', background='#ffce00', font=('arial', 13))
    major_chords_button = tk.Button(keyboard_tutorial_window,
                                    text='Major\nchords', background='#fafa3c', font=('arial', 13))
    minor_chords_button = tk.Button(keyboard_tutorial_window,
                                    text='Minor\nchords', background='#ff5300', font=('arial', 13))
    chord_sheet_button = tk.Button(keyboard_tutorial_window,
                                   text='Chord\nsheet', background='#ff7200', font=('arial', 13))
    two_octave_image_button = tk.Button(
        keyboard_tutorial_window, text='Two\nOctave\nKeyboard', background='#ffa715', font=('arial', 13))
    three_octave_image_button = tk.Button(
        keyboard_tutorial_window, text='Three\nOctave\nKeyboard', background='#d21034', font=('arial', 13))
    text_frame = tk.Frame(keyboard_tutorial_window, borderwidth=5,
                          relief='ridge', background='#fc3d31')
    text_widget = tkst.ScrolledText(text_frame, font="arial 15",
                                    wrap='word', height=35, width=80)

    # place configurations

    getting_started_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0)
    learning_notes_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0.1)
    white_keys_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0.2)
    black_keys_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0.3)
    first_scale_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0.4)
    major_chords_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0.5)
    minor_chords_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0.6)
    chord_sheet_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0.7)
    two_octave_image_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0.8)
    three_octave_image_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0.9)
    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)

    # photoimages

    keyboard_intro_image = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'piano_intro.gif'))
    keyboard_1 = tk.PhotoImage(file=os.path.join(IMG_KEY_TUT_DIR, 'piano_1.gif'))

    # insert text

    text_widget.insert('current', """       """)
    text_widget.image_create('current', image=keyboard_intro_image)
    text_widget.insert('current', """
Piano

    The piano is an acoustic, stringed musical instrument """
                       """invented in Italy by Bartolomeo Cristofori around the year 1700 (the exact year is"""
                       """uncertain), in which the strings are struck by hammers. It is played using a keyboard,"""
                       """which is a row of keys (small levers) that the performer presses down or strikes with """
                       """the fingers and thumbs of both hands to cause the hammers to strike the strings. The """
                       """word piano is a shortened form of pianoforte, the Italian term for the early 1700s """
                       """versions of the instrument, which in turn derives from gravicembalo col piano e """
                       """forte and fortepiano. The Italian musical terms piano and forte indicate 'soft' and """
                       """'loud' respectively, in this context referring to the variations in volume (i.e., """
                       """loudness) produced in response to a pianist's touch or pressure on the keys: the """
                       """greater the velocity of a key press, the greater the force of the hammer hitting the """
                       """strings, and the louder the sound of the note produced and the stronger the attack. """
                       """The first fortepianos in the 1700s had a quieter sound and smaller dynamic range.


           """)
    text_widget.image_create('current', image=keyboard_1)
    text_widget.insert('current', """


    An acoustic piano usually has a protective wooden case surrounding the soundboard """
                       """and metal strings, which are strung under great tension on a heavy metal frame. """
                       """Pressing one or more keys on the piano's keyboard causes a padded hammer (typically """
                       """padded with firm felt) to strike the strings. The hammer rebounds from the strings, """
                       """and the strings continue to vibrate at their resonant frequency. These vibrations """
                       """are transmitted through a bridge to a soundboard that amplifies by more efficiently """
                       """coupling the acoustic energy to the air. When the key is released, a damper stops """
                       """the strings' vibration, ending the sound. Notes can be sustained, even when the keys """
                       """are released by the fingers and thumbs, by the use of pedals at the base of the """
                       """instrument. The sustain pedal enables pianists to play musical passages that would """
                       """otherwise be impossible, such as sounding a 10-note chord in the lower register and """
                       """then, while this chord is being continued with the sustain pedal, shifting both hands """
                       """to the treble range to play a melody and arpeggios over the top of this sustained """
                       """chord. Unlike the pipe organ and harpsichord, two major keyboard instruments widely """
                       """used before the piano, the piano allows gradations of volume and tone according to """
                       """how forcefully a performer presses or strikes the keys.""")

    # event bindings

    getting_started_button.bind('<Button-1>', func=gettingStartedText)
    learning_notes_button.bind('<Button-1>', func=learningNotesText)
    white_keys_button.bind('<Button-1>', func=whiteKeysText)
    black_keys_button.bind('<Button-1>', func=blackKeysText)
    first_scale_button.bind('<Button-1>', func=firstScaleText)
    major_chords_button.bind('<Button-1>', func=majorChordsText)
    minor_chords_button.bind('<Button-1>', func=minorChordsText)
    chord_sheet_button.bind('<Button-1>', func=keyboardChordSheet)
    two_octave_image_button.bind('<Button-1>', func=keyboardTwoOctaveImg)
    three_octave_image_button.bind('<Button-1>', func=keyboardThreeOctaveImg)

    # fonts

    text_widget.tag_config('head', font=('times', 25, 'bold'))
    text_widget.tag_add('head', '1.0', '2.8')

    # mainloop

    keyboard_tutorial_window.mainloop()


# keyboardStartTheoryTutorial()
