from mingus.core import chords
from midiutil import MIDIFile
from graph import Graph

# input an equation
equation = input('Enter a function: f(x) = ').replace("^","**").replace("sin","np.sin").replace("cos","np.cos").replace("tan","np.tan").replace("pi","np.pi").replace(")(", ")*(").replace("1x", "1 * x").replace("2x", "2 * x").replace("3x", "3 * x").replace("4x", "4 * x").replace("5x", "5 * x").replace("6x", "6 * x").replace("7x", "7 * x").replace("8x", "8 * x").replace("9x", "9 * x").replace("x(", "x * (").replace("1(", "1 * (").replace("2(", "2 * (").replace("3(", "3 * (").replace("4(", "4 * (").replace("5(", "5 * (").replace("6(", "6 * (").replace("7(", "7 * (").replace("8(", "8 * (").replace("9(", "9 * (")
# create an instance of 'Graph'
functionGraph = Graph(equation)
# graph the entered equation
functionGraph.graph()