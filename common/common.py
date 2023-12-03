#!/usr/bin/env python3
#
# Author: Panagiotis Chartas (t3l3machus) 
# https://github.com/t3l3machus

import re, sys, os
from time import time, sleep
from subprocess import check_output


''' Colors '''
GREEN = '\033[38;5;82m'
ORANGE = '\033[0;38;5;214m'
BOLD = '\033[1m'
END = '\033[0m'
MAIN = '\033[38;5;85m'

''' Prefixes '''
INFO = f'[{MAIN}Info{END}]'
GREEN_DOT = f'[{GREEN}*{END}]'
DEBUG = f'[{ORANGE}Debug{END}]'


def banner():
	
	padding = '  '

	B = [[' ', '┌','┐',' '], [' ', '├','┴','┐'], [' ', '└','─','┘']]
	A = [[' ', '┌','─','┐'], [' ', '├','─','┤'], [' ', '┴',' ','┴']]
	B = [[' ', '┌','┐',' '], [' ', '├','┴','┐'], [' ', '└','─','┘']]	
	E = [[' ', '┌','─','┐'], [' ', '├','┤',' '], [' ', '└','─','┘']]
	L = [[' ', '┬',' ',' '], [' ', '│',' ', ' '], [' ', '┴','─','┘']]	
	S = [[' ', '┌','─','┐'], [' ', '└','─','┐'], [' ', '└','─','┘']]
	T = [[' ', '┌','┬','┐'], [' ', ' ','│',' '], [' ', ' ','┴',' ']]
	R = [[' ', '┬','─','┐'], [' ', '├','┬','┘'], [' ', '┴','└','─']]
	I =	[[' ', '┬'], [' ', '│',], [' ', '┴']]
	K = [[' ', '┬','┌','─'], [' ', '├','┴','┐'], [' ', '┴',' ','┴']]	
	E = [[' ', '┌','─','┐'], [' ', '├','┤',' '], [' ', '└','─','┘']]	


	banner = [B,A,B,E,L,S,T,R,I,K,E]
	final = []
	print('\r')
	init_color = 31
	txt_color = init_color
	cl = 0

	for charset in range(0, 3):
		
		for pos in range(0, len(banner)):
			
			for i in range(0, len(banner[pos][charset])):
				clr = f'\033[38;5;{txt_color}m'
				char = f'{clr}{banner[pos][charset][i]}'
				final.append(char)
				cl += 1
				txt_color = txt_color + 36 if cl <= 3 else txt_color

			cl = 0

			txt_color = init_color
		init_color += 31

		if charset < 2: final.append('\n   ')

	print(f"   {''.join(final)}")
	print(f'{END}{padding}                              by t3l3machus\n')
	
	

def loadImports(path):
	
	files = os.listdir(path)
	imps = []

	for i in range(len(files)):
		
		name = files[i].split('.')
		
		if len(name) > 1:
			
			if name[1] == 'py' and name[0] != '__init__':
				
			   name = name[0]
			   imps.append(name)

	f = open(path + '__init__.py', 'w')

	toWrite = '__all__ = ' + str(imps)

	f.write(toWrite)
	f.close()
	


class Global:
	
	latin_alphabet = 'abcdefghijklmnopqrstuvwxyz'
	output = None
	parsed_domains = None
	#symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'



def exit_with_msg(msg):
	print(f'{DEBUG} {msg}')
	exit(1)



def chill():
	pass



def parse_comma_seperated_list(user_input):
	
	keywords = []

	if user_input:
		
		for word in user_input.split(","):
			
			if word.strip():
				
				keywords.append(word.strip()) 

		if not keywords:
			
			exit_with_msg("Illegal value(s). Check your input and try again.")
		
		else:

			return keywords



def return_num_of_symbols_in_str(string, blacklisted_symbols):
	
	total = 0
	
	if string:
		
		for char in string:

			if char in blacklisted_symbols:
				total += 1
				
	return total
				


def str_to_class(lang):
    return getattr(sys.modules[f'language_classes.{lang}'], lang)	



def get_file_contents(file_path):
	
	f = open(file_path, 'r', encoding="utf-8")
	contents = f.readlines()
	f.close()
	return contents



def save_output(variations, output_filename):
	
	with open(output_filename + '.txt', 'w', encoding="utf-8") as output:
		for line in variations:
			output.write(line + '\n')



def return_short_if_string_too_long(string):
	
	if len(string) >= 25:
		return string[0:13] + '...'
		
	else:
		return string



def uniq_list(_list):
	
	if _list:
		
		uniq = []
		
		for item in _list:
			if item not in uniq:
				uniq.append(item)
		
		return uniq
	
	return None
		
