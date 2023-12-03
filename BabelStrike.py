#!/usr/bin/env python3
#
# Author: Panagiotis Chartas (t3l3machus) 
# https://github.com/t3l3machus


import argparse, os
from threading import Thread
from common.lang_codes import *
from common.common import *
from langdetect import detect, DetectorFactory

loadImports('language_classes/')
from language_classes import *


# -------------- Arguments -------------- #
parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", action = "store", help = "A wordlist or full names list to process.", required = True)
parser.add_argument("-r", "--romanization", action="store_true", help = "Transliterate each line of the provided file to the latin alphabet. If used in conjunction with --convertion (-c), the file will be interpreted as a full names list.")
parser.add_argument("-c", "--convertion", action="store_true", help = "Perform name-to-username convertions.")
parser.add_argument("-a", "--auto-reverse", action="store_true", help = "Perform name-to-username convertion patterns against the reversed version of each name as well.")
parser.add_argument("-d", "--domain", action="store", help = "Comma seperated list of domains to add as prefix to each generated username (e.g. EVILCORP\\scott.henderson).")
parser.add_argument("-l", "--language", action="store", help = "Manually set the language to transliterate from (e.g., Spanish).")
parser.add_argument("-t", "--troubleshoot", action="store_true", help = "Print sample for each language identified.")
parser.add_argument("-q", "--quiet", action="store_true", help = "Do not print the banner on startup.")

args = parser.parse_args()

if args.domain and not args.convertion:
	exit_with_msg('Domain prefix must be used with --convertion [-c].')

if args.domain:
	Global.parsed_domains = parse_comma_seperated_list(args.domain)


# -------------- Classes & Functions -------------- #
class BabelStrike:
	
	supported_languages = [lang.replace('.py', '') for lang in os.listdir(f'.{os.sep}language_classes')]
	not_supported_lang_alerts = []
	initialized_languages = []
	identified_languages = []
	language_objects = {}
	timestamp = str(time()).split('.')[0]
	transliterated = []
	omitted = []
	

	def is_latin_alphabet_only(self, text):
		
		for char in text:
			
			if char.isalpha() and char not in Global.latin_alphabet:
				return False
		
		return True
		


	def identify_languge(self, text):
		
		if text.strip():
			
			try:
				lang = language_codes[detect(text)]
				return lang
				
			except:
				return False
				
		else:
			return 'None'
		


	def substitution_iterator(self):
		
		DetectorFactory.seed = 0
		contents = get_file_contents(args.file)
		loaded = len(contents)
		converted = 0
		
		print(f'{GREEN_DOT} {BOLD}Initiating Romanization...{END}')
		
		for line in contents:
			
			line = line.lower().strip()
			if not line:
				continue
				
			# This variable is used to store multiple variations of a line's translation
			variations = [line]
			
			# Identify the language	
			lang = self.identify_languge(line) if self.is_latin_alphabet_only(line) == False else 'English'
			
			if not lang:
				print(f' ├─ Failed to identify the language of: {line if len(line) >= 20 else line[0:15] + "..."}')
				self.omitted.append(line)		
				continue
				
			elif lang in ['English', 'None']:
				# ~ print(f'[*] Language identified: {lang} (Skipping)')
				self.transliterated.append(line)
				self.omitted.append(line)
				continue
			
			else:
				
				if lang not in self.supported_languages:
					if lang not in self.not_supported_lang_alerts:
						print(f' ├─ Language identified: {lang} (Not Supported)') if not args.troubleshoot else print(f' ├─ {ORANGE}{line if len(line) <= 20 else line[0:15] + "..."}{END} Language identified: {lang} (Not Supported)')
						self.not_supported_lang_alerts.append(lang)
					self.identified_languages.append(lang)	
					self.omitted.append(line)
					continue
				
				elif lang not in self.initialized_languages:
					self.language_objects[lang] = str_to_class(lang)
					self.initialized_languages.append(lang)					
					self.identified_languages.append(lang)					
					print(f' ├─ Language identified: {lang}') if not args.troubleshoot else print(f' ├─ {ORANGE}{line if len(line) <= 20 else line[0:15] + "..."}{END} Language identified: {lang}')

				converted += 1
				
			# Romanization
			new_variations = []
			
			_alphabet_ = list(self.language_objects[lang].char_substitution_map.keys())
			_alphabet_.sort(key = len)
			_alphabet_.reverse()
			
			for key in _alphabet_:
				
				if key in line:
					
					i = 0
					new_variations = []

					for text in variations:
						sub_values = self.language_objects[lang].char_substitution_map[key]
						
						if isinstance(sub_values, list):
							sub_values.sort(key = len)
							sub_values.reverse()
							count = 0
													
							for sub_value in sub_values:
								
								tmp = text.replace(key, sub_value)
								
								if not count:
									variations[i] = tmp
									
								else:								
									new_variations.append(tmp)
									
								count += 1
																	
						else:
							
							text = text.replace(key, sub_values)
							variations[i] = text
							
						i += 1
					
					if new_variations:
						variations += new_variations
				
			self.transliterated += [v.title() for v in variations]
			
		if self.transliterated:
		
			save_output(self.transliterated, f'transliterated_{self.timestamp}')
			print(f' ├─ Total languages identified: {", ".join(uniq_list(self.identified_languages))}.' if self.identified_languages else ' ├─ Did not identify any non-Latin alphabet names.') 
			if len(uniq_list(self.identified_languages)) >= 5:
				print(f' ├─ {FUXIA}BabelStrike detected many different languages. If the result is inaccurate and you know which language should be used to transliterate from, try providing it with --language (-l).{END}')
			print(f' ├─ Output saved in {ORANGE}transliterated_{self.timestamp}.txt{END} (Transliterated {ORANGE}{converted}/{loaded}{END} lines).')
			Global.output = f'transliterated_{self.timestamp}.txt'
		
		else:
			
			print(f' ├─ Nothing to transliterate ¯\_(ツ)_/¯')
			
			
		if self.omitted:
			save_output(self.omitted, f'omitted_{self.timestamp}')
			print(f' ├─ Omitted {ORANGE}{len(self.omitted)}/{loaded}{END} lines (saved in {ORANGE}omitted_{self.timestamp}.txt{END}).')
		
		print(' └─ Done!')
		return



class Username_Converter:
	
	'''
	Using "John Snow" for pattern examples in the comments below.
	All patterns are applied to the name as found in the source list 
	as well as reversed (John Snow | Snow John).
	'''
	
	contents = []
	convertions = []
	skipped = []
	domain_prefixed = []
	symbols_not_allowed_in_usernames = ['/', '\\', '[', ']', ':', ';', '|', '=', ',', '+', '*', '?', '<', '>', "'", '"']	
	special_char_seperators = ["", " ", ".", "_", "-"]
	
	
	def __init__(self, contents):
		
		self.contents = contents
		
		if args.romanization:
			self.timestamp = BabelStrike.timestamp
			
		else:
			self.timestamp = str(time()).split('.')[0]
		
		
		
	def analyze_name(self, n):
		
		if not n.strip(): return None
		
		words = n.split(" ")
		num_of_words = len(words)
		includes_banned_symbols = return_num_of_symbols_in_str(n, self.symbols_not_allowed_in_usernames)
		num_of_periods = n.count('.')
		includes_dot_initials = 0
		dot_initials = []
		
		c = 0
		
		for w in words:
			
			if w.count('.') == 1 and len(w) == 2:
				includes_dot_initials += 1
				dot_initials.append(c)
			
			c += 1
				
		
		details = {
			'num_of_words' : num_of_words,
			'includes_banned_symbols' : includes_banned_symbols,
			'num_of_periods' : num_of_periods,
			'includes_dot_initials' : includes_dot_initials,
			'dot_initials' : dot_initials
		}
		
		return details

		
		
	def reverse_name(self, n):
		
		n = n.split(" ")
		words = len(n)
		
		if words == 2:
			reverse = f'{n[1]} {n[0]}'
			return reverse
			
		elif words == 3:
			reverse = f'{n[2]} {n[1]} {n[0]}'
			return reverse			



	def single_first_and_last(self, n):
		
		n = n.split(" ")
		
		# Append every word in name seperately to the usernames list
		
		for i in range(0, len(n)):
			
			if len(n[i]) >= 2:
				self.convertions.append(n[i])
		


	def seperate_by_special_char(self, n):
		
		for c in self.special_char_seperators: 
			
			uname = n.replace(" ", c)    # john.snow    [assuming c = "."]
			self.convertions.append(uname)



	def initials_only(self, n):
		
		words = n.split(' ')
		
		for c in self.special_char_seperators:
				
			uname = c.join([w[0] for w in words]) # j-s    [assuming c = "-"]    
			self.convertions.append(uname)



	def first_x_letters_of_name_only(self, n, x):
		
		n = n.split(" ")
		
		if len(n[0]) >= x:
			
			if len(n) == 2:
				
				self.convertions.append(f'{n[0][0:x]}{n[1]}')  # jsnow    [assuming x = 1]
				self.convertions.append(f'{n[1]}{n[0][0:x]}')  # snowj    [assuming x = 1]				
				self.seperate_by_special_char(f'{n[0][0:x]} {n[1]}')	 # j.snow	 [assuming x = 1 AND c = "."]
				self.seperate_by_special_char(f'{n[1]} {n[0][0:x]}')  # snow.j    [assuming x = 1 AND c = "."]
					
			elif len(n) == 3:
				
				self.convertions.append(f'{n[0][0:x]}{n[1]}{n[2]}')  # jjoesnow    [assuming x = 1]
				self.convertions.append(f'{n[2]}{n[1]}{n[0][0:x]}')  # snowjoej    [assuming x = 1]
				self.seperate_by_special_char(f'{n[0][0:x]} {n[1]} {n[2]}')	 # j.joe.snow	 [assuming x = 1 AND c = "."]
				self.seperate_by_special_char(f'{n[2]} {n[1]} {n[0][0:x]}')  # snow.joe.j    [assuming x = 1 AND c = "."]



	def first_x_letters_of_name_and_y_letters_of_lastname(self, n, x, y):
		
		n = n.split(" ")
		
		if len(n[0]) >= x and len(n[1]) >= y:
			
			if len(n) == 2:
				
				self.convertions.append(f'{n[0][0:x]}{n[1][0:y]}')  # jsn    [assuming x = 1 AND y = 2]
				self.convertions.append(f'{n[1][0:y]}{n[0][0:x]}')  # snj    [assuming x = 1 AND y = 2]
				self.seperate_by_special_char(f'{n[0][0:x]} {n[1][0:y]}')	 # j.sn	 [assuming x = 1 AND y = 2 AND c = "."]
				self.seperate_by_special_char(f'{n[1][0:y]} {n[0][0:x]}')  # sn.j    [assuming x = 1 AND y = 2 AND c = "."]
					


	def append_domain(self, username):
		
		for domain in Global.parsed_domains:
			
			self.domain_prefixed.append(f'{domain}\\{username}')



	def apply_convertion_rules(self):
		
		print(f'{GREEN_DOT} {BOLD}Initiating name-to-username conversions. This may take a while...{END}')
		
		appended = 0
		
		for name in self.contents:
			
			name = name.strip().lower()
			
			if not name: 
				continue
			
			
			# Remove any extra spaces, dots, hyphens and underscores
			name = re.sub(' +', ' ', name)
			name = re.sub('[.\-_]*', '', name)

			
			# Get details about the string to be treated as a full name
			details = self.analyze_name(name)
			
			''' Decide what rules to apply in relation to the name's structure '''
			
			# Skip names that include symbols other than dots and spaces: 
			if details['includes_banned_symbols']:
				self.skipped.append(name)
				print(f' ├─ Skipping line "{return_short_if_string_too_long(name)}" [{ORANGE}Contains symbols{END}].')
				continue


			# Skip names that include multiple dot initials like "John S. K.": 
			elif details['includes_dot_initials'] > 2:
				self.skipped.append(name)
				print(f' ├─ Skipping line "{return_short_if_string_too_long(name)}" [{ORANGE}Contains multiple dot initials{END}].')
				continue


			# Append names consisting of a single word directly to the results: 
			elif details['num_of_words'] == 1:
				self.convertions.append(name)
				print(f' ├─ Skipping line "{return_short_if_string_too_long(name)}" [{ORANGE}Consists of 1 word{END}].')
				continue

			# Skip names containing more than 3 words: 
			elif details['num_of_words'] > 3:
				self.skipped.append(name)
				print(f' ├─ Skipping line "{return_short_if_string_too_long(name)}" [{ORANGE}Names with 3+ words not supported{END}].')
				continue
				
			# ------------------- END OF NAME SANITIZATION --------------------

			name_base_variations = [name]
			
			# Get a reverse version of the full name
			if args.auto_reverse and details['num_of_words'] in [2, 3]:
				name_reversed = self.reverse_name(name)
				name_base_variations.append(name_reversed)
			
			# Get a normal and reverse version of the full name with only the inital in middle name
			if args.auto_reverse and details['num_of_words'] == 3:
				tmp = name.split(' ')
				name_middle_initial_only = ' '.join([tmp[0], tmp[1][0], tmp[2]])
				name_reversed = self.reverse_name(name_middle_initial_only)
				name_base_variations.append(name_middle_initial_only)
				name_base_variations.append(name_reversed)
		
			# For "normal" names of only two words AND names with one initial like "John S."
			# AND
			# For names of three words with 1 initial at most like "John Joe Snow", "John J. Snow" etc:
			if details['num_of_words'] in [2, 3] and details['includes_dot_initials'] <= 2:			
				self.single_first_and_last(name)
				for n in name_base_variations:
					# ~ try:
					self.seperate_by_special_char(n)										
						
					for i in range(1,3): 
						self.first_x_letters_of_name_only(n, i)
					
					self.first_x_letters_of_name_and_y_letters_of_lastname(n, 1, 2)
					self.initials_only(n)
						
					# ~ except:
						# ~ self.skipped.append(n)
						# ~ print(f' ├─ Failed to process "{return_short_if_string_too_long(n)}" [{ORANGE}skipped{END}].')
				
		
		if self.convertions:	
			if args.domain:			
				# Append domain(s) prefix
				print(f' ├─ Appending domain prefix to each generated username...')
				
				for username in self.convertions:
					self.append_domain(username)
				
			print(f' ├─ Removing duplicate usernames...')
			final_usernames_list = uniq_list(self.convertions + self.domain_prefixed)
			print(f' ├─ Saving username convertions output...')
			file_name = f'usernames_{BabelStrike.timestamp if args.romanization else self.timestamp}'
			save_output(final_usernames_list, file_name)
			Global.output = f'output_{self.timestamp}.txt'
			print(f' ├─ Output saved in {ORANGE}{file_name}.txt{END}')
			print(f' ├─ Total usernames generated: {ORANGE}{len(final_usernames_list)}{END}')
		
		else:
			print(f' ├─ No usernames generated.')
		
		
		if self.skipped:
			save_output(self.convertions, f'skipped_convertion_{self.timestamp}')
			print(f' ├─ Skipped {ORANGE}{len(self.skipped)}/{len(self.contents)}{END} lines (saved in {ORANGE}skipped_convertion_{self.timestamp}.txt{END}).')
			
		print(' └─ Done!')
		return	
		


def main():	
	
	if not args.quiet:
		banner()
		
	if not args.romanization and not args.convertion:
		print(f'{DEBUG} This tool can perform Romanization AND/OR implement naming conversion patterns against a provided full names list.')
		exit_with_msg(f'Use [-r] to perform Romanization AND/OR [-c] to perform name-to-usernames conversion.')
	
	if args.romanization:			
		babelstrike = BabelStrike()
		babelstrike.substitution_iterator()
		print('\r')

	if args.convertion:
		
		if Global.output:
			
			namelist = BabelStrike.transliterated
			
		else:
			
			try:
				namelist = get_file_contents(args.file)
				
			except:
				exit_with_msg('File not found.')
							
		username_converter = Username_Converter(namelist)
		username_converter.apply_convertion_rules()
	
	print('\r')


if __name__ == '__main__':
	main()
