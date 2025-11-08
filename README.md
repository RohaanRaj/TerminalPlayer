Terminal Player is my first project (i will rename it later).
Written in python Terminal Player is a terminal based music player that fetches data and plays music from Subsonic based servers.

It uses Textual a python module for handling User Interface.
python-mpv is a wrapper for mpv- The command line player used for music playback.

### It currently does the following:

- Loads Artists and plays their songs based on Albums.
- Supports all audio formats (FLAC, OGG, MP3) thanks to mpv.
- Queue functionality.

### Features to Add:

- Play an Album directly.
- Add more interactivity across panels.
- Make the panels more informative.
- Add a progress bar or an audio Visualizer in the now playing panel.
- Few more CSS tweaks.
- Thats all i have in mind for now.

### USAGE :

For linux based systems (tested on Arch):

1. Make sure you have mpv and the corresponding libmpv installed 
2. All the packages in requirements.txt installed.
3. Change the corresponding username, password, version, format and BaseUrl in app/backend.py based on your server.
4. now run python main.py and the application should launch.

For Windows based:

    --- To be Updated ---

### INTERACTIVITY :

The following are a few keybindings for navigating through the interface.

- Arrows up/down or k/j for moving up and down.
- Enter for selecting an Artist/Album/Song.
- Pressing "q" on a song adds it to queue.
- "b" takes you to the previous panel.
- "n" plays the next song in the queue.
- Pressing "h" when focus is in Albums/Songs takes you to the Artists list.
- "Tab" allows you to switch between different panels aswell.







