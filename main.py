from mingus.core import chords
from midiutil import MIDIFile
from graph import Graph

# input an equation
equation = input('Enter a function: f(x) = ').replace("^","**").replace("sin","np.sin").replace("cos","np.cos").replace("tan","np.tan").replace("pi","np.pi").replace(")(", ")*(")
#
functionGraph = Graph(equation)
# graph the entered equation
functionGraph.graph()