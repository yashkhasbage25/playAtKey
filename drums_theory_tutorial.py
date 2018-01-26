import tkinter as tk
import tkinter.scrolledtext as tkst
import os

# global declarations

global IMG_DRM_TUT_DIR, IMG_MAIN_DIR

# diractory paths

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, 'img')
IMG_MAIN_DIR = os.path.join(IMG_DIR, 'main')
IMG_DRM_TUT_DIR = os.path.join(IMG_DIR, 'drumstutorial')

# button functions


def eightPieceText(self):

    # global decalartions

    global drums_1, drums_2

    # Tk widgets

    text_frame = tk.Frame(drums_theory_tutorial_window, borderwidth=5, relief='ridge')
    text_widget = tkst.ScrolledText(text_frame, wrap='word', font='arial 15')

    # photoimages

    drums_1 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_1.gif'))
    drums_2 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_2.gif'))
    # place configurations

    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)

    # insert text

    text_widget.insert('current', """
    Components of an eight-piece Drumset

    """)
    text_widget.image_create('current', image=drums_1)
    text_widget.insert('current', """\n\n\n""")
    text_widget.image_create('current', image=drums_2)

    # fonts

    text_widget.tag_add('head', '2.0', '3.0')
    text_widget.tag_config('head', font=('times', 20, 'bold'))


def basicPatternsText(self):

    # global

    global drums_1, drums_2, drums_3, drums_4

    # Tk widgets

    text_frame = tk.Frame(drums_theory_tutorial_window, borderwidth=5, relief='ridge')
    text_widget = tkst.ScrolledText(text_frame, wrap='word', font='arial 15')

    # photoimages

    drums_1 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_3.gif'))
    drums_2 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_4.gif'))
    drums_3 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_5.gif'))
    drums_4 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_6.gif'))

    # insert text

    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)
    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.insert('current', """
    Basic Drum Patterns

    1.Take a look at the first exercise below. It has a single measure """
                       """of eighth notes. The count is listed above each of the eight notes """
                       """in the measure. The "x" symbol above the top line of the measure """
                       """indicates that these counts are to be played on the hi-hats. Start """
                       """by counting out loud (one and two and three and four and), and then """
                       """play the hi-hats along with your counting. Loop this a few times, """
                       """and focus on playing at a consistent pace.

""")
    text_widget.image_create('current', image=drums_1)
    text_widget.insert('current', """

    2.   In exercise two, you'll learn how to play the bass drum on the one """
                       """and three counts. As you can see below, the bass drum is indicated """
                       """with a solid note in the bottom space of the measure. You can watch """
                       """the video lesson for tips on how to play the pedal with control.
    """)
    text_widget.image_create('current', image=drums_2)
    text_widget.insert('current', """

    3.   Next, exercise three includes the snare drum on counts two and four. """
                       """The snare drum is indicated by a solid note on the middle line of """
                       """each measure. As with the bass drum, you want to focus on playing """
                       """these right with the hi-hats. The strokes should line up perfectly, """
                       """so it sounds like one complete sound.

    """)
    text_widget.image_create('current', image=drums_3)
    text_widget.insert('current', """

    4.   Finally, exercise four brings everything together. The previous """
                       """patterns were all leading up to this. As you can see below, this """
                       """beat includes the hi-hats, snare drum, and bass drum - all together """
                       """in one complete beat. This is how to play the drums in a real """
                       """band setting.

    Be sure you really focus on playing this beat steady and in time. """
                       """It is highly recommended that you play along with a metronome - """
                       """especially when first learning how to play on a drum set. """
                       """Everything needs to sound even and consistent. Just loop the """
                       """pattern over and over until you are feeling very confident.
    """)
    text_widget.image_create('current', image=drums_4)
    text_widget.insert('current', """

    If you are having any difficulty with this last beat, you can """
                       """always go back and practice beats 1 - 3. That will help you """
                       """focus on timing and limb-independence. Then, when you feel ready, """
                       """come back to beat 4.
    """)

    # fonts

    text_widget.tag_add('head', '2.0', '3.0')
    text_widget.tag_config('head', font=('times', 20, 'bold'))


def drumsPatternsText(self):
    # global declarations

    global drums_7, drums_8, drums_9, drums_10

    # Tk widgets

    text_frame = tk.Frame(drums_theory_tutorial_window, borderwidth=5, relief='ridge')
    text_widget = tkst.ScrolledText(text_frame, wrap='word', font='arial 15')

    # photoimages

    drums_7 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_7.gif'))
    drums_8 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_8.gif'))
    drums_9 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_9.gif'))
    drums_10 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_10.gif'))

    # place configurations

    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)

    # insert text

    text_widget.insert('current', """
    Drums Patterns


       """)
    text_widget.image_create('current', image=drums_7)
    text_widget.insert('current', """


    Exercise one is to be played on the hi-hats alone. The hi-hats are """
                       """notated with the "x" symbols above the top line of the measure. """
                       """The numbers 1-4 are there to indicate how you are to count these """
                       """out loud. Simply put your foot down on the hi-hat pedal, and play """
                       """the edge of the hi-hats with your stick on all four counts.


        """)
    text_widget.image_create('current', image=drums_8)
    text_widget.insert('current', """


    The second exercise includes the bass drum being played on counts one """
                       """and three. Focus on keeping the four hi-hat strokes steady, and """
                       """then add in the bass drum. The bass drum should be synced up """
                       """perfectly with the hi-hat strokes as you continue to count out loud.


    """)
    text_widget.image_create('current', image=drums_9)
    text_widget.insert('current', """

    Exercise three brings the snare drum into the mix. Here you will no """
                       """longer be playing the bass drum, but you'll hit the snare drum on """
                       """beats two and four. Again, focus on playing overlapping shots in """
                       """perfect sync. The two and four counts include two voices, but they """
                       """should sound like one combined shot.


    """)
    text_widget.image_create('current', image=drums_10)
    text_widget.insert('current', """

    In exercise four, you will learn to play the first three patterns """
                       """simultaniously. The hi-hats will continue on all four counts, """
                       """while the bass drum and snare drum alternate. Focus on keeping """
                       """everything steady and in time. Many beginners will have a """
                       """tendency to start playing a little choppy. Be sure the hi-hat """
                       """strokes continue to be even and continous while you bring in """
                       """the other two voices.


    """)
    text_widget.insert('current', """

    If this is a little tricky, you can always go back and practice """
                       """exercises 1-3 a little longer. Then come back and give exercise """
                       """four another try. If you are able to play it continously - """
                       """congratulations! You are ready to move on to more challenging """
                       """drum beats!


    """)

    # fonts

    text_widget.tag_add('head', '2.0', '3.0')
    text_widget.tag_config('head', font=('times', 20, 'bold'))


def singleRollText(self):

    # global declarations

    global drums_11, drums_12, drums_13

    # photoimages

    drums_11 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_11.gif'))
    drums_12 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_12.gif'))
    drums_13 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_13.gif'))

    # Tk widgets

    text_frame = tk.Frame(drums_theory_tutorial_window, borderwidth=5, relief='ridge')
    text_widget = tkst.ScrolledText(text_frame, wrap='word', font='arial 15')

    # place configurations

    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)

    # insert text

    text_widget.insert('current', """


    Single Stroke Roll


    The single stroke roll is the most common drum rudiment used on """
                       """the drum set. It's often played in beats, fills, and drum solos. """
                       """It doesn't matter if you are new to the drums, or if you have """
                       """been playing for years, the single stroke roll is absolutely """
                       """essential. Here is how the single stroke roll is notated:


    """)
    text_widget.image_create('current', image=drums_11)
    text_widget.insert('current', """


    As you can see, it's played with simple alternating single strokes """
                       """(R, L, R, L). It is best to start practicing this on a practice pad, """
                       """and then eventually take it to the kit. Once you can play it in """
                       """perfect time with a metronome, begin to speed up the tempo to """
                       """increase your overall speed and endurance.

    Focus on keeping all the strokes at an even volume. Watch how your """
                       """sticks come up for each stroke, and be sure they reach an even """
                       """height. If one stick is coming up higher than the other, it will """
                       """typically create a louder stroke. Practicing in front of a mirror """
                       """is highly recommended, so you can keep an eye on both hands while """
                       """first developing this rudiment.


    """)
    text_widget.insert('current', """
    Here is how you might incorporate the single stroke roll into a drum beat:


    """)
    text_widget.image_create('current', image=drums_12)
    text_widget.insert('current', """
    Exercise three incorporates the single stroke roll into a drum set fill:


    """)
    text_widget.image_create('current', image=drums_13)
    text_widget.insert('current', """


    Once you have mastered this rudiment, you can move on to the single """
                       """stroke four or the double stroke roll.


    """)

    # fonts

    text_widget.tag_add('head', '2.0', '3.0')
    text_widget.tag_config('head', font=('times', 20, 'bold'))


def singleSevenText(self):

    # global declarations

    global drums_14, drums_15, drums_16

    # photoimages

    drums_14 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_14.gif'))
    drums_15 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_15.gif'))
    drums_16 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_16.gif'))

    # Tk widgets

    text_frame = tk.Frame(drums_theory_tutorial_window, borderwidth=5, relief='ridge')
    text_widget = tkst.ScrolledText(text_frame, wrap='word', font='arial 15')

    # place configurations

    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)

    # insert text

    text_widget.insert('current', """
    Single Seven stroke


    The single stroke seven is less common than most rudiments, but it is """
                       """still an excellent pattern to incorporate into your drumming. It is """
                       """similar to the single stroke roll, but is played in groups of seven """
                       """strokes (as the name suggests). Here is how it looks when written """
                       """out in drum notation:


    """)
    text_widget.image_create('current', image=drums_14)
    text_widget.insert('current', """
    Start by developing the pattern slowly on a practice pad, and then move """
                       """it to the drum set. You can use a metronome to be sure the groups """
                       """of seven are played within proper time. Then, when you are ready """
                       """to try something more creative, you can move on to the """
                       """exercises below.

    Here is a simple drum beat that incorporates the single stroke seven:


    """)
    text_widget.image_create('current', image=drums_15)
    text_widget.insert('current', """


    Exercise three uses the single stroke seven around the kit as a drum fil:


    """)
    text_widget.image_create('current', image=drums_16)
    text_widget.insert('current', """


    Once you are finished with this lesson - you can move on to the """
                       """multiple bounce roll, or the double stroke roll.


    """)
    text_widget.tag_add('head', '2.0', '3.0')
    text_widget.tag_config('head', font=('times', 20, 'bold'))


def doubleStrokeText(self):

    # global

    global drums_17, drums_18, drums_19

    # photoimages

    drums_17 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_17.gif'))
    drums_18 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_18.gif'))
    drums_19 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_19.gif'))

    # Tk widgets

    text_frame = tk.Frame(drums_theory_tutorial_window, borderwidth=5, relief='ridge')
    text_widget = tkst.ScrolledText(text_frame, wrap='word', font='arial 15', height=65, width=120)

    # place configurations

    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)

    # insert text

    text_widget.insert('current', """
    Double Stroke Roll

    The double stroke roll is an extremely popular rudiment that should be """
                       """practiced to perfection by anyone serious about playing the drums. """
                       """Not only is it popular for use within beats and fills, but it is also """
                       """the foundation for many other important drum rudiments. Here is how it """
                       """is written out in drum notation:

    """)
    text_widget.image_create('current', image=drums_17)
    text_widget.insert('current', """


    You can start by playing the doubles using your wrists for each stroke. """
                       """Focus on keeping both alternating strokes at an even volume. This can """
                       """be done by watching your stick heights during each stroke, to be """
                       """sure they are all coming up to an even distance from the drum head. """
                       """If the first stroke of each set of doubles is louder than the second, """
                       """your double stroke roll will sound sloppy and un-even.

    Once you have mastered the basic pattern using your wrists, you can begin """
                       """to speed it up. Eventually, you will begin to bounce the sticks to get """
                       """the double strokes. This can take some time to perfect, but it will """
                       """allow you to play with much greater speed. Watch the video lesson on """
                       """this page to see how Lionel plays this rudiment.

This drum beat incorporates the double stroke roll in the first half of the measure:
    """)
    text_widget.image_create('current', image=drums_18)
    text_widget.insert('current', """


    This third exercise features the double stroke roll in the context of a drum fill:


    """)
    text_widget.image_create('current', image=drums_19)

    # fonts

    text_widget.tag_add('head', '2.0', '3.0')
    text_widget.tag_config('head', font=('times', 20, 'bold'))


def fiveStrokeText(self):

    # global declarations

    global drums_20, drums_21, drums_22

    # photoimages

    drums_20 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_20.gif'))
    drums_21 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_21.gif'))
    drums_22 = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_22.gif'))

    # Tk widgets

    text_frame = tk.Frame(drums_theory_tutorial_window, borderwidth=5, relief='ridge')
    text_widget = tkst.ScrolledText(text_frame, wrap='word', font='arial 15')

    # place configurations

    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)

    # insert text

    text_widget.insert('current', """
    Five Stroke Roll

    The five stroke roll is a powerful rudiment based off the double stroke """
                       """roll. Unlike the single, double, and triple stroke rolls may """
                       """suggest - this rudiment does not have alternating groups of five """
                       """strokes per hand. Instead, it is made up of two double strokes, """
                       """and a single. You first play it with right hand lead, and then """
                       """repeat the pattern with left hand lead (or reverse if you are """
                       """left-handed). Here is how it is written out:


    """)
    text_widget.image_create('current', image=drums_20)
    text_widget.insert('current', """


    If you haven't yet mastered the double stroke roll, it's recommended """
                       """that you go and view that lesson before continuing. However, if """
                       """you've already mastered that rudiment, you can begin to develop this """
                       """pattern. As you can see above, it is played with two doubles """
                       """and then a single.

    In this drum set application, you will learn how to incorporate the """
                       """five stroke roll into a drum beat:


    """)
    text_widget.image_create('current', image=drums_21)
    text_widget.insert('current', """
    In this drum set application, you will learn how to incorporate """
                       """the five stroke roll into a drum fill:


    """)
    text_widget.image_create('current', image=drums_22)

    # fonts

    text_widget.tag_add('head', '2.0', '3.0')
    text_widget.tag_config('head', font=('times', 20, 'bold'))


def drumsLegendImg(self):

    # global decalartions

    global drums_legend_img

    # window configurations

    drums_legend_img_window = tk.Toplevel()
    drums_legend_img_window.geometry('596x262+200+200')
    drums_legend_img_window.title('Drums Legend')

    # photoimages

    drums_legend_img = tk.PhotoImage(file=os.path.join(IMG_DRM_TUT_DIR, 'drums_legend.gif'))

    # Tk widgets

    drums_legend_img_label = tk.Label(drums_legend_img_window, image=drums_legend_img)

    # packing and mainloop

    drums_legend_img_label.pack()
    drums_legend_img_window.mainloop()


def drumsStartTheoryTutorial(self):

    # global declarations

    global drums_theory_tutorial_window

    # window configurations

    drums_theory_tutorial_window = tk.Toplevel()
    drums_theory_tutorial_window.geometry("1000x750+200+100")
    drums_theory_tutorial_window.title("Drums Tutorial")
    drums_theory_tutorial_window.configure(background='#18dd38')
    tutorial_icon = tk.Image("photo", file=os.path.join(IMG_MAIN_DIR, 'tutorial_icon.gif'))
    drums_theory_tutorial_window.wm_iconphoto(True, tutorial_icon)

    # Tk widgets

    eight_piece_button = tk.Button(drums_theory_tutorial_window,
                                   text='8 piece\nDrumset', font=('arial', 13), background='#b44010')
    basic_patterns_button = tk.Button(
        drums_theory_tutorial_window, text='Basic\nDrum\nPatterns', font=('arial', 13), background='#e55300')
    drums_patterns_button = tk.Button(drums_theory_tutorial_window,
                                      text='Drum\nPatterns', font=('arial', 13), background='#ff6900')
    single_roll_button = tk.Button(
        drums_theory_tutorial_window, text='Single\nStroke\nRoll', font=('arial', 13), background='#ff2b00')
    single_seven_button = tk.Button(
        drums_theory_tutorial_window, text='Single\nStroke\nSeven', font=('arial', 13), background='#ff4023')
    double_stroke_button = tk.Button(
        drums_theory_tutorial_window, text='Double\nStroke\nRoll', font=('arial', 13), background='#ff5c00')
    five_stroke_button = tk.Button(drums_theory_tutorial_window,
                                   text='Five\nStroke\nRoll', font=('arial', 13), background='#ff8106')
    drums_legend_button = tk.Button(drums_theory_tutorial_window, text='View\nlegend\nfor\nDrums', font=(
        'arial', 13), background='#ff9f00')
    text_frame = tk.Frame(drums_theory_tutorial_window, height=480,
                          width=570, borderwidth=5, relief='ridge')
    text_widget = tkst.ScrolledText(text_frame, font="arial 15", wrap='word')

    # place configurations

    eight_piece_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0)
    basic_patterns_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0.1)
    drums_patterns_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0.2)
    single_roll_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0.3)
    single_seven_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0.4)
    double_stroke_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0.5)
    five_stroke_button.place_configure(relheight=0.1, relwidth=0.1, relx=0, rely=0.6)
    drums_legend_button.place_configure(relheight=0.2, relwidth=0.1, relx=0, rely=0.7)
    text_frame.place_configure(relheight=1, relwidth=0.9, relx=0.1, rely=0)
    text_widget.place_configure(relheight=1, relwidth=1, relx=0, rely=0)

    # photoimages

    drums_intro = tk.PhotoImage(file=os.path.join(
        IMG_DRM_TUT_DIR, 'drums_intro.gif'))

    # insert text

    text_widget.image_create('current', image=drums_intro)
    text_widget.insert('current', """
    Drums


    A drum kit — also called a drum set, trap set, or simply drums — is a """
                       """collection of drums and other percussion instruments, typically cymbals, """
                       """which are set up on stands to be played by a single player, with """
                       """drumsticks held in both hands, and the feet operating pedals that """
                       """control the hi-hat cymbal and the beater for the bass drum. A drum kit """
                       """consists of a mix of drums (categorized classically as membranophones, """
                       """Hornbostel-Sachs high-level classification 2) and idiophones - most """
                       """significantly cymbals, but can also include the woodblock and cowbell """
                       """(classified as Hornbostel-Sachs high-level classification 1). In the """
                       """2000s, some kits also include electronic instruments (Hornbostel-Sachs """
                       """classification 53). Also, both hybrid (mixing acoustic instruments """
                       """and electronic drums) and entirely electronic kits are used.

"""
                       """    A standard modern kit (for a right-handed player), as used in """
                       """popular music and taught in music schools, contains:

"""
                       """    A snare drum, mounted on a stand, placed between the player's knees """
                       """and played with drum sticks (which may include rutes or brushes) """
                       """    A bass drum, played by a pedal operated by the right foot, which """
                       """moves a felt-covered beater """
                       """    One or more toms, played with sticks or brushes (usually three """
                       """toms: rack tom 1 and 2, and floor tom) """
                       """    A hi-hat (two cymbals mounted on a stand), played with the sticks, """
                       """opened and closed with left foot pedal (it can also produce sound """
                       """with the foot alone) """
                       """    One or more cymbals, mounted on stands, played with the sticks """
                       """All of these are classed as non-pitched percussion, allowing for """
                       """the music to be scored using percussion notation, for which a loose """
                       """semi-standardized form exists for the drum kit. If some or all of """
                       """them are replaced by electronic drums, the scoring and most often """
                       """positioning remains the same, allowing a standard teaching approach. """
                       """The drum kit is usually played while seated on a drum stool or """
                       """throne. The drum kit differs from instruments that can be used to """
                       """produce pitched melodies or chords, even though drums are often """
                       """placed musically alongside others that do, such as the guitar or """
                       """piano. The drum kit is a part of the standard rhythm section used """
                       """in many types of popular and traditional music styles, ranging """
                       """from rock and pop to blues and jazz. Other standard instruments """
                       """used in the rhythm section include the piano, electric guitar, """
                       """electric bass, and keyboards.
    """)

    # event bindings

    eight_piece_button.bind('<Button-1>', func=eightPieceText)
    basic_patterns_button.bind('<Button-1>', func=basicPatternsText)
    drums_patterns_button.bind('<Button-1>', func=drumsPatternsText)
    single_roll_button.bind('<Button-1>', func=singleRollText)
    single_seven_button.bind('<Button>', func=singleSevenText)
    double_stroke_button.bind('<Button-1>', func=doubleStrokeText)
    five_stroke_button.bind('<Button-1>', func=fiveStrokeText)
    drums_legend_button.bind('<Button-1>', func=drumsLegendImg)

    # fonts

    text_widget.tag_add('head', '2.0', '3.0')
    text_widget.tag_config('head', font=('times', 25, 'bold'))

    # mainloop

    drums_theory_tutorial_window.mainloop()


# drumsStartTheoryTutorial()
