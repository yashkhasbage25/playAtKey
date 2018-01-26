import tkinter as tk
import pygame
import os
import pysynth as ps
from random import randint

from keyboard_theory_tutorial import keyboardStartTheoryTutorial
from keyboard_play_tutorial import keyboardStartPlayTutorial
from guitar_play_tutorial import guitarStartPlayTutorial
from guitar_theory_tutorial import guitarStartTheoryTutorial
from drums_theory_tutorial import drumsStartTheoryTutorial
from drums_sheet import drumsShowSheet

# some global declarations

global WINDOW_HEIGHT, WINDOW_WIDTH, TITLE_DISPLAY_TIME, NUM_CHANNELS, IMG_DIR,\
    METRONOME_WAV, METRONOME_WAV_NAME, METRONOME_INC_MUL, METRONOME_DEC_MUL,\
    IMG_MAIN_DIR

# defining global vaiables

# directory paths

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SND_DIR = os.path.join(BASE_DIR, "snd")
KEYBOARD_SND_DIR = os.path.join(SND_DIR, 'keyboard')
DRUMS_SND_DIR = os.path.join(SND_DIR, 'drums')
GUITAR_SND_DIR = os.path.join(SND_DIR, 'guitar')
IMG_DIR = os.path.join(BASE_DIR, 'img')
IMG_MAIN_DIR = os.path.join(IMG_DIR, 'main')
IMG_KEY_TUT_DIR = os.path.join(IMG_DIR, 'keyboardtutorial')
IMG_DRM_TUT_DIR = os.path.join(IMG_DIR, 'drumstutorial')
IMG_GTR_TUT_DIR = os.path.join(IMG_DIR, 'guitartutorial')
METRONOME_WAV_NAME = 'test.wav'
METRONOME_WAV = os.path.join(BASE_DIR, METRONOME_WAV_NAME)

# window sizes

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
METRONOME_WINDOW_HEIGHT = 200
METRONOME_WINDOW_WIDTH = 320

# miscellanous

TITLE_DISPLAY_TIME = 2000
NUM_CHANNELS = 20
METRONOME_INC_MUL = 2
METRONOME_DEC_MUL = 0.9

# pygame-initialize mixer

pygame.mixer.init()
pygame.mixer.set_num_channels(NUM_CHANNELS)

# play keyboard notes


def keyboardSoundC1(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "1.wav")))
            notFound = False


def keyboardSoundCs1(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "2.wav")))
            notFound = False


def keyboardSoundD1(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "3.wav")))
            notFound = False


def keyboardSoundDs1(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "4.wav")))
            notFound = False


def keyboardSoundE1(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "5.wav")))
            notFound = False


def keyboardSoundF1(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "6.wav")))
            notFound = False


def keyboardSoundFs1(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "7.wav")))
            notFound = False


def keyboardSoundG1(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "8.wav")))
            notFound = False


def keyboardSoundGs1(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "9.wav")))
            notFound = False


def keyboardSoundA1(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "10.wav")))
            notFound = False


def keyboardSoundAs1(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "11.wav")))
            notFound = False


def keyboardSoundB1(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "12.wav")))
            notFound = False


def keyboardSoundC2(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "13.wav")))
            notFound = False


def keyboardSoundCs2(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "14.wav")))
            notFound = False


def keyboardSoundD2(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "15.wav")))
            notFound = False


def keyboardSoundDs2(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "16.wav")))
            notFound = False


def keyboardSoundE2(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "17.wav")))
            notFound = False


def keyboardSoundF2(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "18.wav")))
            notFound = False


def keyboardSoundFs2(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "19.wav")))
            notFound = False


def keyboardSoundG2(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "20.wav")))
            notFound = False


def keyboardSoundGs2(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "21.wav")))
            notFound = False


def keyboardSoundA2(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "22.wav")))
            notFound = False


def keyboardSoundAs2(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "23.wav")))
            notFound = False


def keyboardSoundB2(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "24.wav")))
            notFound = False


def keyboardSoundC3(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "25.wav")))
            notFound = False


def keyboardSoundCs3(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "26.wav")))
            notFound = False


def keyboardSoundD3(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "27.wav")))
            notFound = False


def keyboardSoundDs3(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "28.wav")))
            notFound = False


def keyboardSoundE3(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "29.wav")))
            notFound = False


def keyboardSoundF3(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "30.wav")))
            notFound = False


def keyboardSoundFs3(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "31.wav")))
            notFound = False


def keyboardSoundG3(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "32.wav")))
            notFound = False


def keyboardSoundGs3(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "33.wav")))
            notFound = False


def keyboardSoundA3(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "34.wav")))
            notFound = False


def keyboardSoundAs3(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "35.wav")))
            notFound = False


def keyboardSoundB3(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "36.wav")))
            notFound = False


def keyboardSoundC4(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(KEYBOARD_SND_DIR, "37.wav")))
            notFound = False


def keyboardPlayNothing(self):
    pass

# play drum drum sounds


def drumsSoundSnare(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(DRUMS_SND_DIR, "snare.wav")))
            notFound = False


def drumsSoundHitom(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(DRUMS_SND_DIR, "hitom.wav")))
            notFound = False


def drumsSoundMidtom(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(DRUMS_SND_DIR, "midtom.wav")))
            notFound = False


def drumsSoundLowtom(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(DRUMS_SND_DIR, "lowtom.wav")))
            notFound = False


def drumsSoundHihatClosed(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(DRUMS_SND_DIR, "hihatclosed.wav")))
            notFound = False


def drumsSoundHihatOpen(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(DRUMS_SND_DIR, "hihatopen.wav")))
            notFound = False


def drumsSoundCrash(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(DRUMS_SND_DIR, "crash.wav")))
            notFound = False


def drumsSoundRide(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(
                pygame.mixer.Sound(
                    file=os.path.join(DRUMS_SND_DIR, "ride.wav")))
            notFound = False


def drumsSoundKick(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(
                pygame.mixer.Sound(
                    file=os.path.join(DRUMS_SND_DIR, "kick.wav")))
            notFound = False

# play guitar chords


def guitarSoundCMajDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'CMajDown.wav')))
            notFound = False


def guitarSoundCMajUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'CMajUp.wav')))
            notFound = False


def guitarSoundCMinDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'CMinDown.wav')))
            notFound = False


def guitarSoundCMinUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'CMinUp.wav')))
            notFound = False


def guitarSoundCsMajDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'CsMajDown.wav')))
            notFound = False


def guitarSoundCsMajUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'CsMajUp.wav')))
            notFound = False


def guitarSoundCsMinDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'CsMinDown.wav')))
            notFound = False


def guitarSoundCsMinUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'CsMinUp.wav')))
            notFound = False


def guitarSoundDMajDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'DMajDown.wav')))
            notFound = False


def guitarSoundDMajUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'DMajUp.wav')))
            notFound = False


def guitarSoundDMinDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'DMinDown.wav')))
            notFound = False


def guitarSoundDMinUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'DMinUp.wav')))
            notFound = False


def guitarSoundDsMajDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'DsMajDown.wav')))
            notFound = False


def guitarSoundDsMajUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'DsMajUp.wav')))
            notFound = False


def guitarSoundDsMinDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'DsMinDown.wav')))
            notFound = False


def guitarSoundDsMinUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'DsMinUp.wav')))
            notFound = False


def guitarSoundEMajDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'EMajDown.wav')))
            notFound = False


def guitarSoundEMajUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'EMajUp.wav')))
            notFound = False


def guitarSoundEMinDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'EMinDown.wav')))
            notFound = False


def guitarSoundEMinUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'EMinUp.wav')))
            notFound = False


def guitarSoundFMajDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'FMajDown.wav')))
            notFound = False


def guitarSoundFMajUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'FMajUp.wav')))
            notFound = False


def guitarSoundFMinDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'FMinDown.wav')))
            notFound = False


def guitarSoundFMinUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'FMinUp.wav')))
            notFound = False


def guitarSoundFsMajDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'FsMajDown.wav')))
            notFound = False


def guitarSoundFsMajUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'FsMajUp.wav')))
            notFound = False


def guitarSoundFsMinDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'FsMinDown.wav')))
            notFound = False


def guitarSoundFsMinUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'FsMinUp.wav')))
            notFound = False


def guitarSoundGMajDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'GMajDown.wav')))
            notFound = False


def guitarSoundGMajUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'GMajUp.wav')))
            notFound = False


def guitarSoundGMinDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'GMinDown.wav')))
            notFound = False


def guitarSoundGMinUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'GMinUp.wav')))
            notFound = False


def guitarSoundGsMajDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'GsMajDown.wav')))
            notFound = False


def guitarSoundGsMajUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'GsMajUp.wav')))
            notFound = False


def guitarSoundGsMinDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'GsMinDown.wav')))
            notFound = False


def guitarSoundGsMinUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'GsMinUp.wav')))
            notFound = False


def guitarSoundAMajDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'AMajDown.wav')))
            notFound = False


def guitarSoundAMajUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'AMajUp.wav')))
            notFound = False


def guitarSoundAMinDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'AMinDown.wav')))
            notFound = False


def guitarSoundAMinUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'AMinUp.wav')))
            notFound = False


def guitarSoundAsMajDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'AsMajDown.wav')))
            notFound = False


def guitarSoundAsMajUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'AsMajUp.wav')))
            notFound = False


def guitarSoundAsMinDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'AsMinDown.wav')))
            notFound = False


def guitarSoundAsMinUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'AsMinUp.wav')))
            notFound = False


def guitarSoundBMajDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'BMajDown.wav')))
            notFound = False


def guitarSoundBMajUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'BMajUp.wav')))
            notFound = False


def guitarSoundBMinDown(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'BMinDown.wav')))
            notFound = False


def guitarSoundBMinUp(self):
    channel_iter = 0
    notFound = True
    while notFound:
        if pygame.mixer.Channel(channel_iter).get_busy():
            channel_iter = (channel_iter + 1) % NUM_CHANNELS
        else:
            pygame.mixer.Channel(channel_iter).play(pygame.mixer.Sound(
                file=os.path.join(GUITAR_SND_DIR, 'BMinUp.wav')))
            notFound = False

# keyboard legend functions


def keyboardThreeOctaveButtonPlay(self):
    global channel_iter
    keyboard_entry.bind('<Shift_L>', func=keyboardSoundC1)
    keyboard_entry.bind('a', func=keyboardSoundCs1)
    keyboard_entry.bind('z', func=keyboardSoundD1)
    keyboard_entry.bind('s', func=keyboardSoundDs1)
    keyboard_entry.bind('x', func=keyboardSoundE1)
    keyboard_entry.bind('d', func=keyboardPlayNothing)
    keyboard_entry.bind('c', func=keyboardSoundF1)
    keyboard_entry.bind('f', func=keyboardSoundFs1)
    keyboard_entry.bind('v', func=keyboardSoundG1)
    keyboard_entry.bind('g', func=keyboardSoundGs1)
    keyboard_entry.bind('b', func=keyboardSoundA1)
    keyboard_entry.bind('h', func=keyboardSoundAs1)
    keyboard_entry.bind('n', func=keyboardSoundB1)
    keyboard_entry.bind('j', func=keyboardPlayNothing)
    keyboard_entry.bind('m', func=keyboardSoundC2)
    keyboard_entry.bind('k', func=keyboardSoundCs2)
    keyboard_entry.bind(',', func=keyboardSoundD2)
    keyboard_entry.bind('l', func=keyboardSoundDs2)
    keyboard_entry.bind('.', func=keyboardSoundE2)
    keyboard_entry.bind(';', func=keyboardPlayNothing)
    keyboard_entry.bind('/', func=keyboardSoundF2)
    keyboard_entry.bind('\'', func=keyboardSoundFs2)
    keyboard_entry.bind('q', func=keyboardSoundG2)
    keyboard_entry.bind('1', func=keyboardSoundFs2)
    keyboard_entry.bind('2', func=keyboardSoundGs2)
    keyboard_entry.bind('w', func=keyboardSoundA2)
    keyboard_entry.bind('3', func=keyboardSoundAs2)
    keyboard_entry.bind('e', func=keyboardSoundB2)
    keyboard_entry.bind('4', func=keyboardPlayNothing)
    keyboard_entry.bind('r', func=keyboardSoundC3)
    keyboard_entry.bind('5', func=keyboardSoundCs3)
    keyboard_entry.bind('t', func=keyboardSoundD3)
    keyboard_entry.bind('6', func=keyboardSoundDs3)
    keyboard_entry.bind('y', func=keyboardSoundE3)
    keyboard_entry.bind('7', func=keyboardPlayNothing)
    keyboard_entry.bind('u', func=keyboardSoundF3)
    keyboard_entry.bind('8', func=keyboardSoundFs3)
    keyboard_entry.bind('i', func=keyboardSoundG3)
    keyboard_entry.bind('9', func=keyboardSoundGs3)
    keyboard_entry.bind('o', func=keyboardSoundA3)
    keyboard_entry.bind('0', func=keyboardSoundAs3)
    keyboard_entry.bind('p', func=keyboardSoundB3)
    keyboard_entry.bind('-', func=keyboardPlayNothing)
    keyboard_entry.bind('[', func=keyboardSoundC4)
    keyboard_three_oct_legend_label = tk.Label(
        keyboard_background_label, image=keyboard_three_oct_legend_img)
    keyboard_three_oct_legend_label.place_configure(
        relheight=0.5, relwidth=0.55, relx=0.35, rely=0.25)


def keyboardTwoOctaveButtonPlay(self):
    global channel_iter
    keyboard_entry.bind('<Shift_L>', func=keyboardPlayNothing)
    keyboard_entry.bind('a', func=keyboardPlayNothing)
    keyboard_entry.bind('z', func=keyboardSoundC2)
    keyboard_entry.bind('s', func=keyboardSoundCs2)
    keyboard_entry.bind('x', func=keyboardSoundD2)
    keyboard_entry.bind('d', func=keyboardSoundDs2)
    keyboard_entry.bind('c', func=keyboardSoundE2)
    keyboard_entry.bind('f', func=keyboardPlayNothing)
    keyboard_entry.bind('v', func=keyboardSoundF2)
    keyboard_entry.bind('g', func=keyboardSoundFs2)
    keyboard_entry.bind('b', func=keyboardSoundG2)
    keyboard_entry.bind('h', func=keyboardSoundGs2)
    keyboard_entry.bind('n', func=keyboardSoundA2)
    keyboard_entry.bind('j', func=keyboardSoundAs2)
    keyboard_entry.bind('m', func=keyboardSoundB2)
    keyboard_entry.bind('k', func=keyboardPlayNothing)
    keyboard_entry.bind(',', func=keyboardSoundC3)
    keyboard_entry.bind('l', func=keyboardPlayNothing)
    keyboard_entry.bind('.', func=keyboardPlayNothing)
    keyboard_entry.bind(';', func=keyboardPlayNothing)
    keyboard_entry.bind('/', func=keyboardPlayNothing)
    keyboard_entry.bind('\'', func=keyboardPlayNothing)
    keyboard_entry.bind('q', func=keyboardPlayNothing)
    keyboard_entry.bind('1', func=keyboardPlayNothing)
    keyboard_entry.bind('2', func=keyboardPlayNothing)
    keyboard_entry.bind('w', func=keyboardSoundC3)
    keyboard_entry.bind('3', func=keyboardSoundCs3)
    keyboard_entry.bind('e', func=keyboardSoundD3)
    keyboard_entry.bind('4', func=keyboardSoundDs3)
    keyboard_entry.bind('r', func=keyboardSoundE3)
    keyboard_entry.bind('5', func=keyboardPlayNothing)
    keyboard_entry.bind('t', func=keyboardSoundF3)
    keyboard_entry.bind('6', func=keyboardSoundFs3)
    keyboard_entry.bind('y', func=keyboardSoundG3)
    keyboard_entry.bind('7', func=keyboardSoundGs3)
    keyboard_entry.bind('u', func=keyboardSoundA3)
    keyboard_entry.bind('8', func=keyboardSoundAs3)
    keyboard_entry.bind('i', func=keyboardSoundB3)
    keyboard_entry.bind('9', func=keyboardPlayNothing)
    keyboard_entry.bind('o', func=keyboardSoundC4)
    keyboard_entry.bind('0', func=keyboardPlayNothing)
    keyboard_entry.bind('p', func=keyboardPlayNothing)
    keyboard_entry.bind('-', func=keyboardPlayNothing)
    keyboard_entry.bind('[', func=keyboardPlayNothing)
    keyboard_two_oct_legend_label = tk.Label(
        keyboard_background_label, image=keyboard_two_oct_legend_img)
    keyboard_two_oct_legend_label.place_configure(
        relheight=0.5, relwidth=0.55, relx=0.35, rely=0.25)

# drums legend


def drumsButtonPlay():
    global channel_iter
    drums_entry.bind('v', func=drumsSoundSnare)
    drums_entry.bind('g', func=drumsSoundHitom)
    drums_entry.bind('h', func=drumsSoundMidtom)
    drums_entry.bind('n', func=drumsSoundLowtom)
    drums_entry.bind('b', func=drumsSoundKick)
    drums_entry.bind('c', func=drumsSoundHihatClosed)
    drums_entry.bind('x', func=drumsSoundHihatOpen)
    drums_entry.bind('f', func=drumsSoundCrash)
    drums_entry.bind('j', func=drumsSoundRide)

# guitar legend


def guitarButtonPlay():

    global channel_iter
    guitar_entry.bind('z', func=guitarSoundCMajDown)
    guitar_entry.bind('<Control-z>', func=guitarSoundCMajUp)
    guitar_entry.bind('<Alt-z>', func=guitarSoundCMinUp)
    guitar_entry.bind('<Control-Alt-z>', func=guitarSoundCMinDown)
    guitar_entry.bind('s', func=guitarSoundCsMajDown)
    guitar_entry.bind('<Control-s>', func=guitarSoundCsMajUp)
    guitar_entry.bind('<Alt-s>', func=guitarSoundCsMinUp)
    guitar_entry.bind('<Control-Alt-s>', func=guitarSoundCsMinDown)
    guitar_entry.bind('x', func=guitarSoundDMajDown)
    guitar_entry.bind('<Control-x>', func=guitarSoundDMajUp)
    guitar_entry.bind('<Alt-x>', func=guitarSoundDMinUp)
    guitar_entry.bind('<Control-Alt-x>', func=guitarSoundDMinDown)
    guitar_entry.bind('d', func=guitarSoundDsMajDown)
    guitar_entry.bind('<Control-d>', func=guitarSoundDsMajUp)
    guitar_entry.bind('<Alt-d>', func=guitarSoundDsMinUp)
    guitar_entry.bind('<Control-Alt-d>', func=guitarSoundDsMinDown)
    guitar_entry.bind('c', func=guitarSoundEMajDown)
    guitar_entry.bind('<Control-c>', func=guitarSoundEMajUp)
    guitar_entry.bind('<Alt-c>', func=guitarSoundEMinUp)
    guitar_entry.bind('<Control-Alt-c>', func=guitarSoundEMinDown)
    guitar_entry.bind('v', func=guitarSoundFMajDown)
    guitar_entry.bind('<Control-v>', func=guitarSoundFMajUp)
    guitar_entry.bind('<Alt-v>', func=guitarSoundFMinUp)
    guitar_entry.bind('<Control-Alt-v>', func=guitarSoundFMinDown)
    guitar_entry.bind('g', func=guitarSoundFsMajDown)
    guitar_entry.bind('<Control-g>', func=guitarSoundFsMajUp)
    guitar_entry.bind('<Alt-g>', func=guitarSoundFsMinUp)
    guitar_entry.bind('<Control-Alt-g>', func=guitarSoundFsMinDown)
    guitar_entry.bind('b', func=guitarSoundGMajDown)
    guitar_entry.bind('<Control-b>', func=guitarSoundGMajUp)
    guitar_entry.bind('<Alt-b>', func=guitarSoundGMinUp)
    guitar_entry.bind('<Control-Alt-b>', func=guitarSoundGMinDown)
    guitar_entry.bind('h', func=guitarSoundGsMajDown)
    guitar_entry.bind('<Control-h>', func=guitarSoundGsMajUp)
    guitar_entry.bind('<Alt-h>', func=guitarSoundGsMinUp)
    guitar_entry.bind('<Control-Alt-h>', func=guitarSoundGsMinDown)
    guitar_entry.bind('n', func=guitarSoundAMajDown)
    guitar_entry.bind('<Control-n>', func=guitarSoundAMajUp)
    guitar_entry.bind('<Alt-n>', func=guitarSoundAMinUp)
    guitar_entry.bind('<Control-Alt-n>', func=guitarSoundAMinDown)
    guitar_entry.bind('j', func=guitarSoundAsMajDown)
    guitar_entry.bind('<Control-j>', func=guitarSoundAsMajUp)
    guitar_entry.bind('<Alt-j>', func=guitarSoundAsMinUp)
    guitar_entry.bind('<Control-Alt-j>', func=guitarSoundAsMinDown)
    guitar_entry.bind('m', func=guitarSoundBMajDown)
    guitar_entry.bind('<Control-m>', func=guitarSoundBMajUp)
    guitar_entry.bind('<Alt-m>', func=guitarSoundBMinUp)
    guitar_entry.bind('<Control-Alt-m>', func=guitarSoundBMinDown)

# metronome functions


def metronomePlay(self):
    bpm = int(metronome_bpm_entry.get())
    strokes = int(metronome_strokes_entry.get())
    tempo = int(metronome_tempo_entry.get())
    bps = (30 * tempo) / bpm
    music = (('c5', bps),)
    for i in range((strokes - 1)):
        music += (('c', bps),)
    ps.make_wav(music, fn=METRONOME_WAV_NAME)
    pygame.mixer.music.load(METRONOME_WAV)
    pygame.mixer.music.play(loops=-1)


def metronomeStop(self):
    pygame.mixer.music.stop()


def metronomeIncVol(self):
    pygame.mixer.music.set_volume(
        METRONOME_INC_MUL * pygame.mixer.music.get_volume())


def metronomeDecVol(self):
    pygame.mixer.music.set_volume(
        METRONOME_DEC_MUL * pygame.mixer.music.get_volume())

# metronome window


def metronomeWindow(self):

    global metronome_bpm_entry, metronome_strokes_entry, metronome_tempo_entry

    # window configurations

    newroot = tk.Toplevel()
    newroot.geometry(str(
        METRONOME_WINDOW_WIDTH) + 'x' + str(METRONOME_WINDOW_HEIGHT) + '+100+100')
    newroot.title('Metronome')
    newroot.configure(background='#ffffff')
    metronome_icon = tk.Image("photo", file=os.path.join(IMG_MAIN_DIR, 'metronome_icon.gif'))
    newroot.wm_iconphoto(False, metronome_icon)
    metronome_qurery_label = tk.Label(
        newroot, text='Metronome\nenter beats per minute', justify='center', font=('Arial', 12), background='#ffffff')
    metronome_bpm_entry = tk.Entry(newroot, font=('Arial', 10), background='#93dc69')
    metronome_strokes_entry = tk.Entry(newroot, font=('Arial', 10), background='#93dc69')
    metronome_slash_label = tk.Label(
        newroot, text='/', justify='center', font=('Arial', 15), background='#ffffff')
    metronome_tempo_entry = tk.Entry(newroot, font=('Arial', 10), background='#93dc69')
    metronome_play_button = tk.Button(
        newroot, text='Play', font=('Arial', 15), background='#ffc800')
    metronome_stop_button = tk.Button(
        newroot, text='Stop', font=('Arial', 15), background='#ff4500')
    metronome_inc_vol_button = tk.Button(
        newroot, text='Increase\nVolume', font=('Arial', 15), background='#cdcd00')
    metronome_dec_vol_button = tk.Button(
        newroot, text='Decrease\nVolume', font=('Arial', 15), background='#eeee00')

    # place configurations

    metronome_bpm_entry.place_configure(
        relwidth=0.3, relheight=0.15, relx=0.6, rely=0)
    metronome_qurery_label.place_configure(
        relwidth=0.6, relheight=0.2, relx=0, rely=0)
    metronome_inc_vol_button.place_configure(
        relwidth=0.3, relheight=0.25, relx=0.1, rely=0.7)
    metronome_dec_vol_button.place_configure(
        relwidth=0.3, relheight=0.25, relx=0.6, rely=0.7)
    metronome_strokes_entry.place_configure(
        relwidth=0.3, relheight=0.15, relx=0.1, rely=0.25)
    metronome_slash_label.place_configure(
        relwidth=0.1, relheight=0.15, relx=0.45, rely=0.25)
    metronome_tempo_entry.place_configure(
        relwidth=0.3, relheight=0.15, relx=0.6, rely=0.25)
    metronome_play_button.place_configure(
        relwidth=0.3, relheight=0.2, relx=0.10, rely=0.45)
    metronome_stop_button.place_configure(
        relwidth=0.3, relheight=0.2, relx=0.6, rely=0.45)

    # event bindings

    metronome_play_button.bind('<Button-1>', func=metronomePlay)
    metronome_stop_button.bind('<Button-1>', func=metronomeStop)
    metronome_inc_vol_button.bind('<Button-1>', func=metronomeIncVol)
    metronome_dec_vol_button.bind('<Button-1>', func=metronomeDecVol)

    newroot.mainloop()

# back buttons


def keyboardBack(self):

    # forgets

    root.destroy()

    # call to choose instruments window

    playAtKey()


def drumsBack(self):

    # forgets

    root.destroy()

    # call to choose instruments window

    playAtKey()


def guitarBack(self):

    # destroy

    root.destroy()

    # call to playAtKey

    playAtKey()

# keyboard window


def playKeyboard(self):

    # place forgets

    keyboard_button_1.place_forget()
    keyboard_button_2.place_forget()
    drums_button_1.place_forget()
    drums_button_2.place_forget()
    guitar_button_1.place_forget()
    guitar_button_2.place_forget()

    # global declarations

    global keyboard_two_oct_legend,  keyboard_two_oct_legend_img, \
        keyboard_three_oct_legend, keyboard_three_oct_legend_img, \
        keyboard_background_img, metronome_button, keyboard_entry, \
        keyboard_background_label

    # photoimages

    keyboard_two_oct_legend_img = tk.PhotoImage(file=os.path.join(
        IMG_MAIN_DIR, 'keyboard_two_oct_legend.png'))
    keyboard_three_oct_legend_img = tk.PhotoImage(
        file=os.path.join(IMG_MAIN_DIR, 'keyboard_three_oct_legend.png'))
    keyboard_background_img = tk.PhotoImage(
        file=os.path.join(IMG_MAIN_DIR, 'background_' + str(randint(1, 10)) + '.gif'))

    # window configurations

    keyboard_background_label = tk.Label(frame, image=keyboard_background_img)
    metronome_button = tk.Button(keyboard_background_label,
                                 text='Metronome', bg='#14D764', font='Helvetica 18')
    three_octave_button = tk.Button(keyboard_background_label,
                                    text='3 Octave\nPiano', bg='#11D0A8', font=('Helvetica', 18))
    two_octave_button = tk.Button(keyboard_background_label,
                                  text='2 Octave\nPiano', bg='#11D0A8', font=('Helvetica', 18))
    keyboard_theory_tutorial_button = tk.Button(
        keyboard_background_label, text='New to\nKeyboard...', bg='#1482D7', font=('Arial', 18))
    keyboard_play_tutorial_button = tk.Button(
        keyboard_background_label, text='Need \nTutorial?', bg='#1482D7', font=('Helvetica', 18))
    keyboard_entry = tk.Entry(keyboard_background_label, font='arial', bd=4,
                              insertwidth=10, justify='left', bg='#ffff99')
    keyboard_back_button = tk.Button(keyboard_background_label,
                                     text='BACK', bg='#cd00cd', font=('Arial', 18))

    # place configurations

    keyboard_background_label.place_configure(relheight=1, relwidth=1, relx=0, rely=0)
    metronome_button.place_configure(relheight=0.1, relwidth=0.15, relx=0.1, rely=0.1)
    three_octave_button.place_configure(relheight=0.1, relwidth=0.15, relx=0.1, rely=0.35)
    two_octave_button.place_configure(relheight=0.1, relwidth=0.15, relx=0.1, rely=0.55)
    keyboard_theory_tutorial_button.place_configure(
        relheight=0.1, relwidth=0.2, relx=0.35, rely=0.1)
    keyboard_play_tutorial_button.place_configure(relheight=0.1, relwidth=0.2, relx=0.55, rely=0.1)
    keyboard_back_button.place_configure(relheight=0.1, relwidth=0.1, relx=0.8, rely=0.1)
    keyboard_entry.place_configure(relheight=0.1, relwidth=0.55, relx=0.35, rely=0.8)

    # Button bindings

    three_octave_button.bind('<Button-1>', func=keyboardThreeOctaveButtonPlay)
    two_octave_button.bind('<Button-1>', func=keyboardTwoOctaveButtonPlay)
    keyboard_back_button.bind('<Button-1>', func=keyboardBack)
    metronome_button.bind('<Button-1>', func=metronomeWindow)
    keyboard_theory_tutorial_button.bind(
        '<Button-1>', func=keyboardStartTheoryTutorial)
    keyboard_play_tutorial_button.bind(
        '<Button-1>', func=keyboardStartPlayTutorial)

# drums window


def playDrums(self):

    # place forgets

    keyboard_button_1.place_forget()
    keyboard_button_2.place_forget()
    drums_button_1.place_forget()
    drums_button_2.place_forget()
    guitar_button_1.place_forget()
    guitar_button_2.place_forget()

    # global declarations

    global drums_background_label, drums_legend_img, drums_entry, \
        drums_back_button, metronome_button, drums_background_img, \
        music_img_label, music_img

    # photoimages

    drums_legend_img = tk.PhotoImage(file=os.path.join(
        IMG_MAIN_DIR, 'drums_legend_img.gif'))
    drums_background_img = tk.PhotoImage(file=os.path.join(
        IMG_MAIN_DIR, 'background_' + str(randint(1, 10)) + '.gif'))
    music_img = tk.PhotoImage(file=os.path.join(IMG_MAIN_DIR, 'music.gif'))

    # Tk widgets

    drums_background_label = tk.Label(root, image=drums_background_img)
    metronome_button = tk.Button(drums_background_label, text='Metronome',
                                 bg='#14D764', font=('Helvetica', 18))
    drums_legend_label = tk.Label(drums_background_label,
                                  image=drums_legend_img, background='#000080')
    drums_entry = tk.Entry(drums_background_label, font=('Helvetica', 18), bd=2,
                           insertwidth=10, justify='left', bg='#98f5ff')
    drums_back_button = tk.Button(drums_background_label, text='BACK',
                                  bg='#e066ff', font=('Helvetica', 18))
    drums_theory_tutorial_button = tk.Button(
        drums_background_label, text='New to\nDrums...', bg='#1482D7', font=('Helvetica', 18))
    drums_play_tutorial_button = tk.Button(
        drums_background_label, text='Wanna practice\nsome songs?', bg='#1482D7', font=('Helvetica', 18))
    music_img_label = tk.Label(drums_background_label, image=music_img, background='black')

    # place configurations

    drums_background_label.place_configure(relheight=1, relwidth=1, relx=0, rely=0)
    drums_back_button.place_configure(relheight=0.1, relwidth=0.1, relx=0.8, rely=0.1)
    drums_legend_label.place_configure(relheight=0.4, relwidth=0.55, relx=0.35, rely=0.3)
    drums_entry.place_configure(relheight=0.1, relwidth=0.55, relx=0.35, rely=0.8)
    metronome_button.place_configure(relheight=0.1, relwidth=0.15, relx=0.1, rely=0.1)
    drums_theory_tutorial_button.place_configure(relheight=0.1, relwidth=0.2, relx=0.35, rely=0.1)
    drums_play_tutorial_button.place_configure(relheight=0.1, relwidth=0.2, relx=0.55, rely=0.1)
    music_img_label.place_configure(relheight=0.37, relwidth=0.25, relx=0.05, rely=0.35)

    # event bindings

    drums_back_button.bind('<Button-1>', func=drumsBack)
    metronome_button.bind('<Button-1>', func=metronomeWindow)
    drums_theory_tutorial_button.bind('<Button-1>', func=drumsStartTheoryTutorial)
    drums_play_tutorial_button.bind('<Button-1>', func=drumsShowSheet)

    drumsButtonPlay()

# guitar window


def playGuitar(self):

    # place forgets

    keyboard_button_1.place_forget()
    keyboard_button_2.place_forget()
    drums_button_1.place_forget()
    drums_button_2.place_forget()
    guitar_button_1.place_forget()
    guitar_button_2.place_forget()

    # global declarations

    global guitar_background_label, guitar_background_img, guitar_entry,\
        guitar_back_button, metronome_button, guitar_img, guitar_img_label, \
        music_img_label, music_img

    # photoimages

    guitar_background_img = tk.PhotoImage(file=os.path.join(
        IMG_MAIN_DIR, 'background_' + str(randint(1, 10)) + '.gif'))
    guitar_img = tk.PhotoImage(file=os.path.join(IMG_MAIN_DIR, 'guitar_legend.png'))
    music_img = tk.PhotoImage(file=os.path.join(IMG_MAIN_DIR, 'music.gif'))

    # Tk widgets

    guitar_background_label = tk.Label(frame, image=guitar_background_img)
    metronome_button = tk.Button(guitar_background_label, text='Metronome',
                                 bg='#14D764', font=('Helvetica', 18))
    guitar_entry = tk.Entry(guitar_background_label, bd=2,
                            insertwidth=10, justify='left', bg='#ffff99', font=('Helvetica', 18))
    guitar_back_button = tk.Button(guitar_background_label, text='BACK',
                                   bg='#e066ff', font=('Helvetica', 18))
    guitar_theory_tutorial_button = tk.Button(
        guitar_background_label, text='New to\nGuitar...', bg='#1482D7', font=('Helvetica', 18))
    guitar_play_tutorial_button = tk.Button(
        guitar_background_label, text='Need \nTutorial?', bg='#1482D7', font=('Helvetica', 18))
    guitar_img_label = tk.Label(guitar_background_label, image=guitar_img)
    music_img_label = tk.Label(guitar_background_label, image=music_img, background='black')

    # place configurations

    guitar_background_label.place_configure(
        relheight=1, relwidth=1, relx=0, rely=0)
    guitar_img_label.place_configure(
        relheight=0.5, relwidth=0.55, relx=0.35, rely=0.25)
    metronome_button.place_configure(
        relheight=0.1, relwidth=0.15, relx=0.1, rely=0.1)
    guitar_back_button.place_configure(
        relheight=0.1, relwidth=0.1, relx=0.8, rely=0.1)
    guitar_entry.place_configure(
        relheight=0.1, relwidth=0.55, relx=0.35, rely=0.8)
    guitar_theory_tutorial_button.place_configure(
        relheight=0.1, relwidth=0.2, relx=0.35, rely=0.1)
    guitar_play_tutorial_button.place_configure(
        relheight=0.1, relwidth=0.2, relx=0.55, rely=0.1)
    music_img_label.place_configure(
        relheight=0.37, relwidth=0.25, relx=0.05, rely=0.35)

    # event bindings

    metronome_button.bind('<Button-1>', func=metronomeWindow)
    guitar_theory_tutorial_button.bind(
        '<Button-1>', func=guitarStartTheoryTutorial)
    guitar_play_tutorial_button.bind(
        '<Button-1>', func=guitarStartPlayTutorial)
    guitar_back_button.bind('<Button-1>', func=guitarBack)
    guitarButtonPlay()

# place configure and bind each button


def keyboardButton1Configure():
    keyboard_button_1.place_configure(
        relheight=0.32, relwidth=0.18, relx=0.03, rely=0.1)
    keyboard_button_1.bind('<Button-1>', playKeyboard)


def keyboardButton2Configure():
    keyboard_button_2.place_configure(
        relheight=0.35, relwidth=0.18, relx=0.6, rely=0.06)
    keyboard_button_2.bind('<Button-1>', playKeyboard)


def drumsButton1Configure():
    drums_button_1.place_configure(
        relheight=0.31, relwidth=0.2, relx=0.5, rely=0.6)
    drums_button_1.bind('<Button-1>', playDrums)


def drumsButton2Configure():
    drums_button_2.place_configure(
        relheight=0.35, relwidth=0.2, relx=0.35, rely=0.03)
    drums_button_2.bind('<Button-1>', playDrums)


def guitarButton1Configure():
    guitar_button_1.place_configure(
        relheight=0.4, relwidth=0.4, relx=0.08, rely=0.45)
    guitar_button_1.bind('<Button-1>', playGuitar)


def guitarButton2Configure():
    guitar_button_2.place_configure(
        relheight=0.45, relwidth=0.2, relx=0.75, rely=0.45)
    guitar_button_2.bind('<Button-1>', playGuitar)

# choose instrument window


def chooseInstrument():

    # global declarations

    global keyboard_button_1, keyboard_button_2, drums_button_1, \
        drums_button_2, guitar_button_1, guitar_button_2, frame, \
        keyboard_button_1_img, keyboard_button_2_img, drums_button_1_img, \
        drums_button_2_img, guitar_button_1_img, guitar_button_2_img, \
        background_img, label

    # photoimages

    keyboard_button_1_img = tk.PhotoImage(
        file=os.path.join(IMG_MAIN_DIR, 'keyboard_button_1.gif'))
    keyboard_button_2_img = tk.PhotoImage(
        file=os.path.join(IMG_MAIN_DIR, 'keyboard_button_2.gif'))
    drums_button_1_img = tk.PhotoImage(
        file=os.path.join(IMG_MAIN_DIR, 'drums_button_1.gif'))
    drums_button_2_img = tk.PhotoImage(
        file=os.path.join(IMG_MAIN_DIR, 'drums_button_2.gif'))
    guitar_button_1_img = tk.PhotoImage(
        file=os.path.join(IMG_MAIN_DIR, 'guitar_button_1.gif'))
    guitar_button_2_img = tk.PhotoImage(
        file=os.path.join(IMG_MAIN_DIR, 'guitar_button_2.gif'))
    background_img = tk.PhotoImage(
        file=os.path.join(IMG_MAIN_DIR, 'background_' + str(randint(1, 10)) + '.gif'))

    # Tk widgets

    frame = tk.Frame(root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, borderwidth=5, relief='ridge')
    label = tk.Label(frame, image=background_img)
    frame.after(TITLE_DISPLAY_TIME, frame.pack)
    keyboard_button_1 = tk.Label(label, image=keyboard_button_1_img, background='red')
    keyboard_button_2 = tk.Label(label, image=keyboard_button_2_img, background='green')
    drums_button_1 = tk.Label(label, image=drums_button_1_img, background='yellow')
    drums_button_2 = tk.Label(label, image=drums_button_2_img, background='purple')
    guitar_button_1 = tk.Label(label, image=guitar_button_1_img, background='blue')
    guitar_button_2 = tk.Label(label, image=guitar_button_2_img, background='orange')

    # place configurations

    label.place_configure(relheight=1, relwidth=1, relx=0, rely=0)

    # after configurations

    keyboard_button_1.after(TITLE_DISPLAY_TIME, keyboardButton1Configure)
    keyboard_button_2.after(TITLE_DISPLAY_TIME, keyboardButton2Configure)
    drums_button_1.after(TITLE_DISPLAY_TIME, drumsButton1Configure)
    drums_button_2.after(TITLE_DISPLAY_TIME, drumsButton2Configure)
    guitar_button_1.after(TITLE_DISPLAY_TIME, guitarButton1Configure)
    guitar_button_2.after(TITLE_DISPLAY_TIME, guitarButton2Configure)

# title window


def titleWindow():

    # global declarations

    global title_image, title_label

    # photoimages

    title_image = tk.PhotoImage(
        file=os.path.join(IMG_MAIN_DIR, 'title_img.png'))

    # Tk widgets

    title_label = tk.Label(
        root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, image=title_image, background='#ffffff')

    # place configurations

    title_label.pack()

    # after bindings

    title_label.after(TITLE_DISPLAY_TIME, title_label.forget)

# play at key


def playAtKey():

    # global declarations

    global root, icon

    # Tk widgets

    root = tk.Tk()
    root.geometry("1280x720+0+0")
    root.configure(background='#ffffff')
    icon = tk.Image("photo", file=os.path.join(IMG_MAIN_DIR, 'icon.gif'))
    root.wm_iconphoto(False, icon)
    root.title("playAtKey")

    # function calls

    titleWindow()
    chooseInstrument()

    root.mainloop()

# main


if __name__ == '__main__':
    playAtKey()
