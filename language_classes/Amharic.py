class Amharic:

	# Amharic Language is Spoken by Ethiopians. 
	# Ethiopia is the only country in Africa with its own distinct alphabet. 
	# it is the Major working language of Ethiopia ( >110M people )
	# There are millions of ethiopians is USA and Europe

	# This language has a letter for each and every sound 
	# here is the list of about 98% of the full alphabet letters. 


	# seems like langdetect is not detecting it. i hope you'll find a way to add it 

	char_substitution_map = {
		'ሀ' : 'ha',
		'ሁ' : 'hu',
		'ሂ' : 'hi',
		'ሃ' : 'ha',
		'ሄ' : 'he',
		'ህ' : ['h', 'hi'],
		'ሆ' : 'ho',
		'ለ' : 'le',
		'ሉ' : 'lu',
		'ሊ' : 'li',
		'ላ' : 'la',
		'ሌ' : 'le',
		'ል' : ['l', 'li'],
		'ሎ' : 'lo',
		'ሐ' : 'ha',
		'ሑ' : 'hu',
		'ሒ' : 'hi',
		'ሓ' : 'ha',
		'ሔ' : 'he',
		'ሕ' : ['h', 'hi'],
		'ሖ' : 'ho',
		'መ' : 'me',
		'ሙ' : 'mu',
		'ሚ' : 'mi',
		'ማ' : 'ma',
		'ሜ' : 'me',
		'ም' : ['m', 'mi'],
		'ሞ' : 'mo',
		'ሠ' : 'se',
		'ሡ' : 'su',
		'ሢ' : 'si',
		'ሣ' : 'sa',
		'ሤ' : 'se',
		'ሥ' : ['s', 'si'],
		'ሦ' : 'so',
		'ረ' : 're',
		'ሩ' : 'ru',
		'ሪ' : 'ri',
		'ራ' : 'ra',
		'ሬ' : 're',
		'ር' : ['r', 'ri'],
		'ሮ' : 'ro',
		'ሰ' : 'se',
		'ሱ' : 'su',
		'ሲ' : 'si',
		'ሳ' : 'sa',
		'ሴ' : 'se',
		'ስ' : ['s', 'si'],
		'ሶ' : 'so',
		'ሸ' : 'she',
		'ሹ' : 'shu',
		'ሺ' : 'she',
		'ሻ' : 'sha',
		'ሼ' : 'she',
		'ሽ' : ['sh', 'shi'],
		'ሾ' : 'sho',
		'ቀ' : ['qe','ke'],
		'ቁ' : ['qu', 'ku'],
		'ቂ' : ['qi', 'ki'],
		'ቃ' : ['qa', 'ka'],
		'ቄ' : ['qe', 'ke'],
		'ቅ' : ['q', 'qi','k','ki'],
		'ቆ' : ['qo','ko'],
		'በ' : 'be',
		'ቡ' : 'bu',
		'ቢ' : 'bi',
		'ባ' : 'ba',
		'ቤ' : 'be',
		'ብ' : ['b', 'bi'],
		'ቦ' : 'bo',
		'ተ' : 'te',
		'ቱ' : 'tu',
		'ቲ' : 'ti',
		'ታ' : 'ta',
		'ቴ' : 'te',
		'ት' : ['t', 'ti'],
		'ቶ' : 'to',
		'ቸ' : 'che',
		'ቹ' : 'chu',
		'ቺ' : 'chi',
		'ቻ' : 'cha',
		'ቼ' : 'che',
		'ች' : ['ch', 'chi'],
		'ቾ' : 'cho',
		'ኅ' : 'ha',
		'ኁ' : 'hu',
		'ኂ' : 'hi',
		'ኃ' : 'ha',
		'ኄ' : 'he',
		'ኅ' : ['h', 'hi'],
		'ኆ' : 'ho',
		'ነ' : 'ne',
		'ኑ' : 'nu',
		'ኒ' : 'ni',
		'ና' : 'na',
		'ኔ' : 'ne',
		'ን' : ['n', 'ni'],
		'ኖ' : 'no',
		'ኘ' : 'gne',
		'ኙ' : 'gnu',
		'ኚ' : 'gni',
		'ኛ' : 'gna',
		'ኜ' : 'gne',
		'ኝ' : ['gn', 'gni'],
		'ኞ' : 'gno',
		'አ' : 'a',
		'ኡ' : ['u','ou'],
		'ኢ' : ['i','e'],
		'ኣ' : 'a',
		'ኤ' : ['a', 'ae'],
		'እ' : ['i','e'],
		'ኦ' : 'o',
		'ከ' : ['ke','qe'],
		'ኩ' : ['ku','qu'],
		'ኪ' : ['ki','qi'],
		'ካ' : ['ka','qa'],
		'ኬ' : ['ke','qe'],
		'ክ' : ['k', 'ki', 'q','qi'],
		'ኮ' : ['ko','qo'],
		'ኸ' : 'he',
		'ኹ' : 'hu',
		'ኺ' : 'hi',
		'ኻ' : 'ha',
		'ኼ' : 'he',
		'ኽ' : ['h', 'hi'],
		'ኾ' : 'ho',
		'ወ' : 'we',
		'ዉ' : 'wu',
		'ዊ' : 'wi',
		'ዋ' : 'wa',
		'ዌ' : 'we',
		'ው' : ['w', 'wi'],
		'ዎ' : 'wo',
		'ዐ' : 'a',
		'ዑ' : ['u', 'ou'],
		'ዒ' : 'i',
		'ዓ' : 'a',
		'ዔ' : 'ae',
		'ዕ' : 'e',
		'ዖ' : 'o',
		'ዘ' : 'ze',
		'ዙ' : 'zu',
		'ዚ' : 'zi',
		'ዛ' : 'za',
		'ዜ' : 'ze',
		'ዝ' : ['z', 'zi'],
		'ዞ' : 'zo',
		'ዠ' : 'zhe',
		'ዡ' : 'zhu',
		'ዢ' : 'zhi',
		'ዣ' : 'zha',
		'ዤ' : 'zhe',
		'ዥ' : ['zh', 'zhi'],
		'ዦ' : 'zho',
		'የ' : 'ye',
		'ዩ' : 'yu',
		'ዪ' : 'yi',
		'ያ' : 'ya',
		'ዬ' : 'ye',
		'ይ' : ['y', 'yi'],
		'ዮ' : 'yo',
		'ደ' : 'de',
		'ዱ' : 'du',
		'ዲ' : 'di',
		'ዳ' : 'da',
		'ዴ' : 'de',
		'ድ' : ['d', 'di'],
		'ዶ' : 'do',
		'ጀ' : 'je',
		'ጁ' : 'ju',
		'ጂ' : 'ji',
		'ጃ' : 'ja',
		'ጄ' : 'je',
		'ጅ' : ['j', 'ji'],
		'ጆ' : 'jo',
		'ገ' : 'ge',
		'ጉ' : 'gu',
		'ጊ' : 'gi',
		'ጋ' : 'ga',
		'ጌ' : 'ge',
		'ግ' : 'gi',
		'ጐ' : 'go',
		'ጠ' : 'te',
		'ጡ' : 'tu',
		'ጢ' : 'ti',
		'ጣ' : 'ta',
		'ጤ' : 'te',
		'ጥ' : ['t', 'ti'],
		'ጦ' : 'to',
		'ጨ' : 'che',
		'ጩ' : 'chu',
		'ጪ' : 'chi',
		'ጫ' : ['cha'],
		'ጭ' : ['ch', 'chi'],
		'ጮ' : 'cho',
		'ጰ' : 'pe',
		'ጱ' : 'pu',
		'ጲ' : 'pi',
		'ጳ' : 'pa',
		'ጴ' : 'pe',
		'ጵ' : ['p', 'pi'],
		'ጶ' : 'po',
		'ጸ' : 'tse',
		'ጹ' : 'tsu',
		'ጺ' : 'tsi',
		'ጻ' : 'tsa',
		'ጼ' : 'tse',
		'ጽ' : ['ts', 'tsi'],
		'ጾ' : 'tso',
		'ፀ' : 'tse',
		'ፁ' : 'tsu',
		'ፂ' : 'tsi',
		'ፃ' : 'tsa',
		'ፄ' : 'tse',
		'ፅ' : ['ts', 'tsi'],
		'ፆ' : 'tso',
		'ፈ' : 'fe',
		'ፉ' : 'fu',
		'ፊ' : 'fi',
		'ፋ' : 'fa',
		'ፌ' : 'fe',
		'ፍ' : ['f', 'fi'],
		'ፎ' : 'fo',
		'ፐ' : 'pe',
		'ፑ' : 'pu',
		'ፒ' : 'pi',
		'ፓ' : 'pa',
		'ፔ' : 'pe',
		'ፕ' : ['p', 'pi'],
		'ፖ' : 'po',
}
