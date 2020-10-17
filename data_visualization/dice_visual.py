#!usr/bin/env python

from dice import Dice
import pygal

dice_1 = Dice()
dice_2 = Dice()
dice_3 = Dice()
results = []
for i in range(50000):
	results.append(dice_1.roll() + dice_2.roll() + dice_3.roll())

max_results = dice_1.num_sides + dice_2.num_sides + dice_3.num_sides
frequencies = []
for value in range(3, max_results+1):
	frequencies.append(results.count(value))

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times"
#hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_labels = [x for x in range(3, max_results+1)]
hist.x_title  = "Result"
hist.y_title = "Frequencies of Result"
hist.add('D6', frequencies)
hist.render_to_file('dice_visual.svg')
