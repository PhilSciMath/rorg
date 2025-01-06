# RORG (Roms Organizer)
This is a Python script for Linux whose purpose is to extract game roms compressed with 7z, zip or rar to a directory called ``isos``. It then creates ``.m3u`` files and put them inside a ``m3u`` directory. Inside ``isos`` each game will have its own directory and games with multiple discs will have all their files inside the same directory. <br>
This is meant to work with Retroarch, since it uses ``.m3u`` files to change discs when a game has multiple discs. It also will only work with cores that support reading from ``.m3u`` files, like Swanstation.
- Do not use it with patched roms like hacks or fan translations.
- When prompted to remove compressed files, say **no** to be safe. If some file is corrupted and things go wrong, you'll still have your compressed files to try again later.
- The script has to be in the same directory as the roms you want to extract.
- For now it only works within Linux, run it from a terminal ``python rorg_v1.0.py``.
- I did it for myself in order to automate the boring task of extracting each rom and typing into ``.m3u`` files manually. It will create two directories, ``isos`` and ``m3u``. You're supposed to move them to where it makes sense for you and then use Retroarch to scan the ``m3u`` directory.

