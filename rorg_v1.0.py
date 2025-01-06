#! /usr/bin/env python3

# The purpose of this script is to extract a bunch of zipped game roms
# to a directory called "isos" and create .m3u files inside a directory called
# "m3u", both in the same level. It saves you from the tedious task of
# extracting and creating m3u files manually, which can take quite some time
# depending on how many game roms you have. The idea is that, after running
# this script, you should move the "isos" and "m3u" directories to the right
# place in your system (ex.: "$HOME/Games/PlayStation/" if they are PlayStation
# games) then scan the "m3u" directory with Retroarch.
#
# Note 1: this script must be in the same directory as the
# zipped roms you have (they can be .7z, .zip or .rar)
#
# Note 2: the script depends on Python and 7z
#
# Note 3: it works fine with standard game roms. It DOES NOT WORK with
# most hacked and fan translated from Japanese roms. So if you have any of
# these it is highly advisable to move them to another place before running the
# script, or else errors will occur.
#
# Note 4: I'm not a programer, so this script can be improved by anyone with more 
# skill. I will still make changes now and then as I learn more Python. If you're 
# going to use it, be sure your compressed files aren't corrupted bucause this 
# script as of now won't check what happens when extraction fails. To be safe
# say 'no' when prompted to remove your files.
#

import glob
import os

# choosing to remove or keep the compressed archives
option = input('Remove compressed files?\n[y,n] >> ').lower()
remove = 'rm *.7z *.zip *.rar;' if option[0] == 'y' else ' '

# Creating a list of all the compressed files
archives = glob.glob('*.7z') + glob.glob('*.rar') + glob.glob('*.zip')

# We want game titles that look like "Game Name (USA)", not
# "Game Name (USA) (Disc 1).7z".
titles = []
suffixes = ['.7z', '.rar', '.zip']

def suffix_remover(name, suffixes):    
    for suffix in suffixes:
        if suffix in name:
            return name.removesuffix(suffix)   

for archive in archives:
    end = 0
    if ' (disc' in archive.lower():
        end = archive.lower().find(' (disc')
        titles.append(archive[:end])
    else:
        titles.append(suffix_remover(archive, suffixes))
	
# Removing duplicates and creating directories.
titles = set(titles) 
for title in titles:
    os.makedirs(title, exist_ok=True)

# moving each compressed rom to a directory with same name
for archive in archives:
    for title in titles:
        if title in archive:
            os.system(f'mv "{archive}" "{title}"')

# going into each directory, extracting and deleting each archive and subdirs
for title in titles:
    os.system(f'cd "{title}"; 7z x "*" -y; {remove} mv */* . ;' + 
              ' rm -rf */ *.url')

# Creating dirs and moving game dirs into isos
os.makedirs('isos', exist_ok=True)
for dir_name in os.listdir():
    if os.path.isdir(dir_name) and dir_name != "isos":
        os.system(f'mv "{dir_name}" isos/')

# We need a list of all .cue files to create the .m3u files.
os.makedirs('m3u', exist_ok=True)
os.system('ls isos/*/*.cue > list.txt')
with open("list.txt", "r") as file:
    cue_files = file.read().splitlines()
os.remove('list.txt')

# this will write the .m3u files
for name in cue_files:
    for title in titles:
        if title in name:
            os.system(f'echo "../{name}" >> "m3u/{title}.m3u"')
