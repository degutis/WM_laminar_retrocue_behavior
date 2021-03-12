#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on March 12, 2021, at 16:02
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'WM retro-cue'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'age': '', 'sex at birth': '', 'dominant hand': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Karolis\\Desktop\\retroV1\\retroV1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
Welcome_text = visual.TextStim(win=win, name='Welcome_text',
    text='Welcome to the experiment!\n(Press space to continue)',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space1 = keyboard.Keyboard()

# Initialize components for Routine "Instr1"
Instr1Clock = core.Clock()
Instruction_text = visual.TextStim(win=win, name='Instruction_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space2 = keyboard.Keyboard()

# Initialize components for Routine "trial_Instr"
trial_InstrClock = core.Clock()
stim1_inst = visual.ImageStim(
    win=win,
    name='stim1_inst', 
    image='sin', mask=None,
    ori=0, pos=(-0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
stim2_inst = visual.ImageStim(
    win=win,
    name='stim2_inst', 
    image='sin', mask=None,
    ori=0, pos=(0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
trialExplanation = visual.TextStim(win=win, name='trialExplanation',
    text='You can see the first memory set here',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
space3 = keyboard.Keyboard()

# Initialize components for Routine "masks_Instr"
masks_InstrClock = core.Clock()
mask1_inst = visual.ImageStim(
    win=win,
    name='mask1_inst', 
    image='sin', mask=None,
    ori=0, pos=(-0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
mask2_inst = visual.ImageStim(
    win=win,
    name='mask2_inst', 
    image='sin', mask=None,
    ori=0, pos=(0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

# Initialize components for Routine "trial_Instr_2"
trial_Instr_2Clock = core.Clock()
stim3_instr = visual.ImageStim(
    win=win,
    name='stim3_instr', 
    image='sin', mask=None,
    ori=0, pos=(-0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
stim4_inst = visual.ImageStim(
    win=win,
    name='stim4_inst', 
    image='sin', mask=None,
    ori=0, pos=(0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
trialExplanation_2 = visual.TextStim(win=win, name='trialExplanation_2',
    text='You can see the second memory set here',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
space3_2 = keyboard.Keyboard()

# Initialize components for Routine "masks_Instr_2"
masks_Instr_2Clock = core.Clock()
mask1_inst_2 = visual.ImageStim(
    win=win,
    name='mask1_inst_2', 
    image='sin', mask=None,
    ori=0, pos=(-0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
mask2_inst_2 = visual.ImageStim(
    win=win,
    name='mask2_inst_2', 
    image='sin', mask=None,
    ori=0, pos=(0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

# Initialize components for Routine "cue_Instr"
cue_InstrClock = core.Clock()
cue_txt = visual.TextStim(win=win, name='cue_txt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
cue_instrtxt = visual.TextStim(win=win, name='cue_instrtxt',
    text='This number is the cue. It indicates which memory set you have to remember. Either the initially presented one (when cue=1) or the subsequent one (when cue=2).  ',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
space_InstrCue = keyboard.Keyboard()

# Initialize components for Routine "delayInst"
delayInstClock = core.Clock()
fixDelay_2 = visual.ShapeStim(
    win=win, name='fixDelay_2', vertices='cross',
    size=(0.01, 0.01),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
delayExplanation = visual.TextStim(win=win, name='delayExplanation',
    text='The red cross indicates the delay period. You have to keep the cued images in mind during this time. Fixate on the cross whenever it is present. No response can be made during this time.  ',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
space4 = keyboard.Keyboard()

# Initialize components for Routine "responseInst"
responseInstClock = core.Clock()
probe_inst = visual.ImageStim(
    win=win,
    name='probe_inst', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
probeIndicator_inst = visual.TextStim(win=win, name='probeIndicator_inst',
    text='default text',
    font='Arial',
    pos=(0,0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
fixProbe_inst = visual.ShapeStim(
    win=win, name='fixProbe_inst', vertices='cross',
    size=(0.01, 0.01),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0,1,0], lineColorSpace='rgb',
    fillColor=[0,1,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
reponseInstr = keyboard.Keyboard()
probeInst = visual.TextStim(win=win, name='probeInst',
    text='You just saw the test image. In this case, it was part of the memorized images. You also saw an arrow above the image. Press the correct arrow key to continue. You can answer immediately after the test image is presented without waiting for the green fixation cross. ',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "responseInst_uncued"
responseInst_uncuedClock = core.Clock()
probe_inst_2 = visual.ImageStim(
    win=win,
    name='probe_inst_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
probeIndicator_inst_2 = visual.TextStim(win=win, name='probeIndicator_inst_2',
    text='default text',
    font='Arial',
    pos=(0,0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
fixProbe_inst_2 = visual.ShapeStim(
    win=win, name='fixProbe_inst_2', vertices='cross',
    size=(0.01, 0.01),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0,1,0], lineColorSpace='rgb',
    fillColor=[0,1,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
reponseInstr_2 = keyboard.Keyboard()
probeInst_2 = visual.TextStim(win=win, name='probeInst_2',
    text='Surprise! On this trial you are also tested on the non-cued memory set. Since the presented test image was NOT part of the non-cued memory, you should click the OPPOSITE arrow key for a correct answer. ',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "reward"
rewardClock = core.Clock()
rewardInst = visual.TextStim(win=win, name='rewardInst',
    text="Great! \nWe will now have a couple of training trials to make sure you understood the task. (Press 'space')",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space5 = keyboard.Keyboard()

# Initialize components for Routine "reminderButtons"
reminderButtonsClock = core.Clock()
Button_reminder = visual.TextStim(win=win, name='Button_reminder',
    text='Response reminder: left arrow if "<" and test image was part of memory images. \nRight arrow if ">" and test image was part of memory images\nOPPOSITE arrow key press if test image was NOT part of memory images\n(Press \'space\' to start practice trials)',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space6 = keyboard.Keyboard()

# Initialize components for Routine "trialBegBlank_practice"
trialBegBlank_practiceClock = core.Clock()
fixStartTrial_2 = visual.ShapeStim(
    win=win, name='fixStartTrial_2', vertices='cross',
    size=(0.01, 0.01),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "trial_practice"
trial_practiceClock = core.Clock()
stim1_Practice = visual.ImageStim(
    win=win,
    name='stim1_Practice', 
    image='sin', mask=None,
    ori=0, pos=(-0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
stim2_Practice = visual.ImageStim(
    win=win,
    name='stim2_Practice', 
    image='sin', mask=None,
    ori=0, pos=(0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
mask1_prac = visual.ImageStim(
    win=win,
    name='mask1_prac', 
    image='sin', mask=None,
    ori=0, pos=(-0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
mask2_prac = visual.ImageStim(
    win=win,
    name='mask2_prac', 
    image='sin', mask=None,
    ori=0, pos=(0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
cross_postMem1 = visual.ShapeStim(
    win=win, name='cross_postMem1', vertices='cross',
    size=(0.01, 0.01),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
stim3_Practice = visual.ImageStim(
    win=win,
    name='stim3_Practice', 
    image='sin', mask=None,
    ori=0, pos=(-0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
stim4_Practice = visual.ImageStim(
    win=win,
    name='stim4_Practice', 
    image='sin', mask=None,
    ori=0, pos=(0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
mask3_prac = visual.ImageStim(
    win=win,
    name='mask3_prac', 
    image='sin', mask=None,
    ori=0, pos=(-0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
mask4_prac = visual.ImageStim(
    win=win,
    name='mask4_prac', 
    image='sin', mask=None,
    ori=0, pos=(0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
cross_postMem2 = visual.ShapeStim(
    win=win, name='cross_postMem2', vertices='cross',
    size=(0.01, 0.01),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
cueInstr = visual.TextStim(win=win, name='cueInstr',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
fixDelay_Practice = visual.ShapeStim(
    win=win, name='fixDelay_Practice', vertices='cross',
    size=(0.01, 0.01),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
probe_Practice = visual.ImageStim(
    win=win,
    name='probe_Practice', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-12.0)
probeIndicator_Practice = visual.TextStim(win=win, name='probeIndicator_Practice',
    text='default text',
    font='Arial',
    pos=(0,0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
fixProbe_Practice = visual.ShapeStim(
    win=win, name='fixProbe_Practice', vertices='cross',
    size=(0.01, 0.01),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0,1,0], lineColorSpace='rgb',
    fillColor=[0,1,0], fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
keyResp_Practice = keyboard.Keyboard()

# Initialize components for Routine "feedback_2"
feedback_2Clock = core.Clock()
msg=""
feedbackText = visual.TextStim(win=win, name='feedbackText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "noncuedProbe_Practice"
noncuedProbe_PracticeClock = core.Clock()
Probe_Noncued_Instr = visual.ImageStim(
    win=win,
    name='Probe_Noncued_Instr', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
nonCuedProbeIndicator_practice = visual.TextStim(win=win, name='nonCuedProbeIndicator_practice',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
crossNonCued = visual.ShapeStim(
    win=win, name='crossNonCued', vertices='cross',
    size=(0.01, 0.01),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0,1,0], lineColorSpace='rgb',
    fillColor=[0,1,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
key_resp_NonCue_practice = keyboard.Keyboard()

# Initialize components for Routine "feedback_2_noncue"
feedback_2_noncueClock = core.Clock()
msg=""
feedbackText_2 = visual.TextStim(win=win, name='feedbackText_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "perceptCorrectCalc_practice"
perceptCorrectCalc_practiceClock = core.Clock()

# Initialize components for Routine "feedbackTest"
feedbackTestClock = core.Clock()
key_resp_5 = keyboard.Keyboard()
text_7 = visual.TextStim(win=win, name='text_7',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Before_run"
Before_runClock = core.Clock()
text_run = visual.TextStim(win=win, name='text_run',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "blankStart"
blankStartClock = core.Clock()
fixStart = visual.ShapeStim(
    win=win, name='fixStart', vertices='cross',
    size=(0.01, 0.01),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "trial"
trialClock = core.Clock()
stim1 = visual.ImageStim(
    win=win,
    name='stim1', 
    image='sin', mask=None,
    ori=0, pos=(-0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
stim2 = visual.ImageStim(
    win=win,
    name='stim2', 
    image='sin', mask=None,
    ori=0, pos=(0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
mask1 = visual.ImageStim(
    win=win,
    name='mask1', 
    image='sin', mask=None,
    ori=0, pos=(-0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
mask2 = visual.ImageStim(
    win=win,
    name='mask2', 
    image='sin', mask=None,
    ori=0, pos=(0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
cross_postMem1_2 = visual.ShapeStim(
    win=win, name='cross_postMem1_2', vertices='cross',
    size=(0.01, 0.01),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
stim3 = visual.ImageStim(
    win=win,
    name='stim3', 
    image='sin', mask=None,
    ori=0, pos=(-0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
stim4 = visual.ImageStim(
    win=win,
    name='stim4', 
    image='sin', mask=None,
    ori=0, pos=(0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
mask3 = visual.ImageStim(
    win=win,
    name='mask3', 
    image='sin', mask=None,
    ori=0, pos=(-0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
mask4 = visual.ImageStim(
    win=win,
    name='mask4', 
    image='sin', mask=None,
    ori=0, pos=(0.11, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
cross_postMem2_2 = visual.ShapeStim(
    win=win, name='cross_postMem2_2', vertices='cross',
    size=(0.01, 0.01),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
cue_run = visual.TextStim(win=win, name='cue_run',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
fixDelay = visual.ShapeStim(
    win=win, name='fixDelay', vertices='cross',
    size=(0.01, 0.01),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
probe_run = visual.ImageStim(
    win=win,
    name='probe_run', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-12.0)
probeIndicator = visual.TextStim(win=win, name='probeIndicator',
    text='default text',
    font='Arial',
    pos=(0,0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
fixProbe = visual.ShapeStim(
    win=win, name='fixProbe', vertices='cross',
    size=(0.01, 0.01),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0,1,0], lineColorSpace='rgb',
    fillColor=[0,1,0], fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
keyResp = keyboard.Keyboard()

# Initialize components for Routine "noncuedProbe"
noncuedProbeClock = core.Clock()
Probe_Noncued_Instr_2 = visual.ImageStim(
    win=win,
    name='Probe_Noncued_Instr_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
nonCuedProbeIndicator_practice_2 = visual.TextStim(win=win, name='nonCuedProbeIndicator_practice_2',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
crossNonCued_2 = visual.ShapeStim(
    win=win, name='crossNonCued_2', vertices='cross',
    size=(0.01, 0.01),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0,1,0], lineColorSpace='rgb',
    fillColor=[0,1,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
key_resp_NonCue = keyboard.Keyboard()

# Initialize components for Routine "trialEndBlank"
trialEndBlankClock = core.Clock()
fixStartTrial = visual.ShapeStim(
    win=win, name='fixStartTrial', vertices='cross',
    size=(0.01, 0.01),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "blankEnd"
blankEndClock = core.Clock()
fixEnd = visual.ShapeStim(
    win=win, name='fixEnd', vertices='cross',
    size=(0.01, 0.01),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "feedback_Run"
feedback_RunClock = core.Clock()
space_Run = keyboard.Keyboard()
feedbackTxtRun = visual.TextStim(win=win, name='feedbackTxtRun',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "finalRoutine"
finalRoutineClock = core.Clock()
space_final = keyboard.Keyboard()
txt_final = visual.TextStim(win=win, name='txt_final',
    text="Congratulations! You have finished the experiment. Press 'space' one last time.  ",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
# update component parameters for each repeat
space1.keys = []
space1.rt = []
_space1_allKeys = []
# keep track of which components have finished
WelcomeComponents = [Welcome_text, space1]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome_text* updates
    if Welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome_text.frameNStart = frameN  # exact frame index
        Welcome_text.tStart = t  # local t and not account for scr refresh
        Welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome_text, 'tStartRefresh')  # time at next scr refresh
        Welcome_text.setAutoDraw(True)
    
    # *space1* updates
    waitOnFlip = False
    if space1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space1.frameNStart = frameN  # exact frame index
        space1.tStart = t  # local t and not account for scr refresh
        space1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space1, 'tStartRefresh')  # time at next scr refresh
        space1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space1.status == STARTED and not waitOnFlip:
        theseKeys = space1.getKeys(keyList=['space'], waitRelease=False)
        _space1_allKeys.extend(theseKeys)
        if len(_space1_allKeys):
            space1.keys = _space1_allKeys[-1].name  # just the last key pressed
            space1.rt = _space1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Welcome_text.started', Welcome_text.tStartRefresh)
thisExp.addData('Welcome_text.stopped', Welcome_text.tStopRefresh)
# check responses
if space1.keys in ['', [], None]:  # No response was made
    space1.keys = None
thisExp.addData('space1.keys',space1.keys)
if space1.keys != None:  # we had a response
    thisExp.addData('space1.rt', space1.rt)
thisExp.addData('space1.started', space1.tStartRefresh)
thisExp.addData('space1.stopped', space1.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
instructionLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('instructionTxt.xlsx'),
    seed=None, name='instructionLoop')
thisExp.addLoop(instructionLoop)  # add the loop to the experiment
thisInstructionLoop = instructionLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstructionLoop.rgb)
if thisInstructionLoop != None:
    for paramName in thisInstructionLoop:
        exec('{} = thisInstructionLoop[paramName]'.format(paramName))

for thisInstructionLoop in instructionLoop:
    currentLoop = instructionLoop
    # abbreviate parameter names if possible (e.g. rgb = thisInstructionLoop.rgb)
    if thisInstructionLoop != None:
        for paramName in thisInstructionLoop:
            exec('{} = thisInstructionLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instr1"-------
    continueRoutine = True
    # update component parameters for each repeat
    Instruction_text.setText(instructions)
    space2.keys = []
    space2.rt = []
    _space2_allKeys = []
    # keep track of which components have finished
    Instr1Components = [Instruction_text, space2]
    for thisComponent in Instr1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Instr1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Instr1"-------
    while continueRoutine:
        # get current time
        t = Instr1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Instr1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instruction_text* updates
        if Instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instruction_text.frameNStart = frameN  # exact frame index
            Instruction_text.tStart = t  # local t and not account for scr refresh
            Instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instruction_text, 'tStartRefresh')  # time at next scr refresh
            Instruction_text.setAutoDraw(True)
        
        # *space2* updates
        waitOnFlip = False
        if space2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space2.frameNStart = frameN  # exact frame index
            space2.tStart = t  # local t and not account for scr refresh
            space2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space2, 'tStartRefresh')  # time at next scr refresh
            space2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space2.status == STARTED and not waitOnFlip:
            theseKeys = space2.getKeys(keyList=['space'], waitRelease=False)
            _space2_allKeys.extend(theseKeys)
            if len(_space2_allKeys):
                space2.keys = _space2_allKeys[-1].name  # just the last key pressed
                space2.rt = _space2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instr1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instr1"-------
    for thisComponent in Instr1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructionLoop.addData('Instruction_text.started', Instruction_text.tStartRefresh)
    instructionLoop.addData('Instruction_text.stopped', Instruction_text.tStopRefresh)
    # check responses
    if space2.keys in ['', [], None]:  # No response was made
        space2.keys = None
    instructionLoop.addData('space2.keys',space2.keys)
    if space2.keys != None:  # we had a response
        instructionLoop.addData('space2.rt', space2.rt)
    instructionLoop.addData('space2.started', space2.tStartRefresh)
    instructionLoop.addData('space2.stopped', space2.tStopRefresh)
    # the Routine "Instr1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'instructionLoop'

# get names of stimulus parameters
if instructionLoop.trialList in ([], [None], None):
    params = []
else:
    params = instructionLoop.trialList[0].keys()
# save data for this loop
instructionLoop.saveAsText(filename + 'instructionLoop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
trials_Instr = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trials_Instr.csv', selection='0'),
    seed=None, name='trials_Instr')
thisExp.addLoop(trials_Instr)  # add the loop to the experiment
thisTrials_Instr = trials_Instr.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_Instr.rgb)
if thisTrials_Instr != None:
    for paramName in thisTrials_Instr:
        exec('{} = thisTrials_Instr[paramName]'.format(paramName))

for thisTrials_Instr in trials_Instr:
    currentLoop = trials_Instr
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_Instr.rgb)
    if thisTrials_Instr != None:
        for paramName in thisTrials_Instr:
            exec('{} = thisTrials_Instr[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_Instr"-------
    continueRoutine = True
    # update component parameters for each repeat
    stim1_inst.setImage(image1L)
    stim2_inst.setImage(image1R)
    space3.keys = []
    space3.rt = []
    _space3_allKeys = []
    # keep track of which components have finished
    trial_InstrComponents = [stim1_inst, stim2_inst, trialExplanation, space3]
    for thisComponent in trial_InstrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_InstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_Instr"-------
    while continueRoutine:
        # get current time
        t = trial_InstrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_InstrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim1_inst* updates
        if stim1_inst.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stim1_inst.frameNStart = frameN  # exact frame index
            stim1_inst.tStart = t  # local t and not account for scr refresh
            stim1_inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim1_inst, 'tStartRefresh')  # time at next scr refresh
            stim1_inst.setAutoDraw(True)
        
        # *stim2_inst* updates
        if stim2_inst.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stim2_inst.frameNStart = frameN  # exact frame index
            stim2_inst.tStart = t  # local t and not account for scr refresh
            stim2_inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim2_inst, 'tStartRefresh')  # time at next scr refresh
            stim2_inst.setAutoDraw(True)
        
        # *trialExplanation* updates
        if trialExplanation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialExplanation.frameNStart = frameN  # exact frame index
            trialExplanation.tStart = t  # local t and not account for scr refresh
            trialExplanation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialExplanation, 'tStartRefresh')  # time at next scr refresh
            trialExplanation.setAutoDraw(True)
        
        # *space3* updates
        waitOnFlip = False
        if space3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space3.frameNStart = frameN  # exact frame index
            space3.tStart = t  # local t and not account for scr refresh
            space3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space3, 'tStartRefresh')  # time at next scr refresh
            space3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space3.status == STARTED and not waitOnFlip:
            theseKeys = space3.getKeys(keyList=['space'], waitRelease=False)
            _space3_allKeys.extend(theseKeys)
            if len(_space3_allKeys):
                space3.keys = _space3_allKeys[-1].name  # just the last key pressed
                space3.rt = _space3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_InstrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_Instr"-------
    for thisComponent in trial_InstrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_Instr.addData('stim1_inst.started', stim1_inst.tStartRefresh)
    trials_Instr.addData('stim1_inst.stopped', stim1_inst.tStopRefresh)
    trials_Instr.addData('stim2_inst.started', stim2_inst.tStartRefresh)
    trials_Instr.addData('stim2_inst.stopped', stim2_inst.tStopRefresh)
    trials_Instr.addData('trialExplanation.started', trialExplanation.tStartRefresh)
    trials_Instr.addData('trialExplanation.stopped', trialExplanation.tStopRefresh)
    # check responses
    if space3.keys in ['', [], None]:  # No response was made
        space3.keys = None
    trials_Instr.addData('space3.keys',space3.keys)
    if space3.keys != None:  # we had a response
        trials_Instr.addData('space3.rt', space3.rt)
    trials_Instr.addData('space3.started', space3.tStartRefresh)
    trials_Instr.addData('space3.stopped', space3.tStopRefresh)
    # the Routine "trial_Instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "masks_Instr"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    mask1_inst.setImage(scramble1L)
    mask2_inst.setImage(scramble1R)
    # keep track of which components have finished
    masks_InstrComponents = [mask1_inst, mask2_inst]
    for thisComponent in masks_InstrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    masks_InstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "masks_Instr"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = masks_InstrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=masks_InstrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *mask1_inst* updates
        if mask1_inst.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            mask1_inst.frameNStart = frameN  # exact frame index
            mask1_inst.tStart = t  # local t and not account for scr refresh
            mask1_inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask1_inst, 'tStartRefresh')  # time at next scr refresh
            mask1_inst.setAutoDraw(True)
        if mask1_inst.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask1_inst.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                mask1_inst.tStop = t  # not accounting for scr refresh
                mask1_inst.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mask1_inst, 'tStopRefresh')  # time at next scr refresh
                mask1_inst.setAutoDraw(False)
        
        # *mask2_inst* updates
        if mask2_inst.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            mask2_inst.frameNStart = frameN  # exact frame index
            mask2_inst.tStart = t  # local t and not account for scr refresh
            mask2_inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask2_inst, 'tStartRefresh')  # time at next scr refresh
            mask2_inst.setAutoDraw(True)
        if mask2_inst.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask2_inst.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                mask2_inst.tStop = t  # not accounting for scr refresh
                mask2_inst.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mask2_inst, 'tStopRefresh')  # time at next scr refresh
                mask2_inst.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in masks_InstrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "masks_Instr"-------
    for thisComponent in masks_InstrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_Instr.addData('mask1_inst.started', mask1_inst.tStartRefresh)
    trials_Instr.addData('mask1_inst.stopped', mask1_inst.tStopRefresh)
    trials_Instr.addData('mask2_inst.started', mask2_inst.tStartRefresh)
    trials_Instr.addData('mask2_inst.stopped', mask2_inst.tStopRefresh)
    
    # ------Prepare to start Routine "trial_Instr_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    stim3_instr.setImage(image2L)
    stim4_inst.setImage(image2R)
    space3_2.keys = []
    space3_2.rt = []
    _space3_2_allKeys = []
    # keep track of which components have finished
    trial_Instr_2Components = [stim3_instr, stim4_inst, trialExplanation_2, space3_2]
    for thisComponent in trial_Instr_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_Instr_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_Instr_2"-------
    while continueRoutine:
        # get current time
        t = trial_Instr_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_Instr_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim3_instr* updates
        if stim3_instr.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stim3_instr.frameNStart = frameN  # exact frame index
            stim3_instr.tStart = t  # local t and not account for scr refresh
            stim3_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim3_instr, 'tStartRefresh')  # time at next scr refresh
            stim3_instr.setAutoDraw(True)
        
        # *stim4_inst* updates
        if stim4_inst.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stim4_inst.frameNStart = frameN  # exact frame index
            stim4_inst.tStart = t  # local t and not account for scr refresh
            stim4_inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim4_inst, 'tStartRefresh')  # time at next scr refresh
            stim4_inst.setAutoDraw(True)
        
        # *trialExplanation_2* updates
        if trialExplanation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialExplanation_2.frameNStart = frameN  # exact frame index
            trialExplanation_2.tStart = t  # local t and not account for scr refresh
            trialExplanation_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialExplanation_2, 'tStartRefresh')  # time at next scr refresh
            trialExplanation_2.setAutoDraw(True)
        
        # *space3_2* updates
        waitOnFlip = False
        if space3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space3_2.frameNStart = frameN  # exact frame index
            space3_2.tStart = t  # local t and not account for scr refresh
            space3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space3_2, 'tStartRefresh')  # time at next scr refresh
            space3_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space3_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space3_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space3_2.status == STARTED and not waitOnFlip:
            theseKeys = space3_2.getKeys(keyList=['space'], waitRelease=False)
            _space3_2_allKeys.extend(theseKeys)
            if len(_space3_2_allKeys):
                space3_2.keys = _space3_2_allKeys[-1].name  # just the last key pressed
                space3_2.rt = _space3_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_Instr_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_Instr_2"-------
    for thisComponent in trial_Instr_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_Instr.addData('stim3_instr.started', stim3_instr.tStartRefresh)
    trials_Instr.addData('stim3_instr.stopped', stim3_instr.tStopRefresh)
    trials_Instr.addData('stim4_inst.started', stim4_inst.tStartRefresh)
    trials_Instr.addData('stim4_inst.stopped', stim4_inst.tStopRefresh)
    trials_Instr.addData('trialExplanation_2.started', trialExplanation_2.tStartRefresh)
    trials_Instr.addData('trialExplanation_2.stopped', trialExplanation_2.tStopRefresh)
    # check responses
    if space3_2.keys in ['', [], None]:  # No response was made
        space3_2.keys = None
    trials_Instr.addData('space3_2.keys',space3_2.keys)
    if space3_2.keys != None:  # we had a response
        trials_Instr.addData('space3_2.rt', space3_2.rt)
    trials_Instr.addData('space3_2.started', space3_2.tStartRefresh)
    trials_Instr.addData('space3_2.stopped', space3_2.tStopRefresh)
    # the Routine "trial_Instr_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "masks_Instr_2"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    mask1_inst_2.setImage(scramble2L)
    mask2_inst_2.setImage(scramble2R)
    # keep track of which components have finished
    masks_Instr_2Components = [mask1_inst_2, mask2_inst_2]
    for thisComponent in masks_Instr_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    masks_Instr_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "masks_Instr_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = masks_Instr_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=masks_Instr_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *mask1_inst_2* updates
        if mask1_inst_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            mask1_inst_2.frameNStart = frameN  # exact frame index
            mask1_inst_2.tStart = t  # local t and not account for scr refresh
            mask1_inst_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask1_inst_2, 'tStartRefresh')  # time at next scr refresh
            mask1_inst_2.setAutoDraw(True)
        if mask1_inst_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask1_inst_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                mask1_inst_2.tStop = t  # not accounting for scr refresh
                mask1_inst_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mask1_inst_2, 'tStopRefresh')  # time at next scr refresh
                mask1_inst_2.setAutoDraw(False)
        
        # *mask2_inst_2* updates
        if mask2_inst_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            mask2_inst_2.frameNStart = frameN  # exact frame index
            mask2_inst_2.tStart = t  # local t and not account for scr refresh
            mask2_inst_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask2_inst_2, 'tStartRefresh')  # time at next scr refresh
            mask2_inst_2.setAutoDraw(True)
        if mask2_inst_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask2_inst_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                mask2_inst_2.tStop = t  # not accounting for scr refresh
                mask2_inst_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mask2_inst_2, 'tStopRefresh')  # time at next scr refresh
                mask2_inst_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in masks_Instr_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "masks_Instr_2"-------
    for thisComponent in masks_Instr_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_Instr.addData('mask1_inst_2.started', mask1_inst_2.tStartRefresh)
    trials_Instr.addData('mask1_inst_2.stopped', mask1_inst_2.tStopRefresh)
    trials_Instr.addData('mask2_inst_2.started', mask2_inst_2.tStartRefresh)
    trials_Instr.addData('mask2_inst_2.stopped', mask2_inst_2.tStopRefresh)
    
    # ------Prepare to start Routine "cue_Instr"-------
    continueRoutine = True
    # update component parameters for each repeat
    cue_txt.setText(cue)
    space_InstrCue.keys = []
    space_InstrCue.rt = []
    _space_InstrCue_allKeys = []
    # keep track of which components have finished
    cue_InstrComponents = [cue_txt, cue_instrtxt, space_InstrCue]
    for thisComponent in cue_InstrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    cue_InstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "cue_Instr"-------
    while continueRoutine:
        # get current time
        t = cue_InstrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=cue_InstrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cue_txt* updates
        if cue_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue_txt.frameNStart = frameN  # exact frame index
            cue_txt.tStart = t  # local t and not account for scr refresh
            cue_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_txt, 'tStartRefresh')  # time at next scr refresh
            cue_txt.setAutoDraw(True)
        
        # *cue_instrtxt* updates
        if cue_instrtxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue_instrtxt.frameNStart = frameN  # exact frame index
            cue_instrtxt.tStart = t  # local t and not account for scr refresh
            cue_instrtxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_instrtxt, 'tStartRefresh')  # time at next scr refresh
            cue_instrtxt.setAutoDraw(True)
        
        # *space_InstrCue* updates
        waitOnFlip = False
        if space_InstrCue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space_InstrCue.frameNStart = frameN  # exact frame index
            space_InstrCue.tStart = t  # local t and not account for scr refresh
            space_InstrCue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_InstrCue, 'tStartRefresh')  # time at next scr refresh
            space_InstrCue.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space_InstrCue.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space_InstrCue.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space_InstrCue.status == STARTED and not waitOnFlip:
            theseKeys = space_InstrCue.getKeys(keyList=['space'], waitRelease=False)
            _space_InstrCue_allKeys.extend(theseKeys)
            if len(_space_InstrCue_allKeys):
                space_InstrCue.keys = _space_InstrCue_allKeys[-1].name  # just the last key pressed
                space_InstrCue.rt = _space_InstrCue_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cue_InstrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cue_Instr"-------
    for thisComponent in cue_InstrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_Instr.addData('cue_txt.started', cue_txt.tStartRefresh)
    trials_Instr.addData('cue_txt.stopped', cue_txt.tStopRefresh)
    trials_Instr.addData('cue_instrtxt.started', cue_instrtxt.tStartRefresh)
    trials_Instr.addData('cue_instrtxt.stopped', cue_instrtxt.tStopRefresh)
    # check responses
    if space_InstrCue.keys in ['', [], None]:  # No response was made
        space_InstrCue.keys = None
    trials_Instr.addData('space_InstrCue.keys',space_InstrCue.keys)
    if space_InstrCue.keys != None:  # we had a response
        trials_Instr.addData('space_InstrCue.rt', space_InstrCue.rt)
    trials_Instr.addData('space_InstrCue.started', space_InstrCue.tStartRefresh)
    trials_Instr.addData('space_InstrCue.stopped', space_InstrCue.tStopRefresh)
    # the Routine "cue_Instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "delayInst"-------
    continueRoutine = True
    # update component parameters for each repeat
    space4.keys = []
    space4.rt = []
    _space4_allKeys = []
    # keep track of which components have finished
    delayInstComponents = [fixDelay_2, delayExplanation, space4]
    for thisComponent in delayInstComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    delayInstClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "delayInst"-------
    while continueRoutine:
        # get current time
        t = delayInstClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=delayInstClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixDelay_2* updates
        if fixDelay_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            fixDelay_2.frameNStart = frameN  # exact frame index
            fixDelay_2.tStart = t  # local t and not account for scr refresh
            fixDelay_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixDelay_2, 'tStartRefresh')  # time at next scr refresh
            fixDelay_2.setAutoDraw(True)
        
        # *delayExplanation* updates
        if delayExplanation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            delayExplanation.frameNStart = frameN  # exact frame index
            delayExplanation.tStart = t  # local t and not account for scr refresh
            delayExplanation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(delayExplanation, 'tStartRefresh')  # time at next scr refresh
            delayExplanation.setAutoDraw(True)
        
        # *space4* updates
        waitOnFlip = False
        if space4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space4.frameNStart = frameN  # exact frame index
            space4.tStart = t  # local t and not account for scr refresh
            space4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space4, 'tStartRefresh')  # time at next scr refresh
            space4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space4.status == STARTED and not waitOnFlip:
            theseKeys = space4.getKeys(keyList=['space'], waitRelease=False)
            _space4_allKeys.extend(theseKeys)
            if len(_space4_allKeys):
                space4.keys = _space4_allKeys[-1].name  # just the last key pressed
                space4.rt = _space4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in delayInstComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "delayInst"-------
    for thisComponent in delayInstComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_Instr.addData('fixDelay_2.started', fixDelay_2.tStartRefresh)
    trials_Instr.addData('fixDelay_2.stopped', fixDelay_2.tStopRefresh)
    trials_Instr.addData('delayExplanation.started', delayExplanation.tStartRefresh)
    trials_Instr.addData('delayExplanation.stopped', delayExplanation.tStopRefresh)
    # check responses
    if space4.keys in ['', [], None]:  # No response was made
        space4.keys = None
    trials_Instr.addData('space4.keys',space4.keys)
    if space4.keys != None:  # we had a response
        trials_Instr.addData('space4.rt', space4.rt)
    trials_Instr.addData('space4.started', space4.tStartRefresh)
    trials_Instr.addData('space4.stopped', space4.tStopRefresh)
    # the Routine "delayInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "responseInst"-------
    continueRoutine = True
    # update component parameters for each repeat
    probe_inst.setImage(imageCuedProbe)
    probeIndicator_inst.setText(arrow
)
    reponseInstr.keys = []
    reponseInstr.rt = []
    _reponseInstr_allKeys = []
    # keep track of which components have finished
    responseInstComponents = [probe_inst, probeIndicator_inst, fixProbe_inst, reponseInstr, probeInst]
    for thisComponent in responseInstComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    responseInstClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "responseInst"-------
    while continueRoutine:
        # get current time
        t = responseInstClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=responseInstClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *probe_inst* updates
        if probe_inst.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            probe_inst.frameNStart = frameN  # exact frame index
            probe_inst.tStart = t  # local t and not account for scr refresh
            probe_inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(probe_inst, 'tStartRefresh')  # time at next scr refresh
            probe_inst.setAutoDraw(True)
        if probe_inst.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > probe_inst.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                probe_inst.tStop = t  # not accounting for scr refresh
                probe_inst.frameNStop = frameN  # exact frame index
                win.timeOnFlip(probe_inst, 'tStopRefresh')  # time at next scr refresh
                probe_inst.setAutoDraw(False)
        
        # *probeIndicator_inst* updates
        if probeIndicator_inst.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            probeIndicator_inst.frameNStart = frameN  # exact frame index
            probeIndicator_inst.tStart = t  # local t and not account for scr refresh
            probeIndicator_inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(probeIndicator_inst, 'tStartRefresh')  # time at next scr refresh
            probeIndicator_inst.setAutoDraw(True)
        if probeIndicator_inst.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > probeIndicator_inst.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                probeIndicator_inst.tStop = t  # not accounting for scr refresh
                probeIndicator_inst.frameNStop = frameN  # exact frame index
                win.timeOnFlip(probeIndicator_inst, 'tStopRefresh')  # time at next scr refresh
                probeIndicator_inst.setAutoDraw(False)
        
        # *fixProbe_inst* updates
        if fixProbe_inst.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            fixProbe_inst.frameNStart = frameN  # exact frame index
            fixProbe_inst.tStart = t  # local t and not account for scr refresh
            fixProbe_inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixProbe_inst, 'tStartRefresh')  # time at next scr refresh
            fixProbe_inst.setAutoDraw(True)
        
        # *reponseInstr* updates
        waitOnFlip = False
        if reponseInstr.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            reponseInstr.frameNStart = frameN  # exact frame index
            reponseInstr.tStart = t  # local t and not account for scr refresh
            reponseInstr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reponseInstr, 'tStartRefresh')  # time at next scr refresh
            reponseInstr.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(reponseInstr.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(reponseInstr.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if reponseInstr.status == STARTED and not waitOnFlip:
            theseKeys = reponseInstr.getKeys(keyList=['right'], waitRelease=False)
            _reponseInstr_allKeys.extend(theseKeys)
            if len(_reponseInstr_allKeys):
                reponseInstr.keys = _reponseInstr_allKeys[-1].name  # just the last key pressed
                reponseInstr.rt = _reponseInstr_allKeys[-1].rt
                # was this correct?
                if (reponseInstr.keys == str(buttonCorrect)) or (reponseInstr.keys == buttonCorrect):
                    reponseInstr.corr = 1
                else:
                    reponseInstr.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *probeInst* updates
        if probeInst.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            probeInst.frameNStart = frameN  # exact frame index
            probeInst.tStart = t  # local t and not account for scr refresh
            probeInst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(probeInst, 'tStartRefresh')  # time at next scr refresh
            probeInst.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in responseInstComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "responseInst"-------
    for thisComponent in responseInstComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_Instr.addData('probe_inst.started', probe_inst.tStartRefresh)
    trials_Instr.addData('probe_inst.stopped', probe_inst.tStopRefresh)
    trials_Instr.addData('probeIndicator_inst.started', probeIndicator_inst.tStartRefresh)
    trials_Instr.addData('probeIndicator_inst.stopped', probeIndicator_inst.tStopRefresh)
    trials_Instr.addData('fixProbe_inst.started', fixProbe_inst.tStartRefresh)
    trials_Instr.addData('fixProbe_inst.stopped', fixProbe_inst.tStopRefresh)
    # check responses
    if reponseInstr.keys in ['', [], None]:  # No response was made
        reponseInstr.keys = None
        # was no response the correct answer?!
        if str(buttonCorrect).lower() == 'none':
           reponseInstr.corr = 1;  # correct non-response
        else:
           reponseInstr.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_Instr (TrialHandler)
    trials_Instr.addData('reponseInstr.keys',reponseInstr.keys)
    trials_Instr.addData('reponseInstr.corr', reponseInstr.corr)
    if reponseInstr.keys != None:  # we had a response
        trials_Instr.addData('reponseInstr.rt', reponseInstr.rt)
    trials_Instr.addData('reponseInstr.started', reponseInstr.tStartRefresh)
    trials_Instr.addData('reponseInstr.stopped', reponseInstr.tStopRefresh)
    trials_Instr.addData('probeInst.started', probeInst.tStartRefresh)
    trials_Instr.addData('probeInst.stopped', probeInst.tStopRefresh)
    # the Routine "responseInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "responseInst_uncued"-------
    continueRoutine = True
    # update component parameters for each repeat
    probe_inst_2.setImage(imageUncuedProbe)
    probeIndicator_inst_2.setText(arrow
)
    reponseInstr_2.keys = []
    reponseInstr_2.rt = []
    _reponseInstr_2_allKeys = []
    # keep track of which components have finished
    responseInst_uncuedComponents = [probe_inst_2, probeIndicator_inst_2, fixProbe_inst_2, reponseInstr_2, probeInst_2]
    for thisComponent in responseInst_uncuedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    responseInst_uncuedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "responseInst_uncued"-------
    while continueRoutine:
        # get current time
        t = responseInst_uncuedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=responseInst_uncuedClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *probe_inst_2* updates
        if probe_inst_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            probe_inst_2.frameNStart = frameN  # exact frame index
            probe_inst_2.tStart = t  # local t and not account for scr refresh
            probe_inst_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(probe_inst_2, 'tStartRefresh')  # time at next scr refresh
            probe_inst_2.setAutoDraw(True)
        if probe_inst_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > probe_inst_2.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                probe_inst_2.tStop = t  # not accounting for scr refresh
                probe_inst_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(probe_inst_2, 'tStopRefresh')  # time at next scr refresh
                probe_inst_2.setAutoDraw(False)
        
        # *probeIndicator_inst_2* updates
        if probeIndicator_inst_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            probeIndicator_inst_2.frameNStart = frameN  # exact frame index
            probeIndicator_inst_2.tStart = t  # local t and not account for scr refresh
            probeIndicator_inst_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(probeIndicator_inst_2, 'tStartRefresh')  # time at next scr refresh
            probeIndicator_inst_2.setAutoDraw(True)
        if probeIndicator_inst_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > probeIndicator_inst_2.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                probeIndicator_inst_2.tStop = t  # not accounting for scr refresh
                probeIndicator_inst_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(probeIndicator_inst_2, 'tStopRefresh')  # time at next scr refresh
                probeIndicator_inst_2.setAutoDraw(False)
        
        # *fixProbe_inst_2* updates
        if fixProbe_inst_2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            fixProbe_inst_2.frameNStart = frameN  # exact frame index
            fixProbe_inst_2.tStart = t  # local t and not account for scr refresh
            fixProbe_inst_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixProbe_inst_2, 'tStartRefresh')  # time at next scr refresh
            fixProbe_inst_2.setAutoDraw(True)
        
        # *reponseInstr_2* updates
        waitOnFlip = False
        if reponseInstr_2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            reponseInstr_2.frameNStart = frameN  # exact frame index
            reponseInstr_2.tStart = t  # local t and not account for scr refresh
            reponseInstr_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reponseInstr_2, 'tStartRefresh')  # time at next scr refresh
            reponseInstr_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(reponseInstr_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(reponseInstr_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if reponseInstr_2.status == STARTED and not waitOnFlip:
            theseKeys = reponseInstr_2.getKeys(keyList=['left'], waitRelease=False)
            _reponseInstr_2_allKeys.extend(theseKeys)
            if len(_reponseInstr_2_allKeys):
                reponseInstr_2.keys = _reponseInstr_2_allKeys[-1].name  # just the last key pressed
                reponseInstr_2.rt = _reponseInstr_2_allKeys[-1].rt
                # was this correct?
                if (reponseInstr_2.keys == str(buttonCorrect)) or (reponseInstr_2.keys == buttonCorrect):
                    reponseInstr_2.corr = 1
                else:
                    reponseInstr_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *probeInst_2* updates
        if probeInst_2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            probeInst_2.frameNStart = frameN  # exact frame index
            probeInst_2.tStart = t  # local t and not account for scr refresh
            probeInst_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(probeInst_2, 'tStartRefresh')  # time at next scr refresh
            probeInst_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in responseInst_uncuedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "responseInst_uncued"-------
    for thisComponent in responseInst_uncuedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_Instr.addData('probe_inst_2.started', probe_inst_2.tStartRefresh)
    trials_Instr.addData('probe_inst_2.stopped', probe_inst_2.tStopRefresh)
    trials_Instr.addData('probeIndicator_inst_2.started', probeIndicator_inst_2.tStartRefresh)
    trials_Instr.addData('probeIndicator_inst_2.stopped', probeIndicator_inst_2.tStopRefresh)
    trials_Instr.addData('fixProbe_inst_2.started', fixProbe_inst_2.tStartRefresh)
    trials_Instr.addData('fixProbe_inst_2.stopped', fixProbe_inst_2.tStopRefresh)
    # check responses
    if reponseInstr_2.keys in ['', [], None]:  # No response was made
        reponseInstr_2.keys = None
        # was no response the correct answer?!
        if str(buttonCorrect).lower() == 'none':
           reponseInstr_2.corr = 1;  # correct non-response
        else:
           reponseInstr_2.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_Instr (TrialHandler)
    trials_Instr.addData('reponseInstr_2.keys',reponseInstr_2.keys)
    trials_Instr.addData('reponseInstr_2.corr', reponseInstr_2.corr)
    if reponseInstr_2.keys != None:  # we had a response
        trials_Instr.addData('reponseInstr_2.rt', reponseInstr_2.rt)
    trials_Instr.addData('reponseInstr_2.started', reponseInstr_2.tStartRefresh)
    trials_Instr.addData('reponseInstr_2.stopped', reponseInstr_2.tStopRefresh)
    trials_Instr.addData('probeInst_2.started', probeInst_2.tStartRefresh)
    trials_Instr.addData('probeInst_2.stopped', probeInst_2.tStopRefresh)
    # the Routine "responseInst_uncued" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "reward"-------
    continueRoutine = True
    # update component parameters for each repeat
    space5.keys = []
    space5.rt = []
    _space5_allKeys = []
    # keep track of which components have finished
    rewardComponents = [rewardInst, space5]
    for thisComponent in rewardComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rewardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "reward"-------
    while continueRoutine:
        # get current time
        t = rewardClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rewardClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rewardInst* updates
        if rewardInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rewardInst.frameNStart = frameN  # exact frame index
            rewardInst.tStart = t  # local t and not account for scr refresh
            rewardInst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rewardInst, 'tStartRefresh')  # time at next scr refresh
            rewardInst.setAutoDraw(True)
        
        # *space5* updates
        waitOnFlip = False
        if space5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space5.frameNStart = frameN  # exact frame index
            space5.tStart = t  # local t and not account for scr refresh
            space5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space5, 'tStartRefresh')  # time at next scr refresh
            space5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space5.status == STARTED and not waitOnFlip:
            theseKeys = space5.getKeys(keyList=['space'], waitRelease=False)
            _space5_allKeys.extend(theseKeys)
            if len(_space5_allKeys):
                space5.keys = _space5_allKeys[-1].name  # just the last key pressed
                space5.rt = _space5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rewardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "reward"-------
    for thisComponent in rewardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_Instr.addData('rewardInst.started', rewardInst.tStartRefresh)
    trials_Instr.addData('rewardInst.stopped', rewardInst.tStopRefresh)
    # check responses
    if space5.keys in ['', [], None]:  # No response was made
        space5.keys = None
    trials_Instr.addData('space5.keys',space5.keys)
    if space5.keys != None:  # we had a response
        trials_Instr.addData('space5.rt', space5.rt)
    trials_Instr.addData('space5.started', space5.tStartRefresh)
    trials_Instr.addData('space5.stopped', space5.tStopRefresh)
    # the Routine "reward" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_Instr'

# get names of stimulus parameters
if trials_Instr.trialList in ([], [None], None):
    params = []
else:
    params = trials_Instr.trialList[0].keys()
# save data for this loop
trials_Instr.saveAsText(filename + 'trials_Instr.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
repeat_InstrTrials = data.TrialHandler(nReps=999, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='repeat_InstrTrials')
thisExp.addLoop(repeat_InstrTrials)  # add the loop to the experiment
thisRepeat_InstrTrial = repeat_InstrTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepeat_InstrTrial.rgb)
if thisRepeat_InstrTrial != None:
    for paramName in thisRepeat_InstrTrial:
        exec('{} = thisRepeat_InstrTrial[paramName]'.format(paramName))

for thisRepeat_InstrTrial in repeat_InstrTrials:
    currentLoop = repeat_InstrTrials
    # abbreviate parameter names if possible (e.g. rgb = thisRepeat_InstrTrial.rgb)
    if thisRepeat_InstrTrial != None:
        for paramName in thisRepeat_InstrTrial:
            exec('{} = thisRepeat_InstrTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "reminderButtons"-------
    continueRoutine = True
    # update component parameters for each repeat
    space6.keys = []
    space6.rt = []
    _space6_allKeys = []
    number_correct = 0
    totalN = 0
    
    # keep track of which components have finished
    reminderButtonsComponents = [Button_reminder, space6]
    for thisComponent in reminderButtonsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    reminderButtonsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "reminderButtons"-------
    while continueRoutine:
        # get current time
        t = reminderButtonsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=reminderButtonsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Button_reminder* updates
        if Button_reminder.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Button_reminder.frameNStart = frameN  # exact frame index
            Button_reminder.tStart = t  # local t and not account for scr refresh
            Button_reminder.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Button_reminder, 'tStartRefresh')  # time at next scr refresh
            Button_reminder.setAutoDraw(True)
        
        # *space6* updates
        waitOnFlip = False
        if space6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space6.frameNStart = frameN  # exact frame index
            space6.tStart = t  # local t and not account for scr refresh
            space6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space6, 'tStartRefresh')  # time at next scr refresh
            space6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space6.status == STARTED and not waitOnFlip:
            theseKeys = space6.getKeys(keyList=['space'], waitRelease=False)
            _space6_allKeys.extend(theseKeys)
            if len(_space6_allKeys):
                space6.keys = _space6_allKeys[-1].name  # just the last key pressed
                space6.rt = _space6_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reminderButtonsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "reminderButtons"-------
    for thisComponent in reminderButtonsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeat_InstrTrials.addData('Button_reminder.started', Button_reminder.tStartRefresh)
    repeat_InstrTrials.addData('Button_reminder.stopped', Button_reminder.tStopRefresh)
    # check responses
    if space6.keys in ['', [], None]:  # No response was made
        space6.keys = None
    repeat_InstrTrials.addData('space6.keys',space6.keys)
    if space6.keys != None:  # we had a response
        repeat_InstrTrials.addData('space6.rt', space6.rt)
    repeat_InstrTrials.addData('space6.started', space6.tStartRefresh)
    repeat_InstrTrials.addData('space6.stopped', space6.tStopRefresh)
    # the Routine "reminderButtons" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_instr2 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trials_Instr.csv', selection='1:7'),
        seed=None, name='trials_instr2')
    thisExp.addLoop(trials_instr2)  # add the loop to the experiment
    thisTrials_instr2 = trials_instr2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_instr2.rgb)
    if thisTrials_instr2 != None:
        for paramName in thisTrials_instr2:
            exec('{} = thisTrials_instr2[paramName]'.format(paramName))
    
    for thisTrials_instr2 in trials_instr2:
        currentLoop = trials_instr2
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_instr2.rgb)
        if thisTrials_instr2 != None:
            for paramName in thisTrials_instr2:
                exec('{} = thisTrials_instr2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trialBegBlank_practice"-------
        continueRoutine = True
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        trialBegBlank_practiceComponents = [fixStartTrial_2]
        for thisComponent in trialBegBlank_practiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialBegBlank_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trialBegBlank_practice"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialBegBlank_practiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialBegBlank_practiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixStartTrial_2* updates
            if fixStartTrial_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixStartTrial_2.frameNStart = frameN  # exact frame index
                fixStartTrial_2.tStart = t  # local t and not account for scr refresh
                fixStartTrial_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixStartTrial_2, 'tStartRefresh')  # time at next scr refresh
                fixStartTrial_2.setAutoDraw(True)
            if fixStartTrial_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixStartTrial_2.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    fixStartTrial_2.tStop = t  # not accounting for scr refresh
                    fixStartTrial_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixStartTrial_2, 'tStopRefresh')  # time at next scr refresh
                    fixStartTrial_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialBegBlank_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trialBegBlank_practice"-------
        for thisComponent in trialBegBlank_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_instr2.addData('fixStartTrial_2.started', fixStartTrial_2.tStartRefresh)
        trials_instr2.addData('fixStartTrial_2.stopped', fixStartTrial_2.tStopRefresh)
        
        # ------Prepare to start Routine "trial_practice"-------
        continueRoutine = True
        routineTimer.add(20.000000)
        # update component parameters for each repeat
        stim1_Practice.setImage(image1L)
        stim2_Practice.setImage(image1R)
        mask1_prac.setImage(scramble1L)
        mask2_prac.setImage(scramble1R)
        stim3_Practice.setImage(image2L)
        stim4_Practice.setImage(image2R)
        mask3_prac.setImage(scramble2L)
        mask4_prac.setImage(scramble2R)
        cueInstr.setText(cue)
        probe_Practice.setImage(imageCuedProbe)
        probeIndicator_Practice.setText(arrow
)
        keyResp_Practice.keys = []
        keyResp_Practice.rt = []
        _keyResp_Practice_allKeys = []
        # keep track of which components have finished
        trial_practiceComponents = [stim1_Practice, stim2_Practice, mask1_prac, mask2_prac, cross_postMem1, stim3_Practice, stim4_Practice, mask3_prac, mask4_prac, cross_postMem2, cueInstr, fixDelay_Practice, probe_Practice, probeIndicator_Practice, fixProbe_Practice, keyResp_Practice]
        for thisComponent in trial_practiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_practice"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trial_practiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_practiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stim1_Practice* updates
            if stim1_Practice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                stim1_Practice.frameNStart = frameN  # exact frame index
                stim1_Practice.tStart = t  # local t and not account for scr refresh
                stim1_Practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim1_Practice, 'tStartRefresh')  # time at next scr refresh
                stim1_Practice.setAutoDraw(True)
            if stim1_Practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim1_Practice.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    stim1_Practice.tStop = t  # not accounting for scr refresh
                    stim1_Practice.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim1_Practice, 'tStopRefresh')  # time at next scr refresh
                    stim1_Practice.setAutoDraw(False)
            
            # *stim2_Practice* updates
            if stim2_Practice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                stim2_Practice.frameNStart = frameN  # exact frame index
                stim2_Practice.tStart = t  # local t and not account for scr refresh
                stim2_Practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim2_Practice, 'tStartRefresh')  # time at next scr refresh
                stim2_Practice.setAutoDraw(True)
            if stim2_Practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim2_Practice.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    stim2_Practice.tStop = t  # not accounting for scr refresh
                    stim2_Practice.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim2_Practice, 'tStopRefresh')  # time at next scr refresh
                    stim2_Practice.setAutoDraw(False)
            
            # *mask1_prac* updates
            if mask1_prac.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                mask1_prac.frameNStart = frameN  # exact frame index
                mask1_prac.tStart = t  # local t and not account for scr refresh
                mask1_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mask1_prac, 'tStartRefresh')  # time at next scr refresh
                mask1_prac.setAutoDraw(True)
            if mask1_prac.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mask1_prac.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    mask1_prac.tStop = t  # not accounting for scr refresh
                    mask1_prac.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(mask1_prac, 'tStopRefresh')  # time at next scr refresh
                    mask1_prac.setAutoDraw(False)
            
            # *mask2_prac* updates
            if mask2_prac.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                mask2_prac.frameNStart = frameN  # exact frame index
                mask2_prac.tStart = t  # local t and not account for scr refresh
                mask2_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mask2_prac, 'tStartRefresh')  # time at next scr refresh
                mask2_prac.setAutoDraw(True)
            if mask2_prac.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mask2_prac.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    mask2_prac.tStop = t  # not accounting for scr refresh
                    mask2_prac.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(mask2_prac, 'tStopRefresh')  # time at next scr refresh
                    mask2_prac.setAutoDraw(False)
            
            # *cross_postMem1* updates
            if cross_postMem1.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                cross_postMem1.frameNStart = frameN  # exact frame index
                cross_postMem1.tStart = t  # local t and not account for scr refresh
                cross_postMem1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_postMem1, 'tStartRefresh')  # time at next scr refresh
                cross_postMem1.setAutoDraw(True)
            if cross_postMem1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_postMem1.tStartRefresh + 0.4-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_postMem1.tStop = t  # not accounting for scr refresh
                    cross_postMem1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cross_postMem1, 'tStopRefresh')  # time at next scr refresh
                    cross_postMem1.setAutoDraw(False)
            
            # *stim3_Practice* updates
            if stim3_Practice.status == NOT_STARTED and tThisFlip >= 2.7-frameTolerance:
                # keep track of start time/frame for later
                stim3_Practice.frameNStart = frameN  # exact frame index
                stim3_Practice.tStart = t  # local t and not account for scr refresh
                stim3_Practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim3_Practice, 'tStartRefresh')  # time at next scr refresh
                stim3_Practice.setAutoDraw(True)
            if stim3_Practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim3_Practice.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    stim3_Practice.tStop = t  # not accounting for scr refresh
                    stim3_Practice.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim3_Practice, 'tStopRefresh')  # time at next scr refresh
                    stim3_Practice.setAutoDraw(False)
            
            # *stim4_Practice* updates
            if stim4_Practice.status == NOT_STARTED and tThisFlip >= 2.7-frameTolerance:
                # keep track of start time/frame for later
                stim4_Practice.frameNStart = frameN  # exact frame index
                stim4_Practice.tStart = t  # local t and not account for scr refresh
                stim4_Practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim4_Practice, 'tStartRefresh')  # time at next scr refresh
                stim4_Practice.setAutoDraw(True)
            if stim4_Practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim4_Practice.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    stim4_Practice.tStop = t  # not accounting for scr refresh
                    stim4_Practice.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim4_Practice, 'tStopRefresh')  # time at next scr refresh
                    stim4_Practice.setAutoDraw(False)
            
            # *mask3_prac* updates
            if mask3_prac.status == NOT_STARTED and tThisFlip >= 4.7-frameTolerance:
                # keep track of start time/frame for later
                mask3_prac.frameNStart = frameN  # exact frame index
                mask3_prac.tStart = t  # local t and not account for scr refresh
                mask3_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mask3_prac, 'tStartRefresh')  # time at next scr refresh
                mask3_prac.setAutoDraw(True)
            if mask3_prac.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mask3_prac.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    mask3_prac.tStop = t  # not accounting for scr refresh
                    mask3_prac.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(mask3_prac, 'tStopRefresh')  # time at next scr refresh
                    mask3_prac.setAutoDraw(False)
            
            # *mask4_prac* updates
            if mask4_prac.status == NOT_STARTED and tThisFlip >= 4.7-frameTolerance:
                # keep track of start time/frame for later
                mask4_prac.frameNStart = frameN  # exact frame index
                mask4_prac.tStart = t  # local t and not account for scr refresh
                mask4_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mask4_prac, 'tStartRefresh')  # time at next scr refresh
                mask4_prac.setAutoDraw(True)
            if mask4_prac.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mask4_prac.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    mask4_prac.tStop = t  # not accounting for scr refresh
                    mask4_prac.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(mask4_prac, 'tStopRefresh')  # time at next scr refresh
                    mask4_prac.setAutoDraw(False)
            
            # *cross_postMem2* updates
            if cross_postMem2.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                # keep track of start time/frame for later
                cross_postMem2.frameNStart = frameN  # exact frame index
                cross_postMem2.tStart = t  # local t and not account for scr refresh
                cross_postMem2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_postMem2, 'tStartRefresh')  # time at next scr refresh
                cross_postMem2.setAutoDraw(True)
            if cross_postMem2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_postMem2.tStartRefresh + 0.4-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_postMem2.tStop = t  # not accounting for scr refresh
                    cross_postMem2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cross_postMem2, 'tStopRefresh')  # time at next scr refresh
                    cross_postMem2.setAutoDraw(False)
            
            # *cueInstr* updates
            if cueInstr.status == NOT_STARTED and tThisFlip >= 5.4-frameTolerance:
                # keep track of start time/frame for later
                cueInstr.frameNStart = frameN  # exact frame index
                cueInstr.tStart = t  # local t and not account for scr refresh
                cueInstr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cueInstr, 'tStartRefresh')  # time at next scr refresh
                cueInstr.setAutoDraw(True)
            if cueInstr.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cueInstr.tStartRefresh + 0.6-frameTolerance:
                    # keep track of stop time/frame for later
                    cueInstr.tStop = t  # not accounting for scr refresh
                    cueInstr.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cueInstr, 'tStopRefresh')  # time at next scr refresh
                    cueInstr.setAutoDraw(False)
            
            # *fixDelay_Practice* updates
            if fixDelay_Practice.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
                # keep track of start time/frame for later
                fixDelay_Practice.frameNStart = frameN  # exact frame index
                fixDelay_Practice.tStart = t  # local t and not account for scr refresh
                fixDelay_Practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixDelay_Practice, 'tStartRefresh')  # time at next scr refresh
                fixDelay_Practice.setAutoDraw(True)
            if fixDelay_Practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixDelay_Practice.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    fixDelay_Practice.tStop = t  # not accounting for scr refresh
                    fixDelay_Practice.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixDelay_Practice, 'tStopRefresh')  # time at next scr refresh
                    fixDelay_Practice.setAutoDraw(False)
            
            # *probe_Practice* updates
            if probe_Practice.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
                # keep track of start time/frame for later
                probe_Practice.frameNStart = frameN  # exact frame index
                probe_Practice.tStart = t  # local t and not account for scr refresh
                probe_Practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe_Practice, 'tStartRefresh')  # time at next scr refresh
                probe_Practice.setAutoDraw(True)
            if probe_Practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > probe_Practice.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    probe_Practice.tStop = t  # not accounting for scr refresh
                    probe_Practice.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(probe_Practice, 'tStopRefresh')  # time at next scr refresh
                    probe_Practice.setAutoDraw(False)
            
            # *probeIndicator_Practice* updates
            if probeIndicator_Practice.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
                # keep track of start time/frame for later
                probeIndicator_Practice.frameNStart = frameN  # exact frame index
                probeIndicator_Practice.tStart = t  # local t and not account for scr refresh
                probeIndicator_Practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probeIndicator_Practice, 'tStartRefresh')  # time at next scr refresh
                probeIndicator_Practice.setAutoDraw(True)
            if probeIndicator_Practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > probeIndicator_Practice.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    probeIndicator_Practice.tStop = t  # not accounting for scr refresh
                    probeIndicator_Practice.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(probeIndicator_Practice, 'tStopRefresh')  # time at next scr refresh
                    probeIndicator_Practice.setAutoDraw(False)
            
            # *fixProbe_Practice* updates
            if fixProbe_Practice.status == NOT_STARTED and tThisFlip >= 17-frameTolerance:
                # keep track of start time/frame for later
                fixProbe_Practice.frameNStart = frameN  # exact frame index
                fixProbe_Practice.tStart = t  # local t and not account for scr refresh
                fixProbe_Practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixProbe_Practice, 'tStartRefresh')  # time at next scr refresh
                fixProbe_Practice.setAutoDraw(True)
            if fixProbe_Practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixProbe_Practice.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    fixProbe_Practice.tStop = t  # not accounting for scr refresh
                    fixProbe_Practice.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixProbe_Practice, 'tStopRefresh')  # time at next scr refresh
                    fixProbe_Practice.setAutoDraw(False)
            
            # *keyResp_Practice* updates
            waitOnFlip = False
            if keyResp_Practice.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
                # keep track of start time/frame for later
                keyResp_Practice.frameNStart = frameN  # exact frame index
                keyResp_Practice.tStart = t  # local t and not account for scr refresh
                keyResp_Practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyResp_Practice, 'tStartRefresh')  # time at next scr refresh
                keyResp_Practice.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(keyResp_Practice.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(keyResp_Practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if keyResp_Practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > keyResp_Practice.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    keyResp_Practice.tStop = t  # not accounting for scr refresh
                    keyResp_Practice.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(keyResp_Practice, 'tStopRefresh')  # time at next scr refresh
                    keyResp_Practice.status = FINISHED
            if keyResp_Practice.status == STARTED and not waitOnFlip:
                theseKeys = keyResp_Practice.getKeys(keyList=['right', 'left', 'None'], waitRelease=False)
                _keyResp_Practice_allKeys.extend(theseKeys)
                if len(_keyResp_Practice_allKeys):
                    keyResp_Practice.keys = _keyResp_Practice_allKeys[0].name  # just the first key pressed
                    keyResp_Practice.rt = _keyResp_Practice_allKeys[0].rt
                    # was this correct?
                    if (keyResp_Practice.keys == str(buttonCorrect)) or (keyResp_Practice.keys == buttonCorrect):
                        keyResp_Practice.corr = 1
                    else:
                        keyResp_Practice.corr = 0
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_practice"-------
        for thisComponent in trial_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_instr2.addData('stim1_Practice.started', stim1_Practice.tStartRefresh)
        trials_instr2.addData('stim1_Practice.stopped', stim1_Practice.tStopRefresh)
        trials_instr2.addData('stim2_Practice.started', stim2_Practice.tStartRefresh)
        trials_instr2.addData('stim2_Practice.stopped', stim2_Practice.tStopRefresh)
        trials_instr2.addData('mask1_prac.started', mask1_prac.tStartRefresh)
        trials_instr2.addData('mask1_prac.stopped', mask1_prac.tStopRefresh)
        trials_instr2.addData('mask2_prac.started', mask2_prac.tStartRefresh)
        trials_instr2.addData('mask2_prac.stopped', mask2_prac.tStopRefresh)
        trials_instr2.addData('cross_postMem1.started', cross_postMem1.tStartRefresh)
        trials_instr2.addData('cross_postMem1.stopped', cross_postMem1.tStopRefresh)
        trials_instr2.addData('stim3_Practice.started', stim3_Practice.tStartRefresh)
        trials_instr2.addData('stim3_Practice.stopped', stim3_Practice.tStopRefresh)
        trials_instr2.addData('stim4_Practice.started', stim4_Practice.tStartRefresh)
        trials_instr2.addData('stim4_Practice.stopped', stim4_Practice.tStopRefresh)
        trials_instr2.addData('mask3_prac.started', mask3_prac.tStartRefresh)
        trials_instr2.addData('mask3_prac.stopped', mask3_prac.tStopRefresh)
        trials_instr2.addData('mask4_prac.started', mask4_prac.tStartRefresh)
        trials_instr2.addData('mask4_prac.stopped', mask4_prac.tStopRefresh)
        trials_instr2.addData('cross_postMem2.started', cross_postMem2.tStartRefresh)
        trials_instr2.addData('cross_postMem2.stopped', cross_postMem2.tStopRefresh)
        trials_instr2.addData('cueInstr.started', cueInstr.tStartRefresh)
        trials_instr2.addData('cueInstr.stopped', cueInstr.tStopRefresh)
        trials_instr2.addData('fixDelay_Practice.started', fixDelay_Practice.tStartRefresh)
        trials_instr2.addData('fixDelay_Practice.stopped', fixDelay_Practice.tStopRefresh)
        trials_instr2.addData('probe_Practice.started', probe_Practice.tStartRefresh)
        trials_instr2.addData('probe_Practice.stopped', probe_Practice.tStopRefresh)
        trials_instr2.addData('probeIndicator_Practice.started', probeIndicator_Practice.tStartRefresh)
        trials_instr2.addData('probeIndicator_Practice.stopped', probeIndicator_Practice.tStopRefresh)
        trials_instr2.addData('fixProbe_Practice.started', fixProbe_Practice.tStartRefresh)
        trials_instr2.addData('fixProbe_Practice.stopped', fixProbe_Practice.tStopRefresh)
        # check responses
        if keyResp_Practice.keys in ['', [], None]:  # No response was made
            keyResp_Practice.keys = None
            # was no response the correct answer?!
            if str(buttonCorrect).lower() == 'none':
               keyResp_Practice.corr = 1;  # correct non-response
            else:
               keyResp_Practice.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_instr2 (TrialHandler)
        trials_instr2.addData('keyResp_Practice.keys',keyResp_Practice.keys)
        trials_instr2.addData('keyResp_Practice.corr', keyResp_Practice.corr)
        if keyResp_Practice.keys != None:  # we had a response
            trials_instr2.addData('keyResp_Practice.rt', keyResp_Practice.rt)
        trials_instr2.addData('keyResp_Practice.started', keyResp_Practice.tStartRefresh)
        trials_instr2.addData('keyResp_Practice.stopped', keyResp_Practice.tStopRefresh)
        
        # ------Prepare to start Routine "feedback_2"-------
        continueRoutine = True
        routineTimer.add(0.800000)
        # update component parameters for each repeat
        if keyResp_Practice.corr:
            msg="Correct"
            number_correct = number_correct+1
            totalN = totalN+1
        else:
            msg="Incorrect"
            totalN = totalN+1
        
        feedbackText.setText(msg)
        # keep track of which components have finished
        feedback_2Components = [feedbackText]
        for thisComponent in feedback_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        feedback_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "feedback_2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedback_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=feedback_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedbackText* updates
            if feedbackText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackText.frameNStart = frameN  # exact frame index
                feedbackText.tStart = t  # local t and not account for scr refresh
                feedbackText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbackText, 'tStartRefresh')  # time at next scr refresh
                feedbackText.setAutoDraw(True)
            if feedbackText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackText.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackText.tStop = t  # not accounting for scr refresh
                    feedbackText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedbackText, 'tStopRefresh')  # time at next scr refresh
                    feedbackText.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback_2"-------
        for thisComponent in feedback_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_instr2.addData('feedbackText.started', feedbackText.tStartRefresh)
        trials_instr2.addData('feedbackText.stopped', feedbackText.tStopRefresh)
        
        # set up handler to look after randomisation of conditions etc
        trials_2 = data.TrialHandler(nReps=probeNonCued, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_2')
        thisExp.addLoop(trials_2)  # add the loop to the experiment
        thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        for thisTrial_2 in trials_2:
            currentLoop = trials_2
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    exec('{} = thisTrial_2[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "noncuedProbe_Practice"-------
            continueRoutine = True
            routineTimer.add(4.000000)
            # update component parameters for each repeat
            Probe_Noncued_Instr.setImage(imageUncuedProbe)
            nonCuedProbeIndicator_practice.setText(arrow)
            key_resp_NonCue_practice.keys = []
            key_resp_NonCue_practice.rt = []
            _key_resp_NonCue_practice_allKeys = []
            # keep track of which components have finished
            noncuedProbe_PracticeComponents = [Probe_Noncued_Instr, nonCuedProbeIndicator_practice, crossNonCued, key_resp_NonCue_practice]
            for thisComponent in noncuedProbe_PracticeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            noncuedProbe_PracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "noncuedProbe_Practice"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = noncuedProbe_PracticeClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=noncuedProbe_PracticeClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Probe_Noncued_Instr* updates
                if Probe_Noncued_Instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Probe_Noncued_Instr.frameNStart = frameN  # exact frame index
                    Probe_Noncued_Instr.tStart = t  # local t and not account for scr refresh
                    Probe_Noncued_Instr.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Probe_Noncued_Instr, 'tStartRefresh')  # time at next scr refresh
                    Probe_Noncued_Instr.setAutoDraw(True)
                if Probe_Noncued_Instr.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Probe_Noncued_Instr.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Probe_Noncued_Instr.tStop = t  # not accounting for scr refresh
                        Probe_Noncued_Instr.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Probe_Noncued_Instr, 'tStopRefresh')  # time at next scr refresh
                        Probe_Noncued_Instr.setAutoDraw(False)
                
                # *nonCuedProbeIndicator_practice* updates
                if nonCuedProbeIndicator_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    nonCuedProbeIndicator_practice.frameNStart = frameN  # exact frame index
                    nonCuedProbeIndicator_practice.tStart = t  # local t and not account for scr refresh
                    nonCuedProbeIndicator_practice.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(nonCuedProbeIndicator_practice, 'tStartRefresh')  # time at next scr refresh
                    nonCuedProbeIndicator_practice.setAutoDraw(True)
                if nonCuedProbeIndicator_practice.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > nonCuedProbeIndicator_practice.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        nonCuedProbeIndicator_practice.tStop = t  # not accounting for scr refresh
                        nonCuedProbeIndicator_practice.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(nonCuedProbeIndicator_practice, 'tStopRefresh')  # time at next scr refresh
                        nonCuedProbeIndicator_practice.setAutoDraw(False)
                
                # *crossNonCued* updates
                if crossNonCued.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    crossNonCued.frameNStart = frameN  # exact frame index
                    crossNonCued.tStart = t  # local t and not account for scr refresh
                    crossNonCued.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crossNonCued, 'tStartRefresh')  # time at next scr refresh
                    crossNonCued.setAutoDraw(True)
                if crossNonCued.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crossNonCued.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        crossNonCued.tStop = t  # not accounting for scr refresh
                        crossNonCued.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(crossNonCued, 'tStopRefresh')  # time at next scr refresh
                        crossNonCued.setAutoDraw(False)
                
                # *key_resp_NonCue_practice* updates
                waitOnFlip = False
                if key_resp_NonCue_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_NonCue_practice.frameNStart = frameN  # exact frame index
                    key_resp_NonCue_practice.tStart = t  # local t and not account for scr refresh
                    key_resp_NonCue_practice.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_NonCue_practice, 'tStartRefresh')  # time at next scr refresh
                    key_resp_NonCue_practice.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_NonCue_practice.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_NonCue_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_NonCue_practice.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_NonCue_practice.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_NonCue_practice.tStop = t  # not accounting for scr refresh
                        key_resp_NonCue_practice.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(key_resp_NonCue_practice, 'tStopRefresh')  # time at next scr refresh
                        key_resp_NonCue_practice.status = FINISHED
                if key_resp_NonCue_practice.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_NonCue_practice.getKeys(keyList=['left', 'right', 'None'], waitRelease=False)
                    _key_resp_NonCue_practice_allKeys.extend(theseKeys)
                    if len(_key_resp_NonCue_practice_allKeys):
                        key_resp_NonCue_practice.keys = _key_resp_NonCue_practice_allKeys[0].name  # just the first key pressed
                        key_resp_NonCue_practice.rt = _key_resp_NonCue_practice_allKeys[0].rt
                        # was this correct?
                        if (key_resp_NonCue_practice.keys == str(uncuedButtonCorrect)) or (key_resp_NonCue_practice.keys == uncuedButtonCorrect):
                            key_resp_NonCue_practice.corr = 1
                        else:
                            key_resp_NonCue_practice.corr = 0
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in noncuedProbe_PracticeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "noncuedProbe_Practice"-------
            for thisComponent in noncuedProbe_PracticeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_2.addData('Probe_Noncued_Instr.started', Probe_Noncued_Instr.tStartRefresh)
            trials_2.addData('Probe_Noncued_Instr.stopped', Probe_Noncued_Instr.tStopRefresh)
            trials_2.addData('nonCuedProbeIndicator_practice.started', nonCuedProbeIndicator_practice.tStartRefresh)
            trials_2.addData('nonCuedProbeIndicator_practice.stopped', nonCuedProbeIndicator_practice.tStopRefresh)
            trials_2.addData('crossNonCued.started', crossNonCued.tStartRefresh)
            trials_2.addData('crossNonCued.stopped', crossNonCued.tStopRefresh)
            # check responses
            if key_resp_NonCue_practice.keys in ['', [], None]:  # No response was made
                key_resp_NonCue_practice.keys = None
                # was no response the correct answer?!
                if str(uncuedButtonCorrect).lower() == 'none':
                   key_resp_NonCue_practice.corr = 1;  # correct non-response
                else:
                   key_resp_NonCue_practice.corr = 0;  # failed to respond (incorrectly)
            # store data for trials_2 (TrialHandler)
            trials_2.addData('key_resp_NonCue_practice.keys',key_resp_NonCue_practice.keys)
            trials_2.addData('key_resp_NonCue_practice.corr', key_resp_NonCue_practice.corr)
            if key_resp_NonCue_practice.keys != None:  # we had a response
                trials_2.addData('key_resp_NonCue_practice.rt', key_resp_NonCue_practice.rt)
            trials_2.addData('key_resp_NonCue_practice.started', key_resp_NonCue_practice.tStartRefresh)
            trials_2.addData('key_resp_NonCue_practice.stopped', key_resp_NonCue_practice.tStopRefresh)
            
            # ------Prepare to start Routine "feedback_2_noncue"-------
            continueRoutine = True
            routineTimer.add(0.800000)
            # update component parameters for each repeat
            if key_resp_NonCue_practice.corr:
                msg="Correct"
                number_correct = number_correct+1
                totalN = totalN+1
            else:
                msg="Incorrect"
                totalN = totalN+1
            
            feedbackText_2.setText(msg)
            # keep track of which components have finished
            feedback_2_noncueComponents = [feedbackText_2]
            for thisComponent in feedback_2_noncueComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            feedback_2_noncueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "feedback_2_noncue"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = feedback_2_noncueClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=feedback_2_noncueClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *feedbackText_2* updates
                if feedbackText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedbackText_2.frameNStart = frameN  # exact frame index
                    feedbackText_2.tStart = t  # local t and not account for scr refresh
                    feedbackText_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedbackText_2, 'tStartRefresh')  # time at next scr refresh
                    feedbackText_2.setAutoDraw(True)
                if feedbackText_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedbackText_2.tStartRefresh + 0.8-frameTolerance:
                        # keep track of stop time/frame for later
                        feedbackText_2.tStop = t  # not accounting for scr refresh
                        feedbackText_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(feedbackText_2, 'tStopRefresh')  # time at next scr refresh
                        feedbackText_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedback_2_noncueComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "feedback_2_noncue"-------
            for thisComponent in feedback_2_noncueComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_2.addData('feedbackText_2.started', feedbackText_2.tStartRefresh)
            trials_2.addData('feedbackText_2.stopped', feedbackText_2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed probeNonCued repeats of 'trials_2'
        
        # get names of stimulus parameters
        if trials_2.trialList in ([], [None], None):
            params = []
        else:
            params = trials_2.trialList[0].keys()
        # save data for this loop
        trials_2.saveAsText(filename + 'trials_2.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_instr2'
    
    # get names of stimulus parameters
    if trials_instr2.trialList in ([], [None], None):
        params = []
    else:
        params = trials_instr2.trialList[0].keys()
    # save data for this loop
    trials_instr2.saveAsText(filename + 'trials_instr2.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "perceptCorrectCalc_practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    perceptCorrectCalc_practiceComponents = []
    for thisComponent in perceptCorrectCalc_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    perceptCorrectCalc_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "perceptCorrectCalc_practice"-------
    while continueRoutine:
        # get current time
        t = perceptCorrectCalc_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=perceptCorrectCalc_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in perceptCorrectCalc_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "perceptCorrectCalc_practice"-------
    for thisComponent in perceptCorrectCalc_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    percent_correct = str(round(number_correct/totalN*100,2))
    # the Routine "perceptCorrectCalc_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackTest"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    text_7.setText('Perfomance has to be above 60% to move-on to the real task. Otherwise we can practice a little more. Your performance was '+percent_correct+'%.')
    if number_correct/totalN >= 0.60:
        repeat_InstrTrials.finished = True
    # keep track of which components have finished
    feedbackTestComponents = [key_resp_5, text_7]
    for thisComponent in feedbackTestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackTest"-------
    while continueRoutine:
        # get current time
        t = feedbackTestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackTestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackTestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackTest"-------
    for thisComponent in feedbackTestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    repeat_InstrTrials.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        repeat_InstrTrials.addData('key_resp_5.rt', key_resp_5.rt)
    repeat_InstrTrials.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    repeat_InstrTrials.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    repeat_InstrTrials.addData('text_7.started', text_7.tStartRefresh)
    repeat_InstrTrials.addData('text_7.stopped', text_7.tStopRefresh)
    # the Routine "feedbackTest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 999 repeats of 'repeat_InstrTrials'

# get names of stimulus parameters
if repeat_InstrTrials.trialList in ([], [None], None):
    params = []
else:
    params = repeat_InstrTrials.trialList[0].keys()
# save data for this loop
repeat_InstrTrials.saveAsText(filename + 'repeat_InstrTrials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
runs = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('runs.csv'),
    seed=None, name='runs')
thisExp.addLoop(runs)  # add the loop to the experiment
thisRun = runs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
if thisRun != None:
    for paramName in thisRun:
        exec('{} = thisRun[paramName]'.format(paramName))

for thisRun in runs:
    currentLoop = runs
    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun:
            exec('{} = thisRun[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Before_run"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_run.setText(textBefore_run)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    number_correct = 0
    totalN = 0
    # keep track of which components have finished
    Before_runComponents = [text_run, key_resp_2]
    for thisComponent in Before_runComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Before_runClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Before_run"-------
    while continueRoutine:
        # get current time
        t = Before_runClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Before_runClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_run* updates
        if text_run.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_run.frameNStart = frameN  # exact frame index
            text_run.tStart = t  # local t and not account for scr refresh
            text_run.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_run, 'tStartRefresh')  # time at next scr refresh
            text_run.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Before_runComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Before_run"-------
    for thisComponent in Before_runComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    runs.addData('text_run.started', text_run.tStartRefresh)
    runs.addData('text_run.stopped', text_run.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    runs.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        runs.addData('key_resp_2.rt', key_resp_2.rt)
    runs.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    runs.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "Before_run" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blankStart"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankStartComponents = [fixStart]
    for thisComponent in blankStartComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankStartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blankStart"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankStartClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankStartClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixStart* updates
        if fixStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixStart.frameNStart = frameN  # exact frame index
            fixStart.tStart = t  # local t and not account for scr refresh
            fixStart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixStart, 'tStartRefresh')  # time at next scr refresh
            fixStart.setAutoDraw(True)
        if fixStart.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixStart.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                fixStart.tStop = t  # not accounting for scr refresh
                fixStart.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixStart, 'tStopRefresh')  # time at next scr refresh
                fixStart.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankStartComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blankStart"-------
    for thisComponent in blankStartComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    runs.addData('fixStart.started', fixStart.tStartRefresh)
    runs.addData('fixStart.stopped', fixStart.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trialsRun = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(trialSelect),
        seed=None, name='trialsRun')
    thisExp.addLoop(trialsRun)  # add the loop to the experiment
    thisTrialsRun = trialsRun.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsRun.rgb)
    if thisTrialsRun != None:
        for paramName in thisTrialsRun:
            exec('{} = thisTrialsRun[paramName]'.format(paramName))
    
    for thisTrialsRun in trialsRun:
        currentLoop = trialsRun
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsRun.rgb)
        if thisTrialsRun != None:
            for paramName in thisTrialsRun:
                exec('{} = thisTrialsRun[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(20.000000)
        # update component parameters for each repeat
        stim1.setImage(image1L)
        stim2.setImage(image1R)
        mask1.setImage(scramble1L)
        mask2.setImage(scramble1R)
        stim3.setImage(image2L)
        stim4.setImage(image2R)
        mask3.setImage(scramble2L)
        mask4.setImage(scramble2R)
        cue_run.setText(cue)
        probe_run.setImage(imageCuedProbe)
        probeIndicator.setText(arrow
)
        keyResp.keys = []
        keyResp.rt = []
        _keyResp_allKeys = []
        # keep track of which components have finished
        trialComponents = [stim1, stim2, mask1, mask2, cross_postMem1_2, stim3, stim4, mask3, mask4, cross_postMem2_2, cue_run, fixDelay, probe_run, probeIndicator, fixProbe, keyResp]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stim1* updates
            if stim1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                stim1.frameNStart = frameN  # exact frame index
                stim1.tStart = t  # local t and not account for scr refresh
                stim1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim1, 'tStartRefresh')  # time at next scr refresh
                stim1.setAutoDraw(True)
            if stim1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim1.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    stim1.tStop = t  # not accounting for scr refresh
                    stim1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim1, 'tStopRefresh')  # time at next scr refresh
                    stim1.setAutoDraw(False)
            
            # *stim2* updates
            if stim2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                stim2.frameNStart = frameN  # exact frame index
                stim2.tStart = t  # local t and not account for scr refresh
                stim2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim2, 'tStartRefresh')  # time at next scr refresh
                stim2.setAutoDraw(True)
            if stim2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    stim2.tStop = t  # not accounting for scr refresh
                    stim2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim2, 'tStopRefresh')  # time at next scr refresh
                    stim2.setAutoDraw(False)
            
            # *mask1* updates
            if mask1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                mask1.frameNStart = frameN  # exact frame index
                mask1.tStart = t  # local t and not account for scr refresh
                mask1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mask1, 'tStartRefresh')  # time at next scr refresh
                mask1.setAutoDraw(True)
            if mask1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mask1.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    mask1.tStop = t  # not accounting for scr refresh
                    mask1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(mask1, 'tStopRefresh')  # time at next scr refresh
                    mask1.setAutoDraw(False)
            
            # *mask2* updates
            if mask2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                mask2.frameNStart = frameN  # exact frame index
                mask2.tStart = t  # local t and not account for scr refresh
                mask2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mask2, 'tStartRefresh')  # time at next scr refresh
                mask2.setAutoDraw(True)
            if mask2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mask2.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    mask2.tStop = t  # not accounting for scr refresh
                    mask2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(mask2, 'tStopRefresh')  # time at next scr refresh
                    mask2.setAutoDraw(False)
            
            # *cross_postMem1_2* updates
            if cross_postMem1_2.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                cross_postMem1_2.frameNStart = frameN  # exact frame index
                cross_postMem1_2.tStart = t  # local t and not account for scr refresh
                cross_postMem1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_postMem1_2, 'tStartRefresh')  # time at next scr refresh
                cross_postMem1_2.setAutoDraw(True)
            if cross_postMem1_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_postMem1_2.tStartRefresh + 0.4-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_postMem1_2.tStop = t  # not accounting for scr refresh
                    cross_postMem1_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cross_postMem1_2, 'tStopRefresh')  # time at next scr refresh
                    cross_postMem1_2.setAutoDraw(False)
            
            # *stim3* updates
            if stim3.status == NOT_STARTED and tThisFlip >= 2.7-frameTolerance:
                # keep track of start time/frame for later
                stim3.frameNStart = frameN  # exact frame index
                stim3.tStart = t  # local t and not account for scr refresh
                stim3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim3, 'tStartRefresh')  # time at next scr refresh
                stim3.setAutoDraw(True)
            if stim3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim3.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    stim3.tStop = t  # not accounting for scr refresh
                    stim3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim3, 'tStopRefresh')  # time at next scr refresh
                    stim3.setAutoDraw(False)
            
            # *stim4* updates
            if stim4.status == NOT_STARTED and tThisFlip >= 2.7-frameTolerance:
                # keep track of start time/frame for later
                stim4.frameNStart = frameN  # exact frame index
                stim4.tStart = t  # local t and not account for scr refresh
                stim4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim4, 'tStartRefresh')  # time at next scr refresh
                stim4.setAutoDraw(True)
            if stim4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim4.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    stim4.tStop = t  # not accounting for scr refresh
                    stim4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim4, 'tStopRefresh')  # time at next scr refresh
                    stim4.setAutoDraw(False)
            
            # *mask3* updates
            if mask3.status == NOT_STARTED and tThisFlip >= 4.7-frameTolerance:
                # keep track of start time/frame for later
                mask3.frameNStart = frameN  # exact frame index
                mask3.tStart = t  # local t and not account for scr refresh
                mask3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mask3, 'tStartRefresh')  # time at next scr refresh
                mask3.setAutoDraw(True)
            if mask3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mask3.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    mask3.tStop = t  # not accounting for scr refresh
                    mask3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(mask3, 'tStopRefresh')  # time at next scr refresh
                    mask3.setAutoDraw(False)
            
            # *mask4* updates
            if mask4.status == NOT_STARTED and tThisFlip >= 4.7-frameTolerance:
                # keep track of start time/frame for later
                mask4.frameNStart = frameN  # exact frame index
                mask4.tStart = t  # local t and not account for scr refresh
                mask4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mask4, 'tStartRefresh')  # time at next scr refresh
                mask4.setAutoDraw(True)
            if mask4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mask4.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    mask4.tStop = t  # not accounting for scr refresh
                    mask4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(mask4, 'tStopRefresh')  # time at next scr refresh
                    mask4.setAutoDraw(False)
            
            # *cross_postMem2_2* updates
            if cross_postMem2_2.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                # keep track of start time/frame for later
                cross_postMem2_2.frameNStart = frameN  # exact frame index
                cross_postMem2_2.tStart = t  # local t and not account for scr refresh
                cross_postMem2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_postMem2_2, 'tStartRefresh')  # time at next scr refresh
                cross_postMem2_2.setAutoDraw(True)
            if cross_postMem2_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_postMem2_2.tStartRefresh + 0.4-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_postMem2_2.tStop = t  # not accounting for scr refresh
                    cross_postMem2_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cross_postMem2_2, 'tStopRefresh')  # time at next scr refresh
                    cross_postMem2_2.setAutoDraw(False)
            
            # *cue_run* updates
            if cue_run.status == NOT_STARTED and tThisFlip >= 5.4-frameTolerance:
                # keep track of start time/frame for later
                cue_run.frameNStart = frameN  # exact frame index
                cue_run.tStart = t  # local t and not account for scr refresh
                cue_run.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cue_run, 'tStartRefresh')  # time at next scr refresh
                cue_run.setAutoDraw(True)
            if cue_run.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cue_run.tStartRefresh + 0.6-frameTolerance:
                    # keep track of stop time/frame for later
                    cue_run.tStop = t  # not accounting for scr refresh
                    cue_run.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cue_run, 'tStopRefresh')  # time at next scr refresh
                    cue_run.setAutoDraw(False)
            
            # *fixDelay* updates
            if fixDelay.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
                # keep track of start time/frame for later
                fixDelay.frameNStart = frameN  # exact frame index
                fixDelay.tStart = t  # local t and not account for scr refresh
                fixDelay.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixDelay, 'tStartRefresh')  # time at next scr refresh
                fixDelay.setAutoDraw(True)
            if fixDelay.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixDelay.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    fixDelay.tStop = t  # not accounting for scr refresh
                    fixDelay.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixDelay, 'tStopRefresh')  # time at next scr refresh
                    fixDelay.setAutoDraw(False)
            
            # *probe_run* updates
            if probe_run.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
                # keep track of start time/frame for later
                probe_run.frameNStart = frameN  # exact frame index
                probe_run.tStart = t  # local t and not account for scr refresh
                probe_run.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe_run, 'tStartRefresh')  # time at next scr refresh
                probe_run.setAutoDraw(True)
            if probe_run.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > probe_run.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    probe_run.tStop = t  # not accounting for scr refresh
                    probe_run.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(probe_run, 'tStopRefresh')  # time at next scr refresh
                    probe_run.setAutoDraw(False)
            
            # *probeIndicator* updates
            if probeIndicator.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
                # keep track of start time/frame for later
                probeIndicator.frameNStart = frameN  # exact frame index
                probeIndicator.tStart = t  # local t and not account for scr refresh
                probeIndicator.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probeIndicator, 'tStartRefresh')  # time at next scr refresh
                probeIndicator.setAutoDraw(True)
            if probeIndicator.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > probeIndicator.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    probeIndicator.tStop = t  # not accounting for scr refresh
                    probeIndicator.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(probeIndicator, 'tStopRefresh')  # time at next scr refresh
                    probeIndicator.setAutoDraw(False)
            
            # *fixProbe* updates
            if fixProbe.status == NOT_STARTED and tThisFlip >= 17-frameTolerance:
                # keep track of start time/frame for later
                fixProbe.frameNStart = frameN  # exact frame index
                fixProbe.tStart = t  # local t and not account for scr refresh
                fixProbe.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixProbe, 'tStartRefresh')  # time at next scr refresh
                fixProbe.setAutoDraw(True)
            if fixProbe.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixProbe.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    fixProbe.tStop = t  # not accounting for scr refresh
                    fixProbe.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixProbe, 'tStopRefresh')  # time at next scr refresh
                    fixProbe.setAutoDraw(False)
            
            # *keyResp* updates
            waitOnFlip = False
            if keyResp.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
                # keep track of start time/frame for later
                keyResp.frameNStart = frameN  # exact frame index
                keyResp.tStart = t  # local t and not account for scr refresh
                keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyResp, 'tStartRefresh')  # time at next scr refresh
                keyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(keyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if keyResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > keyResp.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    keyResp.tStop = t  # not accounting for scr refresh
                    keyResp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(keyResp, 'tStopRefresh')  # time at next scr refresh
                    keyResp.status = FINISHED
            if keyResp.status == STARTED and not waitOnFlip:
                theseKeys = keyResp.getKeys(keyList=['right', 'left', 'None'], waitRelease=False)
                _keyResp_allKeys.extend(theseKeys)
                if len(_keyResp_allKeys):
                    keyResp.keys = _keyResp_allKeys[0].name  # just the first key pressed
                    keyResp.rt = _keyResp_allKeys[0].rt
                    # was this correct?
                    if (keyResp.keys == str(buttonCorrect)) or (keyResp.keys == buttonCorrect):
                        keyResp.corr = 1
                    else:
                        keyResp.corr = 0
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trialsRun.addData('stim1.started', stim1.tStartRefresh)
        trialsRun.addData('stim1.stopped', stim1.tStopRefresh)
        trialsRun.addData('stim2.started', stim2.tStartRefresh)
        trialsRun.addData('stim2.stopped', stim2.tStopRefresh)
        trialsRun.addData('mask1.started', mask1.tStartRefresh)
        trialsRun.addData('mask1.stopped', mask1.tStopRefresh)
        trialsRun.addData('mask2.started', mask2.tStartRefresh)
        trialsRun.addData('mask2.stopped', mask2.tStopRefresh)
        trialsRun.addData('cross_postMem1_2.started', cross_postMem1_2.tStartRefresh)
        trialsRun.addData('cross_postMem1_2.stopped', cross_postMem1_2.tStopRefresh)
        trialsRun.addData('stim3.started', stim3.tStartRefresh)
        trialsRun.addData('stim3.stopped', stim3.tStopRefresh)
        trialsRun.addData('stim4.started', stim4.tStartRefresh)
        trialsRun.addData('stim4.stopped', stim4.tStopRefresh)
        trialsRun.addData('mask3.started', mask3.tStartRefresh)
        trialsRun.addData('mask3.stopped', mask3.tStopRefresh)
        trialsRun.addData('mask4.started', mask4.tStartRefresh)
        trialsRun.addData('mask4.stopped', mask4.tStopRefresh)
        trialsRun.addData('cross_postMem2_2.started', cross_postMem2_2.tStartRefresh)
        trialsRun.addData('cross_postMem2_2.stopped', cross_postMem2_2.tStopRefresh)
        trialsRun.addData('cue_run.started', cue_run.tStartRefresh)
        trialsRun.addData('cue_run.stopped', cue_run.tStopRefresh)
        trialsRun.addData('fixDelay.started', fixDelay.tStartRefresh)
        trialsRun.addData('fixDelay.stopped', fixDelay.tStopRefresh)
        trialsRun.addData('probe_run.started', probe_run.tStartRefresh)
        trialsRun.addData('probe_run.stopped', probe_run.tStopRefresh)
        trialsRun.addData('probeIndicator.started', probeIndicator.tStartRefresh)
        trialsRun.addData('probeIndicator.stopped', probeIndicator.tStopRefresh)
        trialsRun.addData('fixProbe.started', fixProbe.tStartRefresh)
        trialsRun.addData('fixProbe.stopped', fixProbe.tStopRefresh)
        # check responses
        if keyResp.keys in ['', [], None]:  # No response was made
            keyResp.keys = None
            # was no response the correct answer?!
            if str(buttonCorrect).lower() == 'none':
               keyResp.corr = 1;  # correct non-response
            else:
               keyResp.corr = 0;  # failed to respond (incorrectly)
        # store data for trialsRun (TrialHandler)
        trialsRun.addData('keyResp.keys',keyResp.keys)
        trialsRun.addData('keyResp.corr', keyResp.corr)
        if keyResp.keys != None:  # we had a response
            trialsRun.addData('keyResp.rt', keyResp.rt)
        trialsRun.addData('keyResp.started', keyResp.tStartRefresh)
        trialsRun.addData('keyResp.stopped', keyResp.tStopRefresh)
        
        # set up handler to look after randomisation of conditions etc
        trialsNonCue = data.TrialHandler(nReps=probeNonCued, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trialsNonCue')
        thisExp.addLoop(trialsNonCue)  # add the loop to the experiment
        thisTrialsNonCue = trialsNonCue.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsNonCue.rgb)
        if thisTrialsNonCue != None:
            for paramName in thisTrialsNonCue:
                exec('{} = thisTrialsNonCue[paramName]'.format(paramName))
        
        for thisTrialsNonCue in trialsNonCue:
            currentLoop = trialsNonCue
            # abbreviate parameter names if possible (e.g. rgb = thisTrialsNonCue.rgb)
            if thisTrialsNonCue != None:
                for paramName in thisTrialsNonCue:
                    exec('{} = thisTrialsNonCue[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "noncuedProbe"-------
            continueRoutine = True
            routineTimer.add(4.000000)
            # update component parameters for each repeat
            Probe_Noncued_Instr_2.setImage(imageUncuedProbe)
            nonCuedProbeIndicator_practice_2.setText(arrow)
            key_resp_NonCue.keys = []
            key_resp_NonCue.rt = []
            _key_resp_NonCue_allKeys = []
            # keep track of which components have finished
            noncuedProbeComponents = [Probe_Noncued_Instr_2, nonCuedProbeIndicator_practice_2, crossNonCued_2, key_resp_NonCue]
            for thisComponent in noncuedProbeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            noncuedProbeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "noncuedProbe"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = noncuedProbeClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=noncuedProbeClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Probe_Noncued_Instr_2* updates
                if Probe_Noncued_Instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Probe_Noncued_Instr_2.frameNStart = frameN  # exact frame index
                    Probe_Noncued_Instr_2.tStart = t  # local t and not account for scr refresh
                    Probe_Noncued_Instr_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Probe_Noncued_Instr_2, 'tStartRefresh')  # time at next scr refresh
                    Probe_Noncued_Instr_2.setAutoDraw(True)
                if Probe_Noncued_Instr_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Probe_Noncued_Instr_2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Probe_Noncued_Instr_2.tStop = t  # not accounting for scr refresh
                        Probe_Noncued_Instr_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Probe_Noncued_Instr_2, 'tStopRefresh')  # time at next scr refresh
                        Probe_Noncued_Instr_2.setAutoDraw(False)
                
                # *nonCuedProbeIndicator_practice_2* updates
                if nonCuedProbeIndicator_practice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    nonCuedProbeIndicator_practice_2.frameNStart = frameN  # exact frame index
                    nonCuedProbeIndicator_practice_2.tStart = t  # local t and not account for scr refresh
                    nonCuedProbeIndicator_practice_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(nonCuedProbeIndicator_practice_2, 'tStartRefresh')  # time at next scr refresh
                    nonCuedProbeIndicator_practice_2.setAutoDraw(True)
                if nonCuedProbeIndicator_practice_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > nonCuedProbeIndicator_practice_2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        nonCuedProbeIndicator_practice_2.tStop = t  # not accounting for scr refresh
                        nonCuedProbeIndicator_practice_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(nonCuedProbeIndicator_practice_2, 'tStopRefresh')  # time at next scr refresh
                        nonCuedProbeIndicator_practice_2.setAutoDraw(False)
                
                # *crossNonCued_2* updates
                if crossNonCued_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    crossNonCued_2.frameNStart = frameN  # exact frame index
                    crossNonCued_2.tStart = t  # local t and not account for scr refresh
                    crossNonCued_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crossNonCued_2, 'tStartRefresh')  # time at next scr refresh
                    crossNonCued_2.setAutoDraw(True)
                if crossNonCued_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crossNonCued_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        crossNonCued_2.tStop = t  # not accounting for scr refresh
                        crossNonCued_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(crossNonCued_2, 'tStopRefresh')  # time at next scr refresh
                        crossNonCued_2.setAutoDraw(False)
                
                # *key_resp_NonCue* updates
                waitOnFlip = False
                if key_resp_NonCue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_NonCue.frameNStart = frameN  # exact frame index
                    key_resp_NonCue.tStart = t  # local t and not account for scr refresh
                    key_resp_NonCue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_NonCue, 'tStartRefresh')  # time at next scr refresh
                    key_resp_NonCue.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_NonCue.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_NonCue.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_NonCue.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_NonCue.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_NonCue.tStop = t  # not accounting for scr refresh
                        key_resp_NonCue.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(key_resp_NonCue, 'tStopRefresh')  # time at next scr refresh
                        key_resp_NonCue.status = FINISHED
                if key_resp_NonCue.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_NonCue.getKeys(keyList=['left', 'right', 'None'], waitRelease=False)
                    _key_resp_NonCue_allKeys.extend(theseKeys)
                    if len(_key_resp_NonCue_allKeys):
                        key_resp_NonCue.keys = _key_resp_NonCue_allKeys[0].name  # just the first key pressed
                        key_resp_NonCue.rt = _key_resp_NonCue_allKeys[0].rt
                        # was this correct?
                        if (key_resp_NonCue.keys == str(uncuedButtonCorrect)) or (key_resp_NonCue.keys == uncuedButtonCorrect):
                            key_resp_NonCue.corr = 1
                        else:
                            key_resp_NonCue.corr = 0
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in noncuedProbeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "noncuedProbe"-------
            for thisComponent in noncuedProbeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trialsNonCue.addData('Probe_Noncued_Instr_2.started', Probe_Noncued_Instr_2.tStartRefresh)
            trialsNonCue.addData('Probe_Noncued_Instr_2.stopped', Probe_Noncued_Instr_2.tStopRefresh)
            trialsNonCue.addData('nonCuedProbeIndicator_practice_2.started', nonCuedProbeIndicator_practice_2.tStartRefresh)
            trialsNonCue.addData('nonCuedProbeIndicator_practice_2.stopped', nonCuedProbeIndicator_practice_2.tStopRefresh)
            trialsNonCue.addData('crossNonCued_2.started', crossNonCued_2.tStartRefresh)
            trialsNonCue.addData('crossNonCued_2.stopped', crossNonCued_2.tStopRefresh)
            # check responses
            if key_resp_NonCue.keys in ['', [], None]:  # No response was made
                key_resp_NonCue.keys = None
                # was no response the correct answer?!
                if str(uncuedButtonCorrect).lower() == 'none':
                   key_resp_NonCue.corr = 1;  # correct non-response
                else:
                   key_resp_NonCue.corr = 0;  # failed to respond (incorrectly)
            # store data for trialsNonCue (TrialHandler)
            trialsNonCue.addData('key_resp_NonCue.keys',key_resp_NonCue.keys)
            trialsNonCue.addData('key_resp_NonCue.corr', key_resp_NonCue.corr)
            if key_resp_NonCue.keys != None:  # we had a response
                trialsNonCue.addData('key_resp_NonCue.rt', key_resp_NonCue.rt)
            trialsNonCue.addData('key_resp_NonCue.started', key_resp_NonCue.tStartRefresh)
            trialsNonCue.addData('key_resp_NonCue.stopped', key_resp_NonCue.tStopRefresh)
            if key_resp_NonCue.corr:
                number_correct = number_correct + 1
                totalN = totalN+1
            
            else:
                totalN = totalN+1
            
                
            
            thisExp.nextEntry()
            
        # completed probeNonCued repeats of 'trialsNonCue'
        
        # get names of stimulus parameters
        if trialsNonCue.trialList in ([], [None], None):
            params = []
        else:
            params = trialsNonCue.trialList[0].keys()
        # save data for this loop
        trialsNonCue.saveAsText(filename + 'trialsNonCue.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "trialEndBlank"-------
        continueRoutine = True
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        trialEndBlankComponents = [fixStartTrial]
        for thisComponent in trialEndBlankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialEndBlankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trialEndBlank"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialEndBlankClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialEndBlankClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixStartTrial* updates
            if fixStartTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixStartTrial.frameNStart = frameN  # exact frame index
                fixStartTrial.tStart = t  # local t and not account for scr refresh
                fixStartTrial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixStartTrial, 'tStartRefresh')  # time at next scr refresh
                fixStartTrial.setAutoDraw(True)
            if fixStartTrial.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixStartTrial.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    fixStartTrial.tStop = t  # not accounting for scr refresh
                    fixStartTrial.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixStartTrial, 'tStopRefresh')  # time at next scr refresh
                    fixStartTrial.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialEndBlankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trialEndBlank"-------
        for thisComponent in trialEndBlankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trialsRun.addData('fixStartTrial.started', fixStartTrial.tStartRefresh)
        trialsRun.addData('fixStartTrial.stopped', fixStartTrial.tStopRefresh)
        if keyResp.corr:
            number_correct = number_correct + 1
            totalN=totalN+1
        else:
            totalN=totalN+1
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trialsRun'
    
    # get names of stimulus parameters
    if trialsRun.trialList in ([], [None], None):
        params = []
    else:
        params = trialsRun.trialList[0].keys()
    # save data for this loop
    trialsRun.saveAsText(filename + 'trialsRun.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "blankEnd"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    percent_correct = str(round(number_correct/totalN*100,2))
    # keep track of which components have finished
    blankEndComponents = [fixEnd]
    for thisComponent in blankEndComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankEndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blankEnd"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankEndClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankEndClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixEnd* updates
        if fixEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixEnd.frameNStart = frameN  # exact frame index
            fixEnd.tStart = t  # local t and not account for scr refresh
            fixEnd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixEnd, 'tStartRefresh')  # time at next scr refresh
            fixEnd.setAutoDraw(True)
        if fixEnd.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixEnd.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                fixEnd.tStop = t  # not accounting for scr refresh
                fixEnd.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixEnd, 'tStopRefresh')  # time at next scr refresh
                fixEnd.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankEndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blankEnd"-------
    for thisComponent in blankEndComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    runs.addData('fixEnd.started', fixEnd.tStartRefresh)
    runs.addData('fixEnd.stopped', fixEnd.tStopRefresh)
    
    # ------Prepare to start Routine "feedback_Run"-------
    continueRoutine = True
    # update component parameters for each repeat
    space_Run.keys = []
    space_Run.rt = []
    _space_Run_allKeys = []
    feedbackTxtRun.setText('Your performance was '+percent_correct+'%. Press space to continue')
    # keep track of which components have finished
    feedback_RunComponents = [space_Run, feedbackTxtRun]
    for thisComponent in feedback_RunComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedback_RunClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback_Run"-------
    while continueRoutine:
        # get current time
        t = feedback_RunClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedback_RunClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *space_Run* updates
        waitOnFlip = False
        if space_Run.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space_Run.frameNStart = frameN  # exact frame index
            space_Run.tStart = t  # local t and not account for scr refresh
            space_Run.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_Run, 'tStartRefresh')  # time at next scr refresh
            space_Run.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space_Run.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space_Run.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space_Run.status == STARTED and not waitOnFlip:
            theseKeys = space_Run.getKeys(keyList=['space'], waitRelease=False)
            _space_Run_allKeys.extend(theseKeys)
            if len(_space_Run_allKeys):
                space_Run.keys = _space_Run_allKeys[-1].name  # just the last key pressed
                space_Run.rt = _space_Run_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *feedbackTxtRun* updates
        if feedbackTxtRun.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackTxtRun.frameNStart = frameN  # exact frame index
            feedbackTxtRun.tStart = t  # local t and not account for scr refresh
            feedbackTxtRun.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackTxtRun, 'tStartRefresh')  # time at next scr refresh
            feedbackTxtRun.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback_RunComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback_Run"-------
    for thisComponent in feedback_RunComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if space_Run.keys in ['', [], None]:  # No response was made
        space_Run.keys = None
    runs.addData('space_Run.keys',space_Run.keys)
    if space_Run.keys != None:  # we had a response
        runs.addData('space_Run.rt', space_Run.rt)
    runs.addData('space_Run.started', space_Run.tStartRefresh)
    runs.addData('space_Run.stopped', space_Run.tStopRefresh)
    runs.addData('feedbackTxtRun.started', feedbackTxtRun.tStartRefresh)
    runs.addData('feedbackTxtRun.stopped', feedbackTxtRun.tStopRefresh)
    # the Routine "feedback_Run" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'runs'

# get names of stimulus parameters
if runs.trialList in ([], [None], None):
    params = []
else:
    params = runs.trialList[0].keys()
# save data for this loop
runs.saveAsText(filename + 'runs.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "finalRoutine"-------
continueRoutine = True
# update component parameters for each repeat
space_final.keys = []
space_final.rt = []
_space_final_allKeys = []
# keep track of which components have finished
finalRoutineComponents = [space_final, txt_final]
for thisComponent in finalRoutineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finalRoutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "finalRoutine"-------
while continueRoutine:
    # get current time
    t = finalRoutineClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finalRoutineClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *space_final* updates
    waitOnFlip = False
    if space_final.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_final.frameNStart = frameN  # exact frame index
        space_final.tStart = t  # local t and not account for scr refresh
        space_final.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_final, 'tStartRefresh')  # time at next scr refresh
        space_final.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_final.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_final.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_final.status == STARTED and not waitOnFlip:
        theseKeys = space_final.getKeys(keyList=['space'], waitRelease=False)
        _space_final_allKeys.extend(theseKeys)
        if len(_space_final_allKeys):
            space_final.keys = _space_final_allKeys[-1].name  # just the last key pressed
            space_final.rt = _space_final_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *txt_final* updates
    if txt_final.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        txt_final.frameNStart = frameN  # exact frame index
        txt_final.tStart = t  # local t and not account for scr refresh
        txt_final.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt_final, 'tStartRefresh')  # time at next scr refresh
        txt_final.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finalRoutineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finalRoutine"-------
for thisComponent in finalRoutineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if space_final.keys in ['', [], None]:  # No response was made
    space_final.keys = None
thisExp.addData('space_final.keys',space_final.keys)
if space_final.keys != None:  # we had a response
    thisExp.addData('space_final.rt', space_final.rt)
thisExp.addData('space_final.started', space_final.tStartRefresh)
thisExp.addData('space_final.stopped', space_final.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('txt_final.started', txt_final.tStartRefresh)
thisExp.addData('txt_final.stopped', txt_final.tStopRefresh)
# the Routine "finalRoutine" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
