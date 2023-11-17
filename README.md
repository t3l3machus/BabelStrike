# BabelStrike
[![Python](https://img.shields.io/badge/Python-%E2%89%A5%203.6-yellow.svg)](https://www.python.org/) 
<img src="https://img.shields.io/badge/Developed%20on-kali%20linux-blueviolet">
[![License](https://img.shields.io/badge/License-CC%20Attr--NonCommercial%204.0-red)](https://github.com/t3l3machus/BabelStrike/blob/main/LICENSE.md)
<img src="https://img.shields.io/badge/Maintained%3F-Yes-96c40f">

## Purpose
The purpose of this tool is to normalize and generate possible usernames out of a full names list that may include names written in multiple (non-English) languages, common problem occurring from scraped employee names lists (e.g. from Linkedin).

BabelStrike takes a full names list as input and performs 1. Romanization of non-English names (based on language alphabet transliteration maps) AND|OR 2. implements name-to-username conversions based on various naming convention rules.

**Romanization feature currently supports**: Greek, Hindi, Spanish, French, Polish and Hungarian. Looking for people to contribute language classes, [check how it's done and contribute](#Contributions)!

### Video Presentation
https://www.youtube.com/watch?v=550S6oAYfDo

## Usage Example
![image](https://github.com/t3l3machus/BabelStrike/assets/75489922/24426b7a-1e0b-4c93-9b6f-5bf658165f1a)


## Name to Usernames Convertion Rules
### Table of rules for generating usernames:  

{f} = first letter of Name, {fi} = first two letters of Name ...  
{l} = first letter of Lastname, {la} = first two letters of Lastname ...  

**The rules can be automatically aplied to the reversed version of the full name as well, by using [-a].**

|                          |                 |                |            |                | 
| :----------------------: |:---------------:|:--------------:| :--------: | :------------: | 
| {firstname}{lastname}    | {f}{l}          | {lastname}{f}    | {f}{la}  | {firstname}    |
| {firstname}.{lastname}   | {f}.{l}         | {lastname}.{f}   | {f}.{la} | {lastname}     |
| {firstname}_{lastname}   | {f}_{l}         | {lastname}_{f}   | {f}_{la} |                |
| {firstname}-{lastname}   | {f}-{l}         | {lastname}-{f}   | {f}-{la} |                |
| {firstname} {lastname}   | {f} {l}         | {lastname} {f}   | {f} {la} |                |
| {f}{lastname}            | {fi}{lastname}  | {lastname}{fi}   | {la}{f}  |                |
| {f}.{lastname}           | {fi}.{lastname} | {lastname}.{fi}  | {la}.{f} |                |
| {f}_{lastname}           | {fi}_{lastname} | {lastname}_{fi}  | {la}_{f} |                |
| {f}-{lastname}           | {fi}-{lastname} | {lastname}-{fi}  | {la}-{f} |                |
| {f} {lastname}           | {fi} {lastname} | {lastname} {fi}  | {la} {f} |                |

#### Conversion rules when middle name is detected

|                                  |                          |                           |             |                | 
| :------------------------------: |:------------------------:|:-------------------------:| :---------: | :------------: | 
| {firstname}{middle}{lastname}    | {f}{m}{l}                | {lastname}{middle}{f}     | {f}{m}{l}   |                |
| {firstname}.{middle}.{lastname}  | {f}.{m}.{l}              | {lastname}.{middle}.{f}   | {f}.{m}.{l} |                |
| {firstname}\_{middle}\_{lastname}  | {f}\_{m}\_{l}              | {lastname}\_{middle}\_{f}   | {f}\_{m}\_{l} |                |
| {firstname}-{middle}-{lastname}  | {f}-{m}-{l}              | {lastname}-{middle}-{f}   | {f}-{m}-{l} |                |
| {firstname} {middle} {lastname}  | {f} {m} {l}              | {lastname} {middle} {f}   | {f} {m} {l} |                |
| {f}{middle}{lastname}            | {fi}{middle}{lastname}   | {lastname}{middle}{fi}    | {firstname} |                |
| {f}.{middle}.{lastname}          | {fi}.{middle}.{lastname} | {lastname}.{middle}.{fi}  | {middle}    |                |
| {f}\_{middle}\_{lastname}          | {fi}\_{middle}\_{lastname} | {lastname}\_{middle}\_{fi}  | {lastname}  |                |
| {f}-{middle}-{lastname}          | {fi}-{middle}-{lastname} | {lastname}-{middle}-{fi}  |             |                |
| {f} {middle} {lastname}          | {fi} {middle} {lastname} | {lastname} {middle} {fi}  |             |                |

## Installation & Usage
### Install requirements with pip
```
pip3 install -r requirements.txt
```
### Install additional fonts for languages 
In order to be able to process certain languages, you may need to install additional fonts on your machine. Here's for example how to install Hindi fonts:
 1. Download the fonts from here: https://fonts.google.com/specimen/Hind.
 2. Unzip and move the fonts in `~/.local/share/fonts` (if the directory does not exist then create it).

If you open a new terminal now the characters will be represented properly (this was tested on kali linux).

### Usage
```
babelstrike.py [-h] -f FILE [-r] [-c] [-a] [-d DOMAIN] [-u] [-q]

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File to process.
  -r, --romanization    Transliterate names to the latin alphabet.
  -c, --convertion      Perform name-to-username convertions.
  -a, --auto-reverse    Perform name-to-username convertion patterns against the reversed version of each name as well.
  -d DOMAIN, --domain DOMAIN
                        Comma seperated list of domains to add as prefix to each generated username (e.g. EVILCORP\scott.henderson).
  -u, --update          Pull the latest version from the original repo.
  -q, --quiet           Do not print the banner on startup.
```

## Contributions
In order for the Romanization feature to be accurate, I decided to use custom character substitution maps for each language preferably made by native speakers. 
I'm looking for some cool people around the world to create such maps that are basically a Python dictionary.

### Instructions
If you want to contribute a language Class all you have to do is:
* Find an official Romanization standard for your language's alphabet (e.g. in Wikipedia),
* Copy a language Class file from the [language_classes](https://github.com/t3l3machus/BabelStrike/tree/main/language_classes) folder to use as a template (I suggest you use Greek.py),
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
* Save the new class in the **language_classes** folder named appropriately.  

