from mingus.core import chords
from midiutil import MIDIFile
from graph import Graph

# input an equation
rawInput = input('Enter a function with integer coefficients: f(x) = ')
equation = rawInput.replace("^","**").replace("sin","np.sin").replace("cos","np.cos").replace("tan","np.tan").replace("pi","np.pi").replace(")(", ")*(").replace("1x", "1 * x").replace("2x", "2 * x").replace("3x", "3 * x").replace("4x", "4 * x").replace("5x", "5 * x").replace("6x", "6 * x").replace("7x", "7 * x").replace("8x", "8 * x").replace("9x", "9 * x").replace("x(", "x * (").replace("1(", "1 * (").replace("2(", "2 * (").replace("3(", "3 * (").replace("4(", "4 * (").replace("5(", "5 * (").replace("6(", "6 * (").replace("7(", "7 * (").replace("8(", "8 * (").replace("9(", "9 * (")
# create an instance of 'Graph'
functionGraph = Graph(equation)
# input amount of notes
while True:
    try:
        amountNotes = int(input('Number of notes (doubled, must be a positive integer): '))
    except:
        print('Invalid number, try again.')
    finally:
        break
# graph the entered equation
functionGraph.graph(raw=rawInput)

notes = []
# lowest value in the domain
floor = round(functionGraph.getY(-amountNotes))
# highest value in the domain
ceiling = round(functionGraph.getY(amountNotes + 1))
# MIDI limitations: Pitch cannot go over 127 or below 0
# a multiplier will change the value of the numbers in the domain so that they fit in the MIDI note range
# shifts the whole graph into minimum value of 0 and biggest
multiplier = 1
# 0 in y-value is middle C, which is note 60
if floor + 60 < 0 or ceiling + 60 > 127:
    multiplier = 127/(abs(floor) + abs(ceiling))
    print(multiplier)
# adjust all values in graph
for i in range(-amountNotes, amountNotes + 1):
    notes.append(round(functionGraph.getY(i) * multiplier + 60))

print(notes)
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 120   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automaxtically)
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(notes):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

with open("output.midi", "wb") as output_file:
    MyMIDI.writeFile(output_file)