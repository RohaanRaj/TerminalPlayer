Terminal Player is my first project (i will rename it later).
Written in python Terminal Player is a terminal based music player that fetches data and plays music from Subsonic based servers.

### USER INTERFACE ###

<img width="1921" height="1081" alt="2025-11-07-185841_hyprshot" src="https://github.com/user-attachments/assets/d0167722-9106-4345-a038-0bdabb90ee67" />


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

1. Make sure you have mpv and the corresponding libmpv installed.
2. All the packages in requirements.txt installed.
3. Change the corresponding username, password, version, format and BaseUrl in app/backend.py based on your server.
4. now run python main.py and the application should launch.

For Windows based:

1. All the packages in requirements.txt installed.
2. Uncomment the first 4 lines in app/main.py.
3. Change the corresponding username, password, version, format and BaseUrl in app/backend.py(expects string format) based on your server.
4. Install libmpv.dll (needed for music playback) from [here](https://sourceforge.net/projects/mpv-player-windows/files/libmpv/) and download the latest version.
5. Place the two libmpv.dll files (not include) in TerminalPlayer-main/app/lib/
6. Open CommandPrompt/Windows Powershell and run ``` cd path/to/folder/TerminalPlayer-main/ ```
7. Now run ``` python app/main.py ``` and the application will launch.

### INTERACTIVITY :

The following are a few keybindings for navigating through the interface.

- Arrows up/down or k/j for moving up and down.
- Enter for selecting an Artist/Album/Song.
- Pressing "q" on a song adds it to queue.
- "b" takes you to the previous panel.
- "n" plays the next song in the queue.
- Pressing "h" when focus is in Albums/Songs takes you to the Artists list.
- "Tab" allows you to switch between different panels aswell.







