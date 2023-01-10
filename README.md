# BabelStrike
[![Python](https://img.shields.io/badge/Python-%E2%89%A5%203.6-yellow.svg)](https://www.python.org/) 
<img src="https://img.shields.io/badge/Developed%20on-kali%20linux-blueviolet">
<img src="https://img.shields.io/badge/Maintained%3F-Yes-96c40f">

## Purpose
The purpose of this tool is to normalize and generate possible usernames out of a full names list that may include names written in multiple (non-English) languages, common problem occuring from scraped data (e.g. Linkedin).

BabelStrike takes a full names list as input and performs 1. Romanization of non-English names (based on language alphabet transliteration maps) AND|OR 2. implements name-to-username conversions based on various naming convention rules.

## Contributions
In order for the Romanization feature to be accurate, I decided to use custom character substitution maps for each language preferably made by native speakers. 
I'm looking for some cool people around the world to create such maps that are basically a Python dictionary.

### Instructions
If you want to contribute a language Class all you have to do is:
* Find an official Romanization standard for your language's alphabet (e.g. in Wikipedia),
* Copy a language Class file from the language_classes folder to use as a template (I suggest you use Greek.py),
* Edit the filename and the Class name to represent your language,
* Edit the **char_substitution_map** dictionary and create the character substitution map (**Important**: Don't change the name of the dictionary),
  * Map lowercase letters only, 
  * Take in consideration double or triple letter sounds that may be transliterated in a single character of the Latin alphabet,
  * Take in consideration accented characters (e.g. à, è, ì, ò, ù),
  * When a letter has more than one transliteration equivalents, use a list to include all of them (BabelStrike will handle all variations). Example: 
  ```
  # In Greek, the letter 'υ' may be transliterated as 'y' or 'u'. 
  # This is how it should be declared in the character mapping dictionary:
  
  char_substitution_map = {
    'ά' : 'a',
    'έ' : 'e',
    'υ' : ['y','u']
  }
  ```