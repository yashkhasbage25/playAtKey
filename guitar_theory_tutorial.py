import tkinter as tk
import tkinter.scrolledtext as tkst
import os

# global declarations

global IMG_GTR_TUT_DIR, IMG_MAIN_DIR

# directory paths

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, 'img')
IMG_MAIN_DIR = os.path.join(IMG_DIR, 'main')
IMG_GTR_TUT_DIR = os.path.join(IMG_DIR, 'guitartutorial')


def guitarChordsText(self):

    # global declarations

    global guitar_2, guitar_3

    # photoimages

    guitar_2 = tk.PhotoImage(file=os.path.join(IMG_GTR_TUT_DIR, 'guitar_2.gif'))
    guitar_3 = tk.PhotoImage(file=os.path.join(IMG_GTR_TUT_DIR, 'guitar_3.gif'))

    # Tk widgets

    text_frame = tk.Frame(guitar_tutorial_window, borderwidth=5, relief='ridge')
    text_widget = tkst.ScrolledText(text_frame, wrap='word', font='arial 15')

    # place configurations

    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)

    text_widget.insert('current', """
    Guitar chord



    In music, a guitar chord is a set of notes played on a guitar. """
                       """A chord's notes are often played simultaneously, but they can """
                       """be played sequentially in an arpeggio. The implementation of """
                       """guitar chords depends on the guitar tuning. Most guitars used """
                       """in popular music have six strings with the "standard" tuning of """
                       """the Spanish classical-guitar, namely E-A-D-G-B-E' (from the lowest """
                       """pitched string to the highest); in standard tuning, the intervals """
                       """present among adjacent strings are perfect fourths except for the """
                       """major third (G,B). Standard tuning requires four chord-shapes """
                       """for the major triads.





    There are separate chord-forms for chords having their root note on """
                       """the third, fourth, fifth, and sixth strings. For a six-string """
                       """guitar in standard tuning, it may be necessary to drop or omit """
                       """one or more tones from the chord; this is typically the root or """
                       """fifth. The layout of notes on the fretboard in standard tuning """
                       """often forces guitarists to permute the tonal order of notes in a chord.




    The playing of conventional chords is simplified by open tunings, """
                       """which are especially popular in folk, blues guitar and non-Spanish """
                       """classical guitar (such as English and Russian guitar). For example, """
                       """the typical twelve-bar blues uses only three chords, each of which """
                       """can be played (in every open tuning) by fretting six-strings with """
                       """one finger. Open tunings are used especially for steel guitar and """
                       """slide guitar. Open tunings allow one-finger chords to be played """
                       """with greater consonance than do other tunings, which use equal """
                       """temperament, at the cost of increasing the dissonance in other chords.\n\n\n\n\n""")
    text_widget.image_create('current', image=guitar_2)
    text_widget.insert('current', """




    The playing of (3-5 string) guitar chords is simplified by the class """
                       """of alternative tunings called regular tunings, in which the musical """
                       """intervals are the same for each pair of consecutive strings. Regular """
                       """tunings include major-thirds tuning, all-fourths, and all-fifths """
                       """tunings. For each regular tuning, chord patterns may be diagonally """
                       '""shifted down the fretboard, a property that simplifies beginners' """
    '"" learning of chords and that simplifies advanced players' """
                       """improvisation. On the other hand, in regular tunings 6-string """
                       """chords (in the keys of C, G, and D) are more difficult to play.


    Conventionally, guitarists double notes in a chord to increase its """
                       """volume, an important technique for players without amplification; """
                       """doubling notes and changing the order of notes also changes the """
                       """timbre of chords. It can make a possible a "chord" which is composed """
                       """of the all same note on different strings. Many chords can be played """
                       """with the same notes in more than one place on the fretboard.


    """)
    text_widget.image_create('current', image=guitar_3)

    # fonts

    text_widget.tag_config('head', font='times 20 bold')
    text_widget.tag_add('head', '2.0', '2.20')


def learnStrummingText(self):

    # global declarations

    global guitar_4, guitar_5

    # photoimages

    guitar_4 = tk.PhotoImage(file=os.path.join(IMG_GTR_TUT_DIR, 'guitar_4.gif'))
    guitar_5 = tk.PhotoImage(file=os.path.join(IMG_GTR_TUT_DIR, 'guitar_5.gif'))

    # Tk widgets

    text_frame = tk.Frame(guitar_tutorial_window, borderwidth=5, relief='ridge')
    text_widget = tkst.ScrolledText(text_frame, wrap='word', font='arial 15')

    # place configurations

    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)
    text_widget.insert('current', """
    Learn Strumming


A guitarist with a good grasp of strumming can bring a two-chord song to """
                       """life. In this first lesson on strumming, we'll examine some of the """
                       """basics of strumming the guitar, and learn a widely used strumming pattern.





Grab your guitar, and, using your fretting hand, form a G major chord """
                       """(review how to play a G major chord).




        """)
    text_widget.image_create('current', image=guitar_5)
    text_widget.insert('current', """






The pattern above is one bar long and contains 8 strums. It might look """
                       """confusing, so for now, pay attention to the arrows at the bottom. An """
                       """arrow pointing down indicates a downward strum. Similarly, an upwards """
                       """arrow indicates that you should strum upwards. Notice that the pattern """
                       """starts with a downstroke, and ends with an upstroke. So, if you were """
                       """to play the pattern twice in a row, your hand wouldn't have to vary """
                       """from its continual down-up motion.





    Play the pattern, taking special care to keep the time between """
                       """strums the same. After you play the example, repeat it without any """
                       """pause. Count out loud: 1 and 2 and 3 and 4 and 1 and 2 and (etc.) """
                       """Notice that on the "and" (referred to as the "offbeat") you are """
                       """always strumming upward. If you are having problems keeping a steady """

                       """"rhythm, try playing along with a mp3 of the strumming pattern.





    """)

    # fonts

    text_widget.tag_config('head', font='times 20 bold')
    text_widget.tag_add('head', '2.0', '2.20')


def moreStrummingText(self):

    # global declarations

    global guitar_6, guitar_7

    # photoimages

    guitar_6 = tk.PhotoImage(file=os.path.join(IMG_GTR_TUT_DIR, 'guitar_6.gif'))
    guitar_7 = tk.PhotoImage(file=os.path.join(IMG_GTR_TUT_DIR, 'guitar_7.gif'))

    # Tk widgets

    text_frame = tk.Frame(guitar_tutorial_window, borderwidth=5, relief='ridge')
    text_widget = tkst.ScrolledText(text_frame, wrap='word', font='arial 15')

    # place configurations

    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)

    # insert text

    text_widget.insert('current', """
    More On Strumming .....




    By removing only one strum from the previous pattern, we'll create one """
                       """of the most widely used strumming patterns in pop, country, and """
                       """rock music.





    When we remove the strum from this pattern, the initial instinct will """
                       """be to stop the strumming motion in your picking hand. This is """
                       """exactly what we don't want, as this alters the on-beat downstrum """
                       """/ off-beat upstrum pattern we've established.





    The key to this playing this strum successfully is to keep the """
                       """strumming motion going while slightly lifting the hand away from """
                       """the body of the guitar momentarily, on the downstroke of the third """
                       """beat, so the pick misses the strings. Then, on the next upstroke """
                       """(the "and" of the third beat), bring the hand closer to the guitar, """
                       """so the pick hits the strings. To summarize: the upward/downward """
                       """motion of the picking hand should not change from the first pattern. """
                       """Deliberately avoiding the strings with the pick on the third beat """
                       """of the pattern is the only change.





    """)
    text_widget.image_create('current', image=guitar_6)
    text_widget.insert('current', """





    Listen to, and play along with, this second strumming pattern, to """
                       """get a better idea on how this new pattern should sound. Once you are """
                       """comfortable with this, try it at a somewhat faster speed. It is """
                       """important to be able to play this accurately - don't be satisfied """
                       """with getting MOST of the up and down strums in the right order. If """
                       """it's not perfect, it will make learning any harder strums virtually """
                       """impossible. Be sure that you can play the pattern many times in a """
                       """row, without having to stop because of an incorrect strum.





    This is a tricky concept, and it can be guaranteed that you will have """
                       """some problems with it at first. The idea is, if you introduce basic """
                       """strumming patterns early, within a couple of lessons, you'll have """
                       """gotten the hang of it, and will be sounding great! It is important """
                       """to try not to get frustrated... soon, this will become second nature.






                """)
    text_widget.image_create('current', image=guitar_7)

    # fonts

    text_widget.tag_config('head', font='times 20 bold')
    text_widget.tag_add('head', '2.0', '3.0')


def guitarStartTheoryTutorial(self):

    # global declarations

    global guitar_tutorial_window, text_frame, getting_started_button

    # window configurations

    guitar_tutorial_window = tk.Toplevel()
    guitar_tutorial_window.geometry("1000x750+200+100")
    guitar_tutorial_window.title("Guitar Tutorial")
    guitar_tutorial_window.configure(background='#5416b4')
    tutorial_icon = tk.Image("photo", file=os.path.join(IMG_MAIN_DIR, 'tutorial_icon.gif'))
    guitar_tutorial_window.wm_iconphoto(True, tutorial_icon)

    # Tk widgets

    guitar_chords_button = tk.Button(
        guitar_tutorial_window, text='Guitar\nChords', font=('Arial', 13), background='#00b5ec')
    learn_strumming_button = tk.Button(
        guitar_tutorial_window, text='Learn\nStrumming', font=('Arial', 13), background='#ff6a00')
    more_strumming_button = tk.Button(
        guitar_tutorial_window, text='More\nStrumming...', font=('Arial', 13), background='#a442dc')
    text_frame = tk.Frame(guitar_tutorial_window, borderwidth=5,
                          relief='ridge', background='#ccff00')
    text_widget = tkst.ScrolledText(text_frame, font="arial 15", wrap='word')

    # place configurations

    guitar_chords_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0)
    learn_strumming_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0.1)
    more_strumming_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0.2)
    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)

    # photoimages

    guitar_intro_img = tk.PhotoImage(file=os.path.join(IMG_GTR_TUT_DIR, 'guitar_intro.gif'))
    guitar_1 = tk.PhotoImage(file=os.path.join(IMG_GTR_TUT_DIR, 'guitar_1.gif'))

    # Tk widgets

    text_widget.image_create('current', image=guitar_intro_img)
    text_widget.insert('current', """
    Guitar




    The guitar is a fretted musical instrument that usually has six strings. """
                       """The sound is projected either acoustically, using a hollow wooden or """
                       """plastic and wood box (for an acoustic guitar), or through electrical """
                       """amplifier and a speaker (for an electric guitar). It is typically played """
                       """by strumming or plucking the strings with the fingers, thumb or """
                       """fingernails of the right hand or with a pick while fretting (or pressing """
                       """against the frets) the strings with the fingers of the left hand. The """
                       """guitar is a type of chordophone, traditionally constructed from wood and """
                       """strung with either gut, nylon or steel strings and distinguished from """
                       """other chordophones by its construction and tuning. The modern guitar was """
                       """preceded by the gittern, the vihuela, the four-course Renaissance guitar, """
                       """and the five-course baroque guitar, all of which contributed to the """
                       """development of the modern six-string instrument.




    There are three main types of modern acoustic guitar: the classical """
                       """guitar (nylon-string guitar), the steel-string acoustic guitar, and """
                       """the archtop guitar, which is sometimes called a "jazz guitar". The """
                       """tone of an acoustic guitar is produced by the strings' vibration, """
                       """amplified by the hollow body of the guitar, which acts as a """
                       """resonating chamber. The classical guitar is often played as a solo """
                       """instrument using a comprehensive finger-picking technique where each """
                       """string is plucked individually by the player's fingers, as opposed to """
                       """being strummed. The term "finger-picking" can also refer to a """
                       """specific tradition of folk, blues, bluegrass, and country guitar """
                       """playing in the United States. The acoustic bass guitar is a """
                       """low-pitched instrument that is one octave below a regular guitar.


        """)
    text_widget.image_create('current', image=guitar_1)
    text_widget.insert('current', """



    The guitar is a fretted musical instrument that usually has six strings. """
                       """The sound is projected either acoustically, using a hollow wooden """
                       """or plastic and wood box (for an acoustic guitar), or through """
                       """electrical amplifier and a speaker (for an electric guitar). It is """
                       """typically played by strumming or plucking the strings with the """
                       """fingers, thumb or fingernails of the right hand or with a pick """
                       """while fretting (or pressing against the frets) the strings with the """
                       """fingers of the left hand. The guitar is a type of chordophone, """
                       """traditionally constructed from wood and strung with either gut, """
                       """nylon or steel strings and distinguished from other chordophones by """
                       """its construction and tuning. The modern guitar was preceded by the """
                       """gittern, the vihuela, the four-course Renaissance guitar, and the """
                       """five-course baroque guitar, all of which contributed to the """
                       """development of the modern six-string instrument.




    There are three main types of modern acoustic guitar: the classical """
                       """guitar (nylon-string guitar), the steel-string acoustic guitar, """
                       """and the archtop guitar, which is sometimes called a "jazz guitar". """
                       """The tone of an acoustic guitar is produced by the strings' vibration, """
                       """amplified by the hollow body of the guitar, which acts as a """
                       """resonating chamber. The classical guitar is often played as a solo """
                       """instrument using a comprehensive finger-picking technique where """
                       """each string is plucked individually by the player's fingers, as """
                       """opposed to being strummed. The term "finger-picking" can also refer """
                       """to a specific tradition of folk, blues, bluegrass, and country """
                       """guitar playing in the United States. The acoustic bass guitar is a """
                       """low-pitched instrument that is one octave below a regular guitar.


    """)

    # fonts

    text_widget.tag_add('head', '1.0', '3.0')
    text_widget.tag_config('head', font=('times', 20, 'bold'))

    # event bindings

    guitar_chords_button.bind('<Button-1>', func=guitarChordsText)
    learn_strumming_button.bind('<Button-1>', func=learnStrummingText)
    more_strumming_button.bind('<Button-1>', func=moreStrummingText)

    # mainloop

    guitar_tutorial_window.mainloop()


# guitarStartTheoryTutorial()
