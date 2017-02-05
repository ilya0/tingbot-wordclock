import tingbot
from tingbot import *
from datetime import datetime, time

# setup code here
screenX, screenY = 300, 220
gridW, gridH = 16, 16
unitX, unitY = screenX / gridW, screenY / gridH

Clock = [[0 for x in range(gridW)] for y in range(gridH)]

# Matrix[0][0] = 'I'
# Matrix[0][1] = 'T'

Matrix = [[] for y in range(gridH)]
Matrix[0] =  list('ITLISOTWENTYRONE')
Matrix[1] =  list('TWOETENMTHIRTEEN')
Matrix[2] =  list('FIVEMELEVENIFOUR')
Matrix[3] =  list('THREEPNINETEENSU')
Matrix[4] =  list('FOURTEENMIDNIGHT')
Matrix[5] =  list('SIXTEENDEIGHTEEN')
Matrix[6] =  list('SEVENTEENOTWELVE')
Matrix[7] =  list('HALFELQUARTEROTO')
Matrix[8] =  list('PASTRONESTWOISIX')
Matrix[9] =  list('TWELVETFOURAFIVE')
Matrix[10] = list('SEVENMEIGHTENINE')
Matrix[11] = list('TENTTHREECOCLOCK')
Matrix[12] = list('INOTHENAFTERNOON')
Matrix[13] = list('MORNINGSATENIGHT')
Matrix[14] = list('EVENINGOMGMOGNET')
Matrix[15] = list('TINGBOTWORDCLOCK')

# [row, start position, length]
words_it = [0,0,2]
words_is = [0,3,2]
words_half = [7,0,4]
words_to = [7,14,2]
words_past = [8,0,4]
words_oclock = [11,10,6]
words_in = [12,0,2]
words_the = [12,3,3]
words_afternoon = [12,7,9]
words_noon = [12,12,4]
words_midnight = [4,8,8]
words_morning = [13,0,7]
words_at = [13,8,2]
words_night = [13,11,5]
words_evening = [14,0,7]
words_el = [9,2,2]

words_minutes = [
    [0,13,3],   #one
    [1,0,3],    #two
    [3,0,5],    #three
    [2,12,4],   #four
    [2,0,4],    #five
    [5,0,3],    #six
    [6,0,5],    #seven
    [5,8,5],    #eight
    [3,6,4],    #nine
    [1,4,3],    #ten
    [2,5,6],    #eleven
    [6,10,6],   #twelve
    [1,8,8],    #thirteen
    [4,0,8],    #fourteen
    [7,6,7],    #quarter
    [5,0,7],    #sixteen
    [6,0,9],    #seventeen
    [5,8,8],    #eighteen
    [3,6,8],    #nineteen
    [0,6,6]     #twenty
]

words_hours = [
    [8,5,3],    #one
    [8,9,3],    #two
    [11,4,5],   #three
    [9,7,4],    #four
    [9,12,4],   #five
    [8,13,3],   #six
    [10,0,5],   #seven
    [10,6,5],   #eight
    [10,12,4],  #nine
    [11,0,3],   #ten
    [10,1,4],   #even
    [9,0,6]     #twelve
]


def addWordToClock(word):
    for i in range(word[2]):
        Clock[word[0]][word[1] + i] = 1

@every(seconds=1.0/30)
def loop():
    m = int(str(datetime.now())[14:16])
    h = int(str(datetime.now())[11:13])
    h2 = h
    
    # Reset the display
    for y in range(gridH):
        for x in range(gridW):
            Clock[y][x] = 0
    
    # Start adding words
    addWordToClock(words_it)
    addWordToClock(words_is)
    
    if m == 0:
        if h == 0:
            addWordToClock(words_midnight)
        elif h == 12:
            addWordToClock(words_noon)
        else:
            addWordToClock(words_oclock)
            
    else:
        if m <= 20:
            addWordToClock(words_minutes[m - 1])
        elif m < 30:
            addWordToClock(words_minutes[19])
            addWordToClock(words_minutes[m - 21])
        elif m == 30:
            addWordToClock(words_half)
        elif m < 40:
            addWordToClock(words_minutes[19])
            addWordToClock(words_minutes[60 - m - 21])
        else:
            addWordToClock(words_minutes[60 - m - 1])
            
        if m <= 30:
            addWordToClock(words_past)
        else:
            addWordToClock(words_to)
            ++h2
            
    if not (m == 0 and (h == 0 or h == 12)):
        if h2 == 0:
            addWordToClock(words_hours[11])
        elif h2 <= 12:
            addWordToClock(words_hours[h2 - 1])
        else:
            addWordToClock(words_hours[h2 - 13])
    
    if h2 == 11 or h2 == 23:
        addWordToClock(words_el)
        
    if h < 6:
        addWordToClock(words_at)
        addWordToClock(words_night)
    elif h < 12:
        addWordToClock(words_in)
        addWordToClock(words_the)
        addWordToClock(words_morning)
    elif h < 18:
        addWordToClock(words_in)
        addWordToClock(words_the)
        addWordToClock(words_afternoon)
    else:
        addWordToClock(words_at)
        addWordToClock(words_night)
    
    screen.fill(color=(26,26,26))
    for y in range(gridH):
        for x in range(gridW):
            color_off = (75,75,75)
            color_on = 'lime'
            screen.text(
                Matrix[y][x], 
                xy=(unitX*(x+.5)+15, unitY*(y+.5)+15), 
                max_width=unitX,
                max_height=unitY,
                font_size=12,
                align='center',
                font='font/Instruction Bold.ttf',
                color = color_on if Clock[y][x] == 1 else color_off
            )

tingbot.run()
