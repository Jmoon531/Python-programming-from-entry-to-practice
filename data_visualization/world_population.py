#!usr/bin/env python
# -*- coding: utf-8 -*-

import pygal
import json
import pygal.maps.world as pywm
from pygal_maps_world.i18n import COUNTRIES
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

def get_country_code(country_name):
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
	return None

def main(args):
	filename = 'population_data.json'
	with open(filename) as f:
		pop_data = json.load(f)

	cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
	for pop_dict in pop_data:
		if pop_dict['Year'] == '2010':
			country_name = pop_dict['Country Name']
			population = int(float(pop_dict['Value']))
			code = get_country_code(country_name)
			if code:
				if population < 10000000:
					cc_pops_1[code] = population
				elif population < 1000000000:
					cc_pops_2[code] = population
				else:
					cc_pops_3[code] = population

	wm_style = RS('#336699', base_style=LCS)
	wm = pywm.World(style=wm_style)
	wm.title = 'World Population in 2010, by Country'

	wm.add('0-10m', cc_pops_1)
	wm.add('10m-1bn', cc_pops_2)
	wm.add('>1bn', cc_pops_3)

	wm.render_to_file('World_population.svg')
	return 0
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
